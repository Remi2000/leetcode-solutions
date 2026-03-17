"""
# 146. LRU Cache

## Idea
To achieve O(1) time for both `get` and `put`, we combine:
- HashMap (dict): key -> node, for O(1) lookup
- Doubly Linked List: maintain usage order

The most recently used node is placed near the head,
and the least recently used node is near the tail.

## Design
- On `get(key)`:
  - If key not found → return -1
  - Otherwise, move the node to the front and return its value

- On `put(key, value)`:
  - If key exists:
      - Update value
      - Move node to front
  - If key does not exist:
      - Create new node
      - Insert to front
      - Add to hashmap
      - If capacity exceeded:
          - Remove node near tail (LRU)
          - Delete from hashmap

## Data Structures
- HashMap
- Doubly Linked List

## Time Complexity
- get: O(1)
- put: O(1)

## Space Complexity
- O(capacity)

## Pattern
- Design
- HashMap + Doubly Linked List
"""


class Node:
    """
    Doubly linked list node.
    Stores key so we can delete from hashmap in O(1).
    """
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> node

        # Dummy head and tail
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node) -> None:
        """Remove a node from the linked list."""
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def _insert_to_front(self, node: Node) -> None:
        """Insert node right after head (most recently used)."""
        next_node = self.head.next

        self.head.next = node
        node.prev = self.head

        node.next = next_node
        next_node.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Move to front since it is recently used
        self._remove(node)
        self._insert_to_front(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update existing node
            node = self.cache[key]
            node.value = value

            self._remove(node)
            self._insert_to_front(node)
        else:
            # Insert new node
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._insert_to_front(new_node)

            # Remove LRU if over capacity
            if len(self.cache) > self.capacity:
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]
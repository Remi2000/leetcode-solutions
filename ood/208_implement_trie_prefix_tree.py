"""
208. Implement Trie (Prefix Tree)

Description:
    Implement a Trie (prefix tree) with insert, search, and startsWith methods.
    insert(word) adds a word to the trie.
    search(word) returns True if the word exists as a complete word.
    startsWith(prefix) returns True if any inserted word has the given prefix.

Approach:
    Each TrieNode has a dictionary mapping characters to child nodes,
    and a boolean is_end flag marking complete words.
    All three methods share the same structure: walk from root
    character by character through the children dictionary.
    - insert: create nodes along the path if missing, mark is_end at the end.
    - search: follow the path, return False if broken, check is_end at the end.
    - startsWith: same as search but skip the is_end check.

Tech Stack:
    - Trie (prefix tree) data structure
    - Dictionary (hashmap) for O(1) child lookup per node

Complexity:
    - Time: O(m) per operation, where m is the word/prefix length
    - Space: O(m) per insert (worst case creates m new nodes),
             O(1) for search and startsWith
"""


class TrieNode:

    def __init__(self):
        # maps character -> child TrieNode
        self.children = {}
        # marks whether this node is the end of a complete word
        self.is_end = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for c in word:
            # create new node if this character path doesn't exist
            if c not in curr.children:
                curr.children[c] = TrieNode()
            # move to the child node
            curr = curr.children[c]
        # mark the end of the word
        curr.is_end = True

    def search(self, word):
        curr = self.root
        for c in word:
            # path broken, word doesn't exist
            if c not in curr.children:
                return False
            curr = curr.children[c]
        # must be a complete word, not just a prefix
        return curr.is_end

    def startsWith(self, prefix):
        curr = self.root
        for c in prefix:
            # path broken, prefix doesn't exist
            if c not in curr.children:
                return False
            curr = curr.children[c]
        # path exists, that's enough for prefix check
        return True
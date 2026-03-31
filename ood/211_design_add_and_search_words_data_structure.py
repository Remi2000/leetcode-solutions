"""
211. Design Add and Search Words Data Structure

Description:
    Design a data structure that supports adding new words and searching
    for words with wildcard support. The dot '.' can match any single letter.
    Implement addWord(word) and search(word).

Approach:
    Use a Trie (same as 208) for storage.
    addWord is identical to Trie insert.
    search uses DFS/backtracking to handle the '.' wildcard:
    - Normal character: follow the one matching path.
    - '.': try all children recursively, return True if any path matches.

Tech Stack:
    - Trie (prefix tree) data structure
    - DFS / Backtracking for wildcard matching
    - Dictionary (hashmap) for O(1) child lookup per node

Complexity:
    - addWord: Time O(m), Space O(m) — same as Trie insert
    - search: Time O(26^n * m) worst case where n = number of dots,
              Space O(m) for recursion stack depth
"""


class TrieNode:

    def __init__(self):
        # maps character -> child TrieNode
        self.children = {}
        # marks whether this node is the end of a complete word
        self.is_end = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        # same as Trie insert
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_end = True

    def search(self, word):
        def dfs(node, i):
            # all characters matched, check if it's a complete word
            if i == len(word):
                return node.is_end

            c = word[i]

            if c != '.':
                # normal character: follow the one path
                if c not in node.children:
                    return False
                return dfs(node.children[c], i + 1)
            else:
                # wildcard: try every child, return True if any path matches
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False

        return dfs(self.root, 0)
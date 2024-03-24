class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Solution:
    def longestWord(self, words: List[str]) -> str:
        def insert_word(root, word):
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end_of_word = True

        def longest_word(words):
            root = TrieNode()
            for word in words:
                insert_word(root, word)

            longest = ""
            stack = [(root, "")]

            while stack:
                node, current_word = stack.pop()
                if len(current_word) > len(longest) or (len(current_word) == len(longest) and current_word < longest):
                    longest = current_word

                for char, child in node.children.items():
                    if child.is_end_of_word:
                        stack.append((child, current_word + char))

            return longest
        
        return longest_word(words)

class TrieNode():
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            num = ord(char)-97
            if not curr.children[num]:
                curr.children[num] = TrieNode()
            curr = curr.children[num]



    def search(self, word):
        curr = self.root
        pre = ""
        for char in word:
            num = ord(char)-97
            if not curr.children[num]:
                return pre
            pre += char
            curr = curr.children[num]

        return pre

class Solution:
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # populate the trie
        strs.sort()
        tree = Trie()
        tree.insert(strs[0])

        prefix = ""

        for word in strs[1:]:
            prefix = tree.search(word)
        
        return strs[0] if len(strs) == 1 else prefix      

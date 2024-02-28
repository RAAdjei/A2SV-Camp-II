class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]

class Trie:
    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            num = ord(char) - 97
            if not curr.children[num]:
                curr.children[num] = TrieNode()
            curr = curr.children[num]
        curr.is_end = True
        

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            num = ord(char)-97
            if not curr.children[num]:
                return False
            curr = curr.children[num]
        
        return curr.is_end
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            num = ord(char)-97
            if not curr.children[num]:
                return False
            curr = curr.children[num]
        return True




        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

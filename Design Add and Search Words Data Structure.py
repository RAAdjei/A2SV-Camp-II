class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

        

    def addWord(self, word: str) -> None:
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]
        
        curr.end = True
        

    def search(self, word: str) -> bool:
        def helper(root,word):
            curr = root
            for i in range(len(word)):
                if word[i] == ".":
                    found = False
                    for c in curr.children:
                        found = found or helper(curr.children[c],word[i+1::])
                    return found
                else:
                    if word[i] not in curr.children:
                        return False                
                    curr = curr.children[word[i]]

            return curr.end
        return helper(self.root,word)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        def convert(string):
            string_bits = [ord(char).bit_length() for char in string]
            return sum(string_bits)

        n = len(words)
        res = []
        maxi = 0
        
        for i in range(n):
            for j in range(i+1, n):
                if not set(words[i]) & set(words[j]):
                    res.append(len(words[i]) * len(words[j]))

       
        if res:
            return max(res)
        else:
            return 0

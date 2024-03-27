class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff = [0] * (n+2)
        output = []

        for l, r, shift in shifts:
            if shift == 0:
                diff[l+1] -= 1 
                diff[r+2] += 1
            else:
                diff[l+1] += 1 
                diff[r+2] -= 1

        pref = [0]* (n+2)

        for i in range(len(diff)):
            pref[i] = pref[i-1] + diff[i]

        for i in range(1, len(pref)-1):
            op = pref[i]
            ans = ord(s[i-1])-ord("a")
            ans = (ans+(op))%26
            char = chr(ans+ord("a"))
            output.append(char)

        return "".join(output)

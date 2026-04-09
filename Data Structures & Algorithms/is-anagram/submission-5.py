class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # return sorted(s) == sorted(t)

        # if len(s) != len(t):
        #     return False

        # countS, countT = {},{}
        # for char in range(len(s)):
        #     countS[s[char]] = 1+countS.get(s[char],0)
        #     countT[t[char]] = 1+countT.get(t[char],0)
        
        # return countS == countT

        if len(s) != len(t):
            return False
        count = [0]*26
        for char in range(len(s)):
            count[ord(s[char])-ord('a')]+=1
            count[ord(t[char])-ord('a')]-=1
        
        for value in count:
            if value!=0:
                return False
        return True
        



        
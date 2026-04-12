class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        count = 0

        for char in range(len(s)):
            charSet = set()
            for nextChar in range(char,len(s)):
                if s[nextChar] in charSet:
                    break
                charSet.add(s[nextChar])
            count = max(count,len(charSet))
        return count
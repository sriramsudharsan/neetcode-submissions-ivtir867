class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        count = 0

        for char in range(len(s)):
            charSet = set()
            for j in range(char,len(s)):
                if s[j] in charSet:
                    break
                charSet.add(s[j])
            count = max(count,len(charSet))
        return count
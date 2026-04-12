class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        result = 0

        for char in range(len(s)):
            charSet = set()
            for nextChar in range(char,len(s)):
            # print(charSet)
                if s[nextChar] in charSet:
                    break
                charSet.add(s[nextChar])

            result = max(result,len(charSet))
        return result


            
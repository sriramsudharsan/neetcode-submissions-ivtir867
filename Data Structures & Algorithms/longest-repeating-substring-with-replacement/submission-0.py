class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        result = 0

        for i in range(len(s)):
            count = {}
            maxfreq = 0

            for j in range(i,len(s)):
                count[s[j]]= 1+count.get(s[j],0)
                maxfreq = max(maxfreq,count[s[j]])

                if(j-i+1)-maxfreq <=k:
                    result = max(result,j-i+1)
        return result
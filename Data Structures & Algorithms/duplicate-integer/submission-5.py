class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if(nums[i]==nums[j]):
        #             return True
        # return False

        
        # hashMap = defaultdict(int)

        # for number in nums:
        #     if(number in hashMap):
        #         return True
        #     else:
        #         hashMap[number]+=1
        # return False

        seen = set()

        for number in nums:
            if number in seen:
                return True
            else:
                seen.add(number)
        return False



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for number1 in range(len(nums)):
            for number2 in range(number1+1,len(nums)):
                complement = target-nums[number1]
                if(nums[number2]==complement):
                    return [number1,number2]
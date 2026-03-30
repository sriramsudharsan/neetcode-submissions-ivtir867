class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result = [0]*len(temperatures)
        stack = []

        for index, element in enumerate(temperatures):
            while stack and element>stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                result[stackIndex] = index - stackIndex
            stack.append((element,index))
        return result
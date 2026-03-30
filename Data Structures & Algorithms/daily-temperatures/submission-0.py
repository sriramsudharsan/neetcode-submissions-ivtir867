class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        result = [0]*len(temperatures)

        for i,n in enumerate(temperatures):
            print (i,n)
            while stack and n>stack[-1][0]:
                print(stack[-1][0])
                stackElement, stackIndex  = stack.pop()
                result[stackIndex] = i-stackIndex
            stack.append((n,i))
        return result
        
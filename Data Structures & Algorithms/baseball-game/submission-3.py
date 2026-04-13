class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        sum = 0
        for char in operations:
            if char == "+":
                sum += stack[-1]+stack[-2]
                stack.append(stack[-1]+stack[-2])
            elif char == "D":
                sum+=2*stack[-1]
                stack.append(2*stack[-1])
            elif char == "C":
                sum -= stack.pop()
            else:
                sum += int(char)
                stack.append(int(char))

        return sum
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for char in tokens:
            if char == "+":
                print(stack)
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif char == "*":
                print(stack)
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif char == "-":
                print(stack)
                a,b = int(stack.pop()),int(stack.pop())
                stack.append(b-a)
            elif char == "/":
                print(stack)
                a,b = int(stack.pop()),int(stack.pop())
                stack.append(b/a)
            else:
                print(stack)

                stack.append(int(char))

        return int(stack[0])
        
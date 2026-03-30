class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stack = []
        paths = path.split("/")
        print(paths)

        for char in paths:
            if char == "." or char == "":
                continue
            elif char == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        return "/"+"/".join(stack)
    
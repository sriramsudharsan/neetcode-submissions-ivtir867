class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stack = []
        paths = path.split("/")
        print(paths)

        for charecter in paths:
            if charecter == "..":
                if stack:
                    stack.pop()
            elif charecter != "" and charecter != ".":
                stack.append(charecter)
        return "/"+"/".join(stack)
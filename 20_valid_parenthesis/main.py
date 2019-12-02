class Solution:
    def isValid(self, s):
        if s == "":
            return True
        
        stack = []

        for c in s:
            if c == '(':
                stack.append(')')
            elif c == '{':
                stack.append('}')
            elif c == '[':
                stack.append(']')

            elif len(stack) == 0:
                return False
            elif c != stack.pop():
                return False

        if len(stack) == 0:
            return True
        else:
            return False

parens = "()"
sol = Solution().isValid(parens)
print("is valid %r" % sol)
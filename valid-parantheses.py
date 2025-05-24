class Solution(object):
    def isValid(self, s):
        stack=[]
        brackets={')': '(', '}': '{', ']': '['}

        for ch in s:
            if ch in brackets.values():
                stack.append(ch)
            elif ch in brackets:
                if not stack or stack[-1] != brackets[ch]:
                    return False
                stack.pop()
            else:
                return False
        return not stack

input_string ="[]{}()"
s1=Solution()
print(s1.isValid(input_string))
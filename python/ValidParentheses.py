class Solution(object):
    def isValid(self, s):
        openP = {
            "{": True,
            "[": True,
            "(": True
        }

        closeP = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        st = []
        for i in s:
            if i in openP:
                st.append(i)
            else:
                if len(st) > 0:
                    c = st.pop()
                    close = closeP.get(i)
                    if c != close:
                        return False
                else:
                    return False
        if len(st) != 0:
            return False
        return True


service = Solution()
print(service.isValid("{{"))

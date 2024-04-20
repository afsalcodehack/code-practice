class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        _map = {'{': '}', '[': ']', '(': ')'}

        for i in s:
            if i in {'{', '(', '['}:
                stack.append(_map[i])
            else:
                if len(stack) <= 0:
                    return False
                else:
                    c = stack.pop()
                    if i != c:
                        return False
        if len(stack) > 0:
            return False
        return True


driver = Solution()
print(driver.isValid('(()[]{}())'))
print(driver.isValid('('))

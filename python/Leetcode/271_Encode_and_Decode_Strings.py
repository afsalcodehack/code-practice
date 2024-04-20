from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ''
        for i in strs:
            result += str(len(i)) + '#' + i
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        j = 1
        print('total len ' , len(s))
        while j < len(s):
            if s[j] == '#':
                print('curr len',j)
                _len = int(s[i:j])
                start = j+1
                item = s[start: start + _len]
                print(int(s[i:j]), item)
                result.append(item)
                i = start+_len
                j = i + 1
            else:
                j += 1

        return result


driver = Solution()

#encoded = driver.encode(['afsal', 'aydin', 'ethan ibrahim'])
encoded = driver.encode(["we","say",":","yes","!@#$%^&*()"])
print(encoded)
print(driver.decode(encoded))

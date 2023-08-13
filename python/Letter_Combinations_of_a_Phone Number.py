class Solution:
    dic = {
        "1": [],
        "2": ['a', 'b', 'c'],
        "3": ['d', 'e', 'f'],
        "4": ['g', 'h', 'i'],
        "5": ['j', 'k', 'l'],
        "6": ['m', 'n', 'o'],
        "7": ['p', 'q', 'r', 's'],
        "8": ['t', 'u', 'v'],
        "9": ['w', 'x', 'y', 'z'],
        "0": []
    }
    result = []

    def rec(self, index, str, digits, _len):

        if index == _len:
            self.result.append(str)
            return

        number_letters = self.dic[digits[index]]
        if not number_letters:
            self.rec(index + 1, str, digits, _len)

        for i in number_letters:
            str += i
            self.rec(index + 1, str, digits, _len)
            str = str[:-1]

    def letterCombinations(self, digits: str) -> List[str]:
        self.result.clear()
        if len(digits) == 1 and digits == '0' or digits == '1' or digits == '':
            return []
        self.rec(0, '', digits, len(digits))
        return self.result


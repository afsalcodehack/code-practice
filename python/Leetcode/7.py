class Solution:
    def reverse(self, x: int) -> int:

        maxim = 2 ** 31 - 1
        minim = -2 ** 31

        result = 0;
        sign = "+"

        if x < 1:
            sign = "-";
            x = 0 - x;

        while x > 9:
            rem = x % 10;
            result = int((result*10) + rem);
            x = int(x / 10)
        result = (result*10) + x;
        if sign == "-":
            result = 0 - result;

        if result > maxim or result < minim:
            return 0

        return result


service = Solution();
print(service.reverse(123))

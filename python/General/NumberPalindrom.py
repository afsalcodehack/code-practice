# Determine whether an integer is a palindrome.
# An integer is a palindrome when it reads the same backward as forward.
def ispalindrom(x):
    if x == 0 : return True
    num = x;
    rev = 1;
    pre_rem = 0;
    while num > 0:
        rem = num % 10;
        rev = (pre_rem * 10) + rem;
        pre_rem = rev;
        num = int(num / 10);
    return rev == x;

print(ispalindrom(101))

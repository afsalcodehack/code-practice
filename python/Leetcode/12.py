
def intiger_to_roman(num):
    result = "";
    letter_dic = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]
    for i in range(len(letter_dic)):
        result = result + int(num / letter_dic[i][0]) * letter_dic[i][1]
        num = num % letter_dic[i][0]
    return result


print(intiger_to_roman(3))

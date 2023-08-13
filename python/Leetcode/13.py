def roman_to_intiger(s):
    map = {
        "M": 1000,
        "D": 500,
        "L": 50,
        "C": 100,
        "X": 10,
        "V": 5,
        "I": 1,
        "0": 0
    }
    result = 0;
    for i in range(len(s)):
        result = result+map.get(str[i]);
        if i-1 >= 0:
            prev = s[i-1];
            if (prev == "I" or prev == "X" or prev == "C") and map.get(s[i]) > map.get(prev):
                result = result - map.get(prev)*2
    return result;


print(roman_to_intiger("MCMXCIV"))

# Define two dictionaries with different keys but same values
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'x': 1, 'y': 2, 'z': 3}

# Check if values are equal
values_equal = sorted(dict1.values()) == sorted(dict2.values())


print(sorted(dict1.values()), sorted(dict2.values()))  # Output: True

print(dict1.values(), dict2.values())  # Output: True

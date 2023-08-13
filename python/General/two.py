
list = ['afsal', 'amal', 'aslam', 'rimsha', 'aydin']

for item in list[:]:
    if item != "aydin":
        list.remove(item)

print(list)
import queue
dict = {(1, 1): True}

dict.update({(1, 2): False})
#print(dict.get((1, 1)))

if dict.get((1, 4)) == True:
    print("yes")
else:
    print("no")


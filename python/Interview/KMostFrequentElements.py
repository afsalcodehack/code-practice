# K Most Frequent Elements
# input: [1,6,2,1,6,1,6], k=2
# output:[1,6]
# #  k1 = will be 1 and k=2 will be 6 so bothe are same count(3)
# in this case combine together

def most_freq_num(ar, k):
    dict = {}
    for i in ar:
        if i in dict:
            dict[i] = dict[i] + 1;
        else:
            dict[i] = 1;

    dict = sorted(dict.items());
    print(dict);

a = [1,6,2,1,6,1,6]
most_freq_num(a, 2)

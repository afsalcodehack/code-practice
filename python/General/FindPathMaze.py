def is_safe(ar, i, j):
    i_len = len(ar)
    j_len = len(ar[0])

    if i_len > i >= 0 and j_len > j >= 0:
        return True
    else:
        return False


def find_path(ar, d, i, j, f_count):
    if is_safe(ar, i, j) is False:
        return
    if ar[i][j] != 0:
        print(i, j)

    if ar[i][j] == 0:
        return

    # print(f_count)
    # if ar[i][j] == 0:
    #     f_count += 1

    if ar[i][j] == d:
        return True

    ar[i][j] = 0

    if find_path(ar, d, i, j - 1, f_count) or find_path(ar, d, i, j + 1, f_count) or \
            find_path(ar, d, i - 1, j, f_count) or find_path(ar, d, i + 1, j, f_count):
        return True

    return False


a = [[0, 3,  2],
     [3, 3, 0],
     [1, 3, 0]]

b = [[0, 3, 1, 0],
     [3, 0, 3, 3],
     [2, 3, 0, 3],
     [0, 3, 3, 3]]

#print(find_path(a, 2, 2, 0, 0))

print(find_path(b, 2, 0, 2, 0))

# print(is_safe(a, 1, -1))

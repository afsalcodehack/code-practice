import queue


def is_path_exist(ar, i, j):
    if i > 2 or j > 2 or ar[i][j] == 0:
        return False

    if ar[i][j] == 2:
        return True

    ar[i][j] = 0

    if is_path_exist(ar, i, j + 1) or is_path_exist(ar, i, j - 1) or \
            is_path_exist(ar, i - 1, j) or is_path_exist(ar, i + 1, j):
        return True

    return False


def is_safe(i, j, n, m, ar):
    print(i, j)
    if n > i > 0 and m > j > 0 and ar[i][j] != 0:
        return True
    else:
        False


def is_path_exist_dfs(ar, i, j):
    q = queue.Queue()

    q.put((i, j))
    m = 2
    n = 2
    while not q.empty():
        v = q.get()
        v1 = v[0]
        v2 = v[1]

        if ar[v1][v2] == 2:
            return True
            break

        if is_safe(v1, v2 + 1, n, m, ar):
            q.put((v1, v2 + 1))
        if is_safe(v1, v2 - 1, n, m, ar):
            q.put((v1, (v2 - 1)))
        if is_safe((v1 + 1), v2, n, m, ar):
            q.put(((v1 + 1), v2))
        if is_safe((v1 - 1), v2, n, m, ar):
            q.put(((v1 - 1), v2))

    return False


g = [[0, 3, 2],
     [3, 3, 0],
     [1, 3, 3]]

# print(is_path_exist(g, 2, 0))


print(is_path_exist_dfs(g, 2, 0))

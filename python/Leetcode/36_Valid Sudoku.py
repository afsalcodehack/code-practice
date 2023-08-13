from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        list_larg = {}
        small_sqr = {}
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == ".":
                    continue
                if (int(i/3), int(j/3)) not in small_sqr.keys():
                    small_sqr[(int(i/3), int(j/3))] = [];
                else:
                    if board[i][j] in small_sqr[(int(i/3), int(j/3))]:
                        return False
                small_sqr[(int(i/3), int(j/3))].append(board[i][j])

                if board[i][j] not in list_larg.keys():
                    list_larg[board[i][j]] = [];
                else:
                    for t in list_larg[board[i][j]]:
                        if t[0] == i or t[1] == j:
                            return False;
                list_larg[board[i][j]].append((i, j));
        return True


service = Solution();
board1 = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]];

board = [[".", ".", ".", ".", "5", ".", ".", "1", "."],
         [".", "4", ".", "3", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", "3", ".", ".", "1"],
         ["8", ".", ".", ".", ".", ".", ".", "2", "."],
         [".", ".", "2", ".", "7", ".", ".", ".", "."],
         [".", "1", "5", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", "2", ".", ".", "."],
         [".", "2", ".", "9", ".", ".", ".", ".", "."],
         [".", ".", "4", ".", ".", ".", ".", ".", "."]]

print(service.isValidSudoku(board));

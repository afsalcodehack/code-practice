class Solution:

    def main(self, tr, tc):
        arr = [[0, 1, 0, 1],
               [1, 1, 1, 0],
               [0, 0, 1, 0]]
        ROW, COL = len(arr), len(arr[0])
        visit = set()
        return self.dfs(ROW, COL, tr, tc, 0, 1, visit, arr)

    def dfs(self, row, col, tr, tc, cr, cc, visit, arr):

        if cr < 0 or cc < 0 or cr >= row or cc >= col or (cr, cc) in visit or arr[cr][cc] == 0:
            return False

        if (tr, tc) == (cr, cc):
            return True

        visit.add((cr, cc))
        result = (self.dfs(row, col, tr, tc, cr + 1, cc, visit, arr) or
                  self.dfs(row, col, tr, tc, cr - 1, cc, visit,arr) or
                  self.dfs(row, col, tr, tc, cr,cc + 1, visit,arr) or
                  self.dfs(row,col,tr,tc,cr,cc - 1,visit,arr))

        visit.pop()

        return result


driver = Solution()
print(driver.main(0, 3))
print(driver.main(0, 1))
print(driver.main(2, 2))
print(driver.main(0, 2))
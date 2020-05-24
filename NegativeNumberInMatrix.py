# 1351. Count Negative Numbers in a Sorted Matrix
from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0 
        for row in grid:
            if row[0] < 0:
                count = count + len(row)
            elif row[-1] < 0:
                row_size = len(row)
                for i in range(len(row)):
                    if row[row_size-i-1] < 0 :
                        count = count + 1
                    else :
                        break
            else:
                pass
        return count


if __name__ == "__main__":
    grid = [[3,2],[1,0]]
    obj = Solution()
    result = obj.countNegatives(grid)
    print(result)
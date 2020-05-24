#1450. Number of Students Doing Homework at a Given Time
from typing import List

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count = 0 
        for i in range(len(startTime)):
            if queryTime >= startTime[i] and queryTime <= endTime[i]:
                count = count + 1         
        return(count)


if __name__ == "__main__":
    startTime = [4]
    endTime = [4]
    queryTime = 4
    obj = Solution()
    result = obj.busyStudent(startTime, endTime, queryTime)
    print(result)


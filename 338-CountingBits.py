from typing import List
class Solution():
    def countBits(self, n: int)-> int:
        sum = 0 
        while (n>=1):
            rem = n%2
            n = int(n/2)
            # sum = (sum*10) + rem
            if rem == 1:
                sum+=1
        return sum


if __name__ == "__main__":
    n = 7
    obj = Solution()
    result = []
    for i in range(n):
        result.append(obj.countBits(i))
    print(result)
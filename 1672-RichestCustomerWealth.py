from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max = 0
        for account in accounts:
            sum = 0 
            for i in account:
                sum = sum + i
            if sum > max:
                max = sum
        return max
    def maximumWealth2(self, accounts: List[List[int]]) -> int:
        account_sum = []
        for account in accounts:
            account_sum.append(sum(account))
        return max(account_sum)

if __name__ == "__main__":
    inp = [[1,5],[7,3],[3,5]]
    obj = Solution()
    result = obj.maximumWealth2(inp)
    print(result)
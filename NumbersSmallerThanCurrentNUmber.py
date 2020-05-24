from typing import List

class Solution:    
    
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:        
        result = []
        for num in nums:
            count = 0            
            for j in nums:                
                if num > j:
                    count = count+1
            print(count)
            result.append(count)
        return result


if __name__ == '__main__':
    ip = [8,1,2,2,3]
    obj = Solution()
    b = obj.smallerNumbersThanCurrent(ip)
    print(b)
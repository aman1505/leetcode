class Solution():
    def removeElements(self, nums, val):        
        i=0
        while(i<len(nums)):
            if (val==nums[i]):
                nums.remove(nums[i])                
            else:
                i+=1
        return i


if __name__ == "__main__":
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    obj = Solution()
    result = obj.removeElements(nums,val)
    print(result)

class Solution():
    def removeElements(self, nums, val):
        
        # for i in range(len(nums)): 
        #     # print(str(num)+"-----"+str(nums))
        #     if (val==nums[i]):
        #         print("val--"+str(val)+"---"+"num--"+str(nums[i])) 
        #         nums.remove(nums[i])
        # return len(nums), nums
        i=0
        while(i<len(nums)):
            print(i)
            if (val==nums[i]):
                nums.remove(nums[i])
                print(len(nums))
                print(nums)
            i+=1
        return len(nums), nums


if __name__ == "__main__":
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    obj = Solution()
    result = obj.removeElements(nums,val)
    print(result)

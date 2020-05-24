nums = [2, 7, 11, 15]
# nums = [2,5,5,11]
# nums = [3,2,4]
# target = 10
target = 9
# target =6
result = {}
flag = 1
for i in range(len(nums)):
    result[nums[i]] = i
print(result)
for i in range(len(nums)-1):
    n2 = target - nums[i]
    print(str(i)+"----"+str(n2))
    if n2 in nums[i+1:] and flag == 1:
        print(str(i)+"-"+str(n2)+"-"+str(flag))
        j, k = result[n2], i
        flag = 0

print(j, k)

#####fastest solution
# for i in range(len(nums)):
#     n2 = target - nums[i]
#     if n2 in result:
#         a,b = i,result[n2]
#     result[nums[i]] = i
#
# print(a,b)
#

def largestMagical(binString):
    # Write your code here
    bal = left =0
    inter_result = []
    for r in range(len(binString)):
        print("for input---"+str(binString[r]))
        if binString[r] == '0':
            bal-=1
        else:
            bal+=1
        print("balance is ---"+str(bal))
        if bal == 0:
            print("-------------inside balance--------------")
            print("input inside balance-----"+str(left+1)+"----"+str(r)+"----"+str(binString[left+1:r]))
            inter_result.append("1"+largestMagical(binString[left+1:r])+ "0")
            print("inter-result--------"+str(inter_result))
            left = r+1
    
    inter_result.sort(reverse= True)
    return "".join(inter_result)


s = "1010111000"
print(largestMagical(s))
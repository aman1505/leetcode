def compressWord(word, k):
    # Write your code here
    stack =[]
    for ch in word:
        if stack and stack[-1][0] ==ch:
            if stack[-1][1] == k-1:
                stack.pop()
            else:
                stack.append([ch,1])
    result = []
    for ch,freq in stack:
        result+=[ch]*freq
    
    return "".join(result)


word="abbcccb"
k=3
print(compressWord(word,k))

def largestMagical(binString):
    # Write your code here
    bal = left =0
    inter_result = []
    
    for r in range(len(binString)):
        if binString[r] == '0':
            bal -= 1
        else:
            bal+=1
        
        if bal == 0:
            inter_result.append("1"+largestMagical(binString[left+1:r])+ "0")
            left = r+1
    
    inter_result.sort(reverse= True)
    return "".join(inter_result)
s = "1010111000"
print(largestMagical(s))
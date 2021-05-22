def Solution(A,K):
    n=len(A)
    for i in range(n -1):
        if(A[i]+1 < A[i+1]):        
            return False
        elif(A[i] not in range(K+1) or A[n-1] < K):            
            return False
    if(A[0]!=1 and A[n-1]!=K):
        return False
    
    else:
        return True

a=[1,2,2,2,2,2]
k=2
result=Solution(a,k)
print(result)
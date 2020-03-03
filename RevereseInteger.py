import math
num = 1230

rev_num = 0
if num < 0:
    num = num*-1
    result_sign = -1
else :
    result_sign = 1

while num > 0:
    rem = num%10
    num = math.floor(num / 10)
    rev_num = (rev_num*10) + rem

rev_num = rev_num*result_sign

if rev_num > (math.pow(2, 31)-1) or rev_num < -(math.pow(2, 31)):
    print(rev_num*result_sign)
else:
    print(rev_num * result_sign)
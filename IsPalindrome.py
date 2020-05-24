import math

original_num = 900
num = original_num
rev_num = 0

while num>0:
    rem = num%10
    num = math.floor(num / 10)
    rev_num = (rev_num*10) + rem

print(rev_num)
if original_num == rev_num:
    print(True)
else:
    print(False)
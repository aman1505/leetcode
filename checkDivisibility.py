def check_division(n):
    if n%4 == 0:
        return("Linked")
    elif n%6 ==0:
        return("In")
    elif n%4 == 0 and n%6 == 0:
        return ("LinkedIn")
    else:
        return n

print(check_division(24))
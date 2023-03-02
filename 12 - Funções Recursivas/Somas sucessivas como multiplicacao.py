def Somas(num1,num2):
    if num1==0 or num2==0:
        return 0
    else:
        if(num2<0):
            return -Somas(num1,-num2)
        else:
            return num1+Somas(num1,num2-1)
        
print(Somas(int(input()),int(input())))
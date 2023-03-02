x= int(input())
y= int(input())
z= int(input())
trol=0
if x==y==z:
    print("1")
    trol=1
if x!=y and y!=z:
    print("2")
if (x==y or x==z or z==y) and trol==0:
    print("3")
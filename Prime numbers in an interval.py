a=int(input("Enter the lower limit : "))
b=int(input("Enter the upper limit : "))
def Prime_In_Interval(x,y):
    for i in range (x,y+1):
        Prime(i)
def Prime(n):
    c=0
    for i in range (1,n+1):
        if n%i==0:
         c+=1
    if c==2:
           print(i)
    else:
         pass
Prime_In_Interval(a,b)
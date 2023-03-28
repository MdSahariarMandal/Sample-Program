x=int(input("Enter the number : "))
def Perfect(a):
    Sum=0
    for i in range(1,a):
        if(a%i==0):
            Sum=Sum+i
        else: continue    
    return Sum
k=int(Perfect(x))
if(k==x): print(x,"is a perfect number")
else: print("It is not a perfect number")
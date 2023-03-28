from cgi import print_arguments


a=int(input("Enter the number : "))
b=int(input("Enter the number : "))
def GCD(a,b):
    if(a%b==0):
     return b
    elif(b==0):
     exit 
    else:
     return GCD(b,(a%b))

k=int(GCD(a,b))
print("The greatest common divisor is : ",k)
from cgi import print_arguments


x=int(input("Enter the number : "))
y=int(input("Enter the number : "))
def GCD(a,b):
    if(a%b==0):
     return b
    elif(b==0):
     exit 
    else:
     return GCD(b,(a%b))

d = int(GCD(x,y))
print("The least common multiple is : ",lcm)

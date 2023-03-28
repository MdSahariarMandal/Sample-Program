P=int(input("Enter the principal  : "))
R=int(input("Enter the rate of interest : "))
T=int(input("Enter the  time  period in  years : "))
def Simple_Interest(a,b,c):
    return  (a*b*c)/100
print("The simple interest is : "+Simple_Interest(P,R,T))
print("The amount is : ",(P+Simple_Interest(P,R,T)))
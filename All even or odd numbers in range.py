a = int(input("Enter the lower limit : "))
b = int(input("Enter the upper limit : "))
print("Enter 1 for even number ")
print("Enter 2 for odd number  ")
c = int(input("Enter your choice : "))
A = []
def Even_Numbers_In_Range(x,y):
    for i in range (x,y+1):
        if i%2==0:
           A.append(i)
    print(A)
def Odd_Numbers_In_Range(x,y):
    for i in range (x,y+1):
        if i%2!=0:
          A.append(i)
    print(A)
if c==1:
 Even_Numbers_In_Range(a,b)
if c==2:
 Odd_Numbers_In_Range(a,b)
else:
    print("Invalid choice")
    exit()
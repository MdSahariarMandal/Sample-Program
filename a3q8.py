a=int(input("Enter the number : "))
k=int(a)
def Palindrome(n):
       d=0
       while(n>0):
         m=int(n%10)
         d=int((d*10)+m)
         n=int(n//10)
       return d  
     
c=int(Palindrome(a))
def Check(c):
    if(c==k):
        return True
    else:
        return False    

print(Check(c))
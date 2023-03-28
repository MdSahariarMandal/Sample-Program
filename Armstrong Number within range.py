a=int(input("Enter the lower limit : "))
b=int(input("Enter the upper limit : "))
def Armstrong_in_Range(x,y):
    for i in range (x,y+1):
        k=Armstrong(i)
        if k==i:
            print(k)
        else:
            continue
def Armstrong(d):
    s=0
    while d!=0:
        c=d%10
        s=s+(c**3)
        d=d//10
    return s
Armstrong_in_Range(a,b)
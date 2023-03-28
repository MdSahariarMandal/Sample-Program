#LIST=[1,2,3,4,5,6,7,8,8,8,1,2,5,4,4]
#print(LIST.count(1))
#print(LIST.count(4))
a=int(input("Enter the size of the list : "))
LIST=[]
def INPUT(b):
    print("Enter the elements of list : ")
    for i in range (b):
        j=int(input())
        LIST.append(j)
    print("The created list is : ",LIST)
INPUT(a)
'''def Count(r,x):
    c=0
    for i in range (r):
        if x in LIST:
          c=c+1
    print(c)

y=int(input("Enter the element to count for : "))
Count(a,y)'''
x = int(input("Enter the element to count for : "))
print("The element ", x , " appears " ,LIST.count(x), " times")
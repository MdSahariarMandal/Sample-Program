a=int(input("Enter the size of the list : "))
LIST=[]
def INPUT(b):
    print("Enter the elements of list : ")
    for i in range (b):
        j=int(input())
        LIST.append(j)
    print("The created list is : ",LIST)
INPUT(a)
def Duplicates(b):
    Duplicate_List=[]
    for i in LIST:
        n = LIST.count(i)
    if n>1:

Duplicates(a)

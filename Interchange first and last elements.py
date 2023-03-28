a=int(input("Enter the size of list : "))
LIST=[]
def LIST_Input(b):
    print("Enter the elements of the list : ")
    for i in range (b):
       j=input()
       LIST.append(j)
    print("The list created is : ",LIST)
def LIST_Elements_Swap(c):
    print("Value before swapping : ")
    print("The first element of the list is : ",c[0])
    print("The last element of the list is : ",c[len(c)-1])
    c[0],c[len(c)-1]=c[len(c)-1],c[0]
    print("Value after swapping : ")
    print("The first element of the list is : ",c[0])
    print("The last element of the list is : ",c[len(c)-1])
LIST_Input(a)
LIST_Elements_Swap(LIST)



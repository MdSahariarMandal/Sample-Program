a=int(input("Enter the size of the list : "))
List=[]
def List_Input(b):
    print("Enter the elements of list : ")
    for i in range (b):
        j=input()
        List.append(j)
    print("The list created is : ", List)
List_Input(a)
s=int(input("Enter the index of the first element to swap : "))
t=int(input("Enter the index of the second element to swap : "))
def Swap_Elements(x,y):
    print("Values before swapping : ")
    print("The initial value at index ",x," is : ",List[x])
    print("The initial value at index ",y," is : ",List[y])
    print("Values after swapping : ")
    List[x],List[y]=List[y],List[x]
    print("The initial value at index " ,x ," is : " , List[x])
    print("The initial value at index " , y ," is : " , List[y])
Swap_Elements(s,t)
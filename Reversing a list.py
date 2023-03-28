a=int(input("Enter the size of the list : "))
List=[]
def List_Input(b):
    print("Enter the elements of list : ")
    for i in range (b):
        j=int(input())
        List.append(j)
    print("The list created is : ", List)
List_Input(a)
#print(List[: : -1])

a=int(input("Enter the size of the list : "))
List=[]
def List_Input(b):
    print("Enter the elements of list : ")
    for i in range (b):
        j=int(input())
        List.append(j)
    print("The list created is : ", List)
def List_Multiply(b):
    s=1
    for i in range (b):
      s=s*List[i]
    print("The product of list elements is : ",s)
List_Input(a)
List_Multiply(a)
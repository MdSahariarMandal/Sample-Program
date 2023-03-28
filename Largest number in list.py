a=int(input("Enter the size of the list : "))
List=[]
def List_Input(b):
    print("Enter the elements of list : ")
    for i in range (b):
        j=int(input())
        List.append(j)
def Maximum_Element(b):
     c=List.remove(max(List))
     print(List)
     print(max(List))
List_Input(a)
Maximum_Element(a)

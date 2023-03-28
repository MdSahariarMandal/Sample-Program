a=int(input("Enter the size of the list : "))
List=[]
def List_Input(b):
    print("Enter the elements of list : ")
    for i in range (b):
        j=int(input())
        List.append(j)
List_Input(a)
def Even_Numbers(b):
    for i in range (b):
        if List[i]%2==0:
            print(List[i],end=" ")
        else:
         pass
Even_Numbers(a)
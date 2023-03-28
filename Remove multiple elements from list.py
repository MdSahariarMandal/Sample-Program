a=int(input("Enter the size of the list : "))
List=[]
def List_Input(b):
    print("Enter the elements of list : ")
    for i in range (b):
        j=int(input())
        List.append(j)
    print("The list created is : ",List)
List_Input(a)

c= int(input("Enter the number of elements to remove : "))
List1 = []
def List1_Input(b):
    print("Enter the elements of list : ")
    for i in range(b):
        j = int(input())
        List1.append(j)
    print("The elements to be removed are  : ", List1)
List1_Input(c)

def Remove_Elements(d):
    for i in range (d):
         if  List1[i] in List:
            List.remove(List1[i])
         else:
            pass
    print("The new list is : ",List)
Remove_Elements(c)
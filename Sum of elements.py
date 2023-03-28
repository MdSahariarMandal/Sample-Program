a=int(input("Enter the size of the list : "))
List=[]
def List_Input(b):
    print("Enter the elements of list : ")
    for i in range (b):
        j=int(input())
        List.append(j)
    print("The list created is : ", List)
def List_Sum(c):
    s=0
    for i in range (c):
        s=s+List[i]
    print(s)
List_Input(a)
List_Sum(a)
#print(sum(List))
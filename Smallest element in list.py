a=int(input("Enter the size of the list : "))
List=[]
def List_Input(b):
    print("Enter the elements of list : ")
    for i in range (b):
        j=int(input())
        List.append(j)
    print("The list created is : ", List)
'''def Smallest_in_List(b):
    MIN=List[0]
    for  i in  range (b):
        if List[i]<MIN:
            MIN=List[i]
    return MIN'''
List_Input(a)
#print("The smallest number in list is : ",Smallest_in_List(a))
print("The smallest number in list is : ",min(List))
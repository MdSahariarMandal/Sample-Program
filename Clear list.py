a=int(input("Enter the size of the list : "))
A=[]
def List_Input(b):
  print("Enter the elements : ")
  for i in range (b):
     j=input()
     A.append(j)
  print("The list created is : ",A)
'''def Clear_List(c):
    for i in range (c):
        A.pop()
    print(A)'''
List_Input(a)
A.clear()
print(A)
#Clear_List(a)

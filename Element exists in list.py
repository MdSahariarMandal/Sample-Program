a=int(input("Enter the size of the list : "))
A=[]
def List_Input(b):
  for i in range (b):
     j=input()
     A.append(j)
  print("The list created is : ",A)
def Search_Elements(c):
      if c in A:
          print("Value is present")
      else:
          print("Value is not present")
List_Input(a)
d=input("Enter the value to be searched : ")
Search_Elements(d)




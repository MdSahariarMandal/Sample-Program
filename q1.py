a = []
b = int(input("Enter number of elements : "))
print("Enter the elements of the list : ")
for i in range(b):
    c = input()
    a.append(c)
d = set(a)
print(d)

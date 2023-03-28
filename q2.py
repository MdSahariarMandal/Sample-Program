a = []
b = int(input("Enter the number of elements : "))
for i in range(b):
    c = int(input())
for i in range(b):
    for j in range(i + 1):
        d = int(i + j)
        a.append(d)
        print(a)

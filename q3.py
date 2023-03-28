a = input("Enter the string : ")
# print(len(a))
for i in a:
    b = a.count(i)
    print(str(i), ":", end=' ' + str(b))

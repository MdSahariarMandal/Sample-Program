def Table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)


n = int(input("Enter the number to print the tables for : "))
Table(n)

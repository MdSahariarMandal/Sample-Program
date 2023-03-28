print("      *      ")
print("   *  *  *   ")
print("*  *  *  *  *")
print("   *  *  *   ")
print("      *      ")
#b
side = int(input("Please Enter any Side of a Square  : "))
ch = '$'

print("Hollow Square Star Pattern") 
for i in range(side):
    for j in range(side):
        if(i == 0 or i == side - 1 or j == 0 or j == side - 1):
            print('%c' %ch, end = '  ')
        else:
            print(' ', end = '  ')
    print()
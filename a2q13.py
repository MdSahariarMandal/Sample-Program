def Collinear(x1, y1, x2, y2, x3, y3):
	a = int(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
	if (a == 0):
		return True
	else:
		return False

# Driver Code
x1=int(input("Enter the point : "))
y1=int(input("Enter the point : "))
x2=int(input("Enter the point : "))
y2=int(input("Enter the point : "))
x3=int(input("Enter the point : "))
y3=int(input("Enter the point : "))

Collinear(x1, y1, x2, y2, x3, y3)


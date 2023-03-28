def areaTriangle(a,b,c):  
 s = float((a + b + c) / 2  )
 area = float((s*(s-a)*(s-b)*(s-c)) ** 0.5)  
 print("The area of the triangle is %0.2f" %area)   

a = int(input('Enter first side: '))  
b = int(input('Enter second side: '))  
c = int(input('Enter third side: '))  
areaTriangle(a,b,c)
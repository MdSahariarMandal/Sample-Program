import copy
List=[2,4,5,6,7]
#List1=List[::]
'''for i in range (len(List)):
    List1.append(List)
print(List1)'''
#List1=List
#List1.extend(List)
List1 = copy.copy(List)
print(List)
print(List1)
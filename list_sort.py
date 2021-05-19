n = int(input("Number of elements in the list : "))
list_Og = []
for i in range(n):
    m = int(input("Enter the element"))
    list_Og.append(m)

list_Og.sort()

print("The sorted list is as follows :")
print(list_Og)
import numpy as np


def unique(list1):
    list_2 = []
    for i in (list_1):
        if int(list_1.count(i)) == 1 :
            list_2.append(i)
    print("The first 2  non-repeating numbers from the list are : ")
    print(list_2[:2])


n = int(input("Number of elements in the list : "))
list_1 = []
for i in range(n):
    m = int(input("Enter the element : "))
    list_1.append(m)

unique(list_1)

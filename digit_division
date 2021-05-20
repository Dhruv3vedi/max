import numpy as np


def digit_list(n):
    digits = [int(x) for x in str(n)]
    x = np.array(digits)
    x = np.unique(x)
    return x


def isDivisible(n, list1):
    for i in range(len(list1)):
        if n % list1[i-1] != 0:
            break
    #print(i)
    #print(len(list1))
    if i == len(list1) - 1:
        print("True")
    else:
        print("False")


m = int(input("Enter the number : "))
digit = digit_list(m)

print(digit)
isDivisible(m, digit)

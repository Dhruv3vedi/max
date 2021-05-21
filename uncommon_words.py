
def list_unique(list1, list2):
    arr = list1 + list2
    arr1 =[]
    for i in arr:
        if int(arr.count(i) == 1):
            arr1.append(i)

    print("The non repeating words in the two strings are : ")
    print(arr1)


list1 = []
list2 = []
str1 = input("Enter the first string: ")
str1 = str1.lower()
str2 = input("Enter the second string: ")
str2 = str2.lower()

list1 = str1.split()
list2 = str2.split()
list_unique(list1, list2)

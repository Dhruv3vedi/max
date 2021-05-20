def pattern(n):
    for i in range(0, n):
        if (i + 1) % 2 == 0:
            k = i + 1
        else:
            k = i + 2

        for j in range(0, n - k):
            print(end=" ")

        for j in range(0, k):
            print("* ", end="")

        # ending line after each row
        print("\r")


m = int(input("Enter the number of rows: "))
pattern(m)

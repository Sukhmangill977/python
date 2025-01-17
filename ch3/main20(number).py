rows = int(input("Enter number of rows: "))
for i in range(rows, 0, -1):
    print("".join(str(j) for j in range(1, i + 1)))

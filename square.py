size = 5
i = 0

while i < size:
    j = 0
    while j < size:
        if i == 0 or i == size - 1 or j == 0 or j == size - 1:
            print("*", end="")
        else:
            print(" ", end="")
        j += 1
    print()
    i += 1
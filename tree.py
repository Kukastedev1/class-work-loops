height = 5
i = 0

# Tree leaves
while i < height:
    print(" " * (height - i - 1) + "*" * (2 * i + 1))
    i += 1

# Tree trunk
trunk_height = 2
i = 0
while i < trunk_height:
    print(" " * (height - 1) + "*")
    i += 1
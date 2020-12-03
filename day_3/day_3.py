trees_encountered = 0
current_pos = 0
f = open("input.txt", "r")
for line in f.readlines():
    if  line[current_pos] == '#':
        trees_encountered += 1
    current_pos += 3
    # The length of a line is always 32 characters
    # Since the trees repeat their pattern forever wrap around to the start
    current_pos %= 31
print(trees_encountered)

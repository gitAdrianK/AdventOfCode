# Steps in the form (moves right, moves down)
steps = (
    (1,1),
    (3,1),
    (5,1),
    (7,1),
    (1,2),
)
trees_encountered = [0] * len(steps)
f = open("input.txt", "r")
for line_counter, line in enumerate(f.readlines()):
    for step_counter, step in enumerate(steps):
        # Skip lines in case the "moves down" step is not 1
        if step[1] != 1 and line_counter % step[1] == 0:
            continue
        if  line[line_counter * step[0] % 31] == '#':
            trees_encountered[step_counter] += 1
print(trees_encountered)
result = 1
for trees in trees_encountered:
    result = result * trees 
print(result) 
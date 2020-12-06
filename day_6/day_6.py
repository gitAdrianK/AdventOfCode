f = open("input.txt", "r")
group = ""
count = 0
for line in f.readlines():
    if line == "\n":
        count += len(set(group))
        group = ""
    group += line.replace("\n", "")
count += len(set(group))
print(count)

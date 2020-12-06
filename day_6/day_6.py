f = open("input.txt", "r")
group = ""
count = 0
for line in f.readlines():
    if line == "\n":
        print(len(set(group)))
        count += len(set(group))
        group = ""
    group += line.replace("\n", "")
print(len(set(group)))
count += len(set(group))
print(count)

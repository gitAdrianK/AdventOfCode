f = open("input.txt", "r")
group = ""
count = 0
# [1,2,3,4] ∩ [3,4,5,6] = [3,4]
intersection_ = None
intersection_count = 0
for line in f.readlines():
    if line == "\n":
        count += len(set(group))
        group = ""
        intersection_count+= len(intersection_)
        intersection_ = None
        continue
    group += line.replace("\n", "")
    if intersection_ is None:
        intersection = set(group)
    else:
        intersection = intersection_.intersection(set(line.replace("\n", "")))
# Again, last line leaves the loop, so we count it manually
count += len(set(group))
intersection_count+= len(intersection_)
print(count, intersection_count)

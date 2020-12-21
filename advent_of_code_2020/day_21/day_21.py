import re
import collections

def solveDay21(input):
    # Setup
    p1 = 0
    p2 = ""
    allergens = {}
    ingredient_use_count = {}
    ingredients = set()
    regex = re.compile("(\w+)")
    f = open(input, "r")
    for line in list(f.readlines()):
        ingr_allerg = regex.findall(line)
        contains_at = ingr_allerg.index("contains")
        ingr = set(ingr_allerg[:contains_at])
        ingredients.update(ingr)
        for i in ingr:
            if i not in ingredient_use_count:
                ingredient_use_count[i] = 1
            else:
                ingredient_use_count[i] += 1
        allerg = set(ingr_allerg[contains_at + 1:])
        for a in allerg:
            if a not in allergens:
                allergens[a] = ingr
            else:
                allergens[a] = ingr.intersection(allergens[a])
    identified = set()
    identified_as = {}
    recentIdentified = None
    areAllIdentified = False
    while not areAllIdentified:
        areAllIdentified = True
        for e in allergens:
            len_ = len(allergens[e])
            if len_ == 1 and list(allergens[e])[0] not in identified:
                identified.add(list(allergens[e])[0])
                identified_as[e] = list(allergens[e])[0]
                recentIdentified = allergens[e]
                removeFromSets(allergens, recentIdentified)
            elif len_ > 0:
                areAllIdentified = False
    for diff in ingredients.difference(identified):
        p1 += ingredient_use_count[diff]
    #print(identified_as)
    od = collections.OrderedDict(sorted(identified_as.items()))
    for _, v in od.items():
        p2 += v + ","
    return (p1, p2[:-1])

def removeFromSets(allergens, recentIdentified):
    for e in allergens:
        allergens[e] = allergens[e].difference(recentIdentified)

assert((5, "mxmxvkd,sqjhc,fvjkl") == solveDay21("test_input.txt"))
print(solveDay21("input.txt"))

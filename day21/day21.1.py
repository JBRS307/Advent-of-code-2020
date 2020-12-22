with open('input.txt', 'r') as inputFile:
    arr = inputFile.read().splitlines()

foodDict = {}
safeIngredients = set()
allIngredients = []

for food in arr:
    ingredients, allergens = food.split(' (contains ')
    allergens = allergens[:-1]
    ingredients = ingredients.split()
    allIngredients.extend(ingredients)
    uniqueIn = set(ingredients)
    safeIngredients = safeIngredients.union(uniqueIn)
    allergens = allergens.split(', ')

    for allergen in allergens:
        if foodDict.get(allergen) is None:
            foodDict[allergen] = uniqueIn
        else:
            foodDict[allergen] = foodDict[allergen].intersection(uniqueIn)

safeIngredients = safeIngredients.difference(set(k for value in foodDict.values() for k in value))
safeCount = sum([ingriedient in safeIngredients for ingriedient in allIngredients])
print(f"Part 1: {safeCount}")
#print(foodDict)

while any([len(i) > 1 for i in foodDict.values()]):
    for a, i in foodDict.items():
        if len(i) == 1:
            alg = list(i)[0]
            for a2, i2 in foodDict.items():
                if a2 == a:
                    continue
                if len(i2) > 1:
                    if alg in i2:
                        foodDict[a2].remove(alg)

names = list(foodDict.keys())
names.sort()

print("Part 2:", ",".join([','.join(foodDict[i]) for i in names]))

#stolen, but very educational

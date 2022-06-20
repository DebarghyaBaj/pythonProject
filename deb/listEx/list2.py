thisList = list(("Apple", "Banana", "Cherry"))
myList = [1, 2, 3]
print(thisList)

thisList[1:3] = ["Debarghya", "Baj"]
print(thisList)

thisList.insert(1, "Squash")
print(thisList)

for x in range(len(thisList)):
    print(thisList[x])

thisList.extend(myList)
print(thisList)

for x in thisList:
    print(x)

thisList.remove("Apple")
print(thisList)

thisList.pop(1)
print(thisList)


mylist1 = ["Apple", "Banana", "Cherry"]
mylist2 = [1, 2, 3]
print(mylist1)

print(mylist1[1])
print(mylist1[-1])

print(len(mylist1))
mylist1[1] = "Mango"

mylistCopy = mylist1.copy()
mylist1.append("Donut")
print(mylist1)
print(mylistCopy)
print(mylistCopy.count(1))

mylist2.clear()
print(mylist2)



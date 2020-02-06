# list
mylist = [1, 2, 3]
mylist = ["string", 1, 2, 3, 23.2, True, 'asdf', [1, 2, 3]]
print(mylist)
print(len(mylist))
mylist = ["a", "b", "c"]
print(mylist[-1])
print(mylist[1:])
print(mylist[:2])

mylist = ["a", "b", "c", "d", "e"]
print("Before reassignment: ")
print(mylist)
mylist[0] = "NEW ITEM"
print("After reassignment:")
print(mylist)

mylist.append("New Item")
print(mylist)
mylist.append(["x", "y", "z"])
print(mylist)

list_two = ["x", "y", "z"]
mylist.extend(list_two)
print(mylist)
item = mylist.pop()
print(mylist)
print(item)
item1 = mylist.pop(0)
print(item1)
mylist.reverse()
print(mylist)
mylist = [4, 6, 1, 7, 43, 2]
mylist.sort()
print(mylist)
mylist = [1, 2, ["x", "y", "z"]]
print(mylist[2][1])

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix[0][0]

# LIST COMPREHENSION
first_col = [row[0] for row in matrix]
print(first_col)

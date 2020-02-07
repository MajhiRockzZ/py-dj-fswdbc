###############################
## COMPARISON OPERATORS #######
###############################

1 > 2
1 < 2
1 >= 1
1 <= 4
1 == 1
"hi" == "bye"
1 != 2

###############################
## LOGICAL OPERATORS ##########
###############################

(1 > 2) and (2 < 3)
(1 > 2) or (2 < 3)

if 1 < 2:
    print("yes!")

if 1 < 2:
    if 2 < 3:
        print("True!")

if 1 < 2:
    print("First Block")
    if 20 < 3:
        print("Second Block")
if 1 == 1:
    if 1 > 2:
        print("hello")
    elif 3 == 3:
        print("elif ran")
    else:
        print("last")

# For Loops
seq = [1, 2, 3, 4, 5, 6]

for item in seq:
    print(item)

d = {"Sam": 1, "Frank": 2, "Dan": 3}

for item in d:
    print(item)
    print(d[item])

mypairs = [(1, 2), (3, 4), (5, 6)]

for tup1, tup2 in mypairs:
    print(tup1)
    print(tup2)

# While Loop
i = 1

while i < 5:
    print("i is: {}".format(i))
    i = i + 1

for item in range(10):
    print(item)

x = [1, 2, 3, 4]

out = []
for num in x:
    out.append(num ** 2)
print(out)

out = [num ** 2 for num in x]
print(out)

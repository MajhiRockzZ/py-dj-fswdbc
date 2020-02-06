# Booleans
True
False

# Tuples
t = (1, 2, 3)
print(t[1])

t = ("a", True, 123)
print(t)

# t[0] = "NEW" ---> Tuples object not support item assignment

# Sets
x = set()

x.add(1)
x.add(2)
x.add(3)
x.add(4)
x.add(0.1)
x.add(4)
print(x)

l = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4]
converted = set(l)
print(converted)

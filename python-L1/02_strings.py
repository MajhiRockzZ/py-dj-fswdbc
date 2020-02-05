# Basics
'hello'
"hello"

"I'm a dog"

# Indexing
mystring = "abcdefg"
print(mystring[0])

# Slicing
print(mystring[2:])
print(mystring[:3])
print(mystring[:])
print(mystring[::])
print(mystring[::2])

# Basic Methods
x = mystring.upper()
print(x)
x = mystring.lower()
print(x)
x = mystring.capitalize()
print(x)
mystring = "Hello World"
x = mystring.split()
print(x)
x = mystring.split("e")
print(x)
x = mystring.split("o")
print(x)

# Print Formatting
x = "Insert another string here: {}".format("INSERT ME!")
print(x)
x = "Item One: {} Item Two: {}".format("dog", "cat")
print(x)
x = "Item One: {y} Item Two: {x}".format(x="dog", y="cat")
print(x)

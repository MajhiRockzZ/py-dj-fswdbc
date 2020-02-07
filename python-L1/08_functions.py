def my_func(param1="default"):
    """ THIS IS THE DOCSTRING """
    print("my first python function! {}".format(param1))


my_func()


def hello():
    print("hello")


hello()


def hello2():
    return "hello"


result = hello2()
print(result)


def addNum(num1, num2):
    if type(num1) == type(num2) == type(10):
        return num1 + num2
    else:
        return "Sorry, I need integers!"


result = addNum(2, 3)
print(result)
print(type(result))
result = addNum("2", "3")
print(result)
print(type(result))

mylist = [1, 2, 3, 4, 5, 6, 7, 8]

# Lambda Expression
evens1 = filter(lambda num: num % 2 == 0, mylist)

print(evens1)
print(list(evens1))

# Filter


def even_bool(num):
    return num % 2 == 0


evens = filter(even_bool, mylist)
print(evens)
print(list(evens))

st = "hello"
st.lower()
st.upper()
st.split()

tweet = "Go Sports! #Sports"
result = tweet.split("#")
print(result)

print("x" in [1, 2, 3])

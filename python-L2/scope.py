x = 25


def my_func():
    x = 50
    return x


print(x)
print(my_func())
my_func()
print(x)

# LOCAL
lambda x: x**2

# Enclosing function locals(EFL)
name = "This is a global name!"


def greet():
    name = "sammy"

    def hello():
        print("hello " + name)

    hello()


greet()
print(name)

x = 50


def func(x):
    print("x is: ", x)
    x = 1000
    print("local x changed to: ", x)


func(x)
print(x)


def global_func():
    # global x
    x = 1000
    return x


print("before function call, x is: ", x)
x = global_func()
print("after function call, x is: ", x)

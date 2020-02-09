s = "GLOBAL VARIABLE!"


def func():
    mylocal = 10
    print(locals())
    print(globals())


func()


def hello(name="Jose"):
    return "hello " + name


print(hello())

mynewgreet = hello
print(mynewgreet())


def hello1(name="jose"):
    print("THE HELLO() FUNCTION HAS BEEN RUN!")

    def greet():
        return "THIS STRING IS INSIDE GREET()"

    def welcome():
        return "THIS STRING IS INSIDE WELCOME!"

    print(greet())
    print(welcome())
    print("End of hello()")

    if name == "jose":
        return greet
    else:
        return welcome


x = hello1()
print(x)


def hello2():
    return "HI JOSE!"


def other(func):
    print("HELLO")
    # print(func())


other(hello2())


def new_decorator(func):

    def wrap_func():
        print("CODE HERE BEFORE EXECUTING FUNC")
        func()
        print("FUNC() HAS BEEN CALLED")

    return wrap_func


def func_needs_decorator():
    print("THIS FUNCTIONS IS IN NEED OF A DECORATOR!")


func_needs_decorator()

class Sample():
    pass


x = Sample()
print(x)


class Dog():

    # CLASS OBJECT ATTRIBUTE
    species = "mammal"

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name


mydog = Dog(breed="Lab", name="Sammy")
# otherdog = Dog(breed = "Huskie")
# print(otherdog.breed)
print(mydog.breed)
print(mydog.name)
print(mydog.species)


class Circle():
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return self.radius*self.radius * Circle.pi

    def set_radius(self, new_r):
        self.radius = new_r


my_c = Circle(4)
my_c.set_radius(999)
print(my_c.area)

# INHERITANCE


class Animal():

    def __init__(self):
        print("ANIMAL CREATED")

    def whoAmI(self):
        print("ANIMAL")

    def eat(self):
        print("EATING")


mya = Animal()
mya.whoAmI()
mya.eat()


class Cat(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("CAT CREATED")

    def sound(self):
        print("MEAOW")

    def eat(self):
        print("CAT EATING")


mycat = Cat()
mycat.whoAmI()
mycat.eat()
mycat.sound()


# SPECIAL METHODS

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title: {}, Author: {}, Pages: {}".format(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book")


b = Book("Python", "Sumesh", 200)
print(b)
print(len(b))

mylist = [1, 2, 3]
print(mylist)

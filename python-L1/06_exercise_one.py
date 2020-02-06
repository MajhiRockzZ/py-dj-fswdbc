# Problem One
s = "django"
print(s)

s[0]
s[-1]
s[:4]
s[1:4]
s[::-1]

# Problem Two
l = [3,7,[1,4,"hello"]]
l[2][2] = "goodbye"


# Problem Three
d1 = {"simple_key":"hello"}
d1["simple_key"]

d2 = {"k1":{"k2":"hello"}}
d2["k1"]["k2"]

d3 = {"k1":[{"nest_key":["this is deep",["hello"]]}]}
d3["k1"][0]["nest_key"][1][0]

# Problem Four
mylist = [1,1,1,1,1,1,2,2,2,2,3,3,3,3]

set(mylist)

# Problem Five
age = 4
name = "Sammy"

print("hello my dog's name is {a} and he is {b} year old.".format(a=name, b=age))

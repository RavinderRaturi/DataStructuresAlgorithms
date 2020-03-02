furit = ["apple", "banana", "cherry"]

print(furit)

furit[0] = "pear"

furit[-1] = "orange"

print(furit)


alist =['a','b','c','d','e','f']
print(alist)
alist [1:3] = ['y','z']
print(alist)

alist [3:5] = []

print(alist)

#string and inMutatable

greeting = "hello workld"

#greeting[1] = "j" # this will give you error.


# how to change hello workd to jello world

newGreeting = "J" + greeting[1:]

print(newGreeting)
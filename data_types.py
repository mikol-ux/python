import math 
# string
# first = "mike"
# last = "ike"
# all = [first, last]
# obb = {first, last}
# print(type(first) == int)
# print(type(first == int))
# print(isinstance(first, str))
# print(type(all))
# print(type(obb))
# constructor

# pizza = str("pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# concatination

first = "mike"
last = " oko"

# fullname = first + last
# print(fullname)
# fullname += "!"
# print(fullname)
# casting number to string

# decade = 1980
# print(type(1980))
# star = str(decade)
# print(type(star))
# multiline 
multiline = '''
how are you ?

missing you .
          

                         hope you are fine 

'''
# print(multiline)

# sentence = 'I\'m back at work!\t Hey!\n\nWhere\'s this at \\ located?'
# print(sentence)

# String Methods
print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("you", "hi"))
print(multiline)

print(len(multiline))
multiline += "                                                         "
multiline = "                            " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))
print(multiline.strip())

# build a menu 
title = "menu".upper()
print(title.center(20, "="))
print("Coffe".ljust(16, ".") + "$1".rjust(4))
print("muffin".ljust(16, ".") + "$1".rjust(4))
print("taffe and choco".ljust(16, ".") + "$1".rjust(4))
print("")

# string index
print(first[1])
print(first[-1])
print(first[0:-1])

# method boolean
print(first.startswith("m"))
print(first.endswith("k"))

# numeric 
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# float
gpa = 3.82
y = float(1.14)
print(type(gpa))

# complex type
comp = 5+3j
print(type(comp))
print(comp.real)
print(comp.imag)


# built in functions for numbers 
print(abs(gpa))
print(abs(gpa * -1))
print(round(gpa))
print(round(gpa, 1))


print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

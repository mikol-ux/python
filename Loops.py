# value = 1
# while value <= 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1

# value = 1
# while value <= 10:
#     value += 1
#     if value == 5:
#         continue
#     print(value)
# else:
#     print("value is now equals to " + str(value))

names = ["pascaline", "mikel", "nono", "favor"]
# print(names)
    
# for x in names:
#     print(x)


# for x in "mississipi":
#     print(x)

# for x in names:
#     if x == "nono":
#         break
#     print(x)



# for x in names:
#     if x == "nono":
#         continue
#     print(x)



# for x in range(8):
#     print(x)





# for x in range(4,8):
#     print(x)



# for x in range(2, 101, 2):
#     print(x)
# else:
#     print("its over")

actions = ["code", "dress", "eat"]
days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

# for name in names:
#     for action in actions:
#         print(name+" "+action+" ")


# for action in actions:
#     for name in names:
#         print(name+" "+action+" ")


for day in days:
    for action in actions:
        for name in names:
            print(name+" "+action+" "+ " on " + day)

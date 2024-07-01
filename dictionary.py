# # dictionary

# band = {
#     "vocals" : "plant",
#     "guiter": "page"
# }

# band2 = dict(vocals="plant", guiter="page")
# print(band)

# print(band2)

# print(type(band))
# print(len(band))
# print(band["vocals"])
# print(band.get("guiter"))
# print(band.keys())
# print(band.values())
# print(band.items())
# print(band.items())

# print("guiter" in band)
# print("tom" in band)
# band["vocals"] = "amampiano"
# band.update({"bass": "JJJ"})
# print(band)
# def sortarr(a,b):
#      newset = set(a+b)
#      newer =  list(sorted(newset))
#      newer.append(100)
#      return newset

# are = [1,23,4,4,5,6,7,1,1]
# p = [1,23,4,4,5,6,7,1,1,8,2,3]

# print(sortarr(are,p))

firstset = {1,2,3,4,5,6}
secondset = set((1,1,1,1,1, 1, 4, 8))
print( secondset)
print(sorted(secondset))

dupeset = {1, True, False, 0, 4, 5, 6, 7}
print(dupeset)


# check if a value is in a set
# print(4 in dupeset)
# print(8 in dupeset)


# add a new value in a set

dupeset.add(18)
print(dupeset)

# add element from one set to another 

morenums = {11, 12, 13, 14}
morenums.update(dupeset)
print(morenums)

one = {1, 2, 3}
two = {4, 5, 6}
sett = one.union(two)
print(sett)

# keeping only duplicates
one = {1, 2, 3, 4, 5, 6}
two = {4, 5, 6}
one.intersection_update(two)
print(one)
one = {1, 2, 3, 4, 5, 6}
two = {4, 5, 6}
one.difference_update(two)
print(one)













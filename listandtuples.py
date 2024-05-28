users = ["dave", "john", "sara"]
data = ["davesss", 13, True]
emptylist = []
print("dave" in emptylist)
print(users[0])
print(users[-2])
print(users.index("sara"))
print(len(users))
strings = [item for item in data if isinstance(item, str)]
secondstr = list(filter(lambda item: isinstance(item, str), data))
print(strings)
print(secondstr)
print(users[0:])
print(users[0:2])
users.pop()
users.append("elsa")
users += ["lime"]
print(users)
# users.extend(["six", "seven"])
# print(users)
# users.extend(data)
# print(users)


users.insert(0, "bob")
print(users)
users[0:0] = [23, 45]
print(users)
users[1:4] = [700, 6000, 300, 500]
print(users)
users.remove("lime")
print(users)

# del data
# print(data)

data.clear()
print(data)
patent = ["sid", "kim", "alex", "kim", "lassss"]
patent[1:2] = ["Ark", "Lin"]
patent.sort()
print(patent)
patent.sort(key=str.lower)
print(patent)



nums = [34, 4, 60, 78, 1, 0]
nums.reverse()
print(nums)
# nums.sort(reverse=True)
# print(nums)

print(sorted(nums, reverse=True))
print(nums)

mynum = nums.copy()
menum = list(nums)
manum = nums[:]

print(mynum)
print(menum)
print(manum)

# tuples

mytuple = tuple(("dave", 42, True))

anothertuple = (1, 45, 60)
print(mytuple)
print(type(mytuple))
print(anothertuple)
print(type(anothertuple))
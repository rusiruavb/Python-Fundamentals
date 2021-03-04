# holds key, value pairs
# mutable
dict1 = {1: 'JavaScript', 2: 'Phthon'}
print(dict1)

dict1[1] = 'Java'
print(dict1)

# add new value
dict1[3] = 'Ruby'
print(dict1)

# delete value
del dict1[1]
print(dict1)

print(dict1.pop(2))
print(dict1.popitem())

# get all keys
print(dict1.keys())
# get all value
print(dict1.values())
# get key value pair
print(dict1.items())
print(type(dict1))

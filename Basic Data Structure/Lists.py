# List
# List are heterogenous data types
# List are mutable - list can have different type of data
list1 = ['Rusiru', 22, 'SE']
print(list1)

# add data elements
list1.append((2.5, 'SLIIT'))  # -> this will create tuple
print(list1)

list1.extend((2, 'Royal'))
print(list1)

list1.insert(3, 'Example')
print(list1)

# delete data elements
del list1[3]
print(list1)

list1.remove('Rusiru')
print(list1)
print(list1[0:3])
print(list1[0:4:2])
print(list1[::-1])
print()

list2 = [1, 2, 85, 7, 128, 96, 78]
print(sorted(list2))
print(list2)
list2.sort(reverse=True)
print(list2)
print(list2.index(2))  # give the index of the element
print(list2.count(85))

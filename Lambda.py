# lambda is an one line anonymus function
x = lambda x: x + 5 # this lambda function will take an argument and add 5 to it and return
print(x(3)) # this will print 8 = 3 + 5

z = lambda x, y: x + y
print(z(12, 10))

# Map and filter
x = [2,3,4,21.45,6,63,454,5646]
mp = map(lambda i: i + 5, x)
print(list(mp))

mp1 = filter(lambda i: i % 2 == 0, x) # return only the even numbers in the list
print(list(mp1))
x = [4, True, 'Rusiru']
y = x[:] # copy list x to y
y = x # create reference from list x to y
x[0] = 'SLIIT'
print(x, y)
print()
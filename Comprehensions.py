x = [x + 5 for x in range(10)]
print(x)

y = [[i for i in range(5)] for j in range(10)] 
# first create an inner list which contains numbers 0 - 4 (using inner for loop)
# then create 10 more list which contains the inner list (using outter for loop)
print(y)

z = [i for i in range(10) if i % 5 == 0] 
# if remainder of the number after divided 5 is 0, then add that number to the list
print(z)

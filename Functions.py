def func(x):
  def func2():
    print(x)
  return func2

print(func(4)()) # this will print 4 and None
func(4)()

# *args and **kwargs
x = [1,78,5,632,45,5,12]
print(x)
print(*x)

# unpack operator
def func(x, y):
  print(x, y)

pairs = [(1,2), (6,8)]

for pair in pairs:
  # func(pair[0], pair[1])
  func(*pair)

# * => Tuple, List
# ** => Dictionary

def func1(*args, **kwargs):
  print(args, kwargs)

func1(1,3,45,5,7,78, one=1, two=4) # print => (1, 3, 45, 5, 7, 78) {'one': 1, 'two': 4}
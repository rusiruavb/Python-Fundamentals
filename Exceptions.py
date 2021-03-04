try:
  x = 8 / 0
except Exception as e:
  print(e)
finally:
  print('This is inside the finally block')

print('Hello this is after exception')
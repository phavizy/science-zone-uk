while True:
  print("This will happen infinitely!")

number = 100
lessThan10 = False
while not lessThan10:
  number = number - 1
  # could also use number -= 1
  if number < 10:
    lessThan10 = True

for iterator in range(10,-1,1):
  print(iterator)
print("Boom!")

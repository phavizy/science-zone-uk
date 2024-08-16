# Calculator application!

print("\
Calculator v1.0\n\
Which operation do you want to perform?\n\
1. Addition\n\
2. Subtraction\n\
3. Multiplication\n\
4. Division")

selection = input(">>> ")
if selection == "1":
  # addition
  number1 = int(input("First number: "))
  number2 = int(input("Second number: "))
  result = number1 + number2
  print("The result is: " + str(result))
  
elif selection == "2":
  # subtraction
  number1 = int(input("First number: "))
  number2 = int(input("Second number: "))
  result = number1 - number2
  print("The result is: " + str(result))

elif selection == "3":
  # multiplication
  number1 = int(input("First number: "))
  number2 = int(input("Second number: "))
  result = number1 * number2
  print("The result is: " + str(result))

elif selection == "4":
  # division
  number1 = int(input("First number: "))
  number2 = int(input("Second number: "))
  result = number1 / number2
  print("The result is: " + str(result))

else:
  print("Invalid selection.")

# Things to consider:
# You could use floats instead of ints in order to have your calculator support fractions
# You could, instead of repeating the same user input in every statement, move it to before the if statement. This avoids repetition and saves time.

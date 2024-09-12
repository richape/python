# My sample is totally incorrect.
#  for number in range(100):
#   if number * 3 == 0 and number * 5 == 0:
#     print("Fizzbuzz")
#   elif number * 3 == 0:
#     print("Fizz")
#   elif number * 5 == 0:
#     print("Buzz")

for number in range(1, 100):  # Corrected range to include 1 to 100
  if number % 3 == 0 and number % 5 == 0:  # Divisible by both 3 and 5
      print("FizzBuzz")
  elif number % 3 == 0:  # Divisible by 3
      print("Fizz")
  elif number % 5 == 0:  # Divisible by 5
      print("Buzz")
  else:
      print(number)  # If not divisible by 3 or 5, just print the number

# number % 3 == 0: This checks if number is divisible by 3.
# number % 5 == 0: This checks if number is divisible by 5.
# The condition number % 3 == 0 and number % 5 == 0 is checked first to handle numbers divisible by both 3 and 5 (like 15, 30, etc.).
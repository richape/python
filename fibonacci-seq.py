# The Fibonacci sequence is a series of numbers where each number (known as a Fibonacci number) is the sum of the two preceding ones, usually starting with 0 and 1. The sequence goes as follows:
# Write a Python function that generates the first n numbers of the Fibonacci sequence, where n is provided by the user.

# F(0) = 0
# F(1) = 1
# F(n) = F(n-1) + F(n-2) for n ≥ 2

def fibonacci(n):
  if n == 0:
    return[]
  elif n == 1:
    return[0]
  elif n == 2:
    return [0, 1]
  
  fib_sequence = [0, 1]
  
  while len(fib_sequence) < n:
    next_fib = fib_sequence[-1] + fib_sequence[-2]
    fib_sequence.append(next_fib)

  return fib_sequence

print(fibonacci(10))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

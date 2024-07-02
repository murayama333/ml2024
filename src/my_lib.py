# 4
def my_factorial(n):
  result = 1
  for i in range(1, n + 1):
    result = result * i
  return result

def my_permutation(n, r):
  return my_factorial(n) // my_factorial(n - r)

def my_combination(n, r):
  return my_permutation(n, r) // my_factorial(r)

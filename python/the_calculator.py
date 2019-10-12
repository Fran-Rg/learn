USE_TIME=0

def sum_two(a,b):
  global USE_TIME
  USE_TIME += 1
  return a+b

def substract_two(a,b):
  global USE_TIME
  USE_TIME += 1
  return a-b

def multiply_two(a,b):
  global USE_TIME
  USE_TIME += 1
  return a*b

def divide_two(a, b):
  global USE_TIME
  USE_TIME += 1
  return a/b
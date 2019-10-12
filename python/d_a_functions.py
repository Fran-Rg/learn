# model
# DECLARATION:
# def my_func(<IN_PARAMETER_1>, <IN_PARAMETER_2>, ...):
  # <CODE>
  # return <value>
# ...
# CALL:
# my_func(<GIVING_PARAMETER_1>, <GIVING_PARAMETER_2>)
# example
def hello(b):
  a=1+b
  return a

# A def is simply a process that takes input (or not*) and usually do something with these inputs to produce an output (or not). It's used in general for processes that need to be done many time with some differences.
#                   +-----------------------+
#         |         |     def          |
# Inputs  +-------->+                       +--------> Outputs
#         |         |     <DO SOMETHING>    |
#                   |                       |
#                   +-----------------------+
# For example, we could create a def that takes 2 inputs and return the sum of these 2 inputs
# We would define this function:
# Input: a and b
# Output: sum of a + b

# There are 2 parts required to use a function: "declaration" and "call".
# DECLARATION: this is where we define how the def is going to work. Like a recipe, we declare how many inputs we require and what we are going to do with these inputs. The declaration only happens ONCE in the code.
def sum_two(a,b):
  # the input names are like variable names. It makes no sense for the program, it is only for the coder
  return a+b

# CALL: this is where we use the function. It can be used many time. The way to call a def is <NAME OF FUNCTION>(). The brackets is the way to call functions
result = sum_two(10, 20)
print(f"result = sum_two(10, 20) : {result}")
result = sum_two(60, 80)
print(f"result = sum_two(60, 80) : {result}")

# Python comes with many functions already made for us. For example one we've been using already is "print()" which takes for input some values and print them to the console
# Look at the other functions that exists: https://docs.python.org/3.7/library/functions.html

# We are going to use:
# - int(<STRING>)
# - type(<VARIABLE>)
a_int_string = "1111";
a_int_int = int("1111")
def details(input_1):
  print(f"I received: {input_1}")
  print(f"It is of type: {type(input_1)}")
  print(f"") # To have a clear blank space
  return 0 # The return value is optional
# ATTENTION: declaring a function, does NOTHING except declaring a recipe


details("TOTO")
a_var = "SOMETHING"

details(a_var)
details(2134)

print(f"Comparing:")
details(a_int_string)
print(f"with")
details(a_int_int)

#functions can be encapsulated one inside the others:
def returning_string():
  return "THIS IS RETURNED FROM THE FUNCTION"


def first_and_last_of_string(in_string):
  out_string = in_string[0]+in_string[-1]
  return out_string

details( first_and_last_of_string( returning_string() ) )

# a def returns when the key word "return <VALUE>" is found.
def return_in_middle():
  print(f"BEFORE RETURN")
  return 0;
  print(f"AFTER RETURN")

return_in_middle();
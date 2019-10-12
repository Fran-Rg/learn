# we have been working on "small" projects where every functions and work are independant one from the other
# But at some point we need to get organized and build re-usable and modular code
# for this we use modules
# visualize a python file like a room. Inside this room you declare some variables and some functions

MY_VAR=0
# A variable inside a module and outside a function is said to be "global" (here MY_VAR is global)
# if you want to access and modify a global variable inside a function you need to specify "global <VARIABLE>" at the beginning of the function:

def my_function():
  global MY_VAR
  print("HELLO, +1 to MY_VAR")
  MY_VAR += 1

# Now MY_VAR == 1

# A project is made of multiple rooms where each room communicate between each other.

# Let's make a module "the_calculator" which is going to provide functions to add_two, substract_two, multiply_two, divide_two, which each takes 2 inputs and make the change. Every time we use a function, a counter is incremented
# first we create a file called "the_calculator.py" and inside we create these 4 functions with the global variable: (see the file the calculator.py)

# now here we want to use these functions
# first we need to access that room, e.g. import that module:
import the_calculator

# we can access module variables (but cannot modify them):
print(the_calculator.USE_TIME)

# we can access each function by doing:
the_sum = the_calculator.sum_two(4,5)

print(the_sum)
print(the_calculator.USE_TIME)

# you can also import specific function from the module:
# import sum_two from the_calculator
# sum_two(2,3) 

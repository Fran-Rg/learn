#model
# for <CHANGING_VAR> in <LIST>:
#   <CODE>
#

# for is used the most used loop. It initialize a variable, then test the condition, as long as the condition is valid, it runs the code inside the brackets then apply the modification

for i in [1,3,4,5]:
  print(f"in the loop, i: {i}")
range(0,5)==[0,1,2,3,4]
for i in range(0,3):
  # range(0,3) == [0,1,2]
  # range(0,6,2) == [0,2,4]
  #https://docs.python.org/3/library/functions.html#func-range
  print(f"i:{i}")

# this loop is extremely used to iterate through an array but NOT modify the array:
one_array = ["PA", "PO", "PI", "PU"]
# len(one_array) is an int that represent the size of the array
# Here len(one_array) == 4
for thing in one_array:
  print(f"thing: {thing}")

print(f"one_array: {one_array}")

#to force to go out of a loop, use the keyword "break;"
for thing in one_array:
  print(f"Second time, thing: {thing}")
  break
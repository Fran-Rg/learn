# EDITION
# PLAYING WITH NUMBERS
my_var_int = 1234
my_var_int = my_var_int + 20
print(f"my_var_int: {my_var_int}")
my_var_int += 20# my_var_int = my_var_int + 20
print(f"my_var_int: {my_var_int}")
my_var_int = my_var_int - 75 # substraction
print(f"my_var_int: {my_var_int}")
my_var_int = my_var_int / 2 # division
print(f"my_var_int: {my_var_int}")
my_var_int = my_var_int * 10 # multiplication
print(f"my_var_int: {my_var_int}")
my_var_int = my_var_int % 10 # modulo. Modulo is the rest when removing the operator to the value as much as possible and keep a positive value
# Example 20-10=10, we can still remove 10, 10-10=0, we can't remove 10 anymore so 20 % 10 = 0
# 21 % 10 = 21 - 10 - 10 = 1, 21 % 10 = 1
print(f"my_var_int: {my_var_int}")

print("") # SPACING

# PLAYING WITH STRINGS
my_var_string = "S_A"
print(f"my_var_string 1: {my_var_string}")
o_var = "S_other"
my_var_string = o_var + my_var_string # "S_A" + "S_other"
print(f"my_var_string 2: {my_var_string}")
my_var_string += o_var
print(f"my_var_string 3: {my_var_string}")
my_var_string = "S_A"
# my_var_string[0] = "B" # BREAKS

print("") # SPACING

# PLAYING WITH ARRAY
my_var_array = [1, 2, 3, 4]
my_var_array.append("a")
print(f"my_var_array after append: {my_var_array}")
my_var_array[0] = "AAA"
print(f"my_var_array after edition at index: {my_var_array}")
my_var_array = [ 123 ]+my_var_array + [9,8]
print(f"my_var_array after addition: {my_var_array}")
my_var_array = my_var_array[1:4] #this "slice" the array and keep between the 2 indexes
print(f"my_var_array after slice: {my_var_array}")

print("") # SPACING

# PLAYING WITH DICT
my_var_dict = {
  'a':'TITI'
}
my_var_dict["a"] = "TOTO"
print(f"my_var_dict 1: {my_var_dict}")
my_var_dict["b"] = "BLABLA"
print(f"my_var_dict 2: {my_var_dict}")
my_var_dict["b"] = "APPLE"
print(f"my_var_dict 3: {my_var_dict}")

# Showing message while your code is running is really important
# It helps debugging and understanding what's happening
print(f"HELLO")

# START
# "XX = <VALUE>" announce that we need a new variable that is going to be called XX with value.
# The name of a variable is only for the coder, it makes no changes to the program


print("") # SPACING

# NOTHING
my_var_nothing = None

#BOOLEAN
my_var_bool = True
my_var_bool = False

print("") # SPACING

# INTEGERS
my_var_int = 1234 #my_now contains the value 1234 inside, an int (integer)
my_var_int = 1235 #now my_contains the value 1235, there's no way to get back the previous value 1234
print(f"my_var_int: {my_var_int}")
my_var_int=10.5 #these are "float" number, decimal numbers
print(f"my_var_int: {my_var_int}")

# STRING
my_var_string = "This is a string" # in Python "TEXT" and 'TEXT' is the same. It's for strings
print(f"my_var_string: {my_var_string}")
print(f"my_var_string[0]: {my_var_string[0]}")
print(f"my_var_string[1]: {my_var_string[1]}")
# print(f"my_var_int[1]: {my_var_int[1]}") # BREAKS

print("") # SPACING

########################
# CONTAINERS
########################

# ARRAY
my_var_array = [1, "TOTO", 7, 4, 5, "HELLO"]
print(f"my_var_array: {my_var_array}")

print(f"my_var_array[0]: {my_var_array[0]}")
print(f"my_var_array[1]: {my_var_array[1]}")
print(f"my_var_array[2]: {my_var_array[2]}")
print(f"my_var_array[-1]: {my_var_array[-1]}")
# print(f"my_var_array[100]: {my_var_array[100]}") # BREAKS

print("") # SPACING

# Dictionnary/dict/object
my_var_dict = {
  1: "int_1",
  "key_1": "value_1",
  "Francois": "Regnoult"
}
print(f"my_var_dict: {my_var_dict}")
print(f"my_var_dict['key_1']: {my_var_dict['key_1']}")

my_accessor = "key_1"
print(f"my_var_dict[my_accessor]: {my_var_dict[my_accessor]}")
print(my_var_dict["key_2"])
# print(f"my_var_dict['key_2']: {my_var_dict['key_2']}") # BREAKS

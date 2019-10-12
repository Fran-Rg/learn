#model
# if <CONDITION 1> :
#   #goes here if CONDITION 1 is True
#   <CODE>
# else if <CONDITION 2> :
#   #goes here if CONDITION 1 is not True but CONDITION 2 is True
#   <CODE>
# else:
#   goes here if CONDITION 1 and CONDITION 2 are False
#   <CODE>
# 
# only "if" is required, else if/else are optional

# CONDITION is everything that returns True/False (or 0/not 0, bad practice)
# Boolean directly
if True :
  print(f"True is True")
else:
  print(f"True is not False, so never see this message")

# Equal: represented as "=="
toto = 2
if 2 == toto :
  print(f"2 == toto")

# Difference: represented as "!="
if 2 != toto :
  print(f"2 != toto, never see this message")
else:
  print(f"else for '2 != toto'")

# equal and difference are only used with int or strings
# To compare an array you need to compare each element of the array from one to the other
# you can show a print out a condition
print(f"2 == toto: {2 == toto}")


# Superior/Inferior: only for numbers, represented as '<' (strictly inferior) / '>' (strictly superior) and '<=' (inferior) / '>=' (superior)
if 10 < toto :
  print(f"10 < toto, never see this message")
elif 1 < toto :
  print(f"1 < toto")
if 2 <= toto :
  print(f"2 >= toto")

# EVERY CONDITION can be "negated" by putting 'not' at the beginning. What was False become True and opposite
# == negated is !=, != negated is ==
# < negate is >=, etc
if not 10 < toto :
  print(f"! 10 < toto")


# you can encapsulate if/else
if 2 <= toto :
  if 2 < toto :
    print(f"2 <= toto AND 2 < toto, never see this message")
  else:
    print(f"2 <= toto AND 2 >= toto")

# MULTI CONDITION:
# AND: <CONDITION 1> and <CONDITION 2>, to be True the 2 conditions have to be True
if  1 < toto and 4 > toto :
  print(f"1 < toto && 4 > toto")
# OR: <CONDITION 1> or <CONDITION 2>, to be True one of the conditions must be True
if  False or True  :
  print(f"False || True")
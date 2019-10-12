# while <CONDITION>:
#   <CODE>

# This loop is a mix between a if/else and a for. It will test the condition, if it's true, run the code, test the condition again, if it's still true, run again and etc. It will only get out of the loop once the condition is false

#CAREFUL: if the condition never get false, you can get locked in the loop
toto=14
tata=654
while toto < tata :
  print(f"toto: {toto} - tata: {tata}")
  toto = toto * 2


# you can also break out of the loop with "break;"
toto=13
tata=110
while toto != tata:
  print(f"breaking toto: {toto} - tata: {tata}")
  toto = toto * 2
  if toto > tata:
    break

#this loop is less used
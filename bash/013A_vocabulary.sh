#3 OPTIONAL OPTIONS/ARGUMENTS:
# options that change the way it behaves slightly. There are options that require a value
# and others that don't
# example:
grep -v toto.txt # '-v' does NOT require a value
cut -c 10 # '-c' requires a value
cut -c=10 # Same as previous line

# The same option can be used usually in 2 ways:
# LONG '--WORD (VALUE)': Option word + value of long option
# example:
grep --ignore-case
grep --before-context=20
grep --before-context 20 #The equal is optional
# SHORT '-LETTER (VALUE)': the first letter of
grep -i
grep -B 20
grep -B20 # the space is optional

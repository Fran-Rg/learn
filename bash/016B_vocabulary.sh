# imagine you have a file with some text
# to see the content you can do
less FILE
# or
cat FILE | less

# What's the difference? in the first case, the file is an argument
# In the second case cat FILE creates some STDOUT and less receives it as STDIN

# find other programs using advantage of STDIN

# what does the following do?
grep -a | less
# WHY?

# Some programs work really well with STDIN some others don't... you'll get to know
# as you experiment
example:
ls *.txt | rm # delete all the ".txt" files
echo 1234 | kill # that does NOT work. kill doesn't like STDIN

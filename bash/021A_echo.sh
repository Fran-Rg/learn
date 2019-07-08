# echo is THE tool to show things

# No quotes: best for showing variable/env variables
echo hello you # it doesn't look right and might cause other problems
echo $PATH

# Double quotes RECOMMENDED
echo "hello you"
# variables in double quotes are "interpreted"
echo "$PATH"
echo "this is the path: $PATH"

# Single quotes
echo 'hello you'
# variables in single quotes aren't interpreted
echo '$PATH'

# echo doesn't take any STDIN
echo 123 | echo 456 # only shows 456

# if you want to use " inside the echo you need to use \"
echo "This is a quote->\", the \ will not show"

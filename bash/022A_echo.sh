# echo can print some nested commands using back quotes:
echo "this is in my dir: `ls` <--"

# can be useful for example for putting things together:
echo "$HOME`ls /tmp/*.txt`"

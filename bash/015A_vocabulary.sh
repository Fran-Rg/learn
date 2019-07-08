# 5 STDERR:
# This is the ERROR OUTPUT of a program if it runs badly
# example
grep -azerty # should show something like: "grep: invalid option -- z ..."
# There's NOTHING showing in human eye the difference between STDOUT and STDERR
# But STDERR isn't passed to pipes |

# To redirect STDERR to a file you need to use:
PROGRAM 2> FILE # '2' means STDERR

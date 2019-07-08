# Try to find 1 or 2 programs that have a required argument
# To be totally sure that there's a required argument, run the program without and
# it should show you "usage: PROGRAM XYZ"
# example:
find #displays
# usage: find [-H | -L | -P] [-EXdsx] [-f path] path ... [expression]
       # find [-H | -L | -P] [-EXdsx] -f path [path ...] [expression]
# Because "path" is NOT under '[]' then it is a required argument

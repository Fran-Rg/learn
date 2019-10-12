# create a module called "my_logging" inside it create a global variable LOG_LEVEL set to 1 at first and 5 functions: debug, info, warning, error, set_level
# debug, info, warning, error take one input. They print that input only if:
# debug: print if LOG_LEVEL is >= 0
# info: print if LOG_LEVEL is >= 1
# warning: print if LOG_LEVEL is >= 2
# error: print if LOG_LEVEL is >= 3

# set_level takes one integer input and if it's between 0 and 3 it will update the LOG_LEVEL value that module should accept the following code:

# import my_logging

# my_logging.debug("hello 0") # should NOT be seen
# my_logging.info("hello 1")
# my_logging.warning("hello 2")


# my_logging.set_level(3)
# my_logging.info("hello 3") # should NOT be seen
# my_logging.warning("hello 4") # should NOT be seen
# my_logging.error("hello 5")


# my_logging.set_level(0)
# my_logging.debug("hello 6")
# my_logging.error("hello 7")
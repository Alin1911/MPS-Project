from functions import *
import random

# Test the function

global res # global variable to store the result
res = -1    # initialize to -1
for k in range(1000): # 1000 tests
    for i in range(100):    # 100 functions (all of them)
        random_list_numers = [random.uniform(0, 1) for _ in range(random.randint(1, 100))] # random list of numbers each time
        code = 'res = function' + str(i) + '(*random_list_numers)' # create the string to execute
        exec(code) # execute the command (res = function0(*random_list_numers))

import os
import random

def choose_operator():
    operators = ['+=', '-=', '*=', '= result and', '= result or']
    return operators[random.randint(0, len(operators) - 1)]

def build_header():
    header = 'import functools\n'
    header += 'import math\n'
    header += 'import numpy as np\n'
    header += '\n'
    return header

def build_body(func, nr_templates):
    body = ''
    if(func == 'AND'):
        body += '\tresult = args[0]\n'
        body += '\tfor i in range(len(args) - 1):\n'
        body += '\t\tresult = result and args[i]\n'
        body +='\treturn result #and\n\n'
    elif(func == 'OR'):
        body += '\tlambda_reduce = functools.reduce(lambda x, y : x or y, args)\n\t'
        body += 'return lambda_reduce # or\n\n'
    elif(func == 'FOR'):
        body += '\tmy_list = []\n\t'
        body += 'cycle_index = 0\n\t'
        body += 'for i in  range(1, ' + str(random.randint(0, 500)) + '):\n\t\t'
        body += 'my_list.append(i + args[cycle_index])\n\t\t'
        body += 'cycle_index += 1\n\t\t'
        body += 'if cycle_index == len(args):\n\t\t\t'
        body += 'cycle_index = 0\n\t'
        body += 'lambda_sum = functools.reduce(lambda x, y: x + y, my_list)\n\t'
        body += 'lambda_avg = lambda_sum / len(my_list)\n\t'
        body += 'result = (lambda_avg - min(my_list)) / (max(my_list) - min(my_list))\n\t'
        body += 'return result #for\n\n'
    elif(func == 'WHILE'):
        body += '\tvalue = index = result = 0\n\t'
        body += 'magic_number = ' + str(random.randint(1, 500)) + '\n\t'
        body += 'while  value <= magic_number:\n\t\t'
        body += 'value += ' + str(random.randint(1, 10)) + '\n\t\t'
        body += 'if index == len(args):\n\t\t\t'
        body += 'index = 0\n\t\t'
        body += 'result += args[index]\n\t\t'
        body += 'index += 1\n\t'
        body += 'return ((result / index) % 100) / 100 #while\n\n'
    elif(func == 'LOG'):
        body += '\tmyval =  np.sum(args)\n\t'
        body += 'if myval <= 0:\n\t\t'
        body += 'return 0\n\t'
        body += 'result = math.fabs((math.log(myval % 10))  % 10 / 10)\n\t'
        body += 'return result #log\n\n'
    elif(func == 'SIN'):
        body += '\tlambda_sum = functools.reduce(lambda x, y: x + y - ' + str(random.randint(1, 100)) + ', args)\n\t'
        body += 'result = math.fabs(math.sin(lambda_sum))\n\t'
        body += 'return result #sin\n\n'
    elif(func == 'COS'):
        body += '\tlambda_sum = functools.reduce(lambda x, y: x + y, args)\n\t'
        body += 'result = math.fabs(math.cos(lambda_sum))\n\t'
        body += 'return result #cos\n\n'
    elif(func == 'TAN'):
        body += '\tlambda_sum = functools.reduce(lambda x, y: x + y, args)\n\t'
        body += 'result = math.fabs(math.tan(lambda_sum) % 0.999)\n\t'
        body += 'return result #tan\n\n'
    elif(func == 'ONE'):
            body += '\treturn 1.0\n\n'
    elif(func == 'DEFAULT'):
        body += '\treturn 0.5\n\n'
    elif(func == '1-1/(1+x)'):
        body += '\tmyval = max(args)\n\t'
        body += 'return 1 - 1/(1 + myval) #ecuation\n\n'
    elif(func == '1 - 1 / (e ^ (2x) + 1)'):
        body += '\tmyval = max(args)\n\t'
        body += 'return 1 - 1 / (math.exp(2 * myval) + 1) #ecuation\n\n'
    elif(func == 'AVG'):
        body += '\tlambda_sum = functools.reduce(lambda x, y: x + y, args)\n\t'
        body += 'result = lambda_sum / len(args)\n\t'
        body += 'if result >= 1:\n\t\t'
        body += 'result = result % 0.999\n\t'
        body += 'return result #AVG\n\n'
    elif(func == 'MEAN'):
        body += '\tresult = np.mean(args) % 0.999\n\t'
        body += 'return result #mean\n\n'
    elif(func == 'RANDOM'):
        body += '\treturn ' + str(random.uniform(0, 1)) + ' #random\n\n'
    elif(func == 'IF'):
        body += '\tmyval = min(args)\n\t'
        magic = random.uniform(0, 1)
        body += 'magic_number = ' + str(magic) + '\n\t'
        body += 'return myval if  myval <= magic_number else ' + str(random.uniform(magic, 1)) + ' #IF\n\n'
    elif(func == 'COMPOSITE_FUNCTION'): #composite a function from a set of templates
        body += '\tresult = ' + str(random.uniform(0, 1)) +'\n\t'
        nr_of_calls = random.randint(1, 3) #number of aux functions that makes composite func.
        for _ in range(nr_of_calls):
            body += 'result ' + choose_operator() + ' math.fabs(function' + str(random.randint(0, nr_templates)) + \
                    '(*args))\n\t'
        body += 'result = math.fabs(result) % 0.999\n\t'
        body += 'return result #composite function\n\n'
    else:
        body += '\tprint(\'UNKNOWN METHOD ! :( \')\n\t'
        body += 'return 0.0\n\n'
    return body

def generate_functions(functions, number_of_functions):
    #Genereaza un modul (fisier) .py cu functii
    name = 'functions.py'
    if os.path.exists(name):
        if os.path.isfile(name):
            print("File already exists !")
        elif os.path.isdir(name):
            print("There is a directory with this name !")
        else:
            print("Error occured at " + name +' crreation')
        return 0 #somehow is ok if we have the file. Continue to execute.
    else:
        with open(name, 'w') as fp:
            # make imports in new file
            fp.write(build_header())
            #create template functions for each type and compose them ( funcions[-1] = COMPOSITE_FUNCTION) )
            for j in range(number_of_functions):
                definition = 'def function' + str(j) + '(*args):\n'
                body = build_body(functions[j], len(functions) - 2) \
                    if j < len(functions) else build_body(functions[-1], len(functions) - 2)
                fp.write(definition + body)
    try:
        err = False
        import functions
    except:
        err = True
        print('This module was not found')
    finally:
        if err != False:
            return -1 # Cracked :(

def generator():
    # implelented functions
    type_of_function = ['AND', 'OR', 'IF', 'FOR', 'LOG', 'WHILE', 'SIN', 'COS', 'TAN', 'DEFAULT', 'ONE', '1-1/(1+x)', '1 - 1 / (e ^ (2x) + 1)', 'AVG', 'MEAN', 'RANDOM', 'COMPOSITE_FUNCTION']
    total_number_functions_to_generate = 100 #set number of functions to generate ( must be > len(type_of_function) )
    generate_functions(type_of_function, total_number_functions_to_generate)
    
if __name__ == '__main__':
    print('FUNCTIONS GENERATOR')
    generator()
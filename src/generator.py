import os
import random
import math

def get_args(args):
    args_string_list = ''
    args_string_list += '\tlist_args = ['
    for i in range(args):
        args_string_list += 'x' + str(i) + ', ' if (i < args - 1) else 'x' + str(i)
    args_string_list += ']\n\t'
    return args_string_list

def build_body(func, args):
    body = ''
    if(func == 'AND'):
        body += '\tresult = x0 and x1\n'
        for i  in range(args - 2):
            body += '\tresult = result and x' + str(i + 2) + '\n'
        body +='\treturn result\n\n'
    elif(func == 'OR'):
        body += get_args(args)
        body += 'lambda_reduce = functools.reduce(lambda x, y : x or y, list_args)\n\t'
        body += 'return lambda_reduce\n\n'
    #FOR: multiplies each number with a random argument, adds the numbers, then normalizes the result, based on the created list
    elif(func == 'FOR'):
        body += '\tmy_list = []\n\t'
        body += 'list_args = ['
        for i in range(args):
            body += 'x' + str(i) + ', ' if (i < args - 1) else 'x' + str(i)
        body += ']\n\t'
        body += 'for _ in  range(' + str(random.randint(0, 500)) + '):\n\t\t'
        body += 'my_list.append(random.randint(0, '+ str(len(func)) +') * list_args[random.randint(0, len(list_args) - 1)])\n\t'
        body += 'lambda_sum = functools.reduce(lambda x, y: x + y, my_list)\n\t'
        body += 'lambda_avg = lambda_sum / len(my_list)\n\t'
        body += 'result = (lambda_avg - min(my_list)) / (max(my_list) - min(my_list))\n\t'
        body += 'return result\n\n'
    elif(func == 'WHILE'):
        body += get_args(args)
        body += 'value = index = result = 0\n\t'
        body += 'magic_number = random.randint(1, 500)\n\t'
        body += 'while  value != magic_number:\n\t\t'
        body += 'value = random.randint(0, 500)\n\t\t'
        body += 'if index == len(list_args):\n\t\t\t'
        body += 'index = 0\n\t\t'
        body += 'result += list_args[index]\n\t\t'
        body += 'index += 1\n\t'
        body += 'return ((result / index) % 100) / 100\n\n'
    elif(func == 'LOG'):
        body += get_args(args)
        body += 'myval = list_args[random.randint(0, len(list_args) - 1)] + 1\n\t'
        body += 'result = (math.log(myval % 10)) / 2.200\n\t'
        body += 'return result\n\n'
    elif(func == 'SIN'):
        body += get_args(args)
        body += 'mychoices = [list_args[random.randint(0, len(list_args) - 1)] for _ in list_args ]\n\t'
        body += 'lambda_sum = functools.reduce(lambda x, y: x + y, mychoices)\n\t'
        body += 'result = math.fabs(math.sin(lambda_sum))\n\t'
        body += 'return result\n\n'
    elif(func == 'COS'):
        body += get_args(args)
        body += 'mychoices = [list_args[random.randint(0, len(list_args) - 1)] for _ in list_args ]\n\t'
        body += 'lambda_sum = functools.reduce(lambda x, y: x + y, mychoices)\n\t'
        body += 'result = math.fabs(math.cos(lambda_sum))\n\t'
        body += 'return result\n\n'
    elif(func == 'TAN'):
        body += get_args(args)
        body += 'mychoices = [list_args[random.randint(0, len(list_args) - 1)] for _ in list_args ]\n\t'
        body += 'lambda_sum = functools.reduce(lambda x, y: x + y, mychoices)\n\t'
        body += 'result = math.fabs(math.tan(lambda_sum) % 0.999)\n\t'
        body += 'return result\n\n'
    elif(func == 'ONE'):
            body += '\treturn 1.0\n\n'
    elif(func == 'DEFAULT'):
        body += '\treturn 0.5\n\n'
    elif(func == '1-1/(1+x)'):
        body += get_args(args)
        body += 'myval = random.randint(0, len(list_args))\n\t'
        body += 'return 1 - 1/(1 + myval)\n\n'
    elif(func == '1 - 1 / (e ^ (2x) + 1)'):
        body += get_args(args)
        body += 'myval = random.randint(0, len(list_args))\n\t'
        body += 'return 1 - 1/(math.exp(2 * myval) + 1)\n\n'
    elif(func == 'AVG'):
        body += get_args(args)
        body += 'lambda_sum = functools.reduce(lambda x, y: x + y, list_args)\n\t'
        body += 'result = lambda_sum / len(list_args)\n\t'
        body += 'if result >= 1:\n\t\t'
        body += 'result = result % 0.999\n\t'
        body += 'return result\n\n'
    elif(func == 'MEAN'):
        body += get_args(args)
        body += 'result = np.mean(list_args) % 0.999\n\t'
        body += 'return result\n\n'
    elif(func == 'RANDOM'):
        body += '\treturn random.uniform(0, 1)\n\n'
    elif(func == 'IF'):
        body += get_args(args)
        body += 'myval = list_args[random.randint(0, len(list_args) - 1)]\n\t'
        body += 'magic_number = random.uniform(0, 1)\n\t'
        body += 'return myval if  myval <= magic_number else random.uniform(magic_number, 1)\n\n'
    # elif()
    else:
        body += '\tprint(\'ERROR ! :( \')\n\t'
        body += 'return 0.0\n\n'
    return body
    # type_of_function = ['AND', 'OR', 'IF', 'FOR', 'WHILE', 'LOG', 'SIN', 'COS', 'TAN', 'DEFAULT', 'ONE', '1-1/(1+x)', '1- 1/(e^(2x) + 1)', 'AVG', 'MEAN', 'RANDOM', 'COMPLEX]

def generate_functions(functions, number_of_functions, max_args):
    #Genereaza un modul (fisier) .py cu functii
    name = 'functions.py'
    if os.path.exists(name):
        if os.path.isfile(name):
            print("File already exists !")
        elif os.path.isdir(name):
            print("There is a directory with this name !")
        else:
            print("Error occured at " + name +'.py crreation')
        return 0 #somehow is ok if we have the file. Continue to execute.
    else:
        with open(name, 'w') as fp:
            base_name = 'function'
            index = 1
            arguments = 5
            arg = ''
            # my_func = random.randint(0, len(functions)) #index type -> or/and/if/for etc
            my_func = 2
            # make imports in new file
            header = 'import random\n'
            header += 'import functools\n'
            header += 'import math\n'
            header += 'import numpy as np\n'
            header += '\n'
            fp.write(header)
            # build arguments: x0, x1, ...
            for j in range(number_of_functions):
                arg = ''
                arguments = random.randint(1, max_args)
                for i in range(arguments):
                    arg += 'x' + str(i) + ', ' if (i < arguments - 1) else 'x' + str(i)
                # definition of function: function1, function2, ...
                definition = 'def function' + str(j) + '(' + arg + '):\n'
                body = build_body(functions[j], arguments) if j < len(functions) else build_body(functions[-1], arguments)
                'return myval if  myval <= magic_number else random.uniform(magic_number, 1)\n\n'
                fp.write(definition + body)
    try:
        err = False
        import functions
    except:
        err = True
        print('This module was not found')
    finally:
        if err == False:
            pass
            # print (functions.function1(1000,2,0.3,400,200000))
        else:
            return -1 # Cracked :(

def main():
    # implelented functions
    type_of_function = ['AND', 'OR', 'IF', 'FOR', 'WHILE', 'LOG', 'SIN', 'COS', 'TAN', 'DEFAULT', 'ONE', '1-1/(1+x)', '1 - 1 / (e ^ (2x) + 1)', 'AVG', 'MEAN', 'RANDOM', 'COMPOSITE_FUNCTION']
    used_functions = 10
    total_number_functions_to_generate = 100
    total_number_functions_to_generate = max(total_number_functions_to_generate,  len(type_of_function) - 1 )

    generate_functions(type_of_function, random.randint(len(type_of_function) - 1,total_number_functions_to_generate), random.randint(1, 10))

if __name__ == '__main__':
    print('FUNCTIONS GENERATOR')
    main()
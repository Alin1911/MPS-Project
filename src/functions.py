import functools
import math
import numpy as np

def function0(*args):
	result = args[0]
	for i in range(len(args) - 1):
		result = result and args[i]
	return result #and

def function1(*args):
	lambda_reduce = functools.reduce(lambda x, y : x or y, args)
	return lambda_reduce # or

def function2(*args):
	myval = min(args)
	magic_number = 0.28415417891681405
	return myval if  myval <= magic_number else 0.29540010057460936 #IF

def function3(*args):
	my_list = []
	cycle_index = 0
	for i in  range(1, 140):
		my_list.append(i + args[cycle_index])
		cycle_index += 1
		if cycle_index == len(args):
			cycle_index = 0
	lambda_sum = functools.reduce(lambda x, y: x + y, my_list)
	lambda_avg = lambda_sum / len(my_list)
	result = (lambda_avg - min(my_list)) / (max(my_list) - min(my_list))
	return result #for

def function4(*args):
	value = index = result = 0
	magic_number = 307
	while  value <= magic_number:
		value += 3
		if index == len(args):
			index = 0
		result += args[index]
		index += 1
	return ((result / index) % 100) / 100 #while

def function5(*args):
	myval =  np.sum(args)
	result = (math.log(myval % 10))  % 10 / 10
	return result #log

def function6(*args):
	lambda_sum = functools.reduce(lambda x, y: x + y - 24, args)
	result = math.fabs(math.sin(lambda_sum))
	return result #sin

def function7(*args):
	lambda_sum = functools.reduce(lambda x, y: x + y, args)
	result = math.fabs(math.cos(lambda_sum))
	return result #cos

def function8(*args):
	lambda_sum = functools.reduce(lambda x, y: x + y, args)
	result = math.fabs(math.tan(lambda_sum) % 0.999)
	return result #tan

def function9(*args):
	return 0.5

def function10(*args):
	return 1.0

def function11(*args):
	myval = max(args)
	return 1 - 1/(1 + myval) #ecuation

def function12(*args):
	myval = max(args)
	return 1 - 1 / (math.exp(2 * myval) + 1) #ecuation

def function13(*args):
	lambda_sum = functools.reduce(lambda x, y: x + y, args)
	result = lambda_sum / len(args)
	if result >= 1:
		result = result % 0.999
	return result #AVG

def function14(*args):
	result = np.mean(args) % 0.999
	return result #mean

def function15(*args):
	return 0.185383622998464 #random

def function16(*args):
	result = 0.7315752284551892
	result = result or function15(*args)
	result += function7(*args)
	result *= function14(*args)
	result *= function4(*args)
	result = result and function13(*args)
	result = result and function1(*args)
	result %= function13(*args)
	result -= function5(*args)
	result %= function7(*args)
	result *= function12(*args)
	result *= function13(*args)
	result *= function9(*args)
	result += function6(*args)
	result *= function4(*args)
	result -= function11(*args)
	result -= function15(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function17(*args):
	result = 0.20281245341059662
	result *= function4(*args)
	result %= function8(*args)
	result = result or function3(*args)
	result -= function6(*args)
	result = result and function2(*args)
	result *= function4(*args)
	result *= function0(*args)
	result -= function7(*args)
	result -= function3(*args)
	result = result or function13(*args)
	result += function10(*args)
	result = result and function10(*args)
	result = result or function2(*args)
	result *= function7(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function18(*args):
	result = 0.9064226250379295
	result *= function7(*args)
	result = result or function10(*args)
	result %= function5(*args)
	result *= function6(*args)
	result = result or function15(*args)
	result -= function2(*args)
	result = result and function0(*args)
	result %= function0(*args)
	result += function12(*args)
	result *= function1(*args)
	result = result or function9(*args)
	result = result or function10(*args)
	result += function2(*args)
	result %= function12(*args)
	result += function2(*args)
	result *= function4(*args)
	result = result and function15(*args)
	result %= function2(*args)
	result %= function12(*args)
	result *= function2(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function19(*args):
	result = 0.4874112345101953
	result = result or function10(*args)
	result %= function6(*args)
	result += function6(*args)
	result %= function8(*args)
	result = result or function3(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function20(*args):
	result = 0.49155539882451604
	result = result or function9(*args)
	result %= function0(*args)
	result += function12(*args)
	result *= function14(*args)
	result = result and function10(*args)
	result %= function11(*args)
	result %= function6(*args)
	result %= function12(*args)
	result -= function11(*args)
	result = result and function5(*args)
	result *= function7(*args)
	result %= function3(*args)
	result %= function3(*args)
	result += function5(*args)
	result *= function5(*args)
	result -= function1(*args)
	result %= function0(*args)
	result *= function5(*args)
	result = result or function13(*args)
	result -= function13(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function21(*args):
	result = 0.3035961346292836
	result = result or function14(*args)
	result += function1(*args)
	result += function8(*args)
	result *= function14(*args)
	result += function2(*args)
	result = result or function5(*args)
	result += function12(*args)
	result %= function0(*args)
	result += function8(*args)
	result = result and function9(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function22(*args):
	result = 0.49534982923024773
	result = result or function7(*args)
	result %= function6(*args)
	result = result or function2(*args)
	result %= function9(*args)
	result %= function4(*args)
	result *= function9(*args)
	result = result and function9(*args)
	result %= function15(*args)
	result += function4(*args)
	result = result or function10(*args)
	result %= function8(*args)
	result -= function13(*args)
	result = result and function7(*args)
	result += function12(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function23(*args):
	result = 0.6554396342200762
	result = result and function4(*args)
	result = result and function7(*args)
	result -= function4(*args)
	result %= function11(*args)
	result = result or function5(*args)
	result -= function4(*args)
	result -= function7(*args)
	result = result or function10(*args)
	result -= function2(*args)
	result %= function11(*args)
	result -= function11(*args)
	result -= function1(*args)
	result += function1(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function24(*args):
	result = 0.6181060348456805
	result -= function9(*args)
	result = result or function15(*args)
	result %= function14(*args)
	result -= function0(*args)
	result += function9(*args)
	result -= function0(*args)
	result = result or function2(*args)
	result *= function12(*args)
	result -= function7(*args)
	result += function13(*args)
	result = result and function1(*args)
	result *= function9(*args)
	result += function15(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function25(*args):
	result = 0.510440627272396
	result = result or function11(*args)
	result %= function2(*args)
	result *= function14(*args)
	result = result and function5(*args)
	result %= function15(*args)
	result *= function12(*args)
	result += function8(*args)
	result = result or function2(*args)
	result %= function8(*args)
	result += function3(*args)
	result *= function15(*args)
	result = result and function6(*args)
	result -= function1(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function26(*args):
	result = 0.34965161871051387
	result *= function10(*args)
	result = result and function14(*args)
	result += function8(*args)
	result += function8(*args)
	result %= function13(*args)
	result = result and function9(*args)
	result %= function7(*args)
	result = result or function11(*args)
	result -= function10(*args)
	result = result and function9(*args)
	result += function14(*args)
	result -= function11(*args)
	result += function14(*args)
	result = result and function3(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function27(*args):
	result = 0.6032973457057986
	result = result and function3(*args)
	result = result or function11(*args)
	result *= function8(*args)
	result = result and function0(*args)
	result = result and function7(*args)
	result += function6(*args)
	result = result or function13(*args)
	result %= function7(*args)
	result -= function3(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function28(*args):
	result = 0.007844989710382166
	result += function12(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function29(*args):
	result = 0.17350294729464533
	result -= function5(*args)
	result = result and function11(*args)
	result = result and function2(*args)
	result -= function4(*args)
	result += function5(*args)
	result += function2(*args)
	result *= function11(*args)
	result = result and function4(*args)
	result = result and function15(*args)
	result *= function15(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function30(*args):
	result = 0.904614725100382
	result *= function8(*args)
	result += function11(*args)
	result *= function11(*args)
	result = result and function8(*args)
	result = result and function4(*args)
	result -= function1(*args)
	result *= function11(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function31(*args):
	result = 0.20596408657211684
	result *= function6(*args)
	result += function9(*args)
	result = result and function3(*args)
	result = result and function5(*args)
	result -= function8(*args)
	result -= function7(*args)
	result -= function3(*args)
	result = result or function1(*args)
	result += function5(*args)
	result %= function9(*args)
	result = result and function3(*args)
	result *= function14(*args)
	result += function9(*args)
	result += function9(*args)
	result = result and function5(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function32(*args):
	result = 0.4194795332005563
	result *= function7(*args)
	result = result or function7(*args)
	result %= function7(*args)
	result %= function7(*args)
	result = result or function5(*args)
	result = result or function8(*args)
	result -= function5(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function33(*args):
	result = 0.09386572486530609
	result = result or function7(*args)
	result %= function7(*args)
	result = result and function6(*args)
	result = result or function2(*args)
	result *= function15(*args)
	result %= function13(*args)
	result = result and function9(*args)
	result *= function10(*args)
	result -= function5(*args)
	result %= function9(*args)
	result -= function8(*args)
	result = result or function2(*args)
	result -= function0(*args)
	result = result or function14(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function34(*args):
	result = 0.641538613130707
	result += function0(*args)
	result %= function11(*args)
	result = result or function7(*args)
	result %= function13(*args)
	result = result and function1(*args)
	result = result or function12(*args)
	result -= function13(*args)
	result += function15(*args)
	result += function0(*args)
	result = result and function9(*args)
	result -= function5(*args)
	result = result and function14(*args)
	result += function6(*args)
	result += function11(*args)
	result = result and function14(*args)
	result += function14(*args)
	result = result and function5(*args)
	result %= function4(*args)
	result += function15(*args)
	result %= function7(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function35(*args):
	result = 0.5997436908779099
	result = result and function10(*args)
	result *= function12(*args)
	result *= function5(*args)
	result = result or function7(*args)
	result += function15(*args)
	result *= function8(*args)
	result += function11(*args)
	result = result or function1(*args)
	result -= function4(*args)
	result %= function7(*args)
	result = result and function1(*args)
	result = result and function2(*args)
	result += function4(*args)
	result = result or function11(*args)
	result %= function3(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function36(*args):
	result = 0.3134096109777553
	result -= function6(*args)
	result %= function10(*args)
	result %= function3(*args)
	result = result or function15(*args)
	result %= function8(*args)
	result += function8(*args)
	result %= function13(*args)
	result %= function2(*args)
	result = result and function15(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function37(*args):
	result = 0.8074340487077809
	result = result or function15(*args)
	result -= function7(*args)
	result = result or function15(*args)
	result %= function4(*args)
	result = result and function4(*args)
	result -= function4(*args)
	result %= function5(*args)
	result *= function12(*args)
	result %= function6(*args)
	result *= function15(*args)
	result += function11(*args)
	result %= function0(*args)
	result -= function5(*args)
	result -= function14(*args)
	result = result or function6(*args)
	result += function9(*args)
	result += function2(*args)
	result = result or function12(*args)
	result = result and function13(*args)
	result *= function13(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function38(*args):
	result = 0.8645326239927469
	result = result and function5(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function39(*args):
	result = 0.4535322711892109
	result *= function0(*args)
	result *= function2(*args)
	result = result and function4(*args)
	result = result and function12(*args)
	result %= function7(*args)
	result %= function1(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function40(*args):
	result = 0.2747337845171681
	result = result or function8(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function41(*args):
	result = 0.6312239366382517
	result += function12(*args)
	result += function15(*args)
	result %= function2(*args)
	result = result or function6(*args)
	result = result and function15(*args)
	result = result and function4(*args)
	result *= function12(*args)
	result = result or function9(*args)
	result *= function0(*args)
	result += function1(*args)
	result += function10(*args)
	result -= function5(*args)
	result += function4(*args)
	result = result or function15(*args)
	result = result or function11(*args)
	result *= function4(*args)
	result *= function15(*args)
	result = result or function14(*args)
	result = result and function2(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function42(*args):
	result = 0.07202272815816202
	result %= function14(*args)
	result -= function4(*args)
	result += function8(*args)
	result += function7(*args)
	result = result or function15(*args)
	result %= function0(*args)
	result += function3(*args)
	result = result or function1(*args)
	result *= function4(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function43(*args):
	result = 0.8392011275173785
	result *= function5(*args)
	result -= function0(*args)
	result -= function11(*args)
	result *= function14(*args)
	result %= function1(*args)
	result = result and function5(*args)
	result = result and function7(*args)
	result *= function6(*args)
	result %= function15(*args)
	result = result or function13(*args)
	result = result or function11(*args)
	result = result or function5(*args)
	result = result or function1(*args)
	result = result or function15(*args)
	result *= function1(*args)
	result -= function9(*args)
	result = result and function13(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function44(*args):
	result = 0.1658020196098794
	result *= function6(*args)
	result %= function14(*args)
	result = result or function2(*args)
	result *= function5(*args)
	result *= function0(*args)
	result *= function7(*args)
	result -= function1(*args)
	result = result or function2(*args)
	result *= function12(*args)
	result = result and function13(*args)
	result = result or function9(*args)
	result += function2(*args)
	result += function14(*args)
	result *= function11(*args)
	result = result or function12(*args)
	result = result and function14(*args)
	result *= function2(*args)
	result -= function1(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function45(*args):
	result = 0.6145497071821834
	result = result or function1(*args)
	result -= function10(*args)
	result += function9(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function46(*args):
	result = 0.9981645720469328
	result += function1(*args)
	result *= function5(*args)
	result += function5(*args)
	result = result and function7(*args)
	result = result and function3(*args)
	result = result or function14(*args)
	result %= function8(*args)
	result -= function14(*args)
	result = result and function1(*args)
	result -= function3(*args)
	result += function5(*args)
	result += function2(*args)
	result = result or function9(*args)
	result %= function5(*args)
	result -= function8(*args)
	result = result or function1(*args)
	result -= function4(*args)
	result %= function9(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function47(*args):
	result = 0.12001412272516543
	result *= function10(*args)
	result = result and function6(*args)
	result += function12(*args)
	result = result and function0(*args)
	result *= function10(*args)
	result %= function15(*args)
	result = result or function0(*args)
	result += function10(*args)
	result %= function8(*args)
	result = result or function8(*args)
	result = result and function0(*args)
	result %= function13(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function48(*args):
	result = 0.14035488965768794
	result *= function10(*args)
	result += function9(*args)
	result += function15(*args)
	result += function8(*args)
	result = result and function6(*args)
	result *= function0(*args)
	result %= function8(*args)
	result += function8(*args)
	result %= function6(*args)
	result %= function3(*args)
	result *= function9(*args)
	result += function3(*args)
	result = result or function8(*args)
	result *= function2(*args)
	result += function15(*args)
	result %= function12(*args)
	result %= function12(*args)
	result -= function5(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function49(*args):
	result = 0.5509691178640703
	result = result and function0(*args)
	result -= function12(*args)
	result = result or function15(*args)
	result = result and function8(*args)
	result *= function0(*args)
	result = result and function15(*args)
	result %= function8(*args)
	result -= function9(*args)
	result -= function9(*args)
	result = result and function12(*args)
	result += function0(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function50(*args):
	result = 0.7820894789221432
	result = result and function13(*args)
	result = result or function2(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function51(*args):
	result = 0.8998063626248852
	result -= function3(*args)
	result %= function14(*args)
	result = result or function14(*args)
	result *= function2(*args)
	result -= function11(*args)
	result %= function5(*args)
	result -= function1(*args)
	result = result and function11(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function52(*args):
	result = 0.1543394136541696
	result -= function0(*args)
	result = result and function7(*args)
	result %= function5(*args)
	result += function14(*args)
	result = result and function2(*args)
	result -= function6(*args)
	result *= function13(*args)
	result %= function1(*args)
	result *= function13(*args)
	result += function13(*args)
	result -= function1(*args)
	result = result or function13(*args)
	result = result or function13(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function53(*args):
	result = 0.1923351849582433
	result -= function3(*args)
	result = result and function12(*args)
	result += function13(*args)
	result *= function1(*args)
	result = result and function14(*args)
	result %= function5(*args)
	result *= function6(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function54(*args):
	result = 0.4202211249934593
	result = result and function7(*args)
	result = result or function13(*args)
	result *= function0(*args)
	result = result and function13(*args)
	result -= function4(*args)
	result %= function5(*args)
	result %= function9(*args)
	result = result or function15(*args)
	result -= function5(*args)
	result = result and function7(*args)
	result = result or function13(*args)
	result -= function14(*args)
	result = result and function10(*args)
	result += function7(*args)
	result -= function5(*args)
	result += function15(*args)
	result += function8(*args)
	result += function9(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function55(*args):
	result = 0.6135286488143179
	result *= function5(*args)
	result *= function6(*args)
	result *= function15(*args)
	result = result and function11(*args)
	result %= function7(*args)
	result = result or function6(*args)
	result *= function12(*args)
	result -= function9(*args)
	result *= function5(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function56(*args):
	result = 0.01345233964203596
	result = result or function13(*args)
	result += function8(*args)
	result *= function11(*args)
	result = result and function13(*args)
	result += function6(*args)
	result %= function2(*args)
	result = result and function7(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function57(*args):
	result = 0.7414184771149942
	result -= function6(*args)
	result = result or function3(*args)
	result = result or function2(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function58(*args):
	result = 0.5308075403938348
	result = result and function9(*args)
	result %= function10(*args)
	result %= function7(*args)
	result %= function4(*args)
	result = result or function2(*args)
	result = result and function14(*args)
	result *= function1(*args)
	result += function6(*args)
	result %= function6(*args)
	result += function12(*args)
	result %= function13(*args)
	result %= function0(*args)
	result *= function6(*args)
	result %= function12(*args)
	result *= function5(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function59(*args):
	result = 0.8876897714483509
	result -= function3(*args)
	result += function8(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function60(*args):
	result = 0.22699538184725665
	result += function5(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function61(*args):
	result = 0.9473844747822956
	result = result and function13(*args)
	result -= function5(*args)
	result -= function9(*args)
	result = result and function8(*args)
	result = result and function11(*args)
	result %= function1(*args)
	result -= function12(*args)
	result = result and function13(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function62(*args):
	result = 0.10004659042195752
	result = result or function12(*args)
	result %= function2(*args)
	result %= function13(*args)
	result -= function1(*args)
	result += function10(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function63(*args):
	result = 0.8392434455261316
	result = result or function14(*args)
	result %= function7(*args)
	result %= function2(*args)
	result -= function7(*args)
	result *= function14(*args)
	result += function7(*args)
	result += function1(*args)
	result -= function9(*args)
	result += function8(*args)
	result %= function5(*args)
	result = result and function6(*args)
	result *= function13(*args)
	result -= function14(*args)
	result = result or function1(*args)
	result %= function8(*args)
	result %= function11(*args)
	result -= function14(*args)
	result = result and function12(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function64(*args):
	result = 0.5174381049490554
	result = result and function14(*args)
	result += function10(*args)
	result = result and function6(*args)
	result %= function6(*args)
	result = result or function14(*args)
	result += function1(*args)
	result = result or function1(*args)
	result -= function4(*args)
	result %= function11(*args)
	result *= function8(*args)
	result = result or function2(*args)
	result *= function3(*args)
	result %= function3(*args)
	result %= function11(*args)
	result = result and function8(*args)
	result *= function10(*args)
	result = result or function1(*args)
	result *= function4(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function65(*args):
	result = 0.7361846814304347
	result -= function11(*args)
	result = result and function5(*args)
	result += function6(*args)
	result += function4(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function66(*args):
	result = 0.9539654903376861
	result = result and function1(*args)
	result = result and function10(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function67(*args):
	result = 0.9040799965359669
	result %= function8(*args)
	result = result or function7(*args)
	result %= function10(*args)
	result *= function10(*args)
	result = result and function3(*args)
	result = result and function14(*args)
	result = result or function15(*args)
	result = result or function3(*args)
	result *= function14(*args)
	result = result and function15(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function68(*args):
	result = 0.6875981295286752
	result += function0(*args)
	result = result and function1(*args)
	result -= function8(*args)
	result *= function14(*args)
	result -= function0(*args)
	result -= function15(*args)
	result *= function6(*args)
	result = result and function7(*args)
	result = result and function9(*args)
	result += function2(*args)
	result %= function14(*args)
	result *= function10(*args)
	result *= function0(*args)
	result -= function14(*args)
	result -= function1(*args)
	result = result and function13(*args)
	result *= function13(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function69(*args):
	result = 0.7751947218615806
	result %= function8(*args)
	result = result or function0(*args)
	result %= function10(*args)
	result -= function8(*args)
	result -= function9(*args)
	result *= function2(*args)
	result = result and function4(*args)
	result = result and function15(*args)
	result %= function0(*args)
	result = result or function3(*args)
	result = result and function4(*args)
	result = result or function7(*args)
	result %= function14(*args)
	result -= function7(*args)
	result = result and function3(*args)
	result %= function4(*args)
	result = result and function6(*args)
	result += function13(*args)
	result *= function6(*args)
	result %= function13(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function70(*args):
	result = 0.5754505838957387
	result = result or function10(*args)
	result += function13(*args)
	result *= function3(*args)
	result += function15(*args)
	result *= function2(*args)
	result %= function11(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function71(*args):
	result = 0.9526777041812586
	result += function9(*args)
	result -= function11(*args)
	result += function2(*args)
	result = result and function10(*args)
	result += function0(*args)
	result += function13(*args)
	result %= function11(*args)
	result = result and function12(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function72(*args):
	result = 0.556826069447831
	result += function4(*args)
	result %= function9(*args)
	result *= function1(*args)
	result += function5(*args)
	result = result or function2(*args)
	result += function13(*args)
	result = result and function2(*args)
	result %= function3(*args)
	result += function10(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function73(*args):
	result = 0.00846350887454761
	result *= function7(*args)
	result += function5(*args)
	result += function12(*args)
	result -= function2(*args)
	result %= function7(*args)
	result = result and function10(*args)
	result = result and function14(*args)
	result -= function13(*args)
	result %= function7(*args)
	result = result and function3(*args)
	result = result or function13(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function74(*args):
	result = 0.8162370876315898
	result *= function9(*args)
	result += function0(*args)
	result += function0(*args)
	result = result or function2(*args)
	result -= function10(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function75(*args):
	result = 0.36405538523606784
	result += function1(*args)
	result = result or function2(*args)
	result -= function4(*args)
	result += function4(*args)
	result %= function12(*args)
	result += function9(*args)
	result = result and function3(*args)
	result *= function10(*args)
	result = result and function5(*args)
	result -= function3(*args)
	result = result or function1(*args)
	result *= function2(*args)
	result = result or function6(*args)
	result = result and function14(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function76(*args):
	result = 0.03840606949301606
	result %= function4(*args)
	result -= function12(*args)
	result = result or function6(*args)
	result = result or function12(*args)
	result -= function15(*args)
	result *= function8(*args)
	result *= function15(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function77(*args):
	result = 0.5381538440450356
	result *= function1(*args)
	result *= function6(*args)
	result += function8(*args)
	result -= function4(*args)
	result -= function5(*args)
	result *= function7(*args)
	result += function9(*args)
	result += function3(*args)
	result *= function7(*args)
	result = result and function1(*args)
	result += function8(*args)
	result *= function13(*args)
	result -= function15(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function78(*args):
	result = 0.85388483517595
	result %= function13(*args)
	result *= function4(*args)
	result %= function3(*args)
	result = result or function15(*args)
	result *= function14(*args)
	result -= function6(*args)
	result -= function6(*args)
	result -= function7(*args)
	result -= function5(*args)
	result %= function6(*args)
	result = result and function8(*args)
	result = result and function15(*args)
	result += function9(*args)
	result -= function6(*args)
	result %= function0(*args)
	result -= function10(*args)
	result *= function9(*args)
	result -= function7(*args)
	result = result and function9(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function79(*args):
	result = 0.6559719783332337
	result %= function14(*args)
	result = result and function1(*args)
	result -= function14(*args)
	result *= function11(*args)
	result = result and function9(*args)
	result *= function12(*args)
	result -= function15(*args)
	result -= function13(*args)
	result -= function7(*args)
	result = result or function6(*args)
	result = result and function1(*args)
	result *= function0(*args)
	result -= function9(*args)
	result *= function10(*args)
	result -= function11(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function80(*args):
	result = 0.6582904118044515
	result = result and function5(*args)
	result = result and function8(*args)
	result *= function1(*args)
	result += function3(*args)
	result %= function3(*args)
	result += function12(*args)
	result = result or function12(*args)
	result %= function8(*args)
	result = result and function11(*args)
	result -= function9(*args)
	result = result and function3(*args)
	result %= function4(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function81(*args):
	result = 0.8752687419196568
	result *= function5(*args)
	result -= function5(*args)
	result %= function1(*args)
	result -= function15(*args)
	result = result and function12(*args)
	result %= function7(*args)
	result = result or function11(*args)
	result += function3(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function82(*args):
	result = 0.05979323421289384
	result -= function14(*args)
	result = result and function6(*args)
	result -= function5(*args)
	result = result or function14(*args)
	result = result and function8(*args)
	result %= function1(*args)
	result = result or function13(*args)
	result %= function1(*args)
	result = result or function13(*args)
	result = result and function11(*args)
	result = result or function7(*args)
	result += function6(*args)
	result = result and function10(*args)
	result += function11(*args)
	result -= function9(*args)
	result -= function5(*args)
	result = result and function4(*args)
	result = result or function13(*args)
	result += function13(*args)
	result = result or function5(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function83(*args):
	result = 0.6373155629532345
	result = result and function7(*args)
	result -= function1(*args)
	result = result and function14(*args)
	result %= function0(*args)
	result = result and function8(*args)
	result -= function8(*args)
	result *= function6(*args)
	result %= function1(*args)
	result = result and function15(*args)
	result = result and function0(*args)
	result = result and function15(*args)
	result = result and function15(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function84(*args):
	result = 0.26089597822494615
	result -= function8(*args)
	result -= function7(*args)
	result *= function5(*args)
	result += function8(*args)
	result %= function3(*args)
	result = result and function2(*args)
	result = result or function9(*args)
	result += function0(*args)
	result %= function15(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function85(*args):
	result = 0.24884626349568695
	result = result and function8(*args)
	result %= function12(*args)
	result = result or function0(*args)
	result *= function7(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function86(*args):
	result = 0.5427553498004685
	result = result or function4(*args)
	result += function2(*args)
	result %= function8(*args)
	result = result or function13(*args)
	result = result and function2(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function87(*args):
	result = 0.5044306824524216
	result = result or function13(*args)
	result = result and function9(*args)
	result -= function10(*args)
	result = result or function4(*args)
	result -= function6(*args)
	result += function7(*args)
	result %= function4(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function88(*args):
	result = 0.9385530440603231
	result -= function3(*args)
	result += function0(*args)
	result += function9(*args)
	result = result and function10(*args)
	result = result and function11(*args)
	result *= function4(*args)
	result -= function9(*args)
	result -= function6(*args)
	result -= function6(*args)
	result %= function10(*args)
	result += function3(*args)
	result += function13(*args)
	result = result or function6(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function89(*args):
	result = 0.7686878358268465
	result *= function13(*args)
	result *= function0(*args)
	result = result or function8(*args)
	result += function7(*args)
	result = result and function13(*args)
	result = result or function11(*args)
	result += function9(*args)
	result = result and function1(*args)
	result = result and function11(*args)
	result %= function11(*args)
	result = result or function9(*args)
	result -= function5(*args)
	result += function5(*args)
	result = result and function6(*args)
	result *= function2(*args)
	result *= function12(*args)
	result *= function3(*args)
	result -= function9(*args)
	result = result or function11(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function90(*args):
	result = 0.13473532907856633
	result *= function5(*args)
	result = result and function8(*args)
	result %= function13(*args)
	result %= function3(*args)
	result *= function13(*args)
	result = result or function1(*args)
	result += function0(*args)
	result = result and function8(*args)
	result = result or function10(*args)
	result += function11(*args)
	result += function8(*args)
	result += function9(*args)
	result *= function5(*args)
	result += function12(*args)
	result *= function6(*args)
	result += function15(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function91(*args):
	result = 0.9916628690095223
	result %= function7(*args)
	result += function11(*args)
	result *= function1(*args)
	result = result and function2(*args)
	result %= function6(*args)
	result %= function1(*args)
	result += function15(*args)
	result %= function15(*args)
	result = result and function15(*args)
	result %= function3(*args)
	result *= function0(*args)
	result += function11(*args)
	result -= function1(*args)
	result += function4(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function92(*args):
	result = 0.7925533933479193
	result += function15(*args)
	result = result or function2(*args)
	result = result or function3(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function93(*args):
	result = 0.4036383586901028
	result = result or function9(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function94(*args):
	result = 0.2531602147826191
	result -= function5(*args)
	result = result or function2(*args)
	result += function7(*args)
	result += function8(*args)
	result += function12(*args)
	result %= function6(*args)
	result = result or function0(*args)
	result -= function1(*args)
	result = result or function14(*args)
	result = result and function9(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function95(*args):
	result = 0.43884694217469644
	result = result and function5(*args)
	result %= function15(*args)
	result -= function3(*args)
	result %= function2(*args)
	result -= function1(*args)
	result = result or function12(*args)
	result %= function6(*args)
	result = result or function0(*args)
	result -= function3(*args)
	result *= function9(*args)
	result = result and function3(*args)
	result = result or function5(*args)
	result *= function0(*args)
	result *= function5(*args)
	result = result or function6(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function96(*args):
	result = 0.761352350181391
	result = result and function3(*args)
	result += function5(*args)
	result %= function14(*args)
	result = result or function9(*args)
	result *= function2(*args)
	result = result and function14(*args)
	result *= function15(*args)
	result += function12(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function97(*args):
	result = 0.5694837807238551
	result += function13(*args)
	result = result or function15(*args)
	result = result or function10(*args)
	result -= function5(*args)
	result = result or function4(*args)
	result -= function12(*args)
	result = result and function15(*args)
	result += function8(*args)
	result = result and function3(*args)
	result %= function9(*args)
	result = result and function15(*args)
	result = result and function8(*args)
	result = result or function12(*args)
	result += function6(*args)
	result *= function4(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function98(*args):
	result = 0.18142434689607545
	result %= function2(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function

def function99(*args):
	result = 0.3535578237897281
	result *= function8(*args)
	result *= function8(*args)
	result += function6(*args)
	result = result or function8(*args)
	result *= function0(*args)
	result *= function4(*args)
	result %= function11(*args)
	result = result or function1(*args)
	result %= function14(*args)
	result *= function8(*args)
	result -= function12(*args)
	result %= function7(*args)
	result *= function9(*args)
	result = result and function4(*args)
	result += function12(*args)
	result += function7(*args)
	if result >= 1 or result < 0:
		result = result % 0.999
	return result #composite function


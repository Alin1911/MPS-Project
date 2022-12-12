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
	magic_number = 0.029325501274651056
	return myval if  myval <= magic_number else 0.18738647016166235 #IF

def function3(*args):
	my_list = []
	cycle_index = 0
	for i in  range(1, 49):
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
	magic_number = 127
	while  value <= magic_number:
		value += 10
		if index == len(args):
			index = 0
		result += args[index]
		index += 1
	return ((result / index) % 100) / 100 #while

def function5(*args):
	lambda_sum = functools.reduce(lambda x, y: x + y - 10, args)
	result = math.fabs(math.sin(lambda_sum))
	return result #sin

def function6(*args):
	lambda_sum = functools.reduce(lambda x, y: x + y, args)
	result = math.fabs(math.cos(lambda_sum))
	return result #cos

def function7(*args):
	lambda_sum = functools.reduce(lambda x, y: x + y, args)
	result = math.fabs(math.tan(lambda_sum) % 0.999)
	return result #tan

def function8(*args):
	return 0.5

def function9(*args):
	return 1.0

def function10(*args):
	myval = max(args)
	return 1 - 1/(1 + myval) #ecuation

def function11(*args):
	myval = max(args)
	return 1 - 1 / (math.exp(2 * myval) + 1) #ecuation

def function12(*args):
	lambda_sum = functools.reduce(lambda x, y: x + y, args)
	result = lambda_sum / len(args)
	if result >= 1:
		result = result % 0.999
	return result #AVG

def function13(*args):
	result = np.mean(args) % 0.999
	return result #mean

def function14(*args):
	return 0.1976945320150465 #random

def function15(*args):
	result = 0.7279316668644221
	result = result and math.fabs(function1(*args))
	result = result and math.fabs(function4(*args))
	result *= math.fabs(function6(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function16(*args):
	result = 0.9367651004581098
	result += math.fabs(function3(*args))
	result *= math.fabs(function0(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function17(*args):
	result = 0.3284798800170614
	result = result or math.fabs(function6(*args))
	result *= math.fabs(function1(*args))
	result = result and math.fabs(function10(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function18(*args):
	result = 0.9412453278598152
	result -= math.fabs(function5(*args))
	result = result or math.fabs(function13(*args))
	result += math.fabs(function10(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function19(*args):
	result = 0.3645764803769268
	result *= math.fabs(function7(*args))
	result *= math.fabs(function11(*args))
	result -= math.fabs(function0(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function20(*args):
	result = 0.010039446548997466
	result += math.fabs(function9(*args))
	result *= math.fabs(function3(*args))
	result = result and math.fabs(function12(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function21(*args):
	result = 0.10959812574744443
	result *= math.fabs(function6(*args))
	result = result or math.fabs(function9(*args))
	result = result and math.fabs(function8(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function22(*args):
	result = 0.11484588790825545
	result = result and math.fabs(function3(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function23(*args):
	result = 0.10328762309384987
	result = result and math.fabs(function14(*args))
	result = result and math.fabs(function5(*args))
	result += math.fabs(function5(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function24(*args):
	result = 0.11662569624646724
	result = result or math.fabs(function9(*args))
	result = result and math.fabs(function9(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function25(*args):
	result = 0.12985463782894202
	result *= math.fabs(function13(*args))
	result *= math.fabs(function7(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function26(*args):
	result = 0.9993042113464087
	result -= math.fabs(function13(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function27(*args):
	result = 0.5602196189031946
	result = result and math.fabs(function0(*args))
	result = result or math.fabs(function10(*args))
	result -= math.fabs(function12(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function28(*args):
	result = 0.7162658863137022
	result = result or math.fabs(function2(*args))
	result += math.fabs(function7(*args))
	result += math.fabs(function8(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function29(*args):
	result = 0.07037967138894474
	result = result or math.fabs(function12(*args))
	result += math.fabs(function10(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function30(*args):
	result = 0.4423668221262518
	result = result or math.fabs(function12(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function31(*args):
	result = 0.6706717213091778
	result += math.fabs(function1(*args))
	result -= math.fabs(function5(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function32(*args):
	result = 0.3339189584968796
	result = result or math.fabs(function9(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function33(*args):
	result = 0.0809204247514188
	result = result or math.fabs(function10(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function34(*args):
	result = 0.2512587930757424
	result *= math.fabs(function9(*args))
	result = result and math.fabs(function13(*args))
	result = result and math.fabs(function12(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function35(*args):
	result = 0.43430496977346533
	result = result and math.fabs(function1(*args))
	result -= math.fabs(function1(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function36(*args):
	result = 0.32125773062456087
	result = result and math.fabs(function3(*args))
	result = result and math.fabs(function14(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function37(*args):
	result = 0.3027846424356766
	result = result or math.fabs(function7(*args))
	result = result or math.fabs(function10(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function38(*args):
	result = 0.09682043781193383
	result = result and math.fabs(function7(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function39(*args):
	result = 0.06694202933419469
	result += math.fabs(function6(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function40(*args):
	result = 0.01728055470685641
	result += math.fabs(function7(*args))
	result = result or math.fabs(function12(*args))
	result = result or math.fabs(function8(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function41(*args):
	result = 0.13960546957361897
	result = result or math.fabs(function5(*args))
	result += math.fabs(function0(*args))
	result += math.fabs(function6(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function42(*args):
	result = 0.014796545336175804
	result *= math.fabs(function14(*args))
	result += math.fabs(function0(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function43(*args):
	result = 0.5723560960023659
	result = result and math.fabs(function12(*args))
	result = result and math.fabs(function12(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function44(*args):
	result = 0.07263583165366183
	result = result and math.fabs(function7(*args))
	result = result and math.fabs(function11(*args))
	result *= math.fabs(function9(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function45(*args):
	result = 0.975580537921323
	result *= math.fabs(function10(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function46(*args):
	result = 0.4412062819469783
	result -= math.fabs(function10(*args))
	result += math.fabs(function5(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function47(*args):
	result = 0.4727748024425583
	result *= math.fabs(function9(*args))
	result += math.fabs(function4(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function48(*args):
	result = 0.34834906502428886
	result += math.fabs(function1(*args))
	result -= math.fabs(function1(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function49(*args):
	result = 0.6751651862601129
	result = result and math.fabs(function12(*args))
	result *= math.fabs(function5(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function50(*args):
	result = 0.8182972638870551
	result *= math.fabs(function4(*args))
	result += math.fabs(function9(*args))
	result -= math.fabs(function0(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function51(*args):
	result = 0.7947403876706478
	result *= math.fabs(function12(*args))
	result = result and math.fabs(function8(*args))
	result -= math.fabs(function1(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function52(*args):
	result = 0.31473670654204566
	result -= math.fabs(function4(*args))
	result = result and math.fabs(function6(*args))
	result = result or math.fabs(function14(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function53(*args):
	result = 0.671205142173933
	result += math.fabs(function11(*args))
	result = result and math.fabs(function3(*args))
	result += math.fabs(function10(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function54(*args):
	result = 0.034740854262266474
	result = result and math.fabs(function2(*args))
	result += math.fabs(function8(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function55(*args):
	result = 0.8273848959444126
	result += math.fabs(function11(*args))
	result = result and math.fabs(function14(*args))
	result -= math.fabs(function13(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function56(*args):
	result = 0.19239983438305186
	result = result or math.fabs(function12(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function57(*args):
	result = 0.11654082413239342
	result -= math.fabs(function8(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function58(*args):
	result = 0.6155745171973271
	result *= math.fabs(function9(*args))
	result = result and math.fabs(function0(*args))
	result -= math.fabs(function0(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function59(*args):
	result = 0.527666460790867
	result *= math.fabs(function7(*args))
	result = result or math.fabs(function13(*args))
	result += math.fabs(function13(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function60(*args):
	result = 0.6512072939838796
	result += math.fabs(function4(*args))
	result = result or math.fabs(function10(*args))
	result = result and math.fabs(function12(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function61(*args):
	result = 0.7685315270545576
	result += math.fabs(function2(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function62(*args):
	result = 0.580549450288307
	result *= math.fabs(function8(*args))
	result = result and math.fabs(function7(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function63(*args):
	result = 0.6499925063788944
	result += math.fabs(function11(*args))
	result = result and math.fabs(function2(*args))
	result = result or math.fabs(function5(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function64(*args):
	result = 0.5920376828139725
	result = result or math.fabs(function4(*args))
	result = result or math.fabs(function12(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function65(*args):
	result = 0.46144344969512985
	result = result and math.fabs(function7(*args))
	result *= math.fabs(function13(*args))
	result *= math.fabs(function8(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function66(*args):
	result = 0.45999689034779545
	result *= math.fabs(function0(*args))
	result *= math.fabs(function11(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function67(*args):
	result = 0.17989895177741455
	result += math.fabs(function12(*args))
	result = result and math.fabs(function6(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function68(*args):
	result = 0.6575912132250579
	result *= math.fabs(function5(*args))
	result -= math.fabs(function12(*args))
	result -= math.fabs(function6(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function69(*args):
	result = 0.33981735355084675
	result -= math.fabs(function8(*args))
	result *= math.fabs(function11(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function70(*args):
	result = 0.6519646359171308
	result = result or math.fabs(function1(*args))
	result = result or math.fabs(function1(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function71(*args):
	result = 0.12826042365572532
	result -= math.fabs(function11(*args))
	result *= math.fabs(function8(*args))
	result = result and math.fabs(function0(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function72(*args):
	result = 0.3901241076598284
	result = result and math.fabs(function3(*args))
	result = result and math.fabs(function0(*args))
	result = result and math.fabs(function6(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function73(*args):
	result = 0.29798609788051933
	result = result or math.fabs(function14(*args))
	result = result or math.fabs(function3(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function74(*args):
	result = 0.31610820223220903
	result -= math.fabs(function7(*args))
	result -= math.fabs(function0(*args))
	result += math.fabs(function8(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function75(*args):
	result = 0.3720576707234553
	result = result or math.fabs(function4(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function76(*args):
	result = 0.22435788690378922
	result = result and math.fabs(function10(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function77(*args):
	result = 0.3521347208853387
	result *= math.fabs(function6(*args))
	result = result or math.fabs(function6(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function78(*args):
	result = 0.3603788213746498
	result = result and math.fabs(function3(*args))
	result -= math.fabs(function10(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function79(*args):
	result = 0.33660659220750666
	result -= math.fabs(function1(*args))
	result -= math.fabs(function0(*args))
	result *= math.fabs(function10(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function80(*args):
	result = 0.6801270715087224
	result = result and math.fabs(function4(*args))
	result = result or math.fabs(function2(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function81(*args):
	result = 0.6629493478885173
	result += math.fabs(function13(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function82(*args):
	result = 0.04828130923760432
	result += math.fabs(function1(*args))
	result = result and math.fabs(function3(*args))
	result -= math.fabs(function5(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function83(*args):
	result = 0.615882625918268
	result += math.fabs(function8(*args))
	result = result and math.fabs(function1(*args))
	result *= math.fabs(function1(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function84(*args):
	result = 0.16782100453451432
	result += math.fabs(function6(*args))
	result -= math.fabs(function2(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function85(*args):
	result = 0.41265210828765997
	result *= math.fabs(function8(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function86(*args):
	result = 0.8690867974043331
	result *= math.fabs(function10(*args))
	result += math.fabs(function9(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function87(*args):
	result = 0.9060199739721294
	result = result and math.fabs(function1(*args))
	result = result or math.fabs(function12(*args))
	result += math.fabs(function8(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function88(*args):
	result = 0.46445897193599384
	result += math.fabs(function1(*args))
	result = result or math.fabs(function9(*args))
	result += math.fabs(function5(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function89(*args):
	result = 0.9839490998842292
	result = result and math.fabs(function3(*args))
	result *= math.fabs(function7(*args))
	result = result and math.fabs(function13(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function90(*args):
	result = 0.6901086404956426
	result = result or math.fabs(function5(*args))
	result = result and math.fabs(function12(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function91(*args):
	result = 0.9797015733596386
	result -= math.fabs(function7(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function92(*args):
	result = 0.9087881532562812
	result *= math.fabs(function5(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function93(*args):
	result = 0.7039966701804543
	result += math.fabs(function3(*args))
	result *= math.fabs(function0(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function94(*args):
	result = 0.8752082990606252
	result = result or math.fabs(function9(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function95(*args):
	result = 0.94835087195487
	result += math.fabs(function5(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function96(*args):
	result = 0.9444889492872741
	result += math.fabs(function2(*args))
	result = result and math.fabs(function7(*args))
	result = result and math.fabs(function1(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function97(*args):
	result = 0.24689645801578408
	result += math.fabs(function1(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function98(*args):
	result = 0.7574432144842094
	result += math.fabs(function13(*args))
	result *= math.fabs(function9(*args))
	result += math.fabs(function13(*args))
	result = math.fabs(result) % 0.999
	return result #composite function

def function99(*args):
	result = 0.3420898213390362
	result -= math.fabs(function3(*args))
	result = math.fabs(result) % 0.999
	return result #composite function


from LOTlib.DataAndObjects import Obj
from LOTlib.WorldState import *

WS_0 = WorldState(n_black_ball=1, n_red_ball=4, n_green_ball=4)
WS_1 = WorldState(n_black_ball=1, n_red_ball=4, n_green_ball=4)

print '0: ' + str(WS_0==WS_1)
print str(WS_0) + '\n-----------------------\n' + str(WS_1)
print '========================================='

WS_0.moveBall('bucket_0', 'bucket_3', 'black')
print '1: ' + str(WS_0==WS_1)
print str(WS_0) + '\n-----------------------\n' + str(WS_1)
print '========================================='

WS_0.moveBall('bucket_0', 'bucket_3', 'black')
print '2: ' + str(WS_0==WS_1)
print str(WS_0) + '\n-----------------------\n' + str(WS_1)
print '========================================='

WS_0.moveBall('bucket_3', 'bucket_0', 'black')
print '3: ' + str(WS_0==WS_1)
print str(WS_0) + '\n-----------------------\n' + str(WS_1)

state = {
	'bucket_0': Bucket(n_black_ball=1, n_red_ball=2, n_green_ball=3)
	'bucket_1': Bucket(n_black_ball=4, n_red_ball=5, n_green_ball=6)
	'bucket_2': Bucket(n_black_ball=7, n_red_ball=8, n_green_ball=9)
	'bucket_3': Bucket(n_black_ball=10, n_red_ball=11, n_green_ball=12)
}

WS_0.setState(state)
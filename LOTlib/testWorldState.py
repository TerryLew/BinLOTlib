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







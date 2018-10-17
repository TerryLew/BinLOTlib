from LOTlib.DataAndObjects import Obj
from LOTlib.WorldState import *

init_state = {
	'bucket_0': Bucket(black=1, red=0, green=0),
	'bucket_1': Bucket(black=0, red=4, green=4),
	'bucket_2': Bucket(black=0, red=0, green=0),
	'bucket_3': Bucket(black=0, red=0, green=0),
	'hand_left': Hand(black=1),
	'hand_right': Hand()
}

def testWorldStateEqual():
	WS_0 = WorldState(init_state)
	WS_1 = WorldState(init_state)

	print '0: ' + str(WS_0==WS_1)
	print str(WS_0) + '\n-----------------------\n' + str(WS_1)
	print '========================================='

	WS_0.moveBall('bucket_0', 'bucket_3', 'black')
	print '1: ' + str(WS_0==WS_1)
	print str(WS_0) + '\n-----------------------\n' + str(WS_1)
	print '========================================='

def testMoveBalls():
	WS_0 = WorldState(init_state)
	WS_0.moveBall('bucket_0', 'bucket_3', 'black')
	print '2: '# + str(WS_0==WS_1)
	print str(WS_0) + '\n-----------------------\n'# + str(WS_1)
	print '========================================='

	WS_0.moveBall('bucket_3', 'bucket_0', 'black')
	print '3: '# + str(WS_0==WS_1)
	print str(WS_0) + '\n-----------------------\n'# + str(WS_1)
	print '========================================='

	WS_0.moveBall('bucket_1', 'hand_right', 'green')
	print '4: '# + str(WS_0==WS_1)
	print str(WS_0) + '\n-----------------------\n'# + str(WS_1)
	print '========================================='

	WS_0.moveBall('bucket_1', 'hand_right', 'green')
	print '5: '# + str(WS_0==WS_1)
	print str(WS_0) + '\n-----------------------\n'# + str(WS_1)
	print '========================================='

	WS_0.moveBall('bucket_1', 'hand_right', 'green')
	print '6: '# + str(WS_0==WS_1)
	print str(WS_0) + '\n-----------------------\n'# + str(WS_1)
	print '========================================='

	WS_0.moveBall('bucket_0', 'hand_right', 'black')
	print '7: '# + str(WS_0==WS_1)
	print str(WS_0) + '\n-----------------------\n'# + str(WS_1)
	print '========================================='

	WS_0.moveBall('hand_right', 'hand_left', 'green')
	print '8: '# + str(WS_0==WS_1)
	print str(WS_0) + '\n-----------------------\n'# + str(WS_1)
	print '========================================='

	WS_0.moveBall('hand_left', 'bucket_0', 'green')
	print '9: '# + str(WS_0==WS_1)
	print str(WS_0) + '\n-----------------------\n'# + str(WS_1)
	print '========================================='

def testSetWorldState():
	state = {
		'bucket_0': Bucket(black=1, red=2, green=3),
		'bucket_1': Bucket(black=4, red=5, green=6),
		'bucket_2': Bucket(black=7, red=8, green=9),
		'bucket_3': Bucket(black=10, red=11, green=12),
		'hand_left': Hand(),
		'hand_right': Hand(black=1, green=1)
	}

	WS_0 = WorldState(init_state)
	WS_0.setWorldState(state)
	print str(WS_0)

testWorldStateEqual()
testMoveBalls()
testSetWorldState()
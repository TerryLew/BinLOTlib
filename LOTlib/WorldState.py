from LOTlib.Miscellaneous import self_update
from LOTlib.DataAndObjects import Obj
from sets import Set
import sys

possible_colors = Set([
	'black',
	'red',
	'green'
	])

class Container(object):
	def __init__(self, **kwargs):
		self._balls = {}
		for color in possible_colors:
			self._balls[color] = 0
		for color, number in kwargs.items():
			if not color in possible_colors:
				sys.exit('[Error]: Color \'' + color + '\' is not allowed.' )
			elif not isinstance(number, int):
				sys.exit('[Error]: \'' + number + '\' is not an integer.' )
			else:
				self._balls[color] = number
		self._capacity = 1000

	def __eq__(self, other):
		for color, number in self._balls.items():
			if color not in other._balls.keys():
				return False
			elif other._balls[color] != number:
				return False
		for color, number in other._balls.items():
			if color not in self._balls.keys():
				return False
			elif self._balls[color] != number:
				return False
		return True

	def __str__(self):
		outstr = '<'
		for color, number in self._balls.items():
			outstr = outstr + color + ': ' + str(number) + ' '
		outstr = outstr + '>'
		return outstr

	def __repr__(self): # used for being printed in lists
		return str(self)

	def remove_all_balls(self):
		for color, number in self._balls.items():
			number = 0

class Bucket(Container):
	def __init__(self, *args, **kwargs):
		super(Bucket, self).__init__(**kwargs)
		for arg in args:
			if isinstance(arg, Bucket):
				for color, number in arg._balls.items():
					self._balls[color] = number
			else:
				sys.exit('[Error]: expect a Bucket object.')
		self._capacity = 1000

	def get_vacancy(self):
		vacancy = self._capacity
		for color, number in self._balls.items():
			vacancy = vacancy - number
		return vacancy


class Hand(Container):
	def __init__(self, *args, **kwargs):
		super(Hand, self).__init__(**kwargs)
		for arg in args:
			if isinstance(arg, Hand):
				for color, number in arg._balls.items():
					self._balls[color] = number
			else:
				sys.exit('[Error]: expect a Hand object.')
		self._capacity = 3

	def get_vacancy(self):
		vacancy = self._capacity
		for color, number in self._balls.items():
			vacancy = vacancy - number
		return vacancy


class WorldState():
	def __init__(self, *args):
		self._container = {
			'bucket_0': Bucket(),
			'bucket_1': Bucket(),
			'bucket_2': Bucket(),
			'bucket_3': Bucket(),
			'hand_left': Hand(),
			'hand_right': Hand()

		}
		self.setWorldState(*args)

	def __eq__(self, other):
		bucket_0_is_equal = (self._container['bucket_0'] == other._container['bucket_0'])
		bucket_1_is_equal = (self._container['bucket_1'] == other._container['bucket_1'])
		bucket_2_is_equal = (self._container['bucket_2'] == other._container['bucket_2'])
		bucket_3_is_equal = (self._container['bucket_3'] == other._container['bucket_3'])
		hand_left_is_equal = (self._container['hand_left'] == other._container['hand_left'])
		hand_right_is_equal = (self._container['hand_right'] == other._container['hand_right'])
		return bucket_0_is_equal and bucket_1_is_equal and bucket_0_is_equal and bucket_1_is_equal and hand_left_is_equal and hand_right_is_equal

	def __str__(self):
		outstr = '<WorldState: \n'
		outstr = outstr + 'bucket_0: ' + str(self._container['bucket_0']) + '\n'
		outstr = outstr + 'bucket_1: ' + str(self._container['bucket_1']) + '\n'
		outstr = outstr + 'bucket_2: ' + str(self._container['bucket_2']) + '\n'
		outstr = outstr + 'bucket_3: ' + str(self._container['bucket_3']) + '\n'
		outstr = outstr + 'hand_left: ' + str(self._container['hand_left']) + '\n'
		outstr = outstr + 'hand_right: ' + str(self._container['hand_right']) + '\n'
		outstr = outstr + '>'
		return outstr

	def __repr__(self): # used for being printed in lists
		return str(self)

	def setWorldState(self, state):
		for container_name, container in self._container.items():
			container.remove_all_balls()
		for container_name, container in state.items():
			if isinstance(container, Bucket):
				self._container[container_name] = Bucket(container)
			elif isinstance(container, Hand):
				self._container[container_name] = Hand(container)
			else:
				sys.exit('[Error]: expect Bucket object or Hand object.')

	def existColor(self, container, color, number=1):
		if container not in self._container.keys():
			sys.exit('[Error]: number of ' + color + ' balls in ' + container + ' is less than' + number)
		elif color in self._container[container]._balls:
			return self._container[container]._balls[color] >= number
		else:
			return False

	def canAddBall(self, container, number=1):
		return self._container[container].get_vacancy() >= number

	def moveBall(self, from_container, to_container, color, number=1):
		assert from_container in self._container, "Incorrect source container name: "+from_container
		assert to_container in self._container, "Incorrect target container name: "+to_container

		if self.existColor(from_container, color, number) and self.canAddBall(to_container, number):
			self._container[from_container]._balls[color] = self._container[from_container]._balls[color] - number
			self._container[to_container]._balls[color] = self._container[to_container]._balls[color] + number


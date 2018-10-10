from LOTlib.Miscellaneous import self_update
from LOTlib.DataAndObjects import Obj

class Bucket():
	def __init__(self, **kwargs):
		self._balls = {'black': 0,
				 'red': 0,
				 'green': 0}
		# Since we apply to this, it must be a list
		if len(kwargs) != 0:
			assert len(kwargs)==3, "Need to specify number of black balls, red balls, and green balls."
			self._balls['black'] = kwargs.get('black')
			self._balls['red'] = kwargs.get('red')
			self._balls['green'] = kwargs.get('green')

	def __eq__(self, other):
		return self._balls['black'] == other._balls['black'] and self._balls['red'] == other._balls['red'] and self._balls['green'] == other._balls['green']

 	def __str__(self):
		outstr = '<Black: ' + str(self._balls['black']) + ', '
		outstr = outstr + 'Red: ' + str(self._balls['red']) + ', '
		outstr = outstr + 'Green: ' + str(self._balls['green']) + '>'
		return outstr

	def __repr__(self): # used for being printed in lists
		return str(self)

class WorldState():
	def __init__(self, **kwargs):
		self._buckets = {}

		assert 'n_black_ball' in kwargs and 'n_red_ball' in kwargs and 'n_green_ball' in kwargs, "Need n_black_ball, n_red_ball, and n_red_ball"
		self._buckets['bucket_0'] = Bucket(black=kwargs.get('n_black_ball'), red=0, green=0)
		self._buckets['bucket_1'] = Bucket(black=0, red=kwargs.get('n_red_ball'), green=kwargs.get('n_green_ball'))

		self._buckets['bucket_2'] = Bucket()
		self._buckets['bucket_3'] = Bucket()

	def __eq__(self, other):
		source_bucket_0_is_equal = (self._buckets['bucket_0'] == other._buckets['bucket_0'])
		source_bucket_1_is_equal = (self._buckets['bucket_1'] == other._buckets['bucket_1'])
		target_bucket_0_is_equal = (self._buckets['bucket_2'] == other._buckets['bucket_2'])
		target_bucket_1_is_equal = (self._buckets['bucket_3'] == other._buckets['bucket_3'])
		return source_bucket_0_is_equal and source_bucket_1_is_equal and target_bucket_0_is_equal and target_bucket_1_is_equal

	def __str__(self):
		outstr = '<WorldState: \n'
		outstr = outstr + 'Bucket 0: ' + str(self._buckets['bucket_0']) + '\n'
		outstr = outstr + 'Bucket 1: ' + str(self._buckets['bucket_1']) + '\n'
		outstr = outstr + 'Bucket 2: ' + str(self._buckets['bucket_2']) + '\n'
		outstr = outstr + 'Bucket 3: ' + str(self._buckets['bucket_3']) + '\n'
		outstr = outstr + '>'
		return outstr

	def __repr__(self): # used for being printed in lists
		return str(self)

	def existColor(self, bucket, color):
		if color=='black':
			return self._buckets[bucket]._balls['black']>0
		elif color=='red':
			return self._buckets[bucket]._balls['red']>0
		elif color=='green':
			return self._buckets[bucket]._balls['green']>0
		else:
			return False

	def moveBall(self, from_bucket, to_bucket, color):
		assert from_bucket in self._buckets and to_bucket in self._buckets, "Incorrect bucket name"
		if self.existColor(from_bucket, color):
			self._buckets[from_bucket]._balls[color] = self._buckets[from_bucket]._balls[color] - 1
			self._buckets[to_bucket]._balls[color] = self._buckets[to_bucket]._balls[color] + 1











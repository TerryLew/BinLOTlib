
from LOTlib.Grammar import Grammar
from math import log
from LOTlib.Hypotheses.LOTHypothesis import LOTHypothesis
from LOTlib.DataAndObjects import FunctionData
from LOTlib.Inference.Samplers.MetropolisHastings import MHSampler


class MyHypothesis(LOTHypothesis):
    def __init__(self, **kwargs):
        LOTHypothesis.__init__(self, grammar=grammar, display="lambda x: %s", **kwargs)
    
    def __call__(self, *args):
        try:
            # try to do it from the superclass
            return LOTHypothesis.__call__(self, *args)
        except ZeroDivisionError:
            # and if we get an error, return nan
            return float("nan")
        
    def compute_single_likelihood(self, datum):
        if self(*datum.input) == datum.output:
            return log((1.0-datum.alpha)/100. + datum.alpha)
        else:
            return log((1.0-datum.alpha)/100.)
'''
    def compute_single_likelihood(self, datum):
        try:
            return log(datum.alpha * (self(*datum.input) == datum.output) + (1.0-datum.alpha) / 2.0)
        except RecursionDepthException as e: # we get this from recursing too deep -- catch and thus treat "ret" as None
            return -Infinity
'''
# Define a grammar object
# Defaultly this has a start symbol called 'START' but we want to call
# it 'EXPR'
grammar = Grammar(start='EXPR')

# Define some operations
grammar.add_rule('EXPR', '(%s + %s)', ['EXPR', 'EXPR'], 1.0)
grammar.add_rule('EXPR', '(%s * %s)', ['EXPR', 'EXPR'], 1.0)
grammar.add_rule('EXPR', '(float(%s) / float(%s))', ['EXPR', 'EXPR'], 1.0)
grammar.add_rule('EXPR', '(-%s)', ['EXPR'], 1.0)

# And define some numbers. We'll give them a 1/n^2 probability
for n in xrange(1,10):
    grammar.add_rule('EXPR', str(n), None, 10.0/n**2)

data = [ FunctionData(input=[6], output=12, alpha=0.95) ]


#h = MyHypothesis()
#print h.compute_prior(), h.compute_likelihood(data), h
# define a "starting hypothesis". This one is essentially copied by
# all proposers, so the sampler doesn't need to know its type or anything.

h0 = MyHypothesis()
from collections import Counter

count = Counter()
for h in MHSampler(h0, data, steps=10000):
    count[h] += 1

#for h in sorted(count.keys(), key=lambda x: count[x]):
#    print count[h], h.posterior_score, h

from LOTlib.Miscellaneous import logsumexp
from numpy import exp # but things that are handy in numpy are not duplicated (usually)

# get a list of all the hypotheses we found. This is necessary because we need a fixed order,
# which count.keys() does not guarantee unless we make a new variable.
hypotheses = count.keys()

# first convert posterior_scores to probabilities. To this, we'll use a simple hack of
# renormalizing the psoterior_scores that we found. This is a better estimator of each hypothesis'
# probability than the counts from the sampler
z = logsumexp([h.posterior_score for h in hypotheses])

posterior_probabilities = [ exp(h.posterior_score - z) for h in hypotheses ]

# and compute the probabilities over the sampler run
cntz = sum(count.values())
sampler_counts = [ float(count[h])/cntz for h in hypotheses ]

## and let's just make a simple plot
import matplotlib.pyplot as pyplot
fig = pyplot.figure()
plt = fig.add_subplot(1,1,1)
plt.scatter(posterior_probabilities, sampler_counts)
plt.plot([0,1], [0,1], color='red')
fig.show()
fig.savefig('./posterior.png')


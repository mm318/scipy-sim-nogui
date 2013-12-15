'''
Created on Feb 3, 2010

@author: brianthorne
'''

import unittest

from scipysim.actors.signal.split import SplitTests
from scipysim.actors.signal.decimator import DecimatorTests
from scipysim.actors.signal.delay import DelayTests
from scipysim.actors.signal.interpolator import InterpolateTests
from scipysim.actors.signal.eventfilter import EventFilterTests
from scipysim.actors.signal.merge import MergeTests
from scipysim.actors.signal.quantizer import QuantizerTests
from scipysim.actors.signal.sampler import SamplerTests
from scipysim.actors.signal.sink import SinkTests

# from ramp import RampTests # TODO
# from random_signal import RandomSourceTests # TODO


if __name__ == "__main__":
    # import sys
    # sys.argv = ['', 'Test.testName']
    unittest.main()


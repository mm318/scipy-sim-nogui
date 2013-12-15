from scipysim.actors import SisoTestHelper, Channel, Event, LastEvent
from scipysim.actors.math import Abs

import numpy

import unittest


class AbsTests( unittest.TestCase ):
    '''Test the absolute actor'''

    def setUp( self ):
        '''
        Unit test setup code
        '''
        self.q_in = Channel()
        self.q_out = Channel()

    def test_positive_integers( self ):
        '''Test a simple positive integer signal.
        '''
        inp = [Event(value=i, tag=i) for i in xrange( 0, 100, 1 )]

        expected_outputs = inp[:]

        abs = Abs( self.q_in, self.q_out )
        abs.start()
        [self.q_in.put( val ) for val in inp]
        self.q_in.put( LastEvent() )
        abs.join()

        for expected_output in expected_outputs:
            out = self.q_out.get()
            self.assertEquals( out.value, expected_output.value )
            self.assertEquals( out.tag, expected_output.tag )
        self.assertTrue( self.q_out.get().last )

from scipysim.actors.math.ct_integrator import CTIntegratorTests

from scipysim.actors.math.ct_integrator_qs1 import CTintegratorQSTests

from scipysim.actors.math.dt_integrator import DTIntegratorTests

from scipysim.actors.math.derivative import BundleDerivativeTests

from scipysim.actors.math.proportional import ProportionalTests

from scipysim.actors.math.summer import SummerTests


if __name__ == "__main__":
    # import sys
    # sys.argv = ['', 'Test.testName']
    unittest.main()


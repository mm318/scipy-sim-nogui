#!/usr/bin/env python

import os, sys, inspect
# realpath() with make your script run, even if you symlink it :)
cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))
if(cmd_folder not in sys.path):
  sys.path.insert(0, cmd_folder)

# use this if you want to include modules from a subforder
cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile(inspect.currentframe()))[0], '..')))
if(cmd_subfolder not in sys.path):
    sys.path.insert(0, cmd_subfolder)


'''
Created on Feb 7, 2010

brianthorne
'''

from scipysim.actors import Channel, CompositeActor, MakeChans

from scipysim.actors.math import Constant
from scipysim.actors.signal import Split, Step
from scipysim.actors.io import TextWriter, NumpyWriter

import numpy as np
import scipy
import scipy.signal


import logging
# logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.DEBUG)
logging.info("Debugging Logger Enabled")


class ControlStep(CompositeActor):
    '''This simulation is a P controller responding to a step input.'''

    def __init__(self):
        '''Create the components'''
        super(ControlStep, self).__init__()

        # Simulation time in seconds
        T = 120
        freq = 50

        wire_names = ('constant_src', 'constant_out', 'constant_out_np',
            'step_src', 'step_out', 'step_out_np')
        wire_list = MakeChans(len(wire_names))
        wires = dict(zip(wire_names, wire_list))

        # Create a time vector
        src = Constant(wires['constant_src'], value=15.5, resolution=freq, simulation_time=T)
        src_dup = Split(wires['constant_src'], [wires['constant_out'], wires['constant_out_np']])

        # Create the signal source
        step = Step(wires['step_src'], switch_time=60, simulation_time=T)
        step_dup = Split(wires['step_src'], [wires['step_out'], wires['step_out_np']])

        # keeping track of components
        self.components = [src, src_dup, step, step_dup]

        src_out = TextWriter(wires['constant_out'], 'constant')
        src_out_np = NumpyWriter(wires['constant_out_np'], 'constant')
        self.components.append(src_out)
        self.components.append(src_out_np)

        step_out = TextWriter(wires['step_out'], 'step')
        step_out_np = NumpyWriter(wires['step_out_np'], 'step')
        self.components.append(step_out)
        self.components.append(step_out_np)

        # not working examples
        # plot1 = Plotter(wires[0])
        # plot2 = Plotter(wires[1])
        # plot3 = StemPlotter(wires[0])
        # plot4 = StemPlotter(wires[1])
        # self.components = [src, plot1, plot2, plot3, plot4, signal]


if __name__ == '__main__':
    ControlStep().run()


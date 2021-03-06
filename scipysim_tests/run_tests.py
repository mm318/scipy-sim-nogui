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

import unittest


from test_actors_display import BundlePlotTests
from test_actors_io import BundleTests
from test_actors_io import FileIOTests
from test_actors_io import ReaderTests
from test_actors_io import TextWriterTests
from test_actors_logic import CompareTests
from test_actors_logic import ElsePassThroughTests
from test_actors_logic import PassThroughTests
from test_actors_math import AbsTests
from test_actors_math import BundleDerivativeTests
from test_actors_math import CTintegratorQSTests
from test_actors_math import CTIntegratorTests
from test_actors_math import DTIntegratorTests
from test_actors_math import ProportionalTests
from test_actors_math import SummerTests
from test_actors_signal import DecimatorTests
from test_actors_signal import DelayTests
from test_actors_signal import EventFilterTests
from test_actors_signal import InterpolateTests
from test_actors_signal import MergeTests
from test_actors_signal import QuantizerTests
# from test_actors_signal import RampTests	# TODO
# from test_actors_signal import RandomSourceTests	# TODO
from test_actors_signal import SamplerTests
from test_actors_signal import SinkTests
from test_actors_signal import SplitTests
from test_actors_string import IntParserTests

from test_core import ActorTests
from test_core import EventTests
from test_core import GraphTests
from test_core import LastEventTests
from test_core import NodeTests
from test_core_codefile import Code_File_Input_Output_Domain_Parsing_Tests
from test_core_codefile import Code_File_Num_Input_Output_Parsing_Tests
from test_core_codefile import Code_File_Parameters_Tests
from test_core_codefile import Code_File_Path_Tests
from test_core_codefile import CodeFile_Imports_Tests
# from test_core_parser import CodeGroupTests	# TODO


if(__name__ == "__main__"):
    unittest.main()

from scipysim.core.actor import Actor
from scipysim.core.errors import NoProcessFunctionDefined

from scipysim.core.event import EventTests, LastEventTests
from scipysim.core.graph import NodeTests, GraphTests

import unittest


class ActorTests(unittest.TestCase):

    def setUp(self):
        self.block = Actor()

    def test_actor_is_abstract(self):
        self.assertRaises(NoProcessFunctionDefined, self.block.run)

    def test_input_queue_made(self):
        self.block.input_channel.put("Something")
        self.assertEquals("Something", self.block.input_channel.get())

    def test_actor_has_default_port_nums(self):
        '''Test by loading a siso actor from a hardcoded path'''
        my_actor = Actor()
        self.assertEqual(my_actor.num_inputs, None)
        self.assertEqual(my_actor.num_outputs, None)


if __name__ == "__main__":
    unittest.main()

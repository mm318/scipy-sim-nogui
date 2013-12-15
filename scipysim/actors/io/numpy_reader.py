'''
Created on Feb 1, 2010

@author: brianthorne
'''

from scipysim.actors import Source, Channel, Event
from reader import Reader

import numpy


class NumpyReader(Reader):
    '''
    Reads a tagged signal from a file - the signal can be any
    domain - the data for both tags and values are stored as 64bit floats.
    The data must have been saved with the WriteFile Actor NOT CSV.
    
    The numpy structured record array is as follows: 
        dtype=
        {
            'names': ["Tag", "Value"],
            'formats': ['f8','f8'],
            'titles': ['Domain', 'Name']
         }
    Note the titles may be used to store domain and signal name information.
    
    The data can be recovered as seperate arrays with data['Tag'] and data['Value']
    or it can be treated as a list of event tuples.
    '''
    
    def __init__(self, output_channel, file_name):
        super(NumpyReader, self).__init__(output_channel, file_name)

    def process(self):
        x = numpy.load(self.filename)
        [self.output_channel.put(Event(tag, value)) for (tag, value) in x]
        self.output_channel.put(None)
        self.stop = True


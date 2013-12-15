'''
Created on Feb 1, 2010

@author: brianthorne
'''

from scipysim.actors import Actor, Channel


class Writer(Actor):
    '''
    This Actor writes tagged signal data to a file.
    It writes ascii to a file, first it gets all the input
    So make sure the signal can fit in memory!
    '''

    num_outputs = 0
    num_inputs = 1

    def __init__(self, input_channel, file_name="signal_data"):
        '''
        Constructor for a File Writer Actor
        '''
        super(Writer, self).__init__(input_channel=input_channel)
        self.filename = file_name
        self.temp_data = []

    def process(self):
        obj = self.input_channel.get(True)     # this is blocking
        self.temp_data.append(obj)
        if obj is None:
            self.write_file()
            self.stop = True
            return

    def write_file(self):
        out_file = open(self.filename, 'wb')
        # convert this to list comprehension in the future
        for element in self.temp_data:
            if(element != None):
                out_file.write('%0.8e,%0.8e\n' % (element['tag'], element['value']))
        out_file.close()


'''
Created on Feb 1, 2010

@author: brianthorne
'''

from scipysim.actors import Source, Channel, Event
import numpy


class Reader(Source):
    '''
    Reads a CSV file. Expects two values per line: tag, value
    '''

    def __init__(self, output_channel, file_name):
        super(Reader, self).__init__(output_channel=output_channel)
        self.filename = file_name

    def process(self):
        in_file = open(self.filename, 'rb')
        for line in in_file:
            data = line.split(',')
            tag = float(data[0].strip())
            value = float(data[1].strip())
            self.output_channel.put(Event(tag, value))
        in_file.close()
        self.output_channel.put(None)        
        self.stop = True


class TextReader(Source):
    '''This source creates string objects from a file.'''
    
    def __init__(self, output_channel, filename, send_as_words=False):
        '''A TextReader requires a valid filename to read from.
        The data may be sent as lines or words, lines are the
        default. The tag is the line number.
        '''
        super(TextReader, self).__init__(output_channel=output_channel)
        self.file = open(filename, 'r')
        self.send_as_words = send_as_words

    def process(self):
        for i, line in enumerate(self.file):
            if self.send_as_words:
                [self.output_channel.put(Event(tag=i, value=word.strip())) for j, word in enumerate(line.split())]
            else:
                self.output_channel.put(Event(tag=i, value=line.strip()))
        self.output_channel.put(None)
        self.stop = True


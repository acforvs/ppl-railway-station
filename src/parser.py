import argparse
from usage import USAGE, ARGUMENTS

class Parser:
    '''
    Command line arguments parser
    '''
    def __init__(self):
        self.parser = argparse.ArgumentParser()

    def parse(self):
        self.parser.add_argument(
            '-u', 
            '--usage',
            action='store_true',
            help='Usage'
        )
        self.parser.add_argument(
            '-f',
            '--file',
            action='store',
            nargs=1,
            type=str,
            help='Setting the filepath'
        )
        arguments = self.parser.parse_args()
        return arguments

    def process_arguments(self):
        '''
        Processing the arguments from the command line
        '''
        arguments = self.parse()
        if arguments['usage']:
            print(USAGE)
            return
        if arguments['file']:
            return arguments.file[0]

        print(ARGUMENTS)
        return
            



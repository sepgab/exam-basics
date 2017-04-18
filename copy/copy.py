# This should be the basic replica of the 'cp' command
# If ran from the command line without arguments
# It should print out the usage:
# copy [source] [destination]
# When just one argument is provided print out
# No destination provided
# When both arguments provided and the source is a file
# Read all contents from it and write it to the destination

import sys
import os

class Controller():

    def __init__(self):
        self.list_argv = []
        self.arg_reader()
        self.manager()

    def arg_reader(self):
        if len(sys.argv) <= 1:
            self.list_argv = []
        else:
            self.list_argv = sys.argv[1:]

    def manager(self):
        if len(self.list_argv) == 0:
            print('copy [source] [destination]')
        elif len(self.list_argv) == 1:
            print('No destination provided')
        elif len(self.list_argv) == 2:
            try:
                self.file_to_copy = open(self.list_argv[0], 'r')
            except FileNotFoundError:
                print('Source file doesn\'t exist!')
                return
            self.file_content = self.file_to_copy.readlines()
            self.file_copied = open(self.list_argv[1], 'w')
            for element in self.file_content:
                self.file_copied.write(element)
            self.file_to_copy.close()
            self.file_copied.close()
        else:
            print('Two arguments are needed e.g: \npython copy.py test.txt test_copied.txt/')

controller = Controller()

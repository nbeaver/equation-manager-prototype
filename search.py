#!/usr/bin/python
import os, sys
directory = os.path.dirname(__file__)
database = os.path.join(directory, './equation-database.txt')

query = ''.join(sys.argv[1:]) # check commandline arguments first
if query == '-': # if the only argument is '-', check stdin.
    query = sys.stdin.readlines()
if query == '': # if there's still nothing, then print a message and exit.
    sys.exit("Usage: search <query here>")
    
with open(database,'r') as f:
    for record in f.read().split('%%'):
        if record == "":
            pass
        lines =  record.split('\n')
        try:
            first_line = lines[1].lower()
            if query in first_line:
                print record.strip()
                print '--------------------------------------------------------------------------------'
        except IndexError:
            pass

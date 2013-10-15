#!/usr/bin/python
import os, sys
directory = os.path.dirname(__file__)
database = os.path.join(directory, './equation-database.txt')

query = ''.join(sys.argv[1:]) # check commandline arguments first
if query == '-': # if the only argument is '-', check stdin.
    query = sys.stdin.readlines()
if query == '': # if there's still nothing, then print a message and exit.
    sys.exit("Usage: search <query here>")

query_lowercase = query.lower() # we'll make the comparison in lowercase, too, so it's case insensitive
    
f = open(database,'r')
for record in f.read().split('%%'):
    if record == "":
        pass
    lines = record.split('\n')
    try:
        first_line_lowercase = lines[1].lower()
        if query_lowercase in first_line_lowercase:
            print record.strip()
            print '--------------------------------------------------------------------------------'
    except IndexError:
        pass
f.close()

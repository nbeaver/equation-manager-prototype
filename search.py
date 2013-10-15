#!/usr/bin/python
import sys
query = ''.join(sys.argv[1:]) # check commandline arguments first
if query == '-': # if the only argument is '-', check stdin.
    query = sys.stdin.readlines()
if query == '': # if there's still nothing, then print a message and exit.
    sys.exit("Usage: search <query here>")
    
with open('equation-database.txt','r') as f:
    for record in f.read().split('%%'):
        if record == "":
            pass
        lines =  record.split('\n')
        try:
            first_line = lines[1].lower()
            if query in first_line:
                print record.strip()
        except IndexError:
            pass

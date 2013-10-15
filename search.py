#!/usr/bin/python
import sys
query = ''.join(sys.argv[1:]) # check commandline arguments first
if query == '-': # if the only argument is '-', check stdin.
    query = sys.stdin.readlines()
if query == '': # if there's still nothing, then print a message and exit.
    sys.exit("Usage: search <query here>")
    
with open('equation-database.txt','r') as f:
    for line in f:
        if '%%' in line:
             pass # Go to the next line
        if query in line.lower():
             print line,
             while '%%' not in line:
                 try:
                     line = f.next()
                     print line,
                 except StopIteration:
                     break # If we hit the end of the file, exit the loop.

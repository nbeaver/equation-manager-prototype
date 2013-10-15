#!/usr/bin/python
query = raw_input().lower() # can take a commandline argument or a piped text stream
with open('equation-database.txt','r') as f:
    for line in f:
        if '%%' in line:
             pass
        if query in line.lower():
             print line
             while '%%' not in line:
                 print next(f)

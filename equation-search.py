#!/usr/bin/python
# This is released under the terms of the MIT license:
# http://opensource.org/licenses/MIT
import os, sys
directory = os.path.dirname(__file__)
database = os.path.join(directory, './equation-database.txt')

query = ''.join(sys.argv[1:]) # Check commandline arguments first.
if query == '-': # If the only argument is '-', check stdin.
    query = sys.stdin.readlines()
if query == '': # If there's still nothing, then print a message and exit.
    sys.exit("Usage: search <query here>")

query_lowercase = query.lower() # We'll make the comparison in lowercase, too, so it's case-insensitive.
    
f = open(database,'r')

def match(query, candidate):
    """
    Defining whether a query matches a candidate string.
    For the moment, just checking if the query is in the candidate string is sufficient.
    """
    if query in candidate:
        return True
    else:
        return False

for record in f.read().split('%%'):
    if record == "": # This happens for every comment line.
        pass
    lines = record.split('\n')
    try:
        first_line_lowercase = lines[1].lower()
        # For the moment, we just check the first string of the record for matches to the query.
        if match(query_lowercase, first_line_lowercase):
            print record.strip() # Remove the linefeeds
            # Add a visual separator between multiple matches.
            print '--------------------------------------------------------------------------------'
    except IndexError: # This happens if, e.g. there's an empty record so len(lines)==0.
        pass
f.close()

#!/usr/bin/env python
# This is released under the terms of the MIT license:
# http://opensource.org/licenses/MIT
import os, sys
directory = sys.path[0]
database = os.path.join(directory, 'equation-database.txt')

query = ''.join(sys.argv[1:]) # Check commandline arguments first.
if query == '-': # If the only argument is '-', check stdin.
    query = sys.stdin.readlines()
if query == '': # If there's still nothing, then print a message and exit.
    sys.exit("Usage: search <query here>")

def match(query, candidate):
    """
    Defining whether a query matches a candidate string.
    For the moment, just checking if the query is in the candidate string is sufficient.
    We'll do the comparison in lowercase so that the search is case-insensitive.
    """
    if query.lower() in candidate.lower():
        return True
    else:
        return False

# This will put the entire database into memory.
# Currently it is small enough that this does not matter.
with open(database, 'r') as f:
    records = f.read().split('%%\n')

for record in records:
    try:
        if match(query, record):
            print record.strip() # Remove the linefeeds
            # Add a visual separator between multiple matches.
            print '--------------------------------------------------------------------------------'
    except IndexError: # This happens if, e.g. there's an empty record so len(lines)==0.
        pass

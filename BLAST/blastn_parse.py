#!/usr/bin/env python3

"""
Parses blastn output file, through the use of regular expression, extracts the 
accession, length, and score, and prints the first ten of the parsed 
entries of the file
"""
import re

query_length_list = [] # holds the lengths to extract the query length
 

accession_section = False

accessions = [] # holds the accessions of each alignment 
lengths = [] # holds the lengths of each alignment
scores = [] # holds the scores of each alignment

x = 0
alignment_number = 1

for line in open('example_blast.txt'):
    if line.startswith('Query='):
        query_list = line.rstrip().split() # extract the query line
        query = query_list[1] # extract the query
    if line.startswith('Length='):
        query_length_list.append(line.rstrip()) # extract every length
        query_length_split = query_length_list[0].split('=') # extract the first length line (query length)
        query_length = query_length_split[1]
        
    
    accession = re.match(">(\S+)\s+(.+)", line) # matches accession lines
    length = re.match("(\S+)=(.+)", line) # matches length lines
    score = re.match("(\s+)(Score)(\s+=\s+)(\S+)", line) # matchs score lines
    
    if line.startswith("ALIGNMENTS"): # if in alignments section of file
        accession_section = True
        continue
    
    if accession: 
        accession_value = accession.groups()
        accessions.append(accession_value[0]) # extracts the accession names  
        
    if accession_section: # ignores query length line
        if length:
            length_value = length.groups()
            lengths.append(length_value[1]) # extracts each length value
        if score:
            score_value = score.groups()
            scores.append(score_value[3]) # extracts each score value

print("Query ID: {0} Query Length: {1}".format(query, query_length))

while x <= 10 and alignment_number <= 10: # prints first 10 alignment entries
    print("Alignment #{0}: Accession = {1} (Length = {2}, Score = {3})".format(alignment_number, accessions[x], lengths[x], scores[x]))
    x += 1
    alignment_number += 1
    
        

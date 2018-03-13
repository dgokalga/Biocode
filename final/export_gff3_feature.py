#!/usr/bin/env python3

"""
Parses gff3 file, requiring: path to gff3 file, type of sequence, atribute of sequence, 
and unique value of the sequence then extracts and prints the sequence from the 
fasta portion of the file
"""

import argparse

def main():
    """
    argparse creates the arguments required to parse the gff3 file and extract the fasta sequence,
    a dictionary is built for each entry in the fasta portion and uses start and stop coordinates 
    to extract the proper sequence
    """    
    parser = argparse.ArgumentParser(description = 'Parses GFF3 file')

    parser.add_argument('--source_gff', type = str, required = True, help = 'path to the gff3 file')
    parser.add_argument('--type', type = str, required = True, help = 'type of sequence (gene, CDS, chrmosome, etc)')
    parser.add_argument('--attribute', type = str, required = True, help = 'attribute of the sequence (ID)')
    parser.add_argument('--value', type = str, required = True, help = 'Unique value of the sequence')
        
    args = parser.parse_args()
    
    in_fasta_section = False
    fasta = {}
    
    reverse_dict = {'A':'T', 'C':'G', 'T':'A', 'G':'C'}
    
    reverse_comp = ''
    
    if args.type == '':
        print("No type argument present in query") # if type argument is blank
    elif args.attribute == '':
        print("No attribute argument present in query") # if attribute argument is blank
    elif args.value == '':
        print("No value argument present in query") # if value argument is blank
    else:
          
        for line in open(args.source_gff):
            
            cols = line.split('\t') # splits gff3 portion into 9 columns
            
            if len(cols) == 9:
                name = cols[0] # name of location of the sequence
                category = cols[2] # type of sequence
                start = cols[3] # start position
                stop = cols[4] # stop position
                strand = cols[6] # plus or minus strand
                key_value = cols[8] # unique value for the sequence
            
                if args.type == category and (args.attribute + '=' + args.value) in key_value: 
                   # if the inputted type and value match an entry in the file, extract location, start, stop
                    header = name
                    begin = start
                    end = stop
                    plus_minus = strand
        
            if line.startswith('##FASTA'):
                # if in the fasta portion of the file
                in_fasta_section = True
                continue    
            if in_fasta_section:
                # create dictionary of each entry in the fasta portion
                if line.startswith('>'):
                    key = line.rstrip()[1:]
                    fasta[key] = ''
                else:
                    fasta[key] += line.rstrip()
                    
   
        print('>{0}:{1}:{2}'.format(args.type, args.attribute, args.value)) # prints query
        for keys in fasta:
            if keys == header:
                sequence = fasta[keys][(int(begin)-1):(int(end))] 
                # extract appropriate sequence value using location key in dictionary and start, stop 
        
        if plus_minus == '-': # if minus strand
            reverse_seq = sequence[::-1] # reverse complement the extracted fasta sequence and print it
            for nuc in reverse_seq:
                reverse_comp += reverse_dict[nuc]
            for x in range (0, len(reverse_comp) - 1, 60):
                print(reverse_comp[x:x + 60])                
        else:
            for x in range (0, len(sequence) - 1, 60): # prints 60 nucleotides per line
                print(sequence[x:x + 60])
                                        
    
if __name__ == '__main__':
    main()
 
        
    
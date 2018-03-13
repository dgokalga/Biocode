#!/usr/bin/env python3

"""
Prompts user to keep enter a valid oligonucleotide sequence (comprised of A, C, G, T)
and prints the reverse complement of the sequence. If an invalid character exists
in the sequence, the program will stop prompting the user
""" 

reverse_dict = {'A':'T', 'C':'G', 'T':'A', 'G':'C'}

reverse_comp = ''
valid = True

while valid:
    seq = input("Please enter a valid oligonucleotide sequence: ")
    reverse_seq = seq[::-1]
    for nuc in reverse_seq:
        if nuc not in reverse_dict:
            valid = False
        else:
            reverse_comp += reverse_dict[nuc]
    
    if valid == False:
        print("Invalid nucleotide found in input sequence")
    else:
        print('The reverse complement is: {0}'.format(reverse_comp))
        reverse_comp = ''
        

#! /usr/bin/python3.4
# -*-coding:utf-8 -*

"""
Codes done thanks to the Coursera course named Biology Meets Programming: Bioinformatics for Beginners

"""

""" Module reverse_complement that return the reverse complement of a DNA sequence"""

def complement(Nucleotide):
    """
        Returns the complement sequence of the input sequence
    """
    comp = '' # output variable
    # your code here
    Nucleotide=str(Nucleotide)
    for i in Nucleotide:
        if i=='A':
            comp=comp + 'T'
        elif i=='T':
            comp=comp + 'A'
        elif i=='C':
            comp=comp + 'G'
        else :
            comp=comp + 'C'
    return comp

def ReverseComplement(Pattern):
    """
        Returns the reverse complement sequence of the input sequence.
        Calls the complement() function.
    """
    revComp = '' # output variable
    # your code here
    comp=complement(Pattern)
    for i in comp:
        revComp = str(i) + revComp
    return revComp

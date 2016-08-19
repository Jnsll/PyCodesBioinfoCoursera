#! /usr/bin/python3.4
# -*-coding:utf-8 -*

""" Codes done thanks to the Coursera course named Biology Meets Programming: Bioinformatics for Beginners """

""" Module reverse_complement that return the reverse complement of a DNA sequence"""

def complement(Nucleotide):
    """
        Returns the complement sequence of the input sequence
	
	:param: the sequence made of the letters A,C,G,T
	:type: string
	:return: the complement sequence
	:rtype: string

	:Example:

	>>> complement('ATTGC')
	'TAACG'

	..warnings:: The input sequence absolutely needs to only contain the letters A, C, T and G. No other letter is allowed.
    """

    comp = '' # output variable
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


def reverseComplement(Pattern):
    """
        Returns the reverse complement sequence of the input sequence.
        
	:param: The sequence made of the letters A,C,G,T
	:type: string
	:return: the reverse complement of the sequence
	:rtype: string

	:Example:

	>>> reverseComplement('ATGCT')
	'AGCAT' 

	..seealso:: complement()
	.. warnings:: The input sequence absolutely needs to only contain the letters A, C, T and G. No other letter is allowed.
    """

    revComp = '' # output variable
    comp=complement(Pattern)
    for i in comp:
        revComp = str(i) + revComp
    return revComp

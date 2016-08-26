#! /usr/bin/python3.4
# -*-coding:utf-8 -*

def FrequentWords(Text, k):
    """
	Search for the most repeated patterns in a text.

	:param Text: the text to look at.
	:param k: size of the patterns to look for in the text.
	:type Text: string
	:type k: int
	:return: list of the patterns most repeated in the text.
	:rtype: list of string

	..warnings:: int must be <= to len(Text)
	..seealso:: countDict(), remove_duplicates()
    """

    FrequentPatterns = []
    Count = countDict(Text, k)
    m = max(Count.values())
    for i in Count:
        if Count[i] == m:
            FrequentPatterns.append(Text[i:i+k])
    FrequentPatternsNoDuplicates = remove_duplicates(FrequentPatterns)
    return FrequentPatternsNoDuplicates

# Input:  A list Items
# Output: A list containing all objects from Items without duplicates
def remove_duplicates(Items):
    """
	Removes the duplicates in a list.

	:param Items: a list of string.
	:type: a list of strings
	:return: a list of string without duplicates.
	:rtype: a list of strings

	:Example:

	>>> remove_duplicates(['ATTC', 'ATTG', 'ATTC'])
	['ATTC', 'ATTG']
    """

    ItemsNoDuplicates = [] # output variable
    for x in Items:
        if x not in ItemsNoDuplicates:
            ItemsNoDuplicates.append(x)
    return ItemsNoDuplicates

# Input:  A string Text and an integer k
# Output: CountDict(Text, k)
def countDict(Text, k):
    """
	Counts how often the k-mers in a text appear.

	:param Text: a text you want to analyse
	:param k: the size of the k-mers to search for in the text.
	:type Text: string
	:type k: int
	:return: the number of times each k-mer is seen in Text.
	:rtype: dict of int

	..warnings:: k must be inferior/egal to len(Text)
	..seealso:: patternCount()
    """

    Count = {}
    for i in range(len(Text)-k+1):
        Pattern = Text[i:i+k]
        Count[i] = patternCount(Pattern, Text)
    return Count

# Input:  Strings Pattern and Text
# Output: The number of times Pattern appears in Text
def patternCount(Pattern, Text):
    """
	Counts how often a pattern appears in a Text.


	:param Pattern: the pattern to search for
	:param Text: Text in which the Pattern has to be searched for.
	:type Pattern: string
	:type Text: string
	:return: the number of times the Pattern appears in the Text.
	:rtype: int

	..warnings:: len(Pattern) must be <= to len(Text)
    """

    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count

###PatternMatching

def patternMatching(Pattern, Genome):
    """
	Gives the positions a pattern appears at in a Genome.

	:param Pattern: the pattern to look for.
	:param Genome: the text in which the pattern has to be looked for.
	:type Pattern: string
	:type Genome: string
	:return: list of the positions of the pattern in the genome
	:rtype: list of int

	..warnings:: len(Pattern) has to be <= to len(Genome)
    """

    positions = []
    for i in range(len(Genome)-len(Pattern)+1):
        if Genome[i:i+len(Pattern)] == Pattern:
            positions.append(i)
    return positions

def symbolArray(Genome, symbol):
    """
	Counts how often a symbol appears in the Genome.

	:param Genome: the text in which the symbol has to be looked for.
	:param symbol: the symbol to look for.
	:type Genome: string
	:type symbol: string
	:return: the number of time the symbol appears extending the length of Genome taking into account.
	:rtype: dict of list of int

	..warnings:: symbol must be a signle letter among G,C,T or A.
	..seealso:: patternCount()
    """

    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    for i in range(n):
        array[i] = patternCount(symbol, ExtendedGenome[i:i+(n//2)])
    return array

def FasterSymbolArray(Genome, symbol):
    """
	Counts how often a symbol appears in the Genome.
	Faster than SymbolArray().

	:param Genome: the text in which the symbol has to be looked for.
        :param symbol: the symbol to look for.
        :type Genome: string
        :type symbol: string
        :return: the number of time the symbol appears extending the length of Genome taking into account.
        :rtype: dict of list of int

        ..warnings:: symbol must be a signle letter among G,C,T or A.
        ..seealso:: patternCount()
    """
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    array[0] = patternCount(symbol, Genome[0:n//2])
    for i in range(1, n):
        array[i] = array[i-1]
        if ExtendedGenome[i-1] == symbol:
            array[i] = array[i]-1
        if ExtendedGenome[i+(n//2)-1] == symbol:
            array[i] = array[i]+1
    return array

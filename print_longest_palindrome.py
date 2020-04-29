# Definitions:

# *Palindrome* - "A sequence of characters which reads the same
# backward as forward, such as madam or racecar." [Source wikipedia:
# https://en.wikipedia.org/wiki/Palindrome]

# *Palindromic sequence* - "In most genomes or sets of genetic
# instructions, palindromic motifs are found. The meaning of palindrome
# in the context of genetics is slightly different, however, from the
# definition used for words and sentences. Since the DNA is formed by
# two paired strands of nucleotides, and the nucleotides always pair in
# the same way (Adenine (A) with Thymine (T), Cytosine (C) with Guanine
# (G)), a (single-stranded) sequence of DNA is said to be a palindrome
# if it is equal to its complementary sequence read backward. For
# example, the sequence ACCTAGGT is palindromic because its complement
# is TGGATCCA, which is equal to the original sequence in reverse
# complement." [See: https://en.wikipedia.org/wiki/Palindromic_sequence]

# Challenge:

# Write a function that, when given a string containing an arbitrary
# length DNA sequence, prints:
#   1) The starting index of the longest palindrome contained in the sequence
#   2) Prints the length of the palindrome
#   3) Prints the palindrome itself

# Example inputs with their outputs:

#   Input: ATTACCTAGGT
#   Output:
#     Starting Index: 2 # ERROR in example, should be 3
#     Length: 8
#     Palindrome: "ACCTAGGT"

#   Input: CTTAA
#   Output:
#     Starting Index: 1
#     Length: 4
#     Palindrome: "TTAA"

from genetic_sequence import GeneticSequence


def print_longest_palindrome(sequence_string):
    try:
        sequence = GeneticSequence(sequence_string)
    except GeneticSequence.InvalidSequenceError as e:
        print(f'\n{e}\n')
    else:
        pal = sequence.longest_palindrome
        if pal.sequence:
            print(f'\nStarting Index: {pal.index}')
            print(f'Length: {pal.sequence.length}')
            print(f'Palindrome: "{pal.sequence}"\n')
        else:
            print('\nNo palindrome found\n')


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        print_longest_palindrome(sys.argv[1])
    else:
        print('\nERROR: A sequence string is required.\n')

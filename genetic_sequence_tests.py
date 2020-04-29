import unittest

from genetic_sequence import GeneticSequence


class GeneticSequenceTest(unittest.TestCase):
    def test_invalid(self):
        self.assertRaises(GeneticSequence.InvalidSequenceError, GeneticSequence, 'junk')

    def test_case_insensitive(self):
        self.assertEqual(GeneticSequence('atcg'), 'ATCG')
        self.assertEqual(GeneticSequence('gCtA'), 'GCTA')

    def test_complement(self):
        self.assertEqual(GeneticSequence('ATCG').complement, 'TAGC')

    def test_is_palindrome(self):
        self.assertTrue(GeneticSequence('ACCTAGGT').is_palindrome)
        self.assertTrue(GeneticSequence('TGGATCCA').is_palindrome)
        self.assertTrue(GeneticSequence('TTAA').is_palindrome)
        self.assertTrue(GeneticSequence('CCGG').is_palindrome)
        self.assertTrue(GeneticSequence('AT').is_palindrome)
        self.assertTrue(GeneticSequence('CG').is_palindrome)

        self.assertFalse(GeneticSequence('TTACCTAGGT').is_palindrome)
        self.assertFalse(GeneticSequence('CTTAA').is_palindrome)
        self.assertFalse(GeneticSequence('ATTA').is_palindrome)

    def test_longest_palindrome_none(self):
        sequence = GeneticSequence('ACTG')
        self.assertIsNone(sequence.longest_palindrome.sequence)
        self.assertIsNone(sequence.longest_palindrome.index)

    def test_longest_palindrome_self(self):
        sequence = GeneticSequence('TTAA')
        self.assertEqual(sequence.longest_palindrome.index, 0)
        self.assertIs(sequence.longest_palindrome.sequence, sequence)

    def test_longest_palindrome_beginning(self):
        sequence = GeneticSequence('TGGATCCATTAA')
        self.assertEqual(sequence.longest_palindrome.index, 0)
        self.assertEqual(sequence.longest_palindrome.sequence.length, 8)
        self.assertEqual(sequence.longest_palindrome.sequence, 'TGGATCCA')

        sequence = GeneticSequence('AATTC')
        self.assertEqual(sequence.longest_palindrome.index, 0)
        self.assertEqual(sequence.longest_palindrome.sequence.length, 4)
        self.assertEqual(sequence.longest_palindrome.sequence, 'AATT')

    def test_longest_palindrome_middle(self):
        # Between shorter palindromes.
        sequence = GeneticSequence('TTAATGGATCCACCGG')
        self.assertEqual(sequence.longest_palindrome.index, 4)
        self.assertEqual(sequence.longest_palindrome.sequence.length, 8)
        self.assertEqual(sequence.longest_palindrome.sequence, 'TGGATCCA')

        sequence = GeneticSequence('GCAATTCG')
        self.assertEqual(sequence.longest_palindrome.index, 2)
        self.assertEqual(sequence.longest_palindrome.sequence.length, 4)
        self.assertEqual(sequence.longest_palindrome.sequence, 'AATT')

    def test_longest_palindrome_end(self):
        sequence = GeneticSequence('ATTACCTAGGT')
        self.assertEqual(sequence.longest_palindrome.index, 3)
        self.assertEqual(sequence.longest_palindrome.sequence.length, 8)
        self.assertEqual(sequence.longest_palindrome.sequence, 'ACCTAGGT')

        sequence = GeneticSequence('CTTAA')
        self.assertEqual(sequence.longest_palindrome.index, 1)
        self.assertEqual(sequence.longest_palindrome.sequence.length, 4)
        self.assertEqual(sequence.longest_palindrome.sequence, 'TTAA')


if __name__ == '__main__':
    unittest.main()

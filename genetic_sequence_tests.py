import unittest

from genetic_sequence import GeneticSequence


class GeneticSequenceTest(unittest.TestCase):
    def test_complement(self):
        self.assertEqual(GeneticSequence('ATCG').complement, 'TAGC')

    def test_is_palindrome(self):
        self.assertTrue(GeneticSequence('ACCTAGGT').is_palindrome)
        self.assertTrue(GeneticSequence('TGGATCCA').is_palindrome)
        self.assertTrue(GeneticSequence('TTAA').is_palindrome)
        self.assertTrue(GeneticSequence('AATT').is_palindrome)

        self.assertFalse(GeneticSequence('ATTACCTAGGT').is_palindrome)
        self.assertFalse(GeneticSequence('CTTAA').is_palindrome)

    def test_longest_palindrome(self):
        # At beginning
        self.assertEqual(GeneticSequence('TGGATCCATTAA').longest_palindrome_info.sequence,
                         'TGGATCCA')
        self.assertEqual(GeneticSequence('AATTC').longest_palindrome_info.sequence, 'AATT')

        # In the middle with shorter palindrome at the beginning.
        self.assertEqual(GeneticSequence('TTAATGGATCCACCCC').longest_palindrome_info.sequence,
                         'TGGATCCA')
        self.assertEqual(GeneticSequence('ATAATTT').longest_palindrome_info.sequence, 'AATT')

        # At the end
        self.assertEqual(GeneticSequence('ATTACCTAGGT').longest_palindrome_info.sequence,
                         'ACCTAGGT')
        self.assertEqual(GeneticSequence('CTTAA').longest_palindrome_info.sequence, 'TTAA')


if __name__ == '__main__':
    unittest.main()

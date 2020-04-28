from types import SimpleNamespace


class GeneticSequence:
    """Genetic sequence."""

    class InvalidSequenceError(Exception):
        pass

    COMPLEMENT_MAP = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C',
    }

    def __init__(self, string):
        string = string.upper()
        if not (isinstance(string, str) and all(n in self.COMPLEMENT_MAP for n in string)):
            raise self.InvalidSequenceError(f"ERROR: '{string}' is not a valid genetic sequence")
        self.string = string
        self.length = len(string)

    def __str__(self):
        return self.string

    def __repr__(self):
        return f"{self.__class__.__name__}('{self}')"

    def __eq__(self, other):
        return str(self) == str(other)

    @property
    def complement(self):
        """The genetic complement of this sequence."""
        return ''.join(self.COMPLEMENT_MAP[n] for n in self.string)

    @property
    def is_palindrome(self):
        """Is this sequence a genetic palindrome"""
        return self.string == ''.join(reversed(self.complement))

    @property
    def longest_palindrome_info(self):
        """
        Information about the longest genetic palindrome contained
        within this sequence.
        """
        if self.is_palindrome:
            return SimpleNamespace(index=0, sequence=self)

        longest_index = 0
        longest = GeneticSequence('')
        for index in range(self.length):
            # No need to search this sequence if a longer palindrome
            # has already been found.
            if (self.length - index - 1) <= longest.length:
                continue

            # Check longest sequences first to decrease scope.
            for end_index in range(self.length, index + 1, -1):
                sequence = GeneticSequence(self.string[index:end_index])
                # No point in checking for palindrome if this
                # sequence is shorter than the longest palindrome.
                if sequence.length <= longest.length:
                    break

                if sequence.is_palindrome:
                    longest_index = index
                    longest = sequence
                    # Since we are checking the longest sequences
                    # first, and we have already checked the length of
                    # this sequence against the length of the longest
                    # sequence, we can break out of the inner loop.
                    break

        return SimpleNamespace(index=longest_index, sequence=longest)

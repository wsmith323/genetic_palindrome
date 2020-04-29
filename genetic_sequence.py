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
        self._string = string
        self._length = len(string)
        self._complement = None
        self._is_palindrome = None
        self._longest_palindrome = None

    def __str__(self):
        return self._string

    def __repr__(self):
        return f"{self.__class__.__name__}('{self}')"

    def __eq__(self, other):
        return str(self) == str(other)

    length = property(lambda self: self._length)

    @property
    def complement(self):
        """The genetic complement of this sequence."""
        if self._complement is None:
            self._complement = ''.join(self.COMPLEMENT_MAP[n] for n in self._string)
        return self._complement

    @property
    def is_palindrome(self):
        """Is this sequence a genetic palindrome"""
        if self._is_palindrome is None:
            if self._length % 2:
                # Palindromes can't be odd lengths
                self._is_palindrome = False
            else:
                self._is_palindrome = self._string == ''.join(reversed(self.complement))
        return self._is_palindrome

    @property
    def longest_palindrome(self):
        """
        Longest genetic palindrome contained within this sequence.
        """
        if self._longest_palindrome is None:
            if self.is_palindrome:
                self._longest_palindrome = SimpleNamespace(index=0, sequence=self)
            else:
                longest_index = 0
                longest = GeneticSequence('')
                for index in range(self.length):
                    # No need to search this sequence if a longer palindrome
                    # has already been found.
                    if (self.length - index) <= longest.length:
                        break

                    # Check longest sequences first to decrease scope.
                    for end_index in range(self.length, index + 1, -1):
                        # Palindromes can't be odd lengths.
                        if (end_index - index) % 2:
                            continue

                        sequence = GeneticSequence(self._string[index:end_index])

                        if sequence.length <= longest.length:
                            # No point in checking for palindrome if this
                            # sequence is shorter than the longest palindrome.
                            break

                        elif sequence.is_palindrome:
                            longest_index = index
                            longest = sequence
                            # Since we are checking the longest sequences first,
                            # and we have already checked the length of this palindrome
                            # against the length of the longest palindrome, we can stop
                            # checking any further sub-sequences.
                            break

                if longest.length == 0:
                    self._longest_palindrome = SimpleNamespace(index=None, sequence=None)
                else:
                    self._longest_palindrome = SimpleNamespace(
                        index=longest_index, sequence=longest)

        return self._longest_palindrome

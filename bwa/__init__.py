from typing import List

from bwa.util import Heap


class BWT:
    EOF_CHARACTER = '$'
    """
    class to represent a Transform
    """

    def __init__(self, input_string: str) -> None:
        self._bwt = self.transform_string("{input_string}{self.EOF_CHARACTER}".format(**locals()))
        self._first_column = [r[0] for r in self._bwt]
        self._last_column = [r[-1] for r in self._bwt]

    def get_transform(self) -> str:
        return ''.join([r[-1] for r in self._bwt])

    @classmethod
    def load_bwt(cls, input_file):
        """
        convenience function to load serialized bwt
        :param input_file:
        :return:
        """
        pass

    @staticmethod
    def all_rotations_from_string(input_string: str) -> List[List[str]]:
        rotations = [[''] * len(input_string) for _ in input_string] # type: List[List[str]]
        rotations[0] = list(input_string)
        # position in table
        for table_pos in range(1, len(input_string)):
            for string_pos in range(len(input_string)):
                # position to start in string
                offset = (string_pos + len(input_string) - 1) % len(input_string)
                rotations[table_pos][string_pos] = rotations[table_pos - 1][offset]
        return rotations


    @staticmethod
    def transform_string(input_string: str) -> List[List[str]]:
        rotations = BWT.all_rotations_from_string(input_string)
        heap = Heap.from_lists(rotations) # type: Heap
        heap.sort()
        # return BWT string
        return heap.heap

    def inverse_bwt(self) -> str:
        """
        Let M be BWM(T) for some T.
        Let M0 be the matrix obtained by rotating all the rows of M to the right by one position.
        The first column of M0 equals the last column of M.
        :return:
        """
        # Rows are rotations of T, so the last column of the first row contains the character to the
        # left of $ in T: a in this case.

        """ algo
        special char should be first_column[0]
        first char to the left of the special char is in last_column[0]
        find first char in first_column > index of the last first char
            char in second_column[index of new first char] is to left of first char
            continue.
        """

        first_column_index = 0
        inverse_string = [] # type: List[str]
        for i in range(len(self._last_column) - 1):
            inverse_string.insert(0, self._last_column[first_column_index])
            self._last_column.pop(first_column_index)
            self._first_column.pop(first_column_index)
            first_column_index = self._first_column.index(inverse_string[0])


        return ''.join(inverse_string)


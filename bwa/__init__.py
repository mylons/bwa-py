from bwa.util import Heap


class BWT:
    EOF_CHARACTER = '$'
    """
    class to represent a Transform
    """

    def __init__(self, input_string):
        self._bwt = self.transform_string("{input_string}{self.EOF_CHARACTER}".format(**locals()))

    def get_transform(self):
        return ''.join(self._bwt)

    def get_inverse(self):
        """
        naive inverse that takes advantage of the fact that a property of the BWT is
        that given the last column of the matrix you know the first column.

        given that, you can find the $ char in the last column and the letter that immediately follows it
        is the same index in the first column. then, find that char in the last column, and repeat
        :return:
        """

        h = Heap.from_string_rotations(self._bwt)
        # now have the first row
        h.sort()
        output_string = []
        # find starting index of '$'
        index = self._bwt.index(self.EOF_CHARACTER)
        return ''.join(output_string)

    @classmethod
    def load_bwt(cls, input_file):
        """
        convenience function to load serialized bwt
        :param input_file:
        :return:
        """
        pass

    @staticmethod
    def all_rotations_from_string(input_string):
        rotations = [[None] * len(input_string) for _ in input_string]
        rotations[0] = list(input_string)
        # position in table
        for table_pos in range(1, len(input_string)):
            for string_pos in range(len(input_string)):
                # position to start in string
                offset = (string_pos + len(input_string) - 1) % len(input_string)
                rotations[table_pos][string_pos] = rotations[table_pos - 1][offset]
        return rotations


    @staticmethod
    def transform_string(input_string):
        rotations = BWT.all_rotations_from_string(input_string)
        heap = Heap.from_string_rotations(rotations)
        heap.sort()
        # return BWT string
        return [r[-1] for r in heap.heap]


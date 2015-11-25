from typing import List, Any

from bwa.util import Heap


class BWT:
    EOF_CHARACTER = '$'
    """
    class to represent a Transform
    """

    def __init__(self, input_string: str) -> None:
        self._bwt = self.transform_string("{input_string}{self.EOF_CHARACTER}".format(**locals()))

    def get_transform(self) -> str:
        return ''.join(self._bwt) # type: str


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
    def transform_string(input_string: str) -> List[str]:
        rotations = BWT.all_rotations_from_string(input_string)
        heap = Heap.from_lists(rotations)
        heap.sort()
        # return BWT string
        return [r[-1] for r in heap.heap]


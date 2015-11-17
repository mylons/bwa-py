from bwa.util import transform_string


class BWT:
    EOF_CHARACTER = '$'
    """
    class to represent a Transform
    """

    def __init__(self, input_string):
        self._bwt = [[]]
        self.pre_transformed_string = "{input_string}{self.EOF_CHARACTER}".format(**locals())
        self._bwt = transform_string(self.pre_transformed_string)

    def get_transform(self):
        return ''.join(self._bwt)

    @classmethod
    def load_bwt(cls, input_file):
        """
        convenience function to load serialized bwt
        :param input_file:
        :return:
        """
        pass




import unittest
from hamcrest import is_, assert_that
from bwa import BWT
from bwa.util import all_rotations_from_string


def test_all_rotations_from_string():

    rotations = [['^', 'B', 'A', 'N', 'A', 'N', 'A', '|'],
                 ['|', '^', 'B', 'A', 'N', 'A', 'N', 'A'],
                 ['A', '|', '^', 'B', 'A', 'N', 'A', 'N'],
                 ['N', 'A', '|', '^', 'B', 'A', 'N', 'A'],
                 ['A', 'N', 'A', '|', '^', 'B', 'A', 'N'],
                 ['N', 'A', 'N', 'A', '|', '^', 'B', 'A'],
                 ['A', 'N', 'A', 'N', 'A', '|', '^', 'B'],
                 ['B', 'A', 'N', 'A', 'N', 'A', '|', '^']]
    r = all_rotations_from_string("^Banana|".upper())
    assert_that(r, is_(rotations))

def test_transform():
    bwt = BWT("homolog.us")
    assert_that(bwt.get_transform(), is_("sgo$oolmhu."))




import unittest
from hamcrest import is_, assert_that
from bwa import BWT


def test_all_rotations_from_string():

    rotations = [['^', 'B', 'A', 'N', 'A', 'N', 'A', '|'],
                 ['|', '^', 'B', 'A', 'N', 'A', 'N', 'A'],
                 ['A', '|', '^', 'B', 'A', 'N', 'A', 'N'],
                 ['N', 'A', '|', '^', 'B', 'A', 'N', 'A'],
                 ['A', 'N', 'A', '|', '^', 'B', 'A', 'N'],
                 ['N', 'A', 'N', 'A', '|', '^', 'B', 'A'],
                 ['A', 'N', 'A', 'N', 'A', '|', '^', 'B'],
                 ['B', 'A', 'N', 'A', 'N', 'A', '|', '^']]
    r = BWT.all_rotations_from_string("^Banana|".upper())
    assert_that(r, is_(rotations))

def test_transform():
    original_string = "homolog.us"
    bwt = BWT(original_string)
    assert_that(bwt.get_transform(), is_("sgo$oolmhu."))
    #assert_that(bwt.get_inverse(), is_(original_string))

def test_transform_dna():
    bwt = BWT("ataata")
    assert_that(bwt.get_transform(), is_("atta$aa"))


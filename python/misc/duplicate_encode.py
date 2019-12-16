#!/usr/bin/python

import unittest
from collections import Counter

class DuplicateEncode:
    def duplicate_encode(self, word):
        lower_str, output_str = word.lower(), ""
        for char in lower_str:
            if lower_str.count(char) > 1:
                output_str+=")"
            else:
                output_str+="("
        return output_str


class ValidateDuplicateEncode(unittest.TestCase):

    def test_general_case(self):
        vdcls = DuplicateEncode()
        self.assertEquals(vdcls.duplicate_encode("din"), "(((")

    def test_case_sensitive(self):
        vtcls = DuplicateEncode()
        self.assertEquals(vtcls.duplicate_encode("Success"), ")())())")

if __name__ == "__main__":
    unittest.main()

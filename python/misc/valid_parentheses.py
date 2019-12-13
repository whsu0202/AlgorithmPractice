#!/usr/bin/python

import unittest

class ValidParentheses:
    def valid_parentheses(self, inp_string):
        p_count = 0
        for x in inp_string:
            if x == "(":
                p_count+=1
            if x == ")":
                p_count-=1
            if p_count < 0:
                return False
        return True if p_count == 0 else False

class ValidParenthesesTest(unittest.TestCase):

    def test_single_parentheses_with_space(self):
        vpclass = ValidParentheses()
        self.assertEquals(vpclass.valid_parentheses("  ("),False)

    def test_single_parentheses_with_characters(self):
        vpclass = ValidParentheses()
        self.assertEquals(vpclass.valid_parentheses(")test"),False)

    def test_parentheses_with_empty_input(self):
        vpclass = ValidParentheses()
        self.assertEquals(vpclass.valid_parentheses(""),True)

    def test_parentheses_with_an_extra_left_parentheses(self):
        vpclass = ValidParentheses()
        self.assertEquals(vpclass.valid_parentheses("hi())("),False)

    def test_parentheses_with_correct_quantity(self):
        vpclass = ValidParentheses()
        self.assertEquals(vpclass.valid_parentheses("hi(hi)()"),True)

if __name__ == "__main__":
    unittest.main()

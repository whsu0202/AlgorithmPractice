#!/usr/bin/python

import unittest

class ValidParentheses:
    def valid_parentheses(self, string):
        L_P, R_P, characters = [], [], []
        input_string = list(string)
        print input_string
        for symbl in input_string:
            if input_string[0] == ")":
                return False
            elif input_string[-1] == "(":
                return False
            elif symbl == "(":
                L_P.append(symbl)
            elif symbl == ")":
                R_P.append(symbl)
            else:
                characters.append(symbl)
    
        if len(L_P) != len(R_P):
            return False
        else:
            return True

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

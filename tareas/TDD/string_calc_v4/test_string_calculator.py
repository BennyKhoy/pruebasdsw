import unittest
from . import exercise


class TestStringCalculator(unittest.TestCase):

    '''Test Req1'''
    def test_empty_string_returns_zero(self):
        resultado = exercise.add("")
        self.assertEqual(resultado, 0)

    def test_single_number_returns_itself(self):
        resultado = exercise.add("1")
        self.assertEqual(resultado, 1)

    def test_two_numbers_returns_sum(self):
        resultado = exercise.add("1,2")
        self.assertEqual(resultado, 3)

    def test_return_type_is_int(self):
        resultado = exercise.add("1")
        self.assertIsInstance(resultado, int)

    '''Test Req2'''
    def test_three_numbers_returns_sum(self):
        resultado = exercise.add("1,2,3")
        self.assertEqual(resultado, 6)

    def test_many_numbers_returns_sum(self):
        resultado = exercise.add("1,2,3,4,5")
        self.assertEqual(resultado, 15)

    '''Test Req3'''
    def test_newline_as_separator_returns_sum(self):
        resultado = exercise.add("1,2\n3")
        self.assertEqual(resultado, 6)

    def test_only_newlines_as_separators(self):
        resultado = exercise.add("1\n2\n3")
        self.assertEqual(resultado, 6)

    '''Test Req4'''
    def test_trailing_comma_raises_exception(self):
        with self.assertRaises(Exception):
            exercise.add("1,2,")

    def test_valid_input_without_trailing_comma_does_not_raise(self):
        try:
            exercise.add("1,2")
        except Exception:
            self.fail("add() raised an exception with valid input")

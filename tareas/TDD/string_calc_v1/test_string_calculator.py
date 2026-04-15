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

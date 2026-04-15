# -*- coding: utf-8 -*-
# Alan Varela
# 25 Marzo 26

"""
Test Driven Development
"""

import unittest

from . import exercise

class TestFizzbuzz(unittest.TestCase):
    '''Test Req1'''
    def test_accepts_number_returns_string(self):
        resultado = exercise.fizzbuzz(1)
        self.assertEqual(resultado, "1")
        self.assertIsInstance(resultado, str)
    '''Test Req2'''
    def test_multiples_of_3_returns_fizz(self):
        resultado = exercise.fizzbuzz(3)
        self.assertEqual(resultado, "Fizz")

    
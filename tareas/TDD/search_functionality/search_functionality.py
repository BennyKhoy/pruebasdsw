import unittest
import csv

import os

class CitySearch:
    def __init__(self, csv_filename):
        base_path = os.path.dirname(__file__)
        csv_path = os.path.join(base_path, csv_filename)
        
        self.cities = []
        with open(csv_path, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            self.cities = [row['city'] for row in reader]

    def search(self, text):
        if text == "*": 
            return self.cities
        
        if len(text) < 2: 
            return []
        
        return [c for c in self.cities if text.lower() in c.lower()]


class TestCitySearch(unittest.TestCase):
    def setUp(self):
        self.search_engine = CitySearch('cities.csv')
        self.test_data = [
            {
                "input": "Va", 
                "output": ["Valencia", "Vancouver"] 
            },
            {
                "input": "ape", 
                "output": ["Budapest"] 
            },
            {
                "input": "a", 
                "output": [] 
            }
        ]

    def test_search_cities(self):
        for i in self.test_data:
            with self.subTest(i=i):
                actual = self.search_engine.search(i["input"])
                self.assertEqual(actual, i["output"], f"In: {i['input']}, Out: {actual}")
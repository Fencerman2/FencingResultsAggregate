import unittest
from src.scraper.fetch_result import fetch_pool_results


class TestEventResults(unittest.TestCase):
    def test_get_correct_pool(self):
        pool = fetch_pool_results("Troy", "Smith", 64739)


if __name__ == '__main__':
    unittest.main()

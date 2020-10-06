import unittest
from qual_id.categories.festivals import Festivals
from test.utils.category_helper import CategoryHelper

class TestFestivals(unittest.TestCase):
    def setUp(self):
        self.festivals = Festivals()

    def test__get_values__is_valid(self):
        error_message = CategoryHelper.get_values_error_message(self.festivals)
        self.assertTrue(error_message == "", error_message)

if __name__ == "__main__":  # pragma: no cover
    unittest.main()
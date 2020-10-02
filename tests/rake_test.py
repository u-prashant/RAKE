import unittest
import os
import sys
from rake.rake import RAKE

sys.path.append(os.path.abspath(sys.path[0]) + '/../')


class TestRAKE(unittest.TestCase):

    def setUp(self):
        self.rake = RAKE('rake/resources/SmartStoplist.txt')

    def test_exec(self):
        text = """
        Keyword extraction is not that difficult after all.
        There are many libraries that can help you with keyword extraction.
        Rapid automatic keyword extraction is one of those.
        """
        expected_scores = [
            ('rapid automatic keyword extraction', 13.333333333333332),
            ('keyword extraction', 5.333333333333333),
            ('difficult', 1.0),
            ('libraries', 1.0)]
        actual_scores = self.rake.exec(text)
        self.assertEqual(expected_scores, actual_scores)

        expected_scores = [('difficult', 1.0), ('libraries', 1.0)]
        self.assertNotEqual(expected_scores, actual_scores)


suite = unittest.TestLoader().loadTestsFromTestCase(TestRAKE)
unittest.TextTestRunner(verbosity=2).run(suite)

# if __name__ == '__main__':
#     unittest.main()

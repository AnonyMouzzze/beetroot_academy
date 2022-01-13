import unittest 
import os
from task1 import OpenFile

class TestContextManager(unittest.TestCase):

    def test_file_is_opened(self):
        with OpenFile('myfile.txt', 'w') as file:
            self.assertFalse(file.closed)
            file.close()

    def test_file_exists(self):
        with OpenFile('myfile.txt', 'w') as file:
            self.assertTrue(os.path.exists('myfile.txt'))

    def test_logger_exists(self):
        self.assertTrue(os.path.exists('logger.txt'))

    def test_counter(self):
        with OpenFile('myfile.txt', 'w') as fp:
            fp.close()
        with OpenFile('myfile.txt', 'w') as fp:
            fp.close()
        self.assertEqual(OpenFile.get_usage_count(), 2)
    
    def test_logger(self):
        with OpenFile('logger.txt') as fp:
            self.assertIn('Close file', fp.readlines()[-1])

unittest.main()
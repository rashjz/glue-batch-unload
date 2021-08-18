import sys
import unittest

sys.path.append('python')
sys.path.append('../python')

import unload

JOB_NAME                    = 'AWS DynamoDB Table Unload'
ARGUMENT_KEY_DYNAMODB_TABLE = 'dynamodb_table'
ARGUMENT_KEY_S3_LOCATION    = 's3_location'

class test_unload(unittest.TestCase):
    def test_JOB_NAME_constant(self):
        self.assertEqual(unload.JOB_NAME, JOB_NAME)
        
    def test_ARGUMENT_KEY_DYNAMODB_TABLE_constant(self):
        self.assertEqual(unload.ARGUMENT_KEY_DYNAMODB_TABLE, ARGUMENT_KEY_DYNAMODB_TABLE)
        
    def test_ARGUMENT_KEY_S3_LOCATION_constant(self):
        self.assertEqual(unload.ARGUMENT_KEY_S3_LOCATION, ARGUMENT_KEY_S3_LOCATION)
        
if __name__ == '__main__':
    unittest.main()

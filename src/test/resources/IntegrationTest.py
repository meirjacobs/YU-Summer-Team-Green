import unittest
import requests


class MyTestCase(unittest.TestCase):
    def test_something(self):
        response = requests.get("https://3ef2nnls3c.execute-api.us-east-1.amazonaws.com/deployedStage", "id=1")
        self.assertEqual(response.status_code, 200, "ERROR: statusCode = " + str(response.status_code))


if __name__ == '__main__':
    unittest.main()
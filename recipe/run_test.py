from coscine import ApiClient, AuthenticationError
import unittest


class TestCoscineClient(unittest.TestCase):
  def test___init__(self):
    c = ApiClient("NotAValidToken")
    self.assertTrue(isinstance(c, ApiClient))
    self.assertTrue(isinstance(c.version, str))
  def test___projects(self):
    c = ApiClient("NotAValidToken")
    self.assertRaises(AuthenticationError, c.projects)
 

if __name__ == '__main__':
    unittest.main()

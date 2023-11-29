from coscine import ApiClient, AuthorizationError
import unittest


class TestCoscineClient(unittest.TestCase):
  def test___init__(self):
    c = ApiClient("NotAValidToken")
    self.assertTrue(isinstance(c, ApiClient))
    self.assertTrue(isinstance(c.version, str))
  def test___projects(self):
    c = ApiClient("NotAValidToken")
    self.assertRaises(AuthorizationError, c.projects)
 

if __name__ == '__main__':
    unittest.main()

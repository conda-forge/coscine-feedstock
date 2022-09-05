from coscine import Client, AuthorizationError
import unittest


class TestCoscineClient(unittest.TestCase):
  def test___init__(self):
    c = Client("NotAValidToken")
    self.assertTrue(isinstance(c, Client))
    self.assertTrue(isinstance(c.__version__, str))
  def test___projects(self):
    c = Client("NotAValidToken")
    self.assertRaises(AuthorizationError, c , projects)
 

if __name__ == '__main__':
    unittest.main()

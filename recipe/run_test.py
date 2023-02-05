from coscine import Client
import unittest


class TestCoscineClient(unittest.TestCase):
  def test___init__(self):
    c = Client("NotAValidToken")
    self.assertTrue(isinstance(c, Client))
    self.assertTrue(isinstance(c.version, str))
  def test___projects(self):
    c = Client("NotAValidToken")
    self.assertRaises(PermissionError, c.projects)
 

if __name__ == '__main__':
    unittest.main()

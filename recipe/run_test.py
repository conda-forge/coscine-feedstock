from coscine import ApiClient, AuthenticationError
import unittest


class TestCoscineClient(unittest.TestCase):
  def test___init__(self):
    try:
      c = ApiClient("NotAValidToken")
    except CoscineException:
      pass
  def test___projects(self):
    try:
      c = ApiClient("NotAValidToken")
    except CoscineException:
      pass
 

if __name__ == '__main__':
    unittest.main()

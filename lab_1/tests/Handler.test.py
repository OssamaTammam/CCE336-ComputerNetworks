import unittest
import Handler


class HandlerTest(unittest.TestCase):
    def setUp(self):
        self.handler = Handler()

    def testHandleNoWords(self):
        self.assertEqual(self.handler.handleNoWords("This is a test"), 4)
        self.assertEqual(self.handler.handleNoWords(""), 0)

    def test_handleNoLowercase(self):
        self.assertEqual(self.handler.handleNoLowercase("Hello World"), 8)
        self.assertEqual(self.handler.handleNoLowercase(""), 0)

    def test_handleNoUppercase(self):
        self.assertEqual(self.handler.handleNoUppercase("Hello World"), 2)
        self.assertEqual(self.handler.handleNoUppercase(""), 0)

    def test_handleNoNumeric(self):
        self.assertEqual(self.handler.handleNoNumeric("12345abc"), 5)
        self.assertEqual(self.handler.handleNoNumeric(""), 0)

    def test_handleNoChar(self):
        self.assertEqual(self.handler.handleNoChar("Hello World"), 10)
        self.assertEqual(self.handler.handleNoChar(""), 0)


if __name__ == "__main__":
    unittest.main()

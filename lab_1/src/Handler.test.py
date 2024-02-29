import unittest
from unittest.mock import MagicMock
from Handler import Handler


class HandlerTest(unittest.TestCase):
    def setUp(self):
        self.request = MagicMock()
        self.handler = Handler(self.request, MagicMock(), MagicMock())

    def testHandleNoWords(self):
        self.assertEqual(self.handler.handleNoWords("This is a test"), 4)
        self.assertEqual(self.handler.handleNoWords(""), 0)

    def testHandleNoLowercase(self):
        self.assertEqual(self.handler.handleNoLowercase("Hello World"), 8)
        self.assertEqual(self.handler.handleNoLowercase(""), 0)

    def testHandleNoUppercase(self):
        self.assertEqual(self.handler.handleNoUppercase("Hello World"), 2)
        self.assertEqual(self.handler.handleNoUppercase(""), 0)

    def testHandleNoNumeric(self):
        self.assertEqual(self.handler.handleNoNumeric("12345abc"), 5)
        self.assertEqual(self.handler.handleNoNumeric(""), 0)

    def testHandleNoChar(self):
        self.assertEqual(self.handler.handleNoChar("Hello World"), 10)
        self.assertEqual(self.handler.handleNoChar(""), 0)

    def testHandle(self):
        operations = ["W", "L", "U", "R", "T", "", "B"]
        expectedResults = {
            "W": 5,
            "L": 13,
            "U": 1,
            "R": 1,
            "T": 15,
            "": 14,
            "B": "This is a request 1",
        }
        for operation in operations:
            mockRequest = f"{operation}This is a request 1"
            self.request.recv.return_value = mockRequest.encode("utf-8")
            response = self.handler.handle()

            self.assertEqual(response, expectedResults[operation])

            self.request.recv.assert_called_with(1024)

        self.assertEqual(self.request.recv.call_count, len(operations) + 1)


if __name__ == "__main__":
    unittest.main()

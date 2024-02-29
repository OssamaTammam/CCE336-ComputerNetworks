import unittest
from unittest.mock import MagicMock
from Handler import Handler


class TestHandler(unittest.TestCase):
    def setUp(self):
        self.mockRequest = MagicMock()
        self.mockHandler = Handler(self.mockRequest, MagicMock(), MagicMock())

    # test string is "This is a Response1234"
    def testHandle(self):
        expectedResponses = {
            "W": "The number of words is 4\n",
            "L": "The number of lowercase letters is 13\n",
            "U": "The number of uppercase letters is 2\n",
            "R": "The number of numeric letters is 4\n",
            "T": "The number of characters is 19\n",
            "": "The number of characters is 18\n",
            "B": "BThis is a Response1234\n",
        }

        for operation in expectedResponses:
            message = operation + "This is a Response1234\n"
            message = message.encode("utf-8")

            self.mockHandler.request.recv.return_value = message
            self.mockHandler.handle()

            response = self.mockHandler.request.sendall.call_args[0][0].decode("utf-8")

            self.assertEqual(response, expectedResponses[operation])


if __name__ == "__main__":
    unittest.main()

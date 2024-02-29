import socketserver


class Handler(socketserver.BaseRequestHandler):
    ## TODO: Handle a request logic
    def handle(self):
        data = self.request.recv(1024)
        data = data.decode("utf-8").strip()
        operation = data.split()[0][0]
        string = data[1:]

        if operation == "W":
            self.handleNoWords(string)
        elif operation == "L":
            self.handleNoLowercase(string)
        elif operation == "U":
            self.handleNoUppercase(string)
        elif operation == "R":
            self.handleNoNumeric(string)
        elif operation == "T":
            self.handleNoChar(string)
        else:
            return string

    def handleNoWords(self, string):
        return len(string.split())

    def handleNoLowercase(self, string):
        noLowerCase = 0
        for char in string:
            if ord(char) >= ord("a") and ord(char) <= ord("z"):
                noLowerCase += 1
        return noLowerCase

    def handleNoUppercase(self, string):
        noUppercase = 0
        for char in string:
            if ord(char) >= ord("A") and ord(char) <= ord("Z"):
                noUppercase += 1
        return noUppercase

    def handleNoNumeric(self, string):
        noNumeric = 0
        for char in string:
            if ord(char) >= ord("0") and ord(char) <= ord("9"):
                noNumeric += 1
        return noNumeric

    def handleNoChar(self, string):
        noChar = 0
        for char in string:
            if char != " ":
                noChar += 1
        return noChar

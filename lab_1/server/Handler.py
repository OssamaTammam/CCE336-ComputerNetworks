import socketserver


class Handler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024)
        data = data.decode("utf-8").strip()
        operation = data.split()[0][0]
        string = data[1:]

        if operation == "W":
            response = self.handleNoWords(string)
        elif operation == "L":
            response = self.handleNoLowercase(string)
        elif operation == "U":
            response = self.handleNoUppercase(string)
        elif operation == "R":
            response = self.handleNoNumeric(string)
        elif operation == "T":
            response = self.handleNoChar(string)
        else:
            response = string + "\n"

        self.request.sendall(response.encode("utf-8"))

    def handleNoWords(self, string):
        return f"The number of words is {len(string.split())}\n"

    def handleNoLowercase(self, string):
        noLowerCase = 0
        for char in string:
            if ord(char) >= ord("a") and ord(char) <= ord("z"):
                noLowerCase += 1
        return f"The number of lowercase letters is {noLowerCase}\n"

    def handleNoUppercase(self, string):
        noUppercase = 0
        for char in string:
            if ord(char) >= ord("A") and ord(char) <= ord("Z"):
                noUppercase += 1
        return f"The number of uppercase letters is {noUppercase}\n"

    def handleNoNumeric(self, string):
        noNumeric = 0
        for char in string:
            if ord(char) >= ord("0") and ord(char) <= ord("9"):
                noNumeric += 1
        return f"The number of numeric letters is {noNumeric}\n"

    def handleNoChar(self, string):
        noChar = 0
        for char in string:
            if char != " ":
                noChar += 1
        return f"The number of characters is {noChar}\n"

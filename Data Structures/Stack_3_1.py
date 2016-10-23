
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == [] #An empty list. Could also use 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

# Reverse a string with a Stack
def revString(mystr):
    x = Stack()
    for i in mystr:
        x.push(i)
    revstr = ""  # An empty string
    while not x.isEmpty():
        revstr = revstr + x.pop()
    return revstr

# print(revString("abc"))
#
# test = Stack()
# test.push(0)
# test.push(1)
# print test.isEmpty()
# test.pop()
# test.pop()
# print test.isEmpty()

#Paranthasees Match Checker
def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

# print(parChecker('((()))'))
# print(parChecker('(()'))

# All open/close symbol checker
def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

#helper for checker
def matches(top,close):
    opens = "([{" #Ordering of symbols must be kept the same to match
    closes = ")]}"
    return opens.index(top) == closes.index(close)
#Return: open paren will be index 0, close paren will also be index 0 ...

# print(parChecker('{{([][])}()}'))
# print(parChecker('[{()]'))

# Takes a decimal number and converts to binary
def divideBy2(decNumber):
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2

    binString = ""
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())

    return binString

print(divideBy2(42))


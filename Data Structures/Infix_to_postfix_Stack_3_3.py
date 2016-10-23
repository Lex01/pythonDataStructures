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

#Convert string to list
#if statements for math logic, adding to stack as needed
#return answer

def infixToPostfix(s):
    opstack = Stack()
    output = []
    infix = s.split()
    for item in infix:
        if item == '(': #If left paren, push onto opstack
            opstack.push(item)
        elif item == ')':   #If right paren, pop operators off opstack and append to final list
            top = opstack.pop()
            while top != '(':   #once stack gets to left paren, no more operators left. discard paren
                output.append(top)
                top = opstack.pop()
        elif item in '+-*/':    #If operator, send to opCompare func to check which op is higher precedence
            while not opstack.isEmpty() and opCompare(opstack,item): #if top of opstack is higher,pop and append to output, put item onto stack.
                output.append(opstack.pop())
            opstack.push(item)
        else:                   #If its a number, append to final list
            output.append(item)
    while not opstack.isEmpty():    #Any operators in opstack are added to the end of list.
        output.append(opstack.pop())
    return "".join(output)

def opCompare(opstack, item):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    if prec[opstack.peek()] >= prec[item]:
        return True
    else:
        return False


sample1 = "( A + B ) * ( C + D )"
sample2 = "( A + B ) * C"
print(infixToPostfix(sample2))
print(infixToPostfix("A + B * C"))





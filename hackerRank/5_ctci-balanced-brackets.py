# USE Stacks to match brackets.
# Push each item on Stack. If next item is a closing bracket
#   that matches with the previous, pop it off the stack, getting
#   rid of both of them. If they ever do not match, return False

class Stack:
    def __init__(self):
        self.items = []
    def size(self):
        return len(self.items)
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def isEmpty(self):
        return self.size() == 0


def is_matched(expression):
    s = Stack()
    for ch in expression:
        if ch in '([{':
            s.push(ch)
        elif s.isEmpty():
            return False
        else:
            top = s.pop()
            if not matcher(top,ch):
                return False
    if s.isEmpty():
        return True

def matcher(top,ch):
    openers = "([{"
    closers = ")]}"
    return openers.index(top) == closers.index(ch)

t = int(raw_input().strip())
for a0 in xrange(t):
    expression = raw_input().strip()
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"
#
# 3
# {[()]}
# {[(])}
# {{[[(())]]}}
#Data Structures Ch. 1-13-2
#Logic Gates and Circuits

class LogicGate:
    def __init__(self,n):
        self.label = n
        self.output = None
    def getLabel(self):
        return self.label
    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output



# This is a very common pattern that you should always use when building class hierarchies.
# Child class constructors need to call parent class constructors and then move on to their own
# distinguishing data.
class BinaryGate(LogicGate):
    def __init__(self,n):
        LogicGate.__init__(self,n)
        self.pinA = None
        self.pinB = None
    def getPinA(self):
        if self.pinA is None:
            return int(input("Enter Pin A input for gate " + self.getLabel() + "-->"))
        else:
            return self.pinA.getFrom().getOutput() #pin is wired to a Connector
    def getPinB(self):
        if self.pinB is None:
            return int(input("Enter Pin B input for gate " + self.getLabel() + "-->"))
        else:
            return self.pinB.getFrom().getOutput()
    def setNextPin(self,source):
        if self.pinA is None:
            self.pinA = source
        else:
            if self.pinB is None:
                self.pinB = source
            else:
                raise RuntimeError("Error: NO EMPTY PINS")


class UnaryGate(LogicGate):
    def __init__(self,n):
        LogicGate.__init__(self,n)
        self.pin = None
    def getPin(self):
        if self.pin is None:
            return int(input("Enter Pin input for gate " + self.getLabel() + "-->"))
        else:
            return self.pin.getFrom().getOutput()
    def setNextPin(self,source):
        if self.pin is None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")


class AndGate(BinaryGate):
    def __init__(self,n):
        BinaryGate.__init__(self,n)
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0

class NandGate(AndGate):
    def performGateLogic(self):
        if AndGate.performGateLogic(self) == 1:
            return 0
        else:
            return 1

class OrGate(BinaryGate):
    def __init__(self,n):
        BinaryGate.__init__(self,n)
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a==1 or b==1:
            return 1
        else:
            return 0

class NorGate(OrGate):
    def performGateLogic(self):
        if OrGate.performGateLogic(self) == 1:
            return 0
        else:
            return 1

class NotGate(UnaryGate):
    def __init__(self,n):
        UnaryGate.__init__(self,n)
    def performGateLogic(self):
        pin = self.getPin()
        if pin == 1:
            return 0
        else:
            return 1


class Connector:
    def __init__(self,fgate,tgate):
        self.fromGate = fgate
        self.toGate = tgate
        tgate.setNextPin(self)
    def getFrom(self):
        return self.fromGate
    def getTo(self):
        return self.toGate

def main():
   # g1 = AndGate("G1")
   # g2 = AndGate("G2")
   # g3 = OrGate("G3")
   # g4 = NotGate("G4")
   # c1 = Connector(g1,g3)
   # c2 = Connector(g2,g3)
   # c3 = Connector(g3,g4)
   # print(g4.getOutput())

   # and1 = AndGate("AND1")
   # and2 = AndGate("AND2")
   # nor3 = NorGate("NOR3")
   # c4 = Connector(and1,nor3)
   # c5 = Connector(and2,nor3)
   # print(nor3.getOutput())

   a1 = NandGate("A1")
   a2 = NandGate("A2")
   a3 = AndGate("A3")
   c1 = Connector(a1,a3)
   c2 = Connector(a2,a3)
   print(a3.getOutput())

   # j1 = NandGate("J1")
   # print(j1.getOutput())

main()




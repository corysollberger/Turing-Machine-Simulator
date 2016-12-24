#COS 451: Homework 9 : Turing Machines

class Turing:
    def __init__(self, Q, r, blank, Sig, delt, q0, F, tape):
        self.Q = Q
        self.r = r
        self.blank = blank
        self.Sig = Sig
        self.delt = delt
        self.q0 = q0
        self.F = F
        self.tape = tape
        self.head = 50
        self.tapereset = 50
        self.currentState = q0

    def printElements(self):
        print ("Q: " + str(self.Q))
        print ("r: " + str(self.r))
        print ("blank: " + str(self.blank))
        print ("Sig: " + str(self.Sig))
        print ("delt: " + str(self.delt))
        print ("q0: " + str(self.q0))
        print ("F: " + str(self.F))
        print ("tape: " + str(self.tape))
        print ("tapeHead: " + str(self.head))

    #Used for initialization, writing a string to the tape and reseting the head
    def writeTape(self, s):
        size = len(s)
        for c in s:
            if(c in self.r):
                self.tape[self.head] = c
                self.head+=1
            else:
                print("ERROR: Characters not in tape alphabet\n")
                break;
        print ("Written to tape...\n")
        print (self.tape)
        self.head = self.tapereset

    #Writes to the tape, but does not move the head
    def writeTapeExecute(self, s):
        size = len(s)
        if(s in self.r):
            self.tape[self.head] = s
        else:
            print("ERROR: Characters not in tape alphabet\n")
        print (s + " written to tape...\n")
        print (self.tape)

    #moves the head position on the tape
    def moveHead(self, s):
        if(s == 'R'): #move right
            self.head+=1
        elif(s == 'L'): #move left
            self.head-=1
        else:
            pass
        
    #Read the symbol off the tape
    def readTape(self):
        return self.tape[self.head]

    #executes the turing machine
    def execute(self):
        temp = self.currentState
        currentInput = self.readTape()
        while (temp != '0' and temp not in self.F):
            print("Testing: " + str(temp) + ", " + str(currentInput))
            inl = 0
            for x in self.delt:
                print(str(x[0]) + ", " + str(x[2]))
                if(x[0][0] == temp and x[2] == currentInput):
                    print ("Entered\n")
                    inl = 1
                    self.writeTapeExecute(x[3])
                    self.moveHead(x[4])
                    currentInput = self.readTape()
                    temp = x[1]
                    break
            print (self.tape)
            if(inl == 0):
                temp = '0'
        if(temp not in self.F):
            print ("Ending state: " + str(temp) + ", Fail: Does not reach accepting state\n")
        else:
            print("Success! " + str(temp) + " Accepting State\n")
        
                
#Read the desired information from a file
def readFile(fileName):
    f = open(fileName, 'r') #opens file to read the 5 elements of the NDFA
    inpLines = []
    for line in f:
        inpLines.append(line.rstrip('\n'))
    count = 0
    delt.clear()
    for x in inpLines:
        if count == 0:
            Q.clear()
            for a in inpLines[count]:
                Q.add(a)
        elif count == 1:
            r.clear() 
            for a in inpLines[count]:
                r.add(a)
        elif count == 2:
            for a in inpLines[count]:
                blank = a
        elif count == 3:
            Sig.clear()
            for a in inpLines[count]:
                Sig.add(a)
        elif count == 4:
            for a in inpLines[count]:
                q0 = a
        elif count == 5:
            F.clear() 
            for a in inpLines[count]:
                F.add(a)
        elif count >= 6:
            s = ""
            v = ""
            tempTuple = ()
            for a in inpLines[count]:
                if(a=='.'):
                    v = s
                    tempTuple += (v,)
                    s = ""
                elif(a=='|'):
                    tempTuple += (s,)
                    s = ""
                else:
                    s = s+ a
            delt.append(tempTuple)
        count = count + 1           
        
#Declare the variables associated with the turing machine
tape = [] #tape that will be read
tapeHead = 50 #the middle of the tape so it can move left and right
Q = set(['0','1','2','3','4','5','6','7']) #set of states
r = set(['0', '1', '2', 'x', 'y', 'z', '']) #set of tape alphabet symbols
blank = '' #the symbol occuring infinitely on the tape
Sig = set(['0','1','2']) #the set of input symbols
delt = [] #list of transitions
q0 = '1' #initial state
F = set(['7']) #the set of final (accepting) states

#Initialize values
for x in range(0,100): #initialize tape to blank 100 spots
    tape.append(blank)

readFile("test.txt")
#delt.append(tuple(['1','2', '0', 'x', 'R']))
#delt.append(tuple(['2','2', 'y', 'y', 'R']))
#delt.append(tuple(['2','2', '0', '0', 'R']))
#delt.append(tuple(['2','3', '1', 'y', 'R']))
#delt.append(tuple(['3','3', 'z', 'z', 'R']))
#delt.append(tuple(['3','3', '0', '0', 'L']))
#delt.append(tuple(['3','3', '1', '1', 'L']))
#delt.append(tuple(['3','3', '1', '1', 'R']))
#delt.append(tuple(['3','1', 'x', 'x', 'R']))
#delt.append(tuple(['3','7', '', '', 'S']))
#delt.append(tuple(['3','4', 'y', 'y', 'L']))
#delt.append(tuple(['3','4', '2', 'z', 'L']))
#delt.append(tuple(['4','4', '0', '0', 'L']))
#delt.append(tuple(['4','4', '1', '1', 'L']))
#delt.append(tuple(['4','4', 'z', 'z', 'L']))
#delt.append(tuple(['4','4', 'y', 'y', 'L']))
#delt.append(tuple(['4','1', 'x', 'x', 'R']))
#delt.append(tuple(['4','1', 'x', 'x', 'R']))
#delt.append(tuple(['1','5', 'y', 'y', 'L']))
#delt.append(tuple(['5','5', 'x', 'x', 'L']))
#delt.append(tuple(['5','6', '', '', 'R']))
#delt.append(tuple(['6','6', 'x', 'x', 'R']))
#delt.append(tuple(['6','6', 'y', 'y', 'R']))
#delt.append(tuple(['6','6', 'z', 'z', 'R']))
#delt.append(tuple(['6','7', '', '', 'S']))
#delt.append(tuple(['1','7', '', '', 'S']))

#print(r)

t1 = Turing(Q,r,blank,Sig,delt,q0,F,tape)
t1.printElements()
t1.writeTape("001122")
t1.execute()

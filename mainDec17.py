
import copy

class Slot:
    # index reprensents the slot number, domain is the list of body
    # parts that users can work on, boolean represents if the user
    # is available to practice at the given slot
    def __init__(self, index, domain, boolean):
        self.index = index
        self.domain = domain
        self.free = boolean
        self.value = None

    def getIndex(self):
        return self.index
    def isFree(self):
        return (self.free == 1)
    def getDomain(self):
        return self.domain
    def getValue(self):
        return self.value
    def setValue(self, value):
        self.value = value
    def setDomain(self, domain):
        self.domain = domain

# to hinder repetitiveness
principleZero = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}


# principle of relatability: on the same day, 
    #pick muscles most related to the current muscle to do
principleOne = {1: {2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1}, #all the same, how to convey this? 
                2: {1: 1, 3: 3, 4: 2, 8: 1},
                3: {1: 1, 2: 3, 8: 1},
                4: {1: 1, 8: 3, 2: 1},
                5: {1: 1, 6: 2, 9: 2},
                6: {1: 1, 5: 2, 9: 2},
                7: {1: 1, 8: 3, 3: 1},
                8: {1: 1, 7: 3, 4: 2, 2: 1},
                9: {1: 1, 5: 2, 6: 2}}

# principle of doing push toegtehr and pull together
principleTwo = {1: {1: 1, 7: 1, 8:1, 9: 1}, # pull do together
                    2: {2: 1, 3: 1, 4: 1, 5: 1, 6: 1}, #push do together
                    3: {2: 1, 3: 1, 4: 1, 5: 1, 6: 1}, #push
                    4: {2: 1, 3: 1, 4: 1, 5: 1, 6: 1}, #push
                    5: {2: 1, 3: 1, 4: 1, 5: 1, 6: 1}, #push
                    6: {2: 1, 3: 1, 4: 1, 5: 1, 6: 1}, #push
                    7: {1: 1, 7: 1, 8:1, 9: 1}, #pull
                    8: {1: 1, 7: 1, 8:1, 9: 1}, #pull
                    9: {1: 1, 7: 1, 8:1, 9: 1}} #pull

# principle3 rank muscles from big to small: on the SAME day, better to start with big muscle first
# wrong order, just testing
principleThree = [ 
                (9, 2), 
                (7, 2),
                (4, 2), 
                (5, 2),
                (1, 1),
                (3, 0), 
                (2, 2),
                (6, 0),
                (8, 0)
                        ]

# counting score, return a scoreBoard as a list of tuple of (part, score)
# the scoreboard returned is sorted from big to small
def scoreCount(currBodyPart):

    w1 = 3 # weight of principle 1, we can change this later
    w2 = 1 # weight of principle 1, we can change this later
    scoreBoard = [] # key = body part, value = its score according to principle 1 + 2
    for i in range(9): # iterate through bodyPart, remember to i+1, bc we start from 1
        part = i+1
        score = 0
        if part in principleOne[currBodyPart]:
            score = score + w1*principleOne[currBodyPart][part]
        if part in principleTwo[currBodyPart]:
            score = score + w2*principleTwo[currBodyPart][part]

        # trying priciple zero
        score = score + principleZero[part]

        scoreBoard.append((part, score))
   



    
    scoreBoardSorted = sorted(scoreBoard, key=lambda tup: tup[1])
    scoreBoardSorted.reverse()
    return scoreBoardSorted

# counting score, return a scoreBoard as a list of tuple of (part, score)
# the scoreboard returned is sorted from big to small
def scoreCount2():

    w0 = 2 # weight of principle 1, we can change this later
    #w2 = 1 # weight of principle 1, we can change this later
    scoreBoard = [] # key = body part, value = its score according to principle 1 + 2
    for i in range(9): # iterate through bodyPart, remember to i+1, bc we start from 1
        part = i+1
        score = 0

        for (thisPart, thisScore) in principleThree:
            if thisPart == part:
                score = score + w0*thisScore


        #if part in principleThree[currBodyPart]:
            #score = score + w1*principleOne[currBodyPart][part]

        # trying priciple zero
        score = score + principleZero[part]

        scoreBoard.append((part, score))
    
    
    scoreBoardSorted = sorted(scoreBoard, key=lambda tup: tup[1])
    scoreBoardSorted.reverse()

    return scoreBoardSorted


 
# (will call scoreCount WITHIN this function!!)
# takes in slotList, slotIndex (you want to fill), bodyPart to work on the previous slot
# IMPORTANT: this method only order the domain of the NEXT (one) slot (aka slotIndex) on the SAME day
def orderDomainWithScore(slotList,slotIndex,bodyPart): 
    scoreBoard = scoreCount(bodyPart)
    domain = slotList[slotIndex].getDomain()
    tempDomain = []

    for (part, score) in scoreBoard:
        if part in domain:
            tempDomain.append(part)

    slotList[slotIndex].setDomain(tempDomain)
    #print "1 the ordered domain is", tempDomain
    #print "Xiaoyin did it!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"



# order domain (for the first slot of a new day) from big to small muscles
# according to principle3
# pass in slotList, and the slotIndex you want to fill
def orderDomainBigToSmall(slotList,slotIndex):

    print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    scoreBoard = scoreCount2()
    domain = slotList[slotIndex].getDomain()
    tempDomain = []

    for (part, score) in scoreBoard:
        if part in domain:
            tempDomain.append(part)

    slotList[slotIndex].setDomain(tempDomain)
    #print "2 the ordered domain is", tempDomain


    
def rest(slotList,bodyPart, startingSlot, length):
    end = startingSlot + length
    if startingSlot + length >=21:
        end = 20

    for i in range(startingSlot,end+1):
        slot=slotList[i]
        #print "slot index", slot.getIndex()
        domain = list(slot.getDomain())
        
        #print "domain is", domain
        if bodyPart in domain:
            domain.remove(bodyPart)
        slotList[i].setDomain(domain)
        #print "new domain is", slotList[i].getDomain()
    return None

#when there is no value to choose from for an available slot, it's not consistent
def isConsistent(slotList):
    for s in slotList:
        if (s.isFree) and (len(s.domain)==0):
            return False
    return True


def isComplete(slotList):
#check if all the possible slots have been assigned values
    for c in slotList:
        if (c.isFree):
            if c.value == None:
                return False
    return True
#create the ordered domain list for the rest of the slots in the same day
#reorder domain from best to worst to recommend
# takes in slotList, slotIndex, bodyPart to work on the previous slot, and update the domain list of the rest of the slots
"""def updateDomain(slotList,slotIndex,bodyPart):
    if (slotIndex%3 !=2 ):
        
        principle1 = {'ABS': ["anything"], #how to convey this? 
                'CHEST': ['TRICEPS', 'SHOULDERS', 'BICEPS'],
                'TRICEPS': ['CHEST', 'BICEPS'],
                'SHOULDERS': ['BICEPS', 'CHEST'],
                'QUADS': ['CALVES', 'HAMSTRING'],
                'CALVES': ['QUADS', 'HAMSTRING'],
                'BACK': ['BICEPS', 'TRICEPS'],
                'BICEPS': ['BACK', 'SHOULDERS', 'CHEST'],
                'HAMSTRING': ['QUADS', 'CALVES']}
        recommendedList= principles1[bodyPart]
        recommendedList.reverse()
        domain = slotList[slotIndex].getDomain()
        for item in recommendedList:
            if item in domain:
                domain.remove(item)
                domain.insert(0,item)"""

#backtracking algorithm
def backtracking(slotList):
    global principleZero
    if (isComplete(slotList)):
        #print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!success!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        return slotList
    indexChosen = firstUnassigned(slotList)
    if indexChosen== None:
        #print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!index chosen is None!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        return slotList
    else: 
        if indexChosen%3 == 0:
            orderDomainBigToSmall(slotList, indexChosen)
        domainChosen = slotList[indexChosen].getDomain()
        #print "indexChosen", indexChosen, "domainChosen",domainChosen
    slotListCopy = list(slotList) # save a copy of slot list
    #slotListCopy = copy.deepcopy(slotList)
    # save a copy of current principle zero
    #global principleZero
    principleZeroCopy = copy.deepcopy(principleZero)

    #print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!here is indexChosen is", indexChosen
    for value in domainChosen:
        setValue(slotList,indexChosen,value)
        #print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!here is indexChosen is", indexChosen
        #if (indexChosen % 3 < 2):    #peter try to debug
        if ((indexChosen+1) % 3 != 0): 
            orderDomainWithScore(slotList, indexChosen+1, value)
            #print "Xiaoyin did it!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        #elif (indexChosen!= 20):
        #else:
            #orderDomainBigToSmall(slotList, indexChosen+1)
            #print "Peter did it!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"

        #print "value set for index", indexChosen, "is", value
        
        #print "isConsistent",isConsistent(slotList)
        if isConsistent(slotList):
            printTest(slotList)
            backtracking(slotList)
        else:
            #global principleZero
            #principleZero = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

            slotList = slotListCopy
            # reinstate previous principle zero
            #global principleZero
            principleZero = principleZeroCopy

    if (isComplete(slotList)):
        return -1

#print the final result from the backtracking algorithm
def result(slotList):
    if len(slotList)==0:
        return 
    for c in slotList:
        if c.isFree():
            print "slot", c.getIndex(),"you should work on body part", c.getValue()



#return the index number of the first unassigned slot
def firstUnassigned(slotList):
    
    for c in slotList:
        if c.value==None and c.isFree():
            print "c.Isfree",c.isFree()
            return c.index
    



def setValue(slotList,slotIndex, bodyPart):
    #set the corresponding slot to the input bodyPart
    slotList[slotIndex].setValue(bodyPart)

    #update the domain for the next related slots
    length= restAux1(bodyPart, slotIndex)
    rest(slotList, bodyPart,slotIndex,length)

    #try principle zero, do global this way?
    global principleZero
    principleZero[bodyPart] = - 20
    #print "pzero is", principleZero

    return bodyPart
    
#!!!!!!!!Calculate the number of slots to rest    
# output n: in the future n slots, you can't do that bodyPart 
# to consider: index out of bound
#input:bodyPart is an integer and startingSlot is the index number of the slot
def restAux1(bodyPart, startingSlotIndex):
	day = (startingSlotIndex / 3) + 1
	slotsLeftThisDay = (3*day - 1) - startingSlotIndex
	return slotsLeftThisDay + (getRecoverTime(bodyPart) - 1)*3  #depend on how you write bodyPart data 

# assuming bodyPart is an integer
# output n: the number of days needed to recover for that bodyPart
def getRecoverTime(bodyPart):
    	if bodyPart == 1:
    		return 1

        #elif bodyPart == 2:
         #   return 3
    	else: 
    		return 2

#print our the slotList just to try it out
def printTest(slotList):
    print "/////////////////////Work out Routine////////////"
    for c in slotList:
        bodypart = (0,"ab","chest", "tricep","shoulder","quad","calves","back","biceps","hamstring")
        value = c.getValue()
        print "slot no." ,c.getIndex(), "isFree?", c.isFree()
        if value!=None:
            print "work on:", bodypart[value]
        print "..................................."
def main():
    printwo  =[2,9,7,4,5,1,3,6,8]
    person = raw_input('Enter your name: ')
    arraySize = 21
    bodyPartNum = 9
    weekPlan = raw_input('Enter your availability')
    bodyPart = raw_input('Enter the number representing the body parts you want to exercise, in the following order 1ab,2chest, 3tricep,4shoulder,5quad,6calves,7back,8biceps,9hamstring, e.g 12356, type nothing if you want to exercise all body parts')
    
    #guarantees that the weekPlan user inputs must be of size 21
    if (len(weekPlan) != arraySize):
        raise ValueError('Input has to be of size',arraySize)
    #guarantees that the bodyPart user inputs must be of size 9
    if (len(bodyPart) ==0):
        domain  = printwo
    else:
        body = []
        #for x in printwo:
         #   if x in bodyPart:
        for x in bodyPart:
            body.append(int(x))
            #reverse the schedule list for the ease of popping in the future
        domain = body


    #array to store the schedule
    #For example: [1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1]
    schedule = []
    for c in weekPlan:
        schedule.append(int(c))

    #reverse the schedule list for the ease of popping in the future
    schedule.reverse()

    #generate an array of arraySize number of slots
    slotList = []
    for i in range(arraySize):
        sloti = Slot(i,domain,schedule.pop())
        slotList.append(sloti)

        
        #print " sloti.getIndex", sloti.getIndex()
        #print "sloti.isFree", sloti.isFree()
        #print "sloti.getDomain", sloti.getDomain()
    
    

    #rest(slotList, 2, 3, 4)
    #for i in slotList:
   #     print i.getDomain()

    #print"test"
    #print "restAux1(1,0):",restAux1(1,0)
    #print "restAux1(2,1):",restAux1(2,1)
    #print "restAux1(3,1):",restAux1(3,1)
    #print "restAux1(3,2):",restAux1(3,2)
    #print "restAux1(4,3):",restAux1(4,3)
    #print "restAux1(5,4):",restAux1(5,4)

    sol = backtracking(slotList)
    #print "-------------------------here is the answer-------------------------"
    #printTest(sol)
    




if __name__ == "__main__":
    main()

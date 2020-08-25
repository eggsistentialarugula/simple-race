import random
#super class
class animal:
    def __init__(self, aniType='unknown'):
        self.aniType = aniType
    def getType(self):
        return self.aniType
    def move(self):
        return 1
    
class tortoise(animal):
    def __init__(self, aniType='tortoise'):
        super().__init__(aniType) #initialize type
    def move(self):
        movePattern = (3,3,3,3,3,-6,-6,1,1,1 )
        oddNum = random.randint(0,9)
        return movePattern[oddNum]

class hare(animal):
    def __init__(self, aniType='hare'):
        super().__init__(aniType) #initialize type
    def move(self):
        movePattern = (0,0,9,9,-12,1,1,1,-2,-2 )
        oddNum = random.randint(0,9)
        return movePattern[oddNum]

class track:
    def __init__(self, ani= animal('Unknown')):  
        self.pos=0 # this is the position of the animal
        self.ani = ani # this is the animal running on track
    # Now we implement track when time is tick 1 time
    def trackTick(self):
        self.pos += self.ani.move() #- new position when time tick 1
        if self.pos < 0: #- can not go negative in postion
            self.pos = 0
        elif self.pos > 70: # 70 is the end mark
            self.pos = 70
        dashLine= '-' * 71  # we will display track with animal
        # self.ani.getType()[0 is the first character of animal type]
        print (dashLine[:self.pos] + self.ani.getType()[0]+ dashLine[self.pos+1:])
        return self.pos

Hare = hare()
Tort = tortoise()
track1 = track(Tort) #initalize a track with tortoise
track2 = track(Hare) #initialize a track with hare

posT = 0
posH = 0
tick = 0
while(posT < 70 and posH < 70):
    posT = track1.trackTick()
    posH = track2.trackTick()
    tick += 1

if(posT > posH):
    print("Tortoise is the winner.")
elif(posH > posT):
    print("Hare is the winner.")
else:
    print("It's a tie.")

print('The tick value is ' + str(tick) + '.')

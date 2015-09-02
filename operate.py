def goLeft():
    ldistance = 15; #example
    #robot goes left, motor1 turns counterclockwise until leftStop is true
    return ldistance

def goRight():
    rdistance = 35; #example
    #robot goes right, motor1 turns clockwise until rightStop is true
    return rdistance

def calcLineDistance():
    goLeft() #start at one end
    fullDistance = goRight() #
    return fullDistance/2

def goToMiddle(position):
    mid = repr(position)
    print "hawkbot is now in the middle"

def wait():
#if lsensor sees, go left until stop, then wait for 20 sec return to middle
#if rsensor sees, go right until stop, then wait for 20 sec return to middle 
    return

def run():
  midpoint = calcLineDistance()
  goToMiddle(midpoint)
  wait()

power = True

while power == True:
    run()

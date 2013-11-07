import copy
from operator import itemgetter, attrgetter
from debug import *

def buildByLength(length):
  out = []
  for a in range(0,4):
    for b in range(0, 6):
      for c in range(0, 8):
        if a + b + c == length:
          out.append( [a,b,c] )

  return out

def isChildrenAllTrue(states, state):
  if state[0] + state[1] + state[2] == 1:
    return True

  for x in range(3):
    tmpState = copy.copy(state)
    while tmpState[0] != -1 and tmpState[1] != -1 and tmpState[2] != -1:
      tmpState[x] -= 1

      for s in states:
        if s[0] == tmpState[0] and s[1] == tmpState[1] and s[2] == tmpState[2]:
          if s[3] == False:
            return False

  return True

states = []
for x in range(1,16):
  lengthStates = buildByLength(x)
  for lState in lengthStates:
    if isChildrenAllTrue(states, lState):
      states.append(lState + [False])
      print red(lState),
    else:
      states.append(lState + [True])
      print green(lState),
  print

states = sorted(states, key=itemgetter(0,1,2))

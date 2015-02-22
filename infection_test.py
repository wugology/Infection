mentorA = Mentor("A")
mentorA.add_student(["B", "C", "D", "E", "F"])
mentorC = Mentor("C")
mentorC.add_student(["G", "H", "I"])
mentorJ = Mentor("J")
mentorJ.add_student(["K", "L", "M", "N", "O", "P", "Q"])
mentorQ = Mentor("Q")
mentorQ.add_student(["R", "S", "T", "U", "V"])
mentorZ = Mentor("Z")
mentorZ.add_student(["W", "X", "Y"])

mentorList = [mentorA, mentorC, mentorJ, mentorQ, mentorZ]

## Infecting A, C, or any of A's or C's students will infect all of them.

infected = [] #no infected users
infect("A")
#Returns: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

infected = []
infect("C")
#Returns: ['C', 'A', 'B', 'D', 'E', 'F', 'G', 'H', 'I']

infected = []
infect("D")
#Returns: ['D', 'A', 'B', 'C', 'E', 'F', 'G', 'H', 'I']

infected = []
infect("H")
#Returns: ['H', 'C', 'G', 'I']
## BUG: because mentorC is listed after mentorA in the mentorList,
## the infection doesn't spread backwards to A's class


## Infecting J, Q, or  any of J's or Q's students will infect all of them.
infected = []
infect("J")
#Returns: ['J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V']

infected = []
infect("Q")
#Returns: ['Q', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'V']

infected = []
infect("M")
#Returns: ['M', 'J', 'K', 'L', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V']

infected = []
infect("T")
#Returns: ['T', 'Q', 'R', 'S', 'U', 'V']
## BUG: because mentorQ is listed after mentorJ in the mentorList,
## the infection doesn't spread backwards to J's class


## Infecting Z or any of Z's students will only infect them.
infected = []
infect("Z")
#Returns: ['Z', 'W', 'X', 'Y']

infected = []
infect("W")
#Returns: ['W', 'Z', 'X', 'Y']

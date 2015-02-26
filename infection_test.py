CoachA = Coach("A")
CoachA.add_student(["B", "C", "D", "E", "F"]) #C is teacher
CoachC = Coach("C")
CoachC.add_student(["G", "H", "I"]) #C is student of A
CoachJ = Coach("J")
CoachJ.add_student(["K", "L", "M", "N", "Q"]) #Q is teacher
CoachP = Coach("P")
CoachP.add_student(["B", "E", "H", "C", "O"]) #contains O and students from A and C
CoachQ = Coach("Q")
CoachQ.add_student(["R", "S", "T", "U", "V"]) #Q is student of J
CoachZ = Coach("Z")
CoachZ.add_student(["W", "X", "Y"]) #no connections with other classes

coachList = [CoachA, CoachC, CoachJ, CoachP, CoachQ, CoachZ]
users = getUserList()

## Infecting A, C, P, or any of their students will infect all of them.
## Infecting J, Q, or  any of their students will infect all of them.
## Infecting Z or any of Z's students will only infect that class.

for u in range(0,len(users)):
    total_infection(users[u])
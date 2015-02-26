CoachA = Coach("A")
CoachA.add_student(["B", "C", "D", "E", "F","DD"]) #C is teacher
CoachC = Coach("C")
CoachC.add_student(["G", "H", "I","AA","BB","CC"]) #C is student of A
CoachJ = Coach("J")
CoachJ.add_student(["K", "L", "M", "N", "Q"]) #Q is teacher
CoachP = Coach("P")
CoachP.add_student(["B", "E", "H", "C", "O","EE"]) #contains O and students from A and C
CoachQ = Coach("Q")
CoachQ.add_student(["R", "S", "T", "U", "V"]) #Q is student of J
CoachZ = Coach("Z")
CoachZ.add_student(["W", "X", "Y"]) #no connections with other classes

coachList = [CoachA, CoachC, CoachJ, CoachP, CoachQ, CoachZ]

## Limiting the infection to 16 or more users will catch all users.
## Infecting A, C, P, or any of their students will infect 16 users.
## Limiting the infection to 15 or fewer users will catch all but students of A, C, and P.
## Infecting J, Q, or  any of their students will infect 11.
## Limiting the infection to 10 or fewer users will catch only Z and their students.
## Infecting Z or any of Z's students will only infect 4.
## Limiting the infection to 3 or fewer users will catch no users.

for u in range(0,17):
    limited_infection(u)
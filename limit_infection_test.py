mentorA = Mentor("A")
mentorA.add_student(["B", "C", "D", "E", "F","DD"]) #C is teacher
mentorC = Mentor("C")
mentorC.add_student(["G", "H", "I","AA","BB","CC"]) #C is student of A
mentorJ = Mentor("J")
mentorJ.add_student(["K", "L", "M", "N", "Q"]) #Q is teacher
mentorP = Mentor("P")
mentorP.add_student(["B", "E", "H", "C", "O","EE"]) #contains O and students from A and C
mentorQ = Mentor("Q")
mentorQ.add_student(["R", "S", "T", "U", "V"]) #Q is student of J
mentorZ = Mentor("Z")
mentorZ.add_student(["W", "X", "Y"]) #no connections with other classes

mentorList = [mentorA, mentorC, mentorJ, mentorP, mentorQ, mentorZ]

## Limiting the infection to 16 or more users will catch all users.
## Infecting A, C, P, or any of their students will infect 16 users.
## Limiting the infection to 15 or fewer users will catch all but students of A, C, and P.
## Infecting J, Q, or  any of their students will infect 11.
## Limiting the infection to 10 or fewer users will catch only Z and their students.
## Infecting Z or any of Z's students will only infect 4.
## Limiting the infection to 3 or fewer users will catch no users.

for u in range(0,17):
    limitInfection(u)
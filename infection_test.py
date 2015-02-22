mentorA = Mentor("A")
mentorA.add_student(["B", "C", "D", "E", "F"]) #C is teacher
mentorC = Mentor("C")
mentorC.add_student(["G", "H", "I"]) #C is student of A
mentorJ = Mentor("J")
mentorJ.add_student(["K", "L", "M", "N", "Q"]) #Q is teacher
mentorP = Mentor("P")
mentorP.add_student(["B", "E", "H", "C", "O"]) #contains O and students from A and C
mentorQ = Mentor("Q")
mentorQ.add_student(["R", "S", "T", "U", "V"]) #Q is student of J
mentorZ = Mentor("Z")
mentorZ.add_student(["W", "X", "Y"]) #no connections with other classes

mentorList = [mentorA, mentorC, mentorJ, mentorP, mentorQ, mentorZ]
users = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

## Infecting A, C, P, or any of their students will infect all of them.
## Infecting J, Q, or  any of their students will infect all of them.
## Infecting Z or any of Z's students will only infect them.

for u in range(0,len(users)):
    infected = []
    infect(users[u])
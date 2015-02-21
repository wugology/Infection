#users = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "Z", "Y", "Z"]


mentorA = Mentor("A")
mentorA.add_student(["B", "C", "D", "E", "F"])
mentorC = Mentor("C")
mentorC.add_student(["G", "H", "I"])
mentorJ = Mentor("J")
mentorJ.add_student(["K", "L", "M", "N", "O", "P", "Q"])
mentorQ = Mentor("Q")
mentorQ.add_student(["R", "S", "T", "U", "V", "W", "Z", "Y", "Z","A"])

mentorList = [mentorA, mentorC, mentorJ, mentorQ]

## Infecting A will also infect all of A's students, and C's students (since C is a student of A).
## Infecting C will only infect C's students.
## Infecting J will infect everyone, since Q is a student of J and A is a student of Q and C is a student of A.
## Infecting Q will infect everyone but J and J's students.

infect(mentorA)
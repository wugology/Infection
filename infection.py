class Mentor:
    def __init__(self, name):
        self.name = name
        self.students = [] #makes an empty list of students
    def add_student(self, student):
        self.students.extend(student) #fills empty list with students

def infect(mentor):
    infected = [] #initializes a list of infected users
    if mentor.name not in infected: #if the teacher isn't already infected
        infected.append(mentor.name) #then the teacher is added to the list
    for m in range(0,len(mentorList)): #check all the teachers
        if mentorList[m].name in infected: #if a teacher is infected
            for i in range(0,len(mentor.students)): #check all the teacher's students
                if mentor.students[i] not in infected: #if the student isn't already infected
                    infected.append(mentor.students[i]) #then the student is added to the list
        for s in range(0,len(mentorList[m].students)): #check all the teacher's students
            if mentorList[m].students[s] in infected: #if the student is infected
                infected.append(mentorList[m].name) #then the teacher must be infected
                for j in range(0,len(mentor.students)): #and all the other students must be infected too
                    if mentor.students[j] not in infected:
                        infected.append(mentor.students[j])
    print infected



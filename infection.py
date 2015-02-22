class Mentor:
    def __init__(self, name):
        self.name = name
        self.students = [] #makes an empty list of students
    def add_student(self, student):
        self.students.extend(student) #fills empty list with students

def infect(user):
    if user not in infected: #if the user isn't already infected
        infected.append(user) #then the user is added to the list
    for m in range(0,len(mentorList)): #check all the teachers
        if mentorList[m].name in infected: #if a teacher is infected
            for i in range(0,len(mentorList[m].students)): #check all the teacher's students
                if mentorList[m].students[i] not in infected: #if the student isn't infected
                    infected.append(mentorList[m].students[i]) #then the student is added to the list
        for s in range(0,len(mentorList[m].students)): #check all the teacher's students
            if mentorList[m].students[s] in infected: #if the student is infected
                if mentorList[m].name not in infected: #if the teacher isn't already infected
                    infected.append(mentorList[m].name) #then the teacher is added to the list
                    for j in range(0,len(mentorList[m].students)): #check all the teacher's students
                        if mentorList[m].students[j] not in infected: #if the student isn't infected
                            infected.append(mentorList[m].students[j]) #infect the student
    print infected



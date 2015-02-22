class Mentor:
    def __init__(self, name):
        self.name = name
        self.students = [] #makes an empty list of students
    def add_student(self, student):
        self.students.extend(student) #fills empty list with students


def getUserList():
    userList = []
    for n in range(0,len(mentorList)):
        if mentorList[n].name not in userList:
            userList.append(mentorList[n].name)
        for s in range(0,len(mentorList[n].students)):
            if mentorList[n].students[s] not in userList:
                userList.append(mentorList[n].students[s])
    return userList



def infect(user):
    infected = [user]
    for n in range(0,len(mentorList)): #outer loop ensures double checking
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
    return infected



def limitInfection(N):
    userList = getUserList()
    limitSpread = []
    for u in range(0,len(userList)):
        infected = infect(userList[u])
        if len(infected) <= N:
            limitSpread.append(userList[u])
    print "Infecting any of the following users will limit the infection to " + str(N) + " or fewer users: " + str(limitSpread)



class Coach:
    def __init__(self, name):
        self.name = name
        self.students = [] #makes an empty list of students
    def add_student(self, student):
        self.students.extend(student) #fills empty list with students


def getUserList():
    userList = []
    for n in range(0,len(coachList)): #checks all the coaches' classes
        if coachList[n].name not in userList:
            userList.append(coachList[n].name) #adds coach's name
        for s in range(0,len(coachList[n].students)):
            if coachList[n].students[s] not in userList:
                userList.append(coachList[n].students[s]) #adds students' names
    return userList



def infect(user):
    infected = [user]
    for n in range(0,len(coachList)): #outer loop ensures double checking
        for m in range(0,len(coachList)): #check all the coaches
            if coachList[m].name in infected: #if a coach is infected
                for i in range(0,len(coachList[m].students)): #check all the coach's students
                    if coachList[m].students[i] not in infected: #if the student isn't infected
                        infected.append(coachList[m].students[i]) #then the student is added to the list
            for s in range(0,len(coachList[m].students)): #check all the coach's students
                if coachList[m].students[s] in infected: #if the student is infected
                    if coachList[m].name not in infected: #if the coach isn't already infected
                        infected.append(coachList[m].name) #then the coach is added to the list
                        for j in range(0,len(coachList[m].students)): #check all the coach's students
                            if coachList[m].students[j] not in infected: #if the student isn't infected
                                infected.append(coachList[m].students[j]) #infect the student
    return infected



def limitInfection(N):
    userList = getUserList()
    limitSpread = []
    for u in range(0,len(userList)): #checks all the users
        infected = infect(userList[u]) #tries to infect the user
        if len(infected) <= N: #if the infection is less than or equal to the target number
            limitSpread.append(userList[u]) #add the user to the list
    print "Infecting any of the following users will limit the infection to " + str(N) + " or fewer users: " + str(limitSpread)



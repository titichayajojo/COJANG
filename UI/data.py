
from manipulateData import *
import currentUser
class DataManagement():
    def __init__(self):
        self.people  = ManipulateData().loadUsersData()
       

    def getUserByEmail(self):
        self.email = currentUser.email
        f = open('users', 'rb')
        self.objs = pickle.load(f)

        for key in self.objs:
            if self.objs[key]['email'] == self.email:
                return self.objs[key]


    def getAllPeople(self):
        return self.people
    
    def getAllProvice(self):
        List_p = []
        for i in self.people:
            a = self.people[i]
            p = a["province"]
            if p not in List_p:
                List_p.append(p)
        return List_p

    
    def getPeopleByName(self,n):
        print("eiei")
        List = []
        List_name = []
        for item in self.people:
            # print(item)
            person = self.people[item]
            s = person['fullname']
            # print(s)    
            if s.rfind(n) != -1:
                List.append(self.people[item])
        
        for j in List:
            List_name.append(j['fullname'])
        return List_name

        
        
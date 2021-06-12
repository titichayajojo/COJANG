

class DataManagement():
    def __init__(self):
        self.people = {
    "p01" : {
        "Name" : "Boon",
        "Surname" : "Pliasub",
        "Email" : "Boon@kmitl.ac.th",
        "Tel" : "0945462171",
        "STATE" : "Bangkok",
        "Status" : "Dead",
      

    },
    "p02" : {
        "Name" : "Jojo",
        "Surname" : "eiei",
        "Tel" : "0945462171",
        "STATE" : "Samut Sakorn",
        "Status" : "Vacinated",
        "Email" : "Jojo@kmitl.ac.th",
    

    },
    "p03" : {
        "Name" : "Tee",
        "Surname" : "eueu",
        "Tel" : "0945462171",
        "STATE" : "Lumpun",
         "Status" : "Non-Vacinated",
         "Email" : "Tee@kmitl.ac.th",

    },
    "p04" : {
        "Name" : "Rit",
        "Surname" : "pipi",
        "Tel" : "0945462171",
        "STATE" : "Chiang Mai",
         "Status" : "Infected",
         "Email" : "Rit@kmitl.ac.th",

    },
    "p05" : {
        "Name" : "Hbeat",
        "Surname" : "soo",
        "Tel" : "0945462171",
        "STATE" : "Lao",
         "Status" : "Infected",
         "Email" : "Hbeat@kmitl.ac.th",

    },
    "p06" : {
        "Name" : "Unn",
        "Surname" : "pl",
        "Tel" : "0945462171",
        "STATE" : "Pee Pee",
         "Status" : "Infected",
         "Email" : "Unn@kmitl.ac.th",

    },
    "p07" : {
        "Name" : "Bum",
        "Surname" : "Pliasub",
        "Tel" : "0945462171",
        "STATE" : "Pee Pee",
        "Status" : "Infected",
        "Email" : "Bum@kmitl.ac.th",
      

    },
     "p08" : {
        "Name" : "Bum2",
        "Surname" : "Pliasub",
        "Tel" : "0945462171",
        "STATE" : "Pee Pee",
        "Status" : "Dead",
        "Email" : "Bum2@kmitl.ac.th",
      

    },
    "p09" : {
        "Name" : "Bum3",
        "Surname" : "Pliasub",
        "Tel" : "0945462171",
        "STATE" : "Pee Pee",
        "Status" : "Dead",
        "Email" : "Bum2@kmitl.ac.th",
      

    }
    

}
    def getAllPeople(self):
        return self.people
    
    def getAllProvice(self):
        List_p = []
        for i in self.people:
            a = self.people[i]
            p = a["STATE"]
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
            s = person['Name']
            # print(s)    
            if s.rfind(n) != -1:
                List.append(self.people[item])
        
        for j in List:
            List_name.append(j['Name'])
        return List_name

        
        
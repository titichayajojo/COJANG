

class DataManagement():
    def __init__(self):
        self.people = {
    "p01" : {
        "Name" : "Boon",
        "Surname" : "Pliasub",
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
    
       
        

    },
    "p03" : {
        "Name" : "Tee",
        "Surname" : "eueu",
        "Tel" : "0945462171",
        "STATE" : "Lumpun",
         "Status" : "Non-Vacinated"

    },
    "p04" : {
        "Name" : "Rit",
        "Surname" : "pipi",
        "Tel" : "0945462171",
        "STATE" : "Chiang Mai",
         "Status" : "Infected"

    },
    "p05" : {
        "Name" : "Hbeat",
        "Surname" : "soo",
        "Tel" : "0945462171",
        "STATE" : "Lao",
         "Status" : "Infected"

    },
    "p06" : {
        "Name" : "Unn",
        "Surname" : "pl",
        "Tel" : "0945462171",
        "STATE" : "Pee Pee",
         "Status" : "Infected"

    },
    "p07" : {
        "Name" : "Bum",
        "Surname" : "Pliasub",
        "Tel" : "0945462171",
        "STATE" : "Pee Pee",
        "Status" : "Infected",
      

    },
     "p08" : {
        "Name" : "Bum2",
        "Surname" : "Pliasub",
        "Tel" : "0945462171",
        "STATE" : "Pee Pee",
        "Status" : "Dead",
      

    },

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

    
            
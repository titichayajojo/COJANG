
import pickle
from email_error_control import Email_Error

class ManipulateData:
    def __init__(self,fullname = '-',email ='-',password = '-',tel = '-',stage = '-',address = '-',province = '-',age = '-'):
        self.fullname = fullname
        self.email = email
        self.password = password
        self.tel = tel
        self.stage = stage
        self.address = address
        self.province = province
        self.age = age

    def storeData(self):
        user = {'fullname' : self.fullname, 'email': self.email, 'password': self.password, 'tel' : self.tel, 'stage' : self.stage, 'address' : self.address, 'province' : self.province, 'age' : self.age}
        # database
        db = {}
        print(user)
        db[str(self.email)] = user
        
        # Its important to use binary mode
        dbfile = open('users', 'ab')
        
        # source, destination
        pickle.dump(db, dbfile)                     
        dbfile.close()

        return True

    def loadData(self,email):
        self.email_error = Email_Error()
        self.email = email
        self.objs = []
        checkUser = False
        f = open('users', 'rb')     
        while 1:
            try:
                self.objs.append(pickle.load(f))
            except EOFError:
                break

        for dict in self.objs:
            for key in dict:
                if key == self.email:
                    print("email is already used")
                    self.email_error.show()
                    checkUser = True

        if checkUser == False:
            return False

    
    def updateStage(self,stage,email):
        self.email = email
        f = open('users', 'rb')        
        self.objs = pickle.load(f)

        for key in self.objs:
            if self.objs[key]['email'] == self.email:
                self.objs[key]['stage'] = stage
               
        

        with open('users', 'wb') as f:
            pickle.dump(self.objs, f)  

    def update_details(self,age,tel,address,province,email):
        self.email = email
        f = open('users', 'rb') 
        self.objs = pickle.load(f)    
       
        for key in self.objs:
            if self.objs[key]['email'] == self.email:
                self.objs[key]['age'] = age
                self.objs[key]['tel'] = tel
                self.objs[key]['address'] = address
                self.objs[key]['province'] = province
               

        with open('users', 'wb') as file:
            pickle.dump(self.objs, file)

        
if __name__ == "__main__":
    
    f = open('users', 'rb')     
    loaded_dictionary = pickle.load(f)
    print(loaded_dictionary)

import pickle
from email_error_control import Email_Error
import pprint
class ManipulateData:
    def __init__(self,fullname = '-',email ='-',password = '-',tel = '-',stage = '-',address = '-',province = '-',age = '-', sex = '-', id_number = '-' , nationality = '-'):
        self.fullname = fullname
        self.email = email
        self.password = password
        self.tel = tel
        self.stage = stage
        self.address = address
        self.province = province
        self.age = age
        self.sex = sex
        self.id_number = id_number
        self.nationality = nationality

    def storeData(self):
        user = {'fullname' : self.fullname, 'email': self.email, 'password': self.password, 
                'tel' : self.tel, 'stage' : self.stage, 'address' : self.address, 
                'province' : self.province, 'age' : self.age,
                'sex' : self.sex, 'id_number' : self.id_number, 'nationality' : self.nationality}

        # database
        db = {}
        print(user)
        db[self.email] = user
        
        # Its important to use binary mode
        dbfile = open('users', 'rb')
        self.objs = pickle.load(dbfile)
        self.objs[self.email] = user
        dbfile.close()

        file = open('users', 'wb')
        # source, destination
        pickle.dump(self.objs, file)                     
        file.close()

        return True

    def loadData(self,email):
        self.email_error = Email_Error()
        self.email = email
        
        checkUser = False
        try:
            f = open('users', 'rb')        
            self.objs = pickle.load(f)   
        except:
            print("Cannot Open")
            return False

        for key in self.objs:
            if self.objs[key]['email'] == self.email:
                print("email is already used")
                self.email_error.show()
                checkUser = True

        return checkUser 
 
    def update_stage(self,stage,email):
        self.email = email
        f = open('users', 'rb')        
        self.objs = pickle.load(f)

        for key in self.objs:
            if self.objs[key]['email'] == self.email:
                self.objs[key]['stage'] = stage
            
        with open('users', 'wb') as f:
            pickle.dump(self.objs, f)  
        
    def update_sex(self,sex,email):
        self.email = email
        f = open('users', 'rb')        
        self.objs = pickle.load(f)

        for key in self.objs:
            if self.objs[key]['email'] == self.email:
                self.objs[key]['sex'] = sex
            
        with open('users', 'wb') as f:
            pickle.dump(self.objs, f) 

    def update_details(self,age,tel,address,province,id_number,nationality,email):
        self.email = email
        f = open('users', 'rb') 
        self.objs = pickle.load(f)    
       
        for key in self.objs:
            if self.objs[key]['email'] == self.email:
                self.objs[key]['age'] = age
                self.objs[key]['tel'] = tel
                self.objs[key]['address'] = address
                self.objs[key]['province'] = province
                self.objs[key]['id_number'] = id_number
                self.objs[key]['nationality'] = nationality
               
        with open('users', 'wb') as file:
            pickle.dump(self.objs, file)

    def loadUsersData(self):
        f = open('users', 'rb')     
        loaded_dictionary = pickle.load(f)
        return loaded_dictionary
        
if __name__ == "__main__":
    
    f = open('users', 'rb')     
    loaded_dictionary = pickle.load(f)
    pprint.pprint(loaded_dictionary)
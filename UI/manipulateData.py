
import pickle
from create_profile_control import Create_Profile
from email_error_control import Email_Error
from login_control import Login

class ManipulateData:
    def __init__(self,fullname,email,password,tel = '-',stage = '-',address = '-',province = '-'):
        self.fullname = fullname
        self.email = email
        self.password = password
        self.tel = tel
        self.stage = stage
        self.address = address
        self.province = province

    def storeData(self):
        user = {'fullname' : self.fullname, 'email': self.email, 'password': self.password, 'tel' : self.tel, 'stage' : self.stage, 'address' : self.address, 'province' : self.province}
        # database
        db = {}
        print(user)
        db[str(self.email)] = user
        
        # Its important to use binary mode
        dbfile = open('users', 'ab')
        
        # source, destination
        pickle.dump(db, dbfile)                     
        dbfile.close()

        for dict in self.objs:
            for key in dict:
                print(key)

        self.create_profile = Create_Profile()
        self.create_profile.show()
        
    
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
        
if __name__ == "__main__":
    objs = []
    f = open('users', 'rb')     
    while 1:
        try:
            objs.append(pickle.load(f))
        except EOFError:
            break

    print(objs)
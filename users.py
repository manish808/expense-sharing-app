from database import users_table

class User:

    def __init__(self, id, name, email, mobile):
        
        self.id = id 
        self.name = name
        self.email = email
        self.mobile = mobile
        self.expenses = {}
    

class UserManager:

    def add_user(self, id, name, email, mobile):

        if id in users_table:
            print("Users already exist.")
            return
        users_table[id] = User(id, name, email, mobile)
    
    def get_user(self, id):

        if id in users_table:
            return users_table[id]
        print(f"User with id:{id} does not exist.")

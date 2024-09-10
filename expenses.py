from database import users_table
from users import UserManager

class ExpenseSharing:

    def create_user(self, id, name, email, mobile):
        user_admin = UserManager()
        user_admin.add_user(id, name, email, mobile)
    
    def get_user_detail(self, id):
        user_admin = UserManager()
        user_detail = user_admin.get_user(id)
        return user_detail
    

    def expenses(self, payer, borrower, expense_type, amount):

        if not isinstance(borrower, list):
            print("Borrower list is invalid.")
            return
        
        if len(borrower)==0:
            print("Borrowers list cannot be empty.")
            return
        
        payer_person = self.get_user_detail(payer)
        if payer_person is None:
            print("Invalid payer id.")
            return 
        
        
        for person in borrower:
            if person[0] not in users_table:
                print("Invalid id in borrower.")
                return
        
        if expense_type=='EQUAL':
            val = amount/len(borrower)
            for person in borrower:
                if person==payer:
                    continue
                borrower_detail = self.get_user_detail(person)
                if borrower_detail.id in payer_person.expenses:
                    payer_person.expenses[borrower_detail.id]+=val
                else:
                    payer_person.expenses[borrower_detail.id] = val
                
                if payer_person.id in borrower_detail.expenses:
                    borrower_detail.expenses[payer_person.id]-=val
                else:
                    borrower_detail.expenses[payer_person.id] = -val
        
        if expense_type=='EXACT':
            #Validating exact share
            total = 0
            for b in borrower:
                total+=b[1]
            if total!= amount:
                print("Invalid exact shares.")
                return

            #Mapping expenses to users
            for person in borrower:
                if person[0]==payer:
                    continue
                val = person[1]
                borrower_detail = self.get_user_detail(person[0])
                if borrower_detail.id in payer_person.expenses:
                    payer_person.expenses[borrower_detail.id]+=val
                else:
                    payer_person.expenses[borrower_detail.id] = val
                
                if payer_person.id in borrower_detail.expenses:
                    borrower_detail.expenses[payer_person.id]-=val
                else:
                    borrower_detail.expenses[payer_person.id] = -val
        
        if expense_type=='PERCENT':
            #Validating percent share:
            total = 0
            for b in borrower:
                total+=b[1]
            if b!=100.0:
                print("Incorrect percentage share.")
                return
            
            #Mapping expenses to users

            for person in borrower:
                if person[0]==payer:
                    continue
                val = person[1]*amount
                borrower_detail = self.get_user_detail(person[0])
                if borrower_detail.id in payer_person.expenses:
                    payer_person.expenses[borrower_detail.id]+=val
                else:
                    payer_person.expenses[borrower_detail.id] = val
                
                if payer_person.id in borrower_detail.expenses:
                    borrower_detail.expenses[payer_person.id]-=val
                else:
                    borrower_detail.expenses[payer_person.id] = -val
        


                


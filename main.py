from database import users_table
from expenses import ExpenseSharing

app = ExpenseSharing()

#Creating users
app.create_user("1", "Manish", "8083332715", "dummy@gmail.com")
app.create_user("2", "User2", "1234567890", "dummy2@gmail.com")
app.create_user("3", "user3", "0987654321", "dummy3@gmail.com")

#Adding expenses:
app.expenses("1", ["1", "2", "3"], "EQUAL", 300)
app.expenses("2", [("1", 300), ("2", 500), ("3", 100)],  "EXACT",900)


#Getting user detail
detail = app.get_user_detail("2")
print(detail.__dict__)
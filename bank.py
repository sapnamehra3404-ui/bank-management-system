from pathlib import Path
import json
import random

class Bank:
    database = "data.json"
    data = []

    # Load database
    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            with open(database, "w") as fs:
                fs.write("[]")
    except:
        print("Error loading database")

    @staticmethod
    def __update():
        with open(Bank.database, "w") as fs:
            fs.write(json.dumps(Bank.data))

    @staticmethod
    def __generateAcc():
        return random.randint(100000, 999999)

    def CreateAccount(self, name, age, phone, email, pin):
        info = {
            "name": name,
            "age": int(age),
            "phone": phone,
            "email": email,
            "pin": pin,
            "account": Bank.__generateAcc(),
            "balance": 0
        }

        Bank.data.append(info)
        Bank.__update()
        return f"Account Created Successfully 🎉 Your Account No: {info['account']}"

    def Login(self, account, pin):
        for user in Bank.data:
            if str(user["account"]) == str(account) and str(user["pin"]) == str(pin):
                return "Login Successful ✅"
        return "Invalid Account or PIN ❌"

    def Deposit(self, account, amount):
        for user in Bank.data:
            if str(user["account"]) == str(account):
                user["balance"] += int(amount)
                Bank.__update()
                return f"Deposit Successful ✅ New Balance: ₹{user['balance']}"
        return "Account Not Found ❌"

    def CheckBalance(self, account):
        for user in Bank.data:
            if str(user["account"]) == str(account):
                return f"Your Balance is ₹{user['balance']}"
        return "Account Not Found ❌"

    def Withdraw(self, account, amount):
        for user in Bank.data:
            if str(user["account"]) == str(account):
                if user["balance"] >= int(amount):
                    user["balance"] -= int(amount)
                    Bank._Bank__update()
                    return f"Withdraw Successful ✅ Remaining Balance: ₹{user['balance']}"
                else:
                    return "Insufficient Balance ❌"
        return "Account Not Found ❌"
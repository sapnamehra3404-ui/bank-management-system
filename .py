# 1.create class bank
# CRUD Operations -
# 1. Create -> Create User Details
# 2. Read -> Reading User Details
# 3. Update -> Updating User Details
# 4. Delete -> Deleting User Details

from pathlib import Path
import json
import random
import string

class Bank:
    database="data.json"
    data=[]

    try:
        if Path(database).exists():
            print("Database exists")
            with open(database) as fs:       #dumps -> give 
                data=json.loads(fs.read())   #loads -> take

        else:
            print("No such file exists...")

    except Exception as err:
        print("Error Occured")

    @classmethod
    def __update(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(cls.data))
    
    @staticmethod
    def __generateAcc():
        digits=random.choices(string.digits,k=4)
        alpha=random.choices(string.ascii_letters,k=4)
        id=digits+alpha
        random.shuffle(id)
        return "".join(id)

    def CreateAccount(self):
        info={
            'name': input("Enter your name: "),
            'age': int(input("Enter your age: ")),
            'phoneNumber': int(input("Enter your Contact: ")),
            'email': input("Enter your email: "),
            'pin': int(input("Enter your pin: ")),
            'account': Bank.__generateAcc(),
            'balance': 0
        }
        if info['age']>=18 and len(str(info['pin']))==4 and len(str(info['phoneNumber']))==10:
            Bank.data.append(info)
            Bank.__update()
            print('Data added in List')
            
        else:
            print("Credintials are not Valid!")
 
    def depositmoney(self):
        account=input('Enter your account no.: ')
        pin=int(input('Enter your 4 digit pin: '))

        user_data=[i for i in Bank.data if i['account']==account and i['pin']==pin]
        if bool(user_data)==False:
            print('User not found')
        else:
            amount=int(input('Paise: '))
            if amount<=0:
                print("Invalid Amount")
            elif amount>10000:
                print('Greater than 10000')
            else:
                user_data[0]['balance']+=amount
                Bank.__update()
                print('Amount Credited')
    
    def withdrawmoney(self):
        account=input('Enter your account no.: ')
        pin=int(input('Enter your 4 digit pin: '))

        user_data=[i for i in Bank.data if i['account']==account and i['pin']==pin]
        if bool(user_data)==False:
            print('User not found')
        else:
            amount=int(input('Paise: '))
            if amount<=0:
                print("Invalid Amount")
            elif amount>10000:
                print('Greater than 10000')
            else:
                if user_data[0]['balance']<amount:
                    print("Insufficient Funds....")
                else:
                    user_data[0]['balance']-=amount
                    Bank.__update()
                    print('Amount Credited')

    def details(self):
        account=input('Enter your account no.: ')
        pin=int(input('Enter your 4 digit pin: '))

        user_data=[i for i in Bank.data if i['account']==account and i['pin']==pin]
        if bool(user_data)==False:
            print('User not found')
        else:
            for i in user_data[0]:
                print(i,user_data[0][i])

    def update_details(self):
        account=input("Enter your accountno. ")
        pin=int(input("Enter your pin "))
        user_data=[i for i in Bank.data if i['account']==account and i['pin']==pin]
        if bool(user_data)==False:
            print("User not found")
        else:
            new_data={
                'name':input('please tell your name: '),
                'email':input('please tell your mail: '),
                'phoneNumber':input('Tell your phone number: '),
                'pin':input("enter your pin:")
            }
            print("Aap Account No. aur Balance Update/Change nahi kr skte ho")

            print("Enter your details to update or just press enter to skip them")

        if new_data['name']=="":
            new_data['name']=user_data[0]['name']
        
        if new_data['email']=="":
            new_data['email']=user_data[0]['email']

        if new_data['phoneNumber']=="":
            new_data['phoneNumber']=user_data[0]['phoneNumber']
        else:
            new_data['phoneNumber']=int(new_data['phoneNumber'])

        if new_data['pin']=="":
            new_data['pin']=user_data[0]['pin']
        else:
            new_data['pin']=int(new_data['pin'])

        new_data["account"]=user_data[0]['account']
        new_data['balance']=user_data[0]['balance']

        # user_data[0].update(new_data)
        for i in new_data:
            if new_data[i] == user_data[0][i]:
                continue
        else:
            user_data[0][i] = new_data[i]
            
        Bank.__update()

    def delete(self):
        account=input("Enter your accountno. ")
        pin=int(input("Enter your pin "))
        user_data=[i for i in Bank.data if i['account']==account and i['pin']==pin]
        if bool(user_data)==False:
            print("No Such user exists")
        else:
            print("are you sure you want to delete your account? (yes/no)")
            choice=input()
            if choice == 'yes':
                ind=Bank.data.index(user_data[0])
                Bank.data.pop(ind)
                Bank.__update()
                print('Acccount deleted successfully')
            else:
                print('Operation Terminated')

obj=Bank()

print('Press 1 for Creating Account')
print('Press 2 for Depositing Money')
print('Press 3 for Withdrawing Money')
print('Press 4 for Account Details')
print('Press 5 for Updating Account Details')
print('Press 6 for Deleting Account')

choice=int(input("enter your choice "))
if choice==1:
    obj.CreateAccount()
elif choice==2:
    obj.depositmoney()
elif choice==3:
    obj.withdrawmoney()
elif choice==4:
    obj.details()
elif choice==5:
    obj.update_details()
elif choice==6:
    obj.delete()
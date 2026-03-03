



# [
#     {
        
#         "pin": 1234,
#         "account_no": "abcd@123",
        
#     }
# ]



# account = input("Enter your account number:")
# pin = int(input("Enter your pin:"))
# user_data = [ i for i in data if i['accountno']==account and i['pin']==pin]
# print(user_data)

# if user_data ==False:
#     print('No such user')

# else:
#     balance = int(input('Amount'))
#     user_data[0]['balance'] += balance
#     print(user_data)

# main_dict= {"name":"akarsh bhaiya",'age':23,}
# new_dict = {"name":"sapna",'age':20}

# main_dict["name"] = new_dict["name"]
# main_dict['age'] = new_dict['age']




# 2.count pairs and leftovers from a list.
# l = [1,1,1,2,2,2,3,3,3,3]

# l = [1,1,1,2,2,2,3,3,3,3,3]

# pairs = 0
# leftovers = 0

# for i in set(l):
#     count = l.count(i)
#     pairs += count // 2
#     leftovers += count % 2

# print("Pairs:", pairs)
# print("Leftovers:", leftovers)

# 3. count the number of vowel from a string
# s = "This is the simple string"
# s = "This is the simple string"

# vowels = "aeiouAEIOU"
# count = 0

# for ch in s:
#     if ch in vowels:
#         count += 1

# print("Number of vowels:", count)

# check if two number are palindrom or not
# num1 = 121
# num2 = 123

# if str(num1) == str(num1)[::-1]:
#     print(num1, "is Palindrome")
# else:
#     print(num1, "is Not Palindrome")

# if str(num2) == str(num2)[::-1]:
#     print(num2, "is Palindrome")
# else:
#     print(num2, "is Not Palindrome")



# num1 = 121
# num2 = 123

# print(num1, "Palindrome?" , str(num1) == str(num1)[::-1])
# print(num2, "Palindrome?" , str(num2) == str(num2)[::-1])


# u have a list ur task is to count the frequently occuring elements and remove the most occuring
# l = [1,1,1,2,2,3,3,4,4,3,3,2,1,1,5]
#data types

# x = 5
# y = 10.3
# z = 100000000000

# print(x * x)
# print(y + x)
# print(z)

# string1 = "adeleke university"
# string2 = "0"
# string3 = "is the best university"
# #string3 = 5.5
# age = 12

#print(string1 + " is", + age + "years old")
# print('%s is %d years old' % (string1, age))
# print(string1 + " is " + str(age))
# print(len(string1))
# print(string1 + ' ' + string3)

#given a fullname, generate the username to be the surname and the password to be the firstname
# print('username is:')
# print(string1[0:7])
# print("password is:")
# print(string1[8:18])
#print(string1[-1:-10])

#to reverse a given string
#print(string1[::-1])

# #snake case (separate each word with an underscore _ ) usually used for naming in databases; Table name, column name
# name_of_university = "Adeleke University"
# #kebab case (url)
# name-of-university
# #camel case
# nameOfUniversity
# #pascal case
# NameOfUniversity

#and 0 * 1 = 0

cutOffMark = 50
stateOfOrigin = "Ekiti"
if (cutOffMark >= 60 and stateOfOrigin == "Ekiti"):
    print("congratulations, you have been offered admission to study computer science")
elif (cutOffMark < 60 and cutOffMark >50 or stateOfOrigin == "Ekiti"):
     #print("sorry, your score is below our cut off mark")
     print("congratulations, you have been offered admission to study computer science")
# elif (cutOffMark < 60  or stateOfOrigin != "Ekiti"):
#     print("sorry, your score is below our cut off mark")
else:
    print("something went wrong, try again later")




# print("hello world")
# #print is a function that prints out a message to the console 
# #strings are sourrounded by quotes
# #single or double quotes '' or ""
# #whenever a word is surrounded by quotes it is called a string
# #be consistent with the quotes you use
# print("melany morales")
# print("order of execution")
# print("in python")
# print("*"*20)
# #variables are used to store data
# #variables are created when you assign a value to it
# #variables are case sensitive
# price=10 #integer variable
# name = "John"
# rating= 4.9 #float variable
# is_published = True #boolean variable
# #start all variables with a lower case letter or underscore
# print(name)
# print(price)
# print(rating)
# print(is_published)
# #string iterpolation where you can use variable in a sentence 
# print(name + "is a basketball player")
# #concatenation to join vaiables in a sentence using
# # the plus (+) sign
# print(name + "has a rating of" + str(rating))
# #use the str() function to convert a number to a string
# #this is called type conversion
# print("the price of the book is" + str(price))
# #getting input from the user

name = input("what is your name?")
age = input("what is your age?")
occupation = input("what is your occupation?")
print("Hello" + name + "you are" + age + "years old and you are a" + occupation)
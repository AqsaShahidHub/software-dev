"""
Aqsa Shahid
April 27, Python Applications
"""
# import all from file "lab11_functions"
from lab11_functions import *

#import 'math' module 
import math

print("\n------- Example 1: Python dictionary -------")
# Create a dictionary

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# Print the complete dictionary

print(car)

# To Access items in the dictionary we use [], where [] goes the key's name

print(f"The year of the car is = {car['year']}")

# Update the value of a key

car["year"] = 1980
print(f"The year of the car was updated to = {car['year']}")
print("The year of the car was updated to = ", car['year'])

# Add key:value pair

car["color"] = "red"
print(car)

# Loop through each key in the dictionary

print("\nLoop through each key in the dictionary")
for k in car:
    print(k)

# Loop through each value in the dictionary

print("\nLoop through each value in the dictionary")
for k in car:
    print(car[k])

# Loop through each pair in the dictionary

print("\nLoop through each pair in the dictionary")
for k in car:
    print(f"{k}: {car[k]}")

print("\n------- Example 2: Python dictionary application -------")

# Given the following phrase, create a dictionary that will count the number of times a word appears in the string
#create a dictionary to organize the words as the keys, and the number of occurency of the word as the value of the key

phrase = "to be or not to be"
print(f"Original phrase = {phrase}")

# Split the phrase into words

phrase_split = phrase.split()
print(f"Splitted phrase = {phrase_split}")

# Create the dictionary

word_count_dict = {}

# Loop through each word in the list

for word in phrase_split:
    if word in word_count_dict:
        word_count_dict[word] +=1
    else:
        word_count_dict[word] =1

# Print result

print("Result of dictionary:")
for w in word_count_dict:
    print(f"'{w}' = {word_count_dict[w]}")

print("\n------- Example 3: function that doesn't return values -------")

#call function 'greeting'
greeting()

print("\n------- Example 4: Function with parameters -------")

# call function 'printusername'

printusername("peter pan")
printusername("Prof. Wu")

print("\n------- Example 5: function with default parameters -------")

user_country("Martha", "Chile")
user_country("Anna")
user_country("", "France")

print("\n------- Example 6: function with return value -------")

num1 = 2
num2 = 5
prod1 = product(num1, num2)
print(f"The product of {num1} and {num2} is = {prod1}")

prod1 = product(num1)
print(f"The product is = {prod1}")

prod1 = product()
print(f"The product is = {prod1}")

print("\n------- Example 7: Boolean function -------")
checknum1 = multiple3(num1)
checknum2 = multiple3(num2)

print(f"Is {num1} multiple of 3? {checknum1}")
print(f"Is {num2} multiple of 3? {checknum2}")

print("\n------- Example 8: composition function -------")

# test collectnum()
# number = collectnum()
# print(number)
# test sumnumbers()

sumall = sumnumbers(3)
printresult(sumall)  # printresult(sumnumbers(3))


print("\n------- Example 9: built-in function -------")

r = 2
a = areacircle(r)
areaprint(a, r)

print("\n------- Example 10: try-except -------")

r1 = ratio_hour(0)
r2 = ratio_hour(3)
r3 = ratio_hour("Peter")

print("\n------- Example 11: classes -------")
# create an instant of the class
user1 = Myclass()
print(f"An instance of the class = {user1}")

# call the class' property
user1id = user1.id
print(f"user 1 id = {user1id}")

# call the class' method
user1msg = user1.msg()
print(f"user 1 message = {user1msg}")

print("\n------- Example 12: instantiation classes -------")
# create an instant of the class
paircomplexnumber = Complexnumber(2, 3)

# call the instance object 'r' of the class
real = paircomplexnumber.r
print(f"The real part is {real}")

print("\n------- Example 13: classes application -------")

# create an instant of the class
car1 = Car("Tesla", "S", 2023)

# call property 'odometer_reading'
car_reading = car1.odometer_reading
print(f"Car miles reading = {car_reading}")

# call method 'get_car_description'
print(car1.get_car_description())

# call method 'read_odometer'
print(car1.read_odometer())

# add 20 miles to the odometer
car1.increment_odometer(20)
print(car1.read_odometer())

car1.increment_odometer(-5)
print(car1.read_odometer())

car1.increment_odometer(8)
print(car1.read_odometer())


"""
Aqsa Shahid
Lab 11, class in Python (extra points)
"""
class student:
    def __init__(self, name, age, grade):

    # Initialize attributes
        self.name=name
        self.age=age
        self.grade=grade

student_1=student('Anna', '19', '10')
student_2=student('Elizbeth', '20','20')
student_3=student('Robert', '21', '30')


print(student_1)





        
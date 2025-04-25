"""
Aqsa Shahid
April 24, Conditional Statement
"""

print(f"\n-----------Example 1 and 2: if Statement")
age=20
agecode=123

if age>=21:
    print("You are an adult!")
    agecode=200
else:    
     print("You are under 21!")
     agecode=100

print(f"After the 'if' statement, agecode={agecode}")

print(f"\n-----------Example 3: multi Statement")

age=50
if 0 <= age < 21:
    print("You are minor!")
elif 21 <= age < 65:
    print("You are an adult!")
elif 65 <= age <= 130:
    print("You are Senior citizen!")
else:
    print("Unable to read age!")


print(f"\n-----------Example 4: and operator")

temperature=90 
humidity=60

if 70 < temperature <=90 and humidity < 80:
    print("The weather is pleasent")
else:
    print("The weather is not ideal")

print(f"\n-----------Example 5: or operator")

day="Sunday"
is_holiday=False


if day=="Saturday" or day=="Sunday" or is_holiday:
    print("You can relax today")
else:
    print("It is workday")

print(f"\n-----------Example 6: nested conditional statement")

number=int(input("Enter a number: "))
if (number>=0):
  if number==0:
      print(f"The number is Zero")
  else:
     print(f"{number} is positive")
else:
   print(f"{number} is negative")

print(f"\n-----------Example 7: nested conditional statement")

   #username validation. Username must have 3+ characters

username= input("Enter a username: ")
username= username.strip()
len_username = len(username)
if len_username>= 3:
    print(f"{username} has 3+ characters")
    index_whitespace=username.find(" ")
    if index_whitespace == -1:
        print(f"{username} is valid")
    else:
        print(f"Username Cannot have whitespace")
else:
    print(f"{username} is Invalid. Username must have1 3+ characters")

print(f"\n-----------Example 8: match-case statement")

response_code=404

match response_code:
    case 400:
        print(f"Code = {response_code}. Server cannot understand.")
    case 401 | 403:
        print(f"Code = {response_code}. Server refused to send back.")
    case 404:
        print(f"Code = {response_code}. Server can't find.")
    case _:
        print(f"Invalid Code")

        
print(f"\n----------LAB EXERCISE------------")
# Collect two grades from the user
grade_1 = float(input("Enter your first grade: "))
grade_2 = float(input("Enter your second grade: "))
# Calculate the average
grade_average = (grade_1 + grade_2) / 2

if 90 <= grade_average <= 100:
        gpa = "A"
elif 70 <= grade_average < 90:
        gpa = "B"
elif 60 <= grade_average < 70:
        gpa = "C"
elif 0 <= grade_average < 60:
        gpa = "FAIL!"
else:
        gpa = "UNDEFINED!"
    
    
# Print the result
print(f"For the average of {grade_average:.2f}, your GPA is {gpa}")

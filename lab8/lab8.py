"""
Aqsa Shahid
April 20, Introduction Python
"""
# Single Comment. This line WILL NOT run
print('\n------ Example 1: string characters -------')
print("\tGood morning! \nThis is my first \"Python\" Code!")
print('\n------ Example 2: data type -------')
print(f"Data Type of 3.56={type(3.56)}")
print(f"Data type of -25={type(-25)}")
print(f"Data type of 'Hello World!'={type('Hello World!')}")
print(f"Data type of Character '$'={type('$')}")
print(f"Data type of False={type(False)}")

print('\n------- Example 3: variables  ----------')
#declare variables
number1= 25.5
number2= -12
username= "Peter Pan"
add_numbers= number1 + number2
is_raining=True
# prompt Results
print(f"{username}, the sum of {number1} and {number2} is {add_numbers}")
print(f"Is it raining today? = {is_raining}")
print ('\n------ Example 4: assigning values to multiple variables  ----------')
# declare multiple variables
iteml, item2, item3 = "apples",25, False
print (f"item 1 = {iteml}, item 2 ={item2}, item 3 = {item3}")
# declare multiple variables with the same value
score1= score2=score3 = 88
print (f"score 1 ={score1},score 2 ={score2},score 3 ={score3}")

print('\n-------------- Example 5: input command ---------')
print("Enter username: ")
username=input()
print(f"Collected username={username}")

# Cast from String to Integer
luckynumber=int(input("Enter a lucky number: "))
print(f"Lucky number={luckynumber}")

# double the lucky number.
dblucky= int(luckynumber)*2
print(f"Doubled of lucky={dblucky}")

# Cast from Integer(or Float) into String
triplenumber= str(dblucky)*3
print(f"tripled the casted number={triplenumber}")

#cast integer to bool value
#0=False any other number= True
completed_task= -20
print(f"completed task = {bool(completed_task)}")

print('\n--------- Example 6: Arithmatic Operations -----')


num1 = 25
num2 = 9

print(f"The sum of {num1} and {num2} is                     {num1+num2}")
print(f"The different between {num1} and {num2} is          {num1-num2}")
print(f"The product of {num1} and {num2} is                 {num1*num2}")
print(f"The quotient of {num1} and {num2} is                {num1/num2}")
print(f"The modulus(remainder) of {num1} and \t{num2} is    {num1%num2}")
print(f"The integer of quotient of {num1} and {num2} is     {num1//num2}")
print(f"The result of base {num2} to the power of 3 is      {num2 ** 3}")


print('\n ------ Example 7: finding the hypotesuna ----')
# declare and assign values
x = float(input("Enter side 1: "))
y = float(input("Enter side 2: "))
# calculate the hypotenusa
hyp = (x ** 2 + y ** 2) ** 0.5
# prompt result
print (f"The hypotenuse of {x:0.1f} and {y:0.1f} is {hyp:0.3f}")

print('\n -----Example 8: assignment operators----')
n = 6
print(f"number = {n}")
# assignment operator +
n +=3
print(f"number + 3 = {n}")
# assignment operator -
n -=4
print(f"update number ={n}")
# assignment operator *
n *= 2
print(f"updated * number = {n}")
# assignment operator /
n /= 3
print(f"updated / number = {n}")
# assignment operator //
n //= 2
print(f"updated // number = {n}")
# assignment operator **
n **= 2
print(f"updated ** number = {n}")
# modulus or remainder
n %= 5
print(f"updated %= number = {n}")

print('\n------------ Example 9: comparison operators ----------')
n1=10
n2=3
n3=7
compare1=n1==n2
compare2=n1==(n2+n3)
print(f"is n1 equal n2?                      {compare1}")
print(f"is n1= n2=n3?                        {compare2}")
compare3=n1>n2
compare4=n2<=n3
print(f"is n1 greater than n2?               {compare3}")
print(f"is n2 less than or equal to n3?      {compare3}")

print('\n ------ Example 10: string indexing -------------')
username = "peterpan123"
# positive index
print(f"The fifth character = {username[4]}")

# negative index
print(f"The fifth last character = {username[-5]}")



print('\n ------ Example 11: string slice ------------')
# slice from the beginning to the 4th character
print(f"Slice from beginning to 4th character = {username[:4]}")

# slice from the 5th character to the end
print(f"Slice from the 7th character to the end = {username[6:]}")

# slice from the 3rd to 8th
print(f"Slice from 3rd to 8th                    = {username[2:8]}")

# slice from the 4th to the 6th character using negative index
print(f"Slice from 4th to 6th using negative index =    = {username[-8:-5]}")

print('\n ------ Example 12: total characters in a string (len)--- ')
print(f"The username has = {len(username)} characters")






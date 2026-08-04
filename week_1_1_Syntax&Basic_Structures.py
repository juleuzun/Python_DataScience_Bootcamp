#=================
# Variables
#=================

print("Hello TechIstanbul")

x = 5  #integer
y = 5.9 #float
z = "5" #string

Jule_1 = str(x+y)
print(type(Jule_1))

#Example 1

a = "user_name"
b = "password"
c = "date of birth"

print(a,b,c, sep="\n", end="\n")

print("Jule", end="\n")
print("Uzun")

#Example 2

first_name = "Jule"
last_name = "Uzun"
hobby = "computer games"
philosophy = "live in the moment"

last_name = input("Enter your last name: ")
hobby = input("Enter your hobbies: ")
philosophy = input("Enter your philosophy: ")

first_name = input("Enter your first name: ")

print("Are you sure your name is ",first_name, "?")

print("First Name        :",first_name)
print("Last Name         :",last_name)
print("Hobbies           :",hobby)
print("Philosopy of life :",philosophy)

#=====================
#Calculator
#=====================

num1 = float(input("Enter first number: "))
operator = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if operator =="+":
    print(num1+num2)
elif operator =="-":
    print(num1-num2)
elif operator =="*":
    print(num1*num2)
elif operator =="/":
    print(num1/num2)
else:
    print("Invalid operator!")

#==========================
#Account Login Application
#==========================

username = input("Enter your user name: ")
password = input("Enter your password: ")

stored_username = "juleuzun"
stored_password = "python"

if stored_username != username or stored_password != password:
    print("Invalid username or password!")
else:
    print("Login successful!")
   
#========================== 
#Certificate Calculator
#==========================

student_grade = float(input("Please enter your grade: "))

if 85 <= student_grade <= 100:
    print("Congratulations! You qualified for the Certificate of Appreciation (High Honors).")
elif 70 <= student_grade < 85:
    print("Congratulations! You qualified for the Certificate of Achievement (Honors).")
elif 45 <= student_grade < 70:
    print("You passed the class without any certificate.")
elif 0 <= student_grade < 45:
    print("You failed the class.")
else:
    print("Invalid grade entered.")

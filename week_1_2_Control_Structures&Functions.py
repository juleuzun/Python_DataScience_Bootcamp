#=================================
#Python Practice: Conditions, Loops, Functions, and Data Structures
#=================================

#1. Password Character Validation
# Check whether the password contains forbidden letters

password = input("Set a password: ")

if 'a' in password:
    print("Do not use the letter 'a'!")
if 'b' in password:
    print("Do not use the letter 'b'!")
if 'c' in password:
    print("Do not use the letter 'c'!")

   
#2. Password Symbol Validation
# Check whether the password contains at least one symbol

password = input("Set a password: ")

symbols = "!+%&()?"
counter = 0

for symbol in symbols:
    if symbol not in password:
        print("Please use a symbol")
    else:
        break
    
#3. Loop Through Characters in a String
# Print each digit from the string one by one

numbers ="0123456789"

for x in numbers:
    print(x)
    
    
#4. Using the range() Function
# Print numbers from 0 to 9

for number in range(10):
    print(number)
    
#5. Print Even Numbers from 0 to 100
# Print even numbers between 0 and 100

for number in range(0,101,2):
    print(number)
    
#6. Basic while Loop
# Repeat the message while the condition is true

a = 10
while a == 10:
    print("Learning Data Science with Tech Istanbul is a Great Experience")
    a = a+1
print(a)   

#7. Username and Password Login System
# Simple login system using a while loop

stored_username = "Juleuzun"
stored_password = "techistanbul"

while True:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if stored_username !=username:
        print("Incorrect username.Please try again.")
    elif stored_password != password:
        print("Incorrect password.Please try again.")
    else:
        
        print ("Login successful!")
        break
print("Program finished.")

#8. Adding Two Numbers with a Function
# Define a function to add two numbers

def  add_numbers(first_number,second_number):
    total = first_number + second_number
    print(total)

# Get two numbers from the user    
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

# Call the function
add_numbers(first_number , second_number)

#9. Check Whether a Triangle Is a Right Triangle
# Check whether three sides form a right triangle

def is_right_triangle(a, b, c):
    
    if a**2 + b**2 == c**2:
        return "This is a right triangle."  
    else:
        return "This is not a right triangle."

# Get the side lengths from the user
a = int(input("Enter a value for a: "))
b = int(input("Enter a value for b: "))               
c = int(input("Enter a value for c: "))

# Call the function and display the result
print (is_right_triangle(a, b, c))

#10. Display User Information with String Formatting
# Get the user's first and last name

first_name = input("First Name: ")
last_name = input("Last Name: ")

# Format and display the user's information
text_to_display = """

First Name: {}
Last Name: {}

""".format(first_name, last_name)

print(text_to_display)

#11. Working with Lists and Nested Lists
# Create a list containing different data types and a nested list

list = ["Jule",5,1.9,["uzun",3,5.4]]

# Add a new item to the list
list += ["jule"]

# Access the nested list
print(list[3],[1])


#12. Adding and Displaying Cities in a List
# Create a list of cities

cities =["İstanbul" , "Ankara" , "Adana" , "Konya"]

# Print the existing cities
for a in cities:
    print(a)

# Get a new city from the user
entry = input("\n\nPlease enter a city name: ")

# Add the new city to the list
cities +=[entry]

# Print the updated city list
for b in cities:
    print(b)


#13. Working with Dictionaries
# Create a dictionary containing personal information

dictionary = {
    "Birthyear":1975,
    "Job":"Data Scientist"
}

# Access the value associated with the "Birthyear" key
print(dictionary["Birthyear"])

#14. Comparing Tuples and Lists
# Create a tuple
tuple = ("jule" , 5 , 1.9)
tuple +=("jule")

# Create a list
list = ["jule", 5 , 1.9]

# Display both data structures
print(tuple,list)



#15. Converting User Input to Lowercase
# Convert the user's input to lowercase
a = input("First Name: ")
a = a.lower()

# Check whether the entered name is "jule"
if a == "jule":
    print("Welcome JULE")
    
#16. Creating a Set and Checking Boolean Values
# Create sets containing unique values

my_set = {"Jule", "Uzun", 12, 15, 20, 20}
my_set2 = {"Uzun", 15, "Ahmet", 18}

# Create a non-empty string
sample_string = "dasdas"

# A non-empty string returns True when converted to bool
print(bool(sample_string))


#17. Set Intersection and Union
# Create sets of banned and visitor IDs

banned_ids = {12, 63, 84}
visitor_ids = {12, 1, 5, 8, 3, 8, 84}

# Create a set from the characters in the name
name_characters = set("Jule")

# Find IDs that exist in both sets
common_ids = banned_ids.intersection(visitor_ids)

# Check whether there are any common IDs
if bool(common_ids):
    print("Banned individuals have acceessed the website.")

# Combine both sets using union
combined_ids = banned_ids.union(visitor_ids)
print(combined_ids)


#18. Copying Strings and Lists

a = "Jule"
b = a

a += "Uzun"

# Create a list and make a copy
list = ["Jule"]

list2 = list.copy()

# Add a new item to the original list
list.append("Uzun")

# Display the string variables
print(a,b)

# Display the original list and its copy
print(list,list2)


#19. Sorting and Reversing a List
# Create a list of numbers
list = [5,2,7,9,6,3,6,6,867,53]

# Sort the list in ascending order
list.sort()
print(list)

# Reverse the order of the list
list.reverse()
print(list)


#20. Creating a Simple Translation Dictionary
# Create a Turkish-English dictionary
dictionary = {"siyah": "black", "beyaz": "white", "anıt": "monument", "tane": "piece", "kırmızı": "red"}

# Get a Turkish word from the user
entry = input("Enter a Turkish word: ")

# Search for the word in the dictionary
print("The English translation of: ",dictionary.get(entry,"Sorry, the word you enetered is not in the dictionary."))

# Print all English translations
for a in dictionary.values():
    print(a)
    
#21. Phone Book Application with Nested Dictionaries
# Create a phone book using nested dictionaries
phone_book = {
    "jule":{
        "mobile":5555555555,
        "work": 1212121212,
        "home": 8877777878
    },
    "ahmet":{
        "mobile":4444444444,
        "work":1515151515,
        "home": 9799797979
    }
}

# Keep the program running until the user chooses to quit
while  True:
    name = phone_book.keys()
    
    # Ask the user for a name
    entry = input("Enter a name to search for: ")
    entry = entry.lower()
    
    # Check whether the name exists in the phone book if entry in name:
    
    if entry in name:
        
        # Ask which type of phone number the user wants
        phone_type = input("Enter the type of phone number you want to see (mobile, work, home): ")
        phone_type = phone_type.lower()
        
        # Display the requested phone number
        print(phone_book.get(entry).get(phone_type,"Sorry, the phone type you entered is not in the phone book."))
    else:
        print("Sorry, the name you entered is not in the phone book.")
    
    # Ask whether the user wants to continue
    user_exit = input("Press Enter to search again or 'Q' to quit: ")
    
    if user_exit =="Q" or user_exit == "q":
        print("program finished.")
        break



    

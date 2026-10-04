# ==========================
# Assignment 1 - Riddle Game
# ==========================

secret_number = 110

print("I'm thinking of a number, try to guess it!")

# Get user's guess
guess = int(input("Enter a number: "))

# Apply the required mathematical operation
calculated_result = (guess ** 2) - guess

# Check whether the calculated result matches the target value
if calculated_result == secret_number:
    
    print("Congratulaions! You guessed correctly, you won 100 points!")

else:
    
    # Calculate the absolute difference
    difference = abs(secret_number - calculated_result)
    
    # Award points based on the difference
    if difference <= 10:
        
        print("So close! You won 50 points!")
    
    elif 11<= difference <= 50:
        
        print("You are getting closer, try again!")
    
    else:
        
        print("You lost! Better luck next time!")
        

# ============================
# PYTHON QUIZ GAME
# =============================

# Ask the player for their name to personalize the quiz experience
player_name = input("Enter your name: ")
print("Welcome to the Quiz Game, " + player_name + "!\n")

# Define a list of the questions (string elements)
questions = [
    "What is the capital of Kenya?",
    "What is 5 + 5?",
    "Which programming language is known for its snake logo?",
    "How many days are in a week?",
    "What keyword is used to create a condition in python?",
    
]
# Define a list of correct answers matching the order of the questions list above 
# Note: All string answers are in the lower case to match with .lower()
answers = [
    "nairobi",
    "10",
    "python",
    "7",
    "if",
]

# Initialize the score counter to 0 before the quiz starts 
score = 0

# --- Question 1 ---
# input() prompts the user for text input.
# .lower() converts the user's input to lowercase so 'NAIROBI', Nairobi', and 'nairobi' are all accepted.
user_answer = input(questions[0] + " ").lower()
# Compare the processed user with the correct answer  at index 0
if user_answer == answers[0]:
    print("Correct!")
    score = score + 1 # Increment the score by 1 for a correct answer
else:
    print("Wrong!")
    # --- Question 2 ---
user_answer = input(questions[1] + " ").lower()
if user_answer == answers[1]:
    print("Correct!")
    score = score + 1
else:
    print("Wrong!")
    
    # --- Question 3 ---
user_answer = input(questions[2] + " ").lower()
if user_answer == answers[2]:
    print("Correct!")
    score = score + 1
else:
    print("Wrong!")  
    
    # --- Question 4 ---
user_answer = input(questions[3] + " ").lower()
if user_answer == answers[3]:
    print("Correct!")
    score = score + 1
else:
    print("Wrong!") 
    
    # --- Question 5 ---
user_answer = input(questions[4] + " ").lower()
if user_answer == answers[4]:
    print("Correct!")
    score = score + 1
else:
    print("Wrong!")   
    
    # --- Results & Feedback ---
    # Calculate total number of questions using len()
    total_questions = len(questions)
    
    print("-----------------------------")
    print(player_name + ", your final score is: " + str(score) +  "/" + str(total_questions))
    # Provide feedback based on the fianal score using if/else/elif conditions
    if score == total_questions:
        print("Excellent! You got everything correct!")
    elif score >= 3:
        print("Good job! You got most of the questions right.")
        
    else:
        print("Better luck next time! Keep practicing.")
    print("-----------------------------")
        
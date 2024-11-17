import random
import mysql.connector 

# Connect to the database
db=mysql.connector.connect(host="localhost",user="root",password="varchasva",database="Hangman")
cursor=db.cursor()

# Create the Guess table if it doesn't exist
try:
    cursor.execute("create table guess(words varchar(100))")
except:
    pass  # If the table already exists, no action needed

# Fetch all words from the database
cursor.execute("Select * from Guess")

word_list = []
for word in cursor:
    word_list.extend(list(word))  # Append each word to the list

# Game variables
is_game_active = True
wrong_attempts = 0
vowels = "aeiou"
guessed_word = ""
guessed_letters = ['a','e','i','o','u']  # List to store guessed letters (vowels are allowed automatically)
life_symbol = "X"
wrong_guessed_letters = ""  # Store letters that are guessed wrong

# Main loop for adding words
while True:
    user_choice = input("Would you like to add words? (y/n): ")
    
    if user_choice in ['y', 'Y']:
        word_to_add = input("Enter the word you want to add to the list: ")
        cursor.execute("insert into guess (words) values ('" + word_to_add + "')")
    elif user_choice in ['n', 'N']:
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
db.commit()

# Fetch the updated list of words after addition
cursor.execute("Select * from Guess")
word_list = []
for word in cursor:
    word_list.extend(list(word))

# Main game loop
while True:
    start_game_choice = input("Would you like to start the game? (y/n): ")
    
    if start_game_choice in ['y', 'Y']:
        
        # Select a random word from the list to guess
        word_to_guess = random.choice(word_list).lower()

        # Clean up the word if it has leading/trailing spaces
        if word_to_guess[0] == " ":
            word_to_guess = word_to_guess[1:]
        if word_to_guess[-1] == " ":
            word_to_guess = word_to_guess[:-1]
            
        # Display initial word with blanks
        for letter in word_to_guess:
            if letter in vowels:
                print(letter, end=" ")
            elif letter == " ":
                print('/', end=" ")
            else:
                print('_', end=" ")

        # Game loop
        while is_game_active:            
            # Check if the word has been guessed correctly
            
            if guessed_word == word_to_guess.lower():
                print("You Won ^--^")
                guessed_letters = ['a','e','i','o','u']
                break
            ''' above code checking if the words correct immediately'''

            print("\nGuess the word, letter by letter")
            letter_guess = input("Guess:  ")
            print(guessed_word)
            
            # Input validation: blank guess or invalid character
            if letter_guess == " " or letter_guess == "":
                print('Blank is not a valid guess.')
                continue
            
            # Check if the letter has been guessed already
            elif letter_guess in guessed_letters:
                print("Letter is already in the word.")
            elif letter_guess in wrong_guessed_letters:
                print("This letter has already been guessed wrongly.")
                
            # Correct guess
            elif letter_guess in word_to_guess:
                guessed_letters.append(letter_guess)
                print("Correct!")
            #reseting guessed word 
                guessed_word=""
                for i in word_to_guess:
                    if i in guessed_letters:
                        #adding values to guessed word
                        guessed_word+=i
                        print(i, end=" ")
                    elif i == " ":
                        guessed_word+=" "
                        print('/', end=" ")
                    else:
                        print('_', end=" ")
                        
            # Incorrect guess
            else:
                print("Wrong guess!")
                wrong_guessed_letters += letter_guess
                wrong_attempts += 1
                print(f"You have {6 - wrong_attempts} attempts remaining.")
                print(life_symbol * wrong_attempts)
                
                if wrong_attempts == 6:
                    print("Game Over!")
                    print(f"The word was: {word_to_guess}")
                    break
                
    elif start_game_choice in ['n', 'N']:
        print("Goodbye! Have a nice day!")
        break
    
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
    



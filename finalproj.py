from graphics import Canvas
import random
import time

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300

LEXICON_FILE = "Lexicon.txt"    # File to read word list from
INITIAL_GUESSES = 8             # Max number of guesses per game



def play_game(secret_word, canvas):
    draw_gallow(canvas)

    guess_num = INITIAL_GUESSES
    hidden = "- "*len(secret_word)
    guess_draw = draw_guess(canvas, hidden)

    guessed_letters = []
    missed_letters = []
    missed_draw = False
    while guess_num > 0 and hidden != secret_word:
 
        print(f"You have {guess_num} guesses left")
        guess = input("Type a single letter here, then press enter: ")
        while len(guess) > 1:
            print("Guess should only be a single character.")
            guess = input("Type a single letter here, then press enter: ")
        if guess.upper() in secret_word:
            print(f"That guess is correct.")
            guessed_letters.append(guess.upper())
            hidden = ''.join(x if (x == guess.upper() or x in guessed_letters) else "- " for x in secret_word)
            canvas.delete(guess_draw)
            guess_draw = draw_guess(canvas, hidden)
            canvas.update()
        else:
            print(f"There are no {guess}'s in the word")
            missed_letters.append(guess.upper())
            if missed_draw :canvas.delete(missed_draw)
            missed_draw = draw_missed(canvas, "".join(missed_letters))
            guess_num -=1
            draw_hangman(canvas, guess_num)
            canvas.update()
    if guess_num == 0:
        print(f"Sorry, you lost. The secret word was: {secret_word}")
    else:
        print(f"Congratulation, the word is: {secret_word}")

    time.sleep(5)




def get_word():
    """
    This function returns a secret word that the player is trying
    to guess in the game.  This function initially has a very small
    list of words that it can select from to make it easier for you
    to write and debug the main game playing program.  In Part II of
    writing this program, you will re-implement this function to
    select a word from a much larger list by reading a list of words
    from the file specified by the constant LEXICON_FILE.
    """

    f = open(LEXICON_FILE, "r")
    list = f.readlines()
    random_num = random.randint(0,len(list)-1)
    return ''.join(list[random_num].split()).upper()
    
def draw_gallow(canvas):
    support_bottom_y = 340
    support_top_y = 90
    canvas.create_rectangle(
        300,
        support_top_y,
        support_bottom_y,
        225,
        'brown'
    )
    canvas.create_rectangle(
        250,
        50,
        support_bottom_y,
        support_top_y,
        'brown'
    )
    canvas.create_rectangle(
        262,
        support_top_y,
        267,
        support_top_y+5,
        'black'
    )

def draw_guess(canvas, word):
    return canvas.create_text(
        200, 
        240, 
        anchor='center',
        font='Arial 20',  
        text=word, 
        color='black')

def draw_missed(canvas, word):
    return canvas.create_text(
        200,
        270,
        anchor='center',
        font='Arial 20',  
        text=word, 
        color='red'
    )

def draw_hangman(canvas, guess_num):
    if guess_num == 7: #draws head
        canvas.create_oval(255, 95, 275, 115, 'black')
    elif guess_num == 6: #draws body
        canvas.create_line(265, 115, 265, 165, 'black')
    elif guess_num == 5: #draws left arm
        canvas.create_line(265, 125, 255, 135, 'black')
    elif guess_num == 4: #draws right arm
        canvas.create_line(265, 125, 275, 135, 'black')
    elif guess_num == 3: #draws left leg
        canvas.create_line(265, 165, 255, 195, 'black')
    elif guess_num == 2: #draws right leg
        canvas.create_line(265, 165, 275, 195, 'black')
    elif guess_num == 1: #draws eyes
        canvas.create_oval(259, 100, 262, 105, 'white')
    elif guess_num == 0: #draws eyes
        canvas.create_oval(267, 100, 270, 105, 'white')
        


def main():
    """
    To play the game, we first select the secret word for the
    player to guess and then play the game using that secret word.
    """
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    secret_word = get_word()
    play_game(secret_word, canvas)



# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
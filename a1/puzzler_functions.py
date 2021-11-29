"""Phrase Puzzler: functions"""

# Phrase Puzzler constants

# Name of file containing puzzles
DATA_FILE = 'puzzles_small.txt'

# Letter values
CONSONANT_POINTS = 1
VOWEL_PRICE = 1
CONSONANT_BONUS = 2

# Players' names
PLAYER_ONE = 'Player One'
PLAYER_TWO = 'Player Two'

# Menu options - includes letter types
CONSONANT = 'C'
VOWEL = 'V'
SOLVE = 'S'
QUIT = 'Q'


# Define your functions here.

def is_win(puzzle: str, view: str) -> bool:
    """Return True if and only if puzzle is the same as view.

    >>> is_win('banana', 'banana')
    True
    >>> is_win('apple', 'a^^le')
    False
    """
    # put the function body here
    return puzzle == view

def game_over(puzzle: str, view: str, current_selection: str) -> bool:
    """Return True if and only if the puzzle is 
    the same as the view or the current selection is QUIT.
    
    >>> game_over('banana', 'banana', 'C')
    True
    >>> game_over('apple', '^pple', 'V')
    False
    >>> game_over('orange', '^^^^^^', 'Q')
    True
    """
    return puzzle == view or current_selection == QUIT

def bonus_letter(puzzle: str, view: str, letter_evaluate: str) -> bool:
    """Return True if and only if the letter 
    appears in the puzzle but not in its view.
    
    >>> bonus_letter('banana', '^anana', 'b')
    True
    >>> bonus_letter('banana', '^anana', 'a')
    False
    >>> bonus_letter('banana', '^anana', 'z')
    False
    """
    
    return letter_evaluate in puzzle and not(letter_evaluate in view)

def update_letter_view(puzzle: str, view: str, index: int, letter_guess: str) -> bool:
    """Return a single character string representing the next view of 
    the character at the given index. If the character at that index of 
    the puzzle matches the guess, then return that character. Otherwise, 
    return the character at that index of the view.
    
    >>> update_letter_view('banana', '^anana', 0, 'b')
    'b'
    >>> update_letter_view('apple', 'a^^le', 1, 'z')
    '^'
    """
    
    if letter_guess == puzzle[index:(index+1)]:
        return letter_guess
    else: 
        return view[index:index(index+1)]
    
def calculate_score(current_score: int, number_of_occurance: int, judgement: str) -> int:
    """ Return the new score by adding CONSONANT_POINTS per occurrence of 
    the letter to the current score if the letter is a consonant, 
    or by deducting the VOWEL_PRICE from the score if the letter is a vowel.
    
    >>> calculate_score(0, 2, CONSONANT)
    2
    >>> calculate_score(0, 1, VOWEL)
    -1
    """
    
    if judgement == CONSONANT:
        return current_score + number_of_occurance * CONSONANT_POINTS
    elif judgement == VOWEL and number_of_occurance != 0:
        return current_score - VOWEL_PRICE
    else:
        return current_score
    
def next_player(current_player: str, last_choosen: int) -> str:
    """If and only if the number of occurrences is greater than zero, 
    the current player plays again. Return the next player 
    (one of PLAYER_ONE or PLAYER_TWO).
    
    >>> next_player(PLAYER_ONE, 0)
    Player Two
    >>> next_player(PLAYER_ONE, 2)
    Player One
    """
    
    if last_choosen > 0:
        if current_player == PLAYER_ONE:
            return PLAYER_ONE
        elif current_player == PLAYER_TWO:
            return PLAYER_TWO
    else:
        if current_player == PLAYER_ONE:
            return PLAYER_TWO
        elif current_player == PLAYER_TWO:
            return PLAYER_ONE

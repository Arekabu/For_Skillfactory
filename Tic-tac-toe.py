# Creating the Game Field, which is a dictionary where the keys are the indexes of the rows of the Game Field, and the values are lists of strings.
# The indexes of the lists correspond to the indexes of the columns of the Game Field, and moves are recorded in the strings.

game_field = {0 : ['-', '-', '-'], 1 : ['-', '-', '-'], 2: ['-', '-', '-']}
field_numbers = [0, 1, 2]    #creating a variable to verify the correctness of the entered row and column indexes.
move_counter = 0    #creating moves counter

def show_game_field(field: dict[int,list[str]]) -> None:
    """
    The function displays the current state of the Game Field to the console
    :param field: a dictionary with the Game Field
    :return: None
    """
    print()
    print("  0 1 2")
    for key, value in field.items():
        print(f"{key} {' '.join(value)}")
    print()

def game_over(field: dict[int,list[str]]) -> bool:
    """
    The function checks if the victory conditions are met based on the current state of the Game Field.
    Victory conditions: in any row, column, or diagonal passing through the center of the field,
    all values are equal to "X" or "O". ("X" and "O" are English capital letters).
    :param field: a dictionary with the Game Field
    :return: True if victory conditions are met, otherwise False
    """
    X = ['X', 'X', 'X']     #creating a list to check the victory conditions for 'X'
    O = ['O', 'O', 'O']     #creating a list to check the victory conditions for 'O'
    C0, C1, C2, D00_22, D02_20 = [], [], [], [], []     #creating empty lists to check columns and diagonals
    for key, value in field.items():
        if value == O or value == X:       #checking the rows
            return True
        C0.append(value[0])                #filling in the list to check column 0
        C1.append(value[1])                #filling in the list to check column 1
        C2.append(value[2])                #filling in the list to check column 2
        D00_22.append(value[key])          #filling in the list to check diagonal 0:0 - 1:1 - 2:2
        D02_20.append(value[abs(key - 2)]) #filling in the list to check diagonal 0:2 - 1:1 - 2:0
    return any([C0 == X, C0 == O,
           C1 == X, C1 == O,
           C2 == X, C2 == O,
           D00_22 == X, D00_22 == O,
           D02_20 == X, D02_20 == O])       #checking columns and diagonals

print()
print("""   Yakomazov Aleksey
---==Tic--tac--toe==---""")

show_game_field(game_field)     #displaying the initial state of the game field

while True:     #launching the game
    move_counter += 1   #updating moves counter

    if move_counter == 10:    #if the victory conditions aren't met by move 10, then it is a draw, because all fields are occupied
        print("Draw!")
        break

    # identifying the current Player
    # the game is always started by 'X', which means that with odd moves it is Player X, and with even moves it is Player O
    current_player = 'O' if move_counter % 2 == 0 else 'X'

    #Implementing Rounds system. A new round begins when both players have made a move.
    if not move_counter % 2 == 0:
        print(f"-------------==Round {1 if move_counter == 1 else int((move_counter + 1)/2)}==-------------")
    print(f"Player {current_player}")

    while True:     #starting the correctness of rows and columns input check
        row = int(input("Please enter the row index: "))
        while not row in field_numbers:    #repeating row index input until it's correct
            print("Wrong row index!")
            row = int(input("Please enter the row index: "))

        column = int(input("Please enter the column index: "))
        while not column in field_numbers: #repeating column index input until it's correct
            print("Wrong column index!")
            column = int(input("Please enter the column index: "))

        if not game_field[row][column] == '-':   #by row and column indexes checking if the corresponding cell is available
            print("The cell is occupied! Please choose another one.")
        else:
            game_field[row][column] = current_player  #if the cell is empty adding the symbol of the current Player into it and interrupting the index entry check
            break

    show_game_field(game_field)  #displaying the current state of the game field
    if game_over(game_field):  #by the current state of the game field checking if the victory conditions are met
        print(f"Player {current_player} wins the Game on {move_counter}th move!") #if the victory conditions are met congratulating the winner and interrupting the game.
        break







'''
Classic tic-tac-toe.
The Game Field is 3x3. Player X starts.
The moves are performed by entering the
indexes of the rows and columns of the Game Field into the console.
'''

# Creating the Game Field, which is a dictionary where the keys
# are the indexes of the rows of the Game Field, and the values are lists of strings.
# The indexes of the lists correspond to the indexes of the columns of the Game Field
# and moves are recorded in the strings.

game_field = {
    0 : ['-', '-', '-'],
    1 : ['-', '-', '-'],
    2 : ['-', '-', '-']
}
# creating a variable to verify the correctness of the entered row and column indexes.
field_numbers = [0, 1, 2]
#creating moves counter
move_counter = 0

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
    The function checks if the victory conditions are met
    based on the current state of the Game Field.
    Victory conditions: in any row, column, or diagonal passing through the center of the field,
    all values are equal to "X" or "O". ("X" and "O" are English capital letters).
    :param field: a dictionary with the Game Field
    :return: True if victory conditions are met, otherwise False
    """
    x_win = ['X', 'X', 'X']     #creating a list to check the victory conditions for 'X'
    o_win = ['O', 'O', 'O']     #creating a list to check the victory conditions for 'O'
    # creating empty lists to check columns and diagonals
    c_0, c_1, c_2, d_00_22, d_02_20 = [], [], [], [], []
    for key, value in field.items():
        if value in (o_win, x_win):         #checking the rows
            return True
        c_0.append(value[0])                # filling in the list to check column 0
        c_1.append(value[1])                # filling in the list to check column 1
        c_2.append(value[2])                # filling in the list to check column 2
        d_00_22.append(value[key])          # filling in the list to check diagonal 0:0 - 1:1 - 2:2
        d_02_20.append(value[abs(key - 2)]) # filling in the list to check diagonal 0:2 - 1:1 - 2:0
    return any([c_0 == x_win, c_0 == o_win,
           c_1 == x_win, c_1 == o_win,
           c_2 == x_win, c_2 == o_win,
           d_00_22 == x_win, d_00_22 == o_win,
           d_02_20 == x_win, d_02_20 == o_win]) # checking columns and diagonals

print()
print("""   Yakomazov Aleksey
---==Tic--tac--toe==---""")

show_game_field(game_field) #displaying the initial state of the game field

while True:     # launching the game
    move_counter += 1 # updating moves counter
    # if the victory conditions aren't met by move 10
    # then it is a draw, because all fields are occupied
    if move_counter == 10:
        print("Draw!")
        break

    # identifying the current Player
    # the game is always started by 'X', which means that with odd moves it is Player X
    # and with even moves it is Player O
    current_player = 'O' if move_counter % 2 == 0 else 'X'

    #Implementing Rounds system. A new round begins when both players have made a move.
    if move_counter % 2 != 0:
        print(f"-------------==Round"
              f"{1 if move_counter == 1 else int((move_counter + 1)/2)}"
              f"==-------------")
    print(f"Player {current_player}")

    while True: #starting the correctness of rows and columns input check
        # repeating row index input until it's correct
        row = None
        while True:
            try:
                row = int(input("Please enter the row index: "))
            except ValueError as e:
                pass
            if row in field_numbers:
                break
            print('Wrong row index!')

        # repeating column index input until it's correct
        column = None
        while True:
            try:
                column = int(input("Please enter the column index: "))
            except ValueError as e:
                pass
            if column in field_numbers:
                break
            print("Wrong column index!")

        # by row and column indexes checking if the corresponding cell is available
        if game_field[row][column] != '-':
            print("The cell is occupied! Please choose another one.")
        else:
            # if the cell is empty adding the symbol of the current Player into it
            # and interrupting the index entry check
            game_field[row][column] = current_player
            break

    show_game_field(game_field)  #displaying the current state of the game field
    # by the current state of the game field checking if the victory conditions are met
    if game_over(game_field):
        # if the victory conditions are met congratulating the winner and interrupting the game
        print(f"Player {current_player} wins the Game on {move_counter}th move!")
        break

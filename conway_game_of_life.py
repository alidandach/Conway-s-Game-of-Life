from cellular_automaton import CA


def play():
    number_of_rows = int(input('please enter the number of rows (must be less than or equal 10):'))
    number_of_columns = int(input('please enter the number of columns (must be less than or equal 10):'))

    if number_of_rows <= 0 or number_of_columns <= 0:
        raise ValueError('number of row or column must positive')

    if number_of_rows > 10 and number_of_columns > 10:
        raise ValueError('number of row or column must be less than or equal 10')

    game_of_life_board = CA(number_of_rows, number_of_columns)

    game_of_life_board.print_automata()

    control_command = ''
    while control_command != 'x':
        control_command = input('if you want to stop please press x or you can continue using enter button')

        if control_command == '':
            game_of_life_board.get_next_generation()
            game_of_life_board.print_automata()


play()

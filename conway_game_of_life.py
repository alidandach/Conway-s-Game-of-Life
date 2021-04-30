from cellular_automaton import CA


def play():
    number_of_rows = int(input('please enter the number of rows'))
    number_of_columns = int(input('please enter the number of columns'))

    game_of_life_board = CA(number_of_rows, number_of_columns)

    game_of_life_board.print_automata()

    user_action = ''
    while user_action != 'x':
        user_action = input('if you want to stop please press x or you can continue using enter button')

        if user_action == '':
            game_of_life_board.get_next_generation()
            game_of_life_board.print_automata()


play()

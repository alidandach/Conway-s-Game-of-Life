from cell import Cell
from random import randint


class CA:
    def __init__(self, rows, columns):
        self._rows = rows
        self._columns = columns
        self._automata = [[Cell() for _ in range(self._columns)] for _ in range(self._rows)]
        self._generate_automata()

    def print_automata(self):
        print('\n' * 10)
        print('printing Spaceships pattern')
        for row in self._automata:
            for column in row:
                print(column.get_print_character(), end='')
            print()

    def _generate_automata(self):
        for row in self._automata:
            for column in row:
                is_positive = randint(0, 2)
                if is_positive == 1:
                    column.set_alive()

    def check_neighbour_cells(self, target_row, target_column):
        search_min = -1
        search_max = 2

        neighbour_cells = []
        for row in range(search_min, search_max):
            for column in range(search_min, search_max):
                cell_row = target_row + row
                cell_column = target_column + column

                valid_cell = True

                if cell_row == target_row and cell_column == target_column:
                    valid_cell = False

                if cell_row < 0 or cell_row >= self._rows:
                    valid_cell = False

                if cell_column < 0 or cell_column >= self._columns:
                    valid_cell = False

                if valid_cell:
                    neighbour_cells.append(self._automata[cell_row][cell_column])
        return neighbour_cells

    def get_next_generation(self):
        alive_cells = []
        dead_cells = []

        for row in range(len(self._automata)):
            for column in range(len(self._automata[row])):

                checked_cells = self.check_neighbour_cells(row, column)

                dead_cell_count = []

                for neighbour_cell in checked_cells:
                    if neighbour_cell.is_alive():
                        dead_cell_count.append(neighbour_cell)

                cell = self._automata[row][column]
                is_neighbour_is_alive = cell.is_alive()

                if is_neighbour_is_alive:
                    if len(dead_cell_count) < 2 or len(dead_cell_count) > 3:
                        dead_cells.append(cell)

                    if len(dead_cell_count) == 3 or len(dead_cell_count) == 2:
                        alive_cells.append(cell)

                else:
                    if len(dead_cell_count) == 3:
                        alive_cells.append(cell)

        for cells in alive_cells:
            cells.set_alive()

        for cells in dead_cells:
            cells.set_dead()

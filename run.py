import random

# Variable for declaring maximum lines to chose from (3)
MAX_LINES = 3
# Variable for declaring Maximum bet for a user to deposit(£100)
MAX_BET = 100
# Variable for decalaring Minimum bet for a user to deposit(£1)
MIN_BET = 1
# Variable for number of rows in game (3)
rows = 3
# Variable for number of columns in game (3)
cols = 3

# Dicitionary for number of symbols to generate
# 2 A's, 4 B's, 6 C's & 8 D's
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
# Dictionary for storing Value of each symbol
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

# Function for checking the rows for a sequence of 3 of the same symbols and
# adding the number of winning lines to a list and calculating winnings
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)


    return winnings, winning_lines

# Function for generating random rows/columns of symbols
def spin_slot_machine(rows, cols, symbols):
    all_symbols = []
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns
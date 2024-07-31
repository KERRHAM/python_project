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

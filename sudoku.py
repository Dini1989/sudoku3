# Wellcome to Petya's and Dénes's sudoku game

import time
import os
from copy import deepcopy


# Source of the grid1 generation.

sudokugamegridblank = [[10, 10, 10, 10, 10, 10, 10, 10, 10],
                       [10, 10, 10, 10, 10, 10, 10, 10, 10],
                       [10, 10, 10, 10, 10, 10, 10, 10, 10],
                       [10, 10, 10, 10, 10, 10, 10, 10, 10],
                       [10, 10, 10, 10, 10, 10, 10, 10, 10],
                       [10, 10, 10, 10, 10, 10, 10, 10, 10],
                       [10, 10, 10, 10, 10, 10, 10, 10, 10],
                       [10, 10, 10, 10, 10, 10, 10, 10, 10],
                       [10, 10, 10, 10, 10, 10, 10, 10, 10]]

sudokugamegrid = [[10, 27, 15, 10, 19, 10, 10, 10, 16],
                  [10, 12, 13, 10, 18, 10, 10, 14, 10],
                  [18, 10, 10, 10, 10, 13, 10, 10, 11],
                  [15, 10, 10, 17, 10, 12, 10, 10, 10],
                  [10, 14, 10, 18, 10, 16, 10, 12, 10],
                  [10, 10, 10, 19, 10, 11, 10, 10, 13],
                  [19, 10, 10, 14, 10, 10, 10, 10, 17],
                  [10, 16, 10, 10, 17, 10, 15, 18, 10],
                  [17, 10, 10, 10, 11, 10, 13, 19, 10]]

sudokugamegridnormal = [[10, 17, 15, 10, 19, 10, 10, 10, 16],
                        [10, 12, 13, 10, 18, 10, 10, 14, 10],
                        [18, 10, 10, 10, 10, 13, 10, 10, 11],
                        [15, 10, 10, 17, 10, 12, 14, 10, 10],
                        [10, 14, 10, 18, 10, 16, 10, 12, 10],
                        [10, 18, 10, 19, 10, 11, 17, 10, 13],
                        [19, 10, 10, 14, 10, 10, 10, 10, 17],
                        [10, 16, 10, 10, 17, 10, 15, 18, 10],
                        [17, 10, 10, 10, 11, 10, 13, 19, 10]]

sudokugamegrideasy = [[10, 17, 15, 10, 19, 10, 10, 10, 16],
                      [10, 12, 13, 10, 18, 10, 10, 14, 10],
                      [18, 10, 14, 10, 10, 13, 10, 10, 11],
                      [15, 10, 10, 17, 10, 12, 14, 10, 18],
                      [10, 14, 10, 18, 10, 16, 10, 12, 10],
                      [10, 18, 10, 19, 10, 11, 17, 10, 13],
                      [19, 10, 10, 14, 10, 10, 10, 10, 17],
                      [10, 16, 10, 10, 17, 10, 15, 18, 10],
                      [17, 10, 12, 10, 11, 10, 13, 19, 10]]


# Source of the good solution checker grid1.


sudokugridsolution = [[1, 7, 5, 2, 9, 4, 8, 3, 6],
                      [6, 2, 3, 1, 8, 7, 9, 4, 5],
                      [8, 9, 4, 5, 6, 3, 2, 7, 1],
                      [5, 1, 9, 7, 3, 2, 4, 6, 8],
                      [3, 4, 7, 8, 5, 6, 1, 2, 9],
                      [2, 8, 6, 9, 4, 1, 7, 5, 3],
                      [9, 3, 8, 4, 2, 5, 6, 1, 7],
                      [4, 6, 1, 3, 7, 9, 5, 8, 2],
                      [7, 5, 2, 6, 1, 8, 3, 9, 4]]

# GRID2

table2hard = [[10, 10, 14, 10, 17, 15, 10, 10, 10],
              [11, 10, 10, 12, 10, 10, 10, 18, 10],
              [10, 12, 10, 10, 10, 10, 17, 10, 10],
              [19, 18, 10, 10, 10, 10, 14, 10, 10],
              [13, 10, 10, 11, 10, 19, 10, 10, 17],
              [10, 10, 10, 10, 10, 10, 10, 12, 18],
              [10, 10, 11, 10, 10, 10, 10, 16, 10],
              [10, 16, 10, 10, 10, 17, 10, 10, 19],
              [10, 10, 10, 15, 14, 10, 18, 10, 10]]

table2normal = [[10, 10, 14, 10, 17, 15, 10, 10, 10],
                [11, 10, 10, 12, 10, 10, 10, 18, 10],
                [10, 12, 10, 10, 10, 10, 17, 10, 10],
                [19, 18, 10, 17, 10, 10, 14, 10, 10],
                [13, 10, 10, 11, 10, 19, 10, 10, 17],
                [10, 11, 10, 10, 10, 10, 10, 12, 18],
                [10, 10, 11, 10, 10, 10, 10, 16, 10],
                [10, 16, 10, 16, 10, 17, 10, 10, 19],
                [10, 10, 10, 15, 14, 10, 18, 10, 10]]

table2easy = [[18, 10, 14, 10, 17, 15, 10, 10, 16],
              [11, 10, 10, 12, 10, 10, 10, 18, 10],
              [10, 12, 10, 10, 10, 10, 17, 10, 10],
              [19, 18, 10, 17, 10, 10, 14, 10, 10],
              [13, 10, 10, 11, 10, 19, 10, 10, 17],
              [10, 11, 10, 10, 16, 10, 10, 12, 18],
              [10, 10, 11, 10, 10, 10, 10, 16, 10],
              [10, 16, 10, 16, 10, 17, 10, 10, 19],
              [10, 10, 10, 15, 14, 10, 18, 10, 13]]
# GRID2solution
table2solution = [[8, 9, 4, 3, 7, 5, 2, 1, 6],
                  [1, 5, 7, 2, 9, 6, 3, 8, 4],
                  [6, 2, 3, 8, 1, 4, 7, 9, 5],
                  [9, 8, 6, 7, 5, 2, 4, 3, 1],
                  [3, 4, 2, 1, 8, 9, 6, 5, 7],
                  [7, 1, 5, 4, 6, 3, 9, 2, 8],
                  [4, 7, 1, 9, 3, 8, 5, 6, 2],
                  [5, 3, 8, 6, 2, 7, 1, 4, 9],
                  [2, 6, 9, 5, 4, 1, 8, 7, 3]]

# GRID3

table3hard = [[10, 10, 15, 13, 10, 10, 10, 10, 10],
              [18, 10, 10, 10, 10, 10, 10, 12, 10],
              [10, 17, 10, 10, 11, 10, 15, 10, 10],
              [14, 10, 10, 10, 10, 15, 13, 10, 10],
              [10, 11, 10, 10, 17, 10, 10, 10, 16],
              [10, 10, 13, 12, 10, 10, 10, 18, 10],
              [10, 16, 10, 15, 10, 10, 10, 10, 19],
              [10, 10, 14, 10, 10, 10, 10, 13, 10],
              [10, 10, 10, 10, 10, 19, 17, 10, 10]]

table3normal = [[11, 10, 15, 13, 10, 10, 10, 10, 10],
                [18, 10, 10, 10, 10, 10, 10, 12, 10],
                [10, 17, 10, 10, 11, 10, 15, 10, 10],
                [14, 10, 10, 10, 10, 15, 13, 10, 10],
                [10, 11, 10, 10, 17, 10, 10, 10, 16],
                [10, 10, 13, 12, 10, 10, 10, 18, 10],
                [10, 16, 10, 15, 10, 12, 10, 10, 19],
                [10, 10, 14, 10, 10, 10, 10, 13, 10],
                [10, 10, 11, 10, 10, 19, 17, 10, 10]]

table3easy = [[11, 10, 15, 13, 10, 10, 10, 10, 10],
              [18, 10, 10, 10, 10, 10, 10, 12, 10],
              [10, 17, 10, 10, 11, 10, 15, 10, 10],
              [14, 10, 10, 10, 10, 15, 13, 10, 10],
              [10, 11, 10, 10, 17, 10, 10, 10, 16],
              [17, 10, 13, 12, 10, 16, 10, 18, 10],
              [10, 16, 10, 15, 10, 12, 10, 10, 19],
              [10, 10, 14, 10, 10, 10, 10, 13, 10],
              [15, 10, 11, 10, 10, 19, 17, 10, 10]]

# GRID3solution

table3solution = [[1, 4, 5, 3, 2, 7, 6, 9, 8],
                  [8, 3, 9, 6, 5, 4, 1, 2, 7],
                  [6, 7, 2, 9, 1, 8, 5, 4, 3],
                  [4, 9, 6, 1, 8, 5, 3, 7, 2],
                  [2, 1, 8, 4, 7, 3, 9, 5, 6],
                  [7, 5, 3, 2, 9, 6, 4, 8, 1],
                  [3, 6, 7, 5, 4, 2, 8, 1, 9],
                  [9, 8, 4, 7, 6, 1, 2, 3, 5],
                  [5, 2, 1, 8, 3, 9, 7, 6, 4]]


# Generates the grid from the source and adds visuals. Also adds basic
# rules about the displayed grid (17 visualised as 7 etc.)
def table():
    bold = "\033[1m"
    reset = "\033[0;0m"
    yellow = "\033[93m"
    purple = "\033[95m"
    blue = "\033[92m"
    print("   a  b  c    d  e  f    g  h  i\n")
    for row in range(0, 9):
        if row == 3:
            print("   -----------------------------")
        if row == 6:
            print("   -----------------------------")
        print(row + 1, end=" ")
        for column in range(0, 9):
            if column == 3:
                print("｜", end="")
            if column == 6:
                print("｜", end="")

            if (sudokugamegrid[row][column]) <= 10:
                print(" ", purple, gridtransformer(
                    sudokugamegrid[row][column]), reset, sep="", end=" ")

            elif (sudokugamegrid[row][column]) > 20:
                print(" ", blue, bold, gridtransformer(
                    sudokugamegrid[row][column]), reset, sep="", end=" ")

            elif (sudokugamegrid[row][column]) > 10 and (sudokugamegrid[row][column]) < 20:
                print(" ", yellow, bold, gridtransformer(
                    sudokugamegrid[row][column]), reset, sep="", end=" ")

        print()

    print("   -----------------------------")


def tableblank():
    bold = "\033[1m"
    reset = "\033[0;0m"
    purple = "\033[95m"
    print("   a  b  c    d  e  f    g  h  i\n")
    for row in range(0, 9):
        if row == 3:
            print("   -----------------------------")
        if row == 6:
            print("   -----------------------------")
        print(row + 1, end=" ")
        for column in range(0, 9):
            if column == 3:
                print("｜", end="")
            if column == 6:
                print("｜", end="")
            if sudokugamegridblank[row][column] == 10:
                print(" ", purple, gridtransformer(
                    sudokugamegridblank[row][column]), reset, sep="", end=" ")
        print()

    print("   -----------------------------")


def gridtransformer(x):
    if x > 10 and x < 20:
        return x - 10
    if x == 10:
        return "·"
    if x > 20:
        return x - 20
    return x


# Handles the user inputs like uninterpretable expressions. Add rules to
# the game mechanics (Immutable basic existing characters on the grid
# etc.)


def handleinput():
    while True:
        inputfield = input(
            "\nAdd the coordinates and the value(example: 1a5).\nYou can delete with value '10'.\nWrite 'check' to check your solution!\nOr type 'hint' if you want\nto check your good numbers!\nOr type 'exit' to quit!\n\nEnter you choice:")
        if inputfield == str("exit"):
            exit()
        elif inputfield == str("hint"):
            os.system('cls' if os.name == 'nt' else 'clear')
            hint()
            table()
            print("\nThe good numbers are green now!")

        elif inputfield == str("check"):
            os.system('cls' if os.name == 'nt' else 'clear')
            table()
            sudoku_list_matcher(clonelist)
            if int(sudoku_match_sum(clonelist, sudokugridsolution)) == int(81):
                table()
                print("\n!!!!!!!!!!!!YOU WON!!!!!!!!!!!!")
                input("Press any key to exit")
                exit()
            else:
                print("\nContinue the game, it's not good yet :(")

        else:
            try:
                inputrow = int(inputfield[0]) - 1
                inputcolumn = int(ord(inputfield[1])) - 97
                inputvalue = int(inputfield[2:])
                if inputrow not in range(0, 9):
                    raise IndexError
                if inputcolumn not in range(0, 9):
                    raise IndexError
                if inputvalue not in range(1, 11):
                    raise ValueError
                if sudokugamegrid[inputrow][inputcolumn] > 10:
                    raise ReferenceError
                return inputrow, inputcolumn, inputvalue,

            except IndexError:
                os.system('cls' if os.name == 'nt' else 'clear')
                table()
                print("\nYour coordinate is not on the game field, please try again.")
            except ValueError:
                os.system('cls' if os.name == 'nt' else 'clear')
                table()
                print("\nOops!  That was no valid number.  Try again...")
            except ReferenceError:
                os.system('cls' if os.name == 'nt' else 'clear')
                table()
                print("\nYou can't modify the basefield value!")


def hint():
    for row in range(0, 9):
        for column in range(0, 9):
            if sudokugamegrid[row][column] == sudokugridsolution[row][column]:
                sudokugamegrid[row][column] = sudokugamegrid[row][column] + 20


# Checking the solution by comparing the user modified basic grid with the
# solution grid.


def clone_list(x):
    y = deepcopy(x)
    return y


def sudoku_list_matcher(x):
    for i in range(0, 9):
        for n in range(0, 9):
            if x[i][n] > 10:
                x[i][n] = x[i][n] - 10


def sudoku_match_sum(x, y):
    how_many_matches = []
    for i in range(0, 9):
        for n in range(0, 9):
            if x[i][n] == y[i][n]:
                how_many_matches.append(1)
            else:
                how_many_matches.append(0)
    return sum(how_many_matches)


def map_selector():

    global sudokugamegrid
    global sudokugridsolution

    while True:

        os.system('cls' if os.name == 'nt' else 'clear')
        tableblank()
        print("\n\n")

        x = input("""Please choose from three grid and
three difficulty level, like you see in this example:
'map1 normal' or 'map3 hard'
If you want to quit type 'exit'
You only can pass with a valid input.
Type in your choice:""")

        if x == "map1 hard":
            break
        if x == "map1 normal":
            sudokugamegrid = sudokugamegridnormal
            break
        if x == "map1 easy":
            sudokugamegrid = sudokugamegrideasy
            break
        if x == "map2 hard":
            sudokugamegrid = table2hard
            sudokugridsolution = table2solution
            break
        if x == "map2 normal":
            sudokugamegrid = table2normal
            sudokugridsolution = table2solution
            break
        if x == "map2 easy":
            sudokugamegrid = table2easy
            sudokugridsolution = table2easy
            break
        if x == "map3 hard":
            sudokugamegrid = table3hard
            sudokugridsolution = table3solution
            break
        if x == "map3 normal":
            sudokugamegrid = table3normal
            sudokugridsolution = table3solution
            break
        if x == "map3 easy":
            sudokugamegrid = table3easy
            sudokugridsolution = table3solution
            break
        if x == "exit":
            exit()


# Intro text to the program

os.system('cls' if os.name == 'nt' else 'clear')
print("\033[1m", "\033[93m", '''    _n____n__
     /         \---||--<  ___EXTERMINATE--
    <___________>                   --SUDOKU___
    _|____|____|_
    _|____|____|_
     |    |    |
    --------------
    | || || || ||\
    | || || || || \++++++++------<
    ===============
    |   |  |  |   |            by Petya
   (| O | O| O| O |)                & Dénes
   |   |   |   |   |
  (| O | O | O | O |)
   |   |   |   |    |
 (| O |  O | O  | O |)
  |   |    |    |    |
 (| O |  O |  O |  O |)
 ======================''', "\033[m", "\033[0;0m")
print("""\nAdd numbers correctly into their places.\nYou can quit the game on the checker screen.\nEnter the coordinates and the value(example: '1a5')! \nUse the helper grids to identify the coordinates!\nUse 10 value as delete like in this example: 1a10.""")
time.sleep(6)
os.system('cls' if os.name == 'nt' else 'clear')

# Running the functions in the proper order.


map_selector()

os.system('cls' if os.name == 'nt' else 'clear')

while True:

    table()

    print("\n")

    clone_list(sudokugamegrid)

    clonelist = clone_list(sudokugamegrid)

    row, column, value = handleinput()

    os.system('cls' if os.name == 'nt' else 'clear')

    table()

    sudokugamegrid[row][column] = value

    os.system('cls' if os.name == 'nt' else 'clear')


# The file ends here. Live long and prosper!

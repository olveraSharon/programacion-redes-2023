#Aurot: Sharon Michelle Olvera Ibarra
#Fecha: 10/10/2023
#Descripcion:PROYECTO: TIC-TAC-TOE


import random

def DisplayBoard(board):
    for row in board:
        print(f"{row[0]} | {row[1]} | {row[2]}")
        if row != board[-1]:
            print("---------")

############################################################################3

def EnterMove(board):
    while True:
        try:
            move = int(input("Ingresa tu movimiento (1-9): "))
            if move < 1 or move > 9:
                print("El número debe estar entre 1 y 9.")
            else:
                row, col = (move - 1) // 3, (move - 1) % 3
                if board[row][col] == " ":
                    board[row][col] = "O"
                    break
                else:
                    print("Esa casilla ya está ocupada. Elige otra.")
        except ValueError:
            print("Ingresa un número válido.")

################################################################################33

def MakeListOfFreeFields(board):
    free_fields = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                free_fields.append((row, col))
    return free_fields

######################################################################################3

def VictoryFor(board, sign):
    for row in board:
        if all(cell == sign for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == sign for row in range(3)):
            return True

    if all(board[i][i] == sign for i in range(3)) or all(board[i][2 - i] == sign for i in range(3)):
        return True

    return False
################################################################################################3
def DrawMove(board):
#Turno de la maquina
    free_fields = MakeListOfFreeFields(board)
    if free_fields:
        row, col = random.choice(free_fields)
        board[row][col] = "X"


board = [[" " for _ in range(3)] for _ in range(3)]

board[1][1] = "X"

while True:
    DisplayBoard(board)
    EnterMove(board)
    if VictoryFor(board, "O"):
        DisplayBoard(board)
        print("¡Felicidades! ¡Has ganado!")
        break
    elif not MakeListOfFreeFields(board):
        DisplayBoard(board)
        print("¡Es un empate!")
        break

    DrawMove(board)
    if VictoryFor(board, "X"):
        DisplayBoard(board)
        print("¡La máquina gana!")
    
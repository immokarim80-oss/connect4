"""Connect 4 (Puissance 4)"""

from tools import (State, Action, Grid, RED, YELLOW, Score)

def legals(state: State) -> list[Action]:
    """Renvoie la liste des actions légales pour un état donné"""
    grid, player = state
    actions: list[Action] = []
    col = 0
    while col < len(grid[0]):
        if grid[0][col] == 0:
            # si la case situé la plus haute est vide, on peut jouer dans cette colonne
            actions.append((col, player))
        col += 1
    return actions

def ligne(grid: Grid, player: int) -> bool:
    """Renvoie True si le joueur a gagné sur une ligne"""
    for row in grid:
        count = 0
        for cell in row:
            if cell == player:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0
    return False

def colonne(grid: Grid, player: int) -> bool:
    """Renvoie True si le joueur a gagné sur une colonne"""
    nb_rows = len(grid)
    nb_cols = len(grid[0])

    for col in range(nb_cols):
        count = 0
        for row in range(nb_rows):
            if grid[row][col] == player:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0
    return False

   
def diagonale(grid: Grid, player: int) -> bool:
    """Renvoie True si le joueur a gagné sur une diagonale"""
    nb_rows = len(grid)
    nb_cols = len(grid[0])

    # Diagonales descendantes
    for row in range(nb_rows - 3):
        for col in range(nb_cols - 3):
            if (
                grid[row][col] == player
                and grid[row + 1][col + 1] == player
                and grid[row + 2][col + 2] == player
                and grid[row + 3][col + 3] == player
            ):
                return True

    # Diagonales montantes
    for row in range(3, nb_rows):
        for col in range(nb_cols - 3):
            if (
                grid[row][col] == player
                and grid[row - 1][col + 1] == player
                and grid[row - 2][col + 2] == player
                and grid[row - 3][col + 3] == player
            ):
                return True

    return False


def final(grid: Grid) -> bool:
    """Renvoie True si le jeu est terminé."""

    if (
        ligne(grid, YELLOW)
        or colonne(grid, YELLOW)
        or diagonale(grid, YELLOW)
    ):
        return True

    if (
        ligne(grid, RED)
        or colonne(grid, RED)
        or diagonale(grid, RED)
    ):
        return True

    # Plateau plein, match nul
    for row in grid:
        if 0 in row:
            return False

    return True

def score(grid: Grid) -> Score:
    """Renvoie le score d'une position terminale."""

    if (
        ligne(grid, YELLOW)
        or colonne(grid, YELLOW)
        or diagonale(grid, YELLOW)
    ):
        return 1.0

    if (
        ligne(grid, RED)
        or colonne(grid, RED)
        or diagonale(grid, RED)
    ):
        return -1.0

    return 0.0
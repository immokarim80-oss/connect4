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


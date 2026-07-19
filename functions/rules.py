"""Connect 4 (Puissance 4)"""

from connect4.functions.tools import (State, Action, STARTING_STATE)

def legals_actions(state: State) -> list[Action]:
    """Renvoie la liste des actions légales pour un état donné"""
    grid, player = state
    actions: list[Action] = []
    col = 0
    while col < len(grid):
        if grid[col][0] == 0:
            # si la case situé la plus haute est vide, on peut jouer dans cette colonne
            actions.append((col, player))
        col += 1
    return actions

legals_actions((STARTING_STATE))
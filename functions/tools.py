"""Connect 4 (Puissance 4)"""

from typing import Callable

Grid = tuple[tuple[int, ...], ...]  # en s'inspirant du TP
Coord = tuple[
    int, int
]  # on simplifie ici en utilisant deux entiers au lieu des lettres pour les colonnes
   # utile pour détecter un état final
# le premier entier représente le numéro de ligne et le second le numéro de colonne.
Player = int  # 1 pour le joueur jaune (YELLOW), -1 pour le joueur rouge (RED)
Column = int  # le numéro de la colonne où le joueur souhaite jouer (entre 0 et 6)
Action = tuple[Column, Player] # le joueur Player place une pièce dans la colonne Column
Score = float
State = tuple[Grid, Player]
Strategy = Callable[[State], Action]

# Constantes utiles :

YELLOW: Player = 1
RED: Player = -1
STARTING_GRID: Grid = (
    (0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0),
)
STARTING_STATE: State = (STARTING_GRID, YELLOW)

def grid_tuple_to_grid_list(grid: Grid) -> list[list[int]]:
    """Transforme une grille de tuple en grille de liste"""
    listes: list[list[int]] = []
    for t in grid:
        listes.append(list(t))
    return listes


def grid_list_to_grid_tuple(grid: list[list[int]]) -> Grid:
    """Transforme une grille de liste en grille de tuple"""
    tuples: list[tuple[int, ...]] = []
    for l in grid:
        tuples.append(tuple(l))
    return tuple(tuples)


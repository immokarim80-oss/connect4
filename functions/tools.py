"""Connect 4 (Puissance 4)"""

from typing import Callable

Grid = tuple[tuple[int, ...], ...]  # en s'inspirant du TP
Coord = tuple[
    int, int
]  # on simplifie ici en utilisant deux entiers au lieu des lettres pour les colonnes
# le premier entier représente le numéro de ligne et le second le numéro de colonne.
Player = int  # 1 pour le joueur jaune (YELLOW), -1 pour le joueur rouge (RED)
Action = tuple[Coord, Player]
Score = float
State = tuple[Grid, Player]
Strategy = Callable[[State], Action]

# Constantes utiles :

YELLOW: Player = 1
RED: Player = -1
Y_COIN: int = 1
R_COIN: int = -1
STARTING_GRID: Grid = (
    (0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0),
)
STARTING_STATE: State = (STARTING_GRID, YELLOW)

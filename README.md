# Jet-Tic_Tac_Toe

3 levels: easy, medium, hard

The top-left cell will have the coordinates (1, 1) and the bottom-right cell will have the coordinates (3, 3), as shown in this table below. Coordinates start with 1 and can be 1, 2, or 3.

    (1, 1) (1, 2) (1, 3)
    (2, 1) (2, 2) (2, 3)
    (3, 1) (3, 2) (3, 3)

The possible states are:

- **Game not finished** — when no side has three in a row, but the table still has empty cells;
- **Draw** — when no side has three in a row, and the table is complete;
- **X wins** — when there are three X's in a row;
- **O wins** — when there are three O's in a row.

EASY mode:
    - The user plays first as X
    - The computer makes its randomly move as O.

MEDIUM mode:
    - If it already has two in a row and can win with one further move, it does so.
    - If its opponent can win with one move, it plays the move necessary to block this.
    - Otherwise, it makes a random move (easy mode).    
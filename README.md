# Minesweeper

This is a Minesweeper game written in Python using the Pygame library. The game allows the player to click on cells to reveal their contents. The goal is to reveal all cells that do not contain mines without revealing any cells that contain mines. If the player reveals a cell containing a mine, they lose the game.

## Getting Started

To run the game, you will need Python 3 and the Pygame library installed on your computer. You can install Pygame by running `pip install pygame` in your terminal.

Once you have Pygame installed, you can run the game by running the `minesweeper.py` file.

## How to Play

The game starts with a grid of cells, some of which contain mines. The player can click on a cell to reveal its contents. If the cell contains a mine, the player loses the game. If the cell does not contain a mine, it will display a number indicating how many mines are adjacent to the cell. The player can use this information to deduce which cells contain mines and which do not.

The player can also right-click on a cell to mark it with a flag. This can be useful for keeping track of which cells the player thinks contain mines.

The game is won when all non-mine cells have been revealed and all mine cells have been flagged.

## How it Works

The game creates a grid of `Cell` objects, each of which represents a single cell in the game. Each `Cell` object has attributes indicating whether it contains a mine, whether it has been revealed, whether it has been flagged, and how many mines are adjacent to it.

The game uses Pygame to create a graphical user interface for the game. The `draw_cell` function is used to draw each cell on the screen, and the `reveal_cell` function is used to reveal a cell and its neighbors when the player clicks on it.

The game uses a `create_grid` function to randomly place mines on the grid and calculate the number of mines adjacent to each cell.

The game ends when the player wins or loses, and the program terminates.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

import pygame
import random

# Dimensions
WIDTH = 800
HEIGHT = 600
CELL_SIZE = 40
GRID_SIZE_X = WIDTH // CELL_SIZE
GRID_SIZE_Y = HEIGHT // CELL_SIZE

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Configuration de démineur
NUM_MINES = 40

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_mine = False
        self.is_revealed = False
        self.is_flagged = False
        self.mines_around = 0

    def reveal(self):
        self.is_revealed = True

    def toggle_flag(self):
        self.is_flagged = not self.is_flagged


def create_grid():
    grid = [[Cell(x, y) for y in range(GRID_SIZE_Y)] for x in range(GRID_SIZE_X)]
    mines = 0

    while mines < NUM_MINES:
        x = random.randint(0, GRID_SIZE_X - 1)
        y = random.randint(0, GRID_SIZE_Y - 1)
        if not grid[x][y].is_mine:
            grid[x][y].is_mine = True
            mines += 1

    for x in range(GRID_SIZE_X):
        for y in range(GRID_SIZE_Y):
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < GRID_SIZE_X and 0 <= ny < GRID_SIZE_Y:
                        grid[x][y].mines_around += grid[nx][ny].is_mine

    return grid

def draw_cell(screen, cell):
    x, y = cell.x * CELL_SIZE, cell.y * CELL_SIZE
    rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
    border_color = (128, 128, 128)  # Couleur de la bordure (gris)

    if cell.is_revealed:
        pygame.draw.rect(screen, WHITE, rect)
        pygame.draw.rect(screen, border_color, rect, 1)  # Ajout de la bordure
        if cell.is_mine:
            pygame.draw.circle(screen, BLACK, rect.center, CELL_SIZE // 3)
        elif cell.mines_around > 0:
            font = pygame.font.Font(None, 24)
            text = font.render(str(cell.mines_around), True, BLACK)
            screen.blit(text, rect.move(CELL_SIZE // 3, CELL_SIZE // 3))
    else:
        pygame.draw.rect(screen, BLACK, rect)
        pygame.draw.rect(screen, border_color, rect, 1)  # Ajout de la bordure
        if cell.is_flagged:
            pygame.draw.line(screen, WHITE, rect.topleft, rect.bottomright, 2)
            pygame.draw.line(screen, WHITE, rect.topright, rect.bottomleft, 2)

def reveal_cell(grid, x, y):
    cell = grid[x][y]
    if cell.is_revealed or cell.is_flagged:
        return

    cell.reveal()

    if cell.mines_around == 0:
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < GRID_SIZE_X and 0 <= ny < GRID_SIZE_Y:
                    reveal_cell(grid, nx, ny)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Démineur")

    grid = create_grid()
    running = True

    while running:
        screen.fill(WHITE)

        for x in range(GRID_SIZE_X):
            for y in range(GRID_SIZE_Y):
                draw_cell(screen, grid[x][y])

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                cell_x, cell_y = x // CELL_SIZE, y // CELL_SIZE
                cell = grid[cell_x][cell_y]

                if event.button == 1:  # Clic gauche
                    if not cell.is_flagged:
                        reveal_cell(grid, cell_x, cell_y)

                        # Fin du jeu si on clique sur une mine
                        if cell.is_mine:
                            for row in grid:
                                for c in row:
                                    c.reveal()
                            running = False
                            print("Vous avez perdu !")
                elif event.button == 3:  # Clic droit
                    cell.toggle_flag()

    pygame.quit()

if __name__ == "__main__":
    main()
import pygame
import sys
import puzzle_1
import puzzle_3

# 색깔 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# 스도쿠 초기 설정
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# 스도쿠 게임 화면 구현
def puzzle_game(screen, step:int, list):
    # 스도쿠 그리드 초기 설정
    grid_size = 9
    cell_size = 60
    margin = 20

    def get_randgame(what):
        if what == "a":
            puzzle_1.puzzle_game(screen, step + 1, list)
        if what == "b":
            puzzle_3.puzzle_game(screen, step + 1, list)

    def draw_sudoku():
        for y in range(grid_size):
            for x in range(grid_size):
                value = sudoku_board[y][x]
                rect = pygame.Rect(x * cell_size + margin, y * cell_size + margin, cell_size, cell_size)
                pygame.draw.rect(screen, WHITE, rect)
                
                if value != 0:
                    font = pygame.font.SysFont("malgungothic", 40)
                    text = font.render(str(value), True, BLACK)
                    text_rect = text.get_rect(center=rect.center)
                    screen.blit(text, text_rect)

    def draw_subgrid_lines():
        for i in range(1, 3):
            pygame.draw.line(screen, BLACK, (margin, i * cell_size * 3 + margin), (cell_size * grid_size + margin, i * cell_size * 3 + margin), 4)
            pygame.draw.line(screen, BLACK, (i * cell_size * 3 + margin, margin), (i * cell_size * 3 + margin, cell_size * grid_size + margin), 4)

    def is_valid_move(y, x, num):
        # 행과 열 검사
        for i in range(grid_size):
            if sudoku_board[y][i] == num or sudoku_board[i][x] == num:
                return False
        
        # 3x3 서브그리드 검사
        subgrid_x = (x // 3) * 3
        subgrid_y = (y // 3) * 3
        for i in range(subgrid_y, subgrid_y + 3):
            for j in range(subgrid_x, subgrid_x + 3):
                if sudoku_board[i][j] == num:
                    return False
        
        return True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.unicode.isdigit():
                    num = int(event.unicode)
                    if 1 <= num <= 9 and is_valid_move(selected_y, selected_x, num):
                        sudoku_board[selected_y][selected_x] = num
                elif event.key == pygame.K_BACKSPACE:
                    sudoku_board[selected_y][selected_x] = 0

        screen.fill(BLACK)
        draw_subgrid_lines()
        draw_sudoku()
        pygame.display.flip()

        selected_x = (pygame.mouse.get_pos()[0] - margin) // cell_size
        selected_y = (pygame.mouse.get_pos()[1] - margin) // cell_size

        if selected_x >= 0 and selected_x < grid_size and selected_y >= 0 and selected_y < grid_size:
            pygame.draw.rect(screen, RED, (selected_x * cell_size + margin, selected_y * cell_size + margin, cell_size, cell_size), 3)

        if all(all(num != 0 for num in row) for row in sudoku_board):
            font = pygame.font.SysFont("malgungothic", 50)
            text = font.render("스도쿠 완성!", True, WHITE)
            text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
            screen.blit(text, text_rect)
            pygame.display.flip()
            pygame.time.wait(2000)  # 2초 대기
            get_randgame(list[step])
            return


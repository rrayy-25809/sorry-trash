import pygame
import sys
import puzzle_2
import puzzle_3

# 색깔 정의
WHITE = (255, 255, 255)

WINDOW_SIZE = (600, 600)

# 퍼즐 이미지 로드
puzzle_images = [
    pygame.image.load("puzzle_1.png"),  # puzzle_1.png 파일이 퍼즐 이미지로 사용됨
    pygame.image.load("puzzle_2.png"),  # puzzle_2.png 파일이 퍼즐 이미지로 사용됨
    pygame.image.load("puzzle_3.png")   # puzzle_3.png 파일이 퍼즐 이미지로 사용됨
]

# 퍼즐 게임 화면 구현
def puzzle_game(screen, step:int, list):
    block_size = 200
    puzzle = [[0, 1, 2], [3, None, 4], [5, 6, 7]]
    empty_pos = (1, 1)

    def draw_puzzle():
        for y in range(3):
            for x in range(3):
                value = puzzle[y][x]
                rect = pygame.Rect((x * block_size) + (WINDOW_SIZE[0] - 3 * block_size) / 2, 
                                   (y * block_size) + (WINDOW_SIZE[1] - 3 * block_size) / 2, 
                                   block_size, block_size)
                pygame.draw.rect(screen, WHITE, rect, 2)
                if value is not None:
                    screen.blit(puzzle_images[value], rect)

    def move_block(dx, dy):
        x, y = empty_pos
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            # 블록 이동
            puzzle[y][x], puzzle[new_y][new_x] = puzzle[new_y][new_x], puzzle[y][x]
            return new_x, new_y
        return x, y

    def check_completion():# 퍼즐이 완성되었는지 확인하는 함수
        completed_puzzle = [[8, 7, 6], [5, 4, 1], [3, 2, None]]
        return puzzle == completed_puzzle
    
    def get_randgame(what):
        if what == "b":
            puzzle_2.puzzle_game(screen, step + 1, list)
        if what == "c":
            puzzle_3.puzzle_game(screen, step + 1, list)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # 퍼즐 그리기
        screen.fill((0, 0, 0))
        draw_puzzle()
        pygame.display.flip()

        # 퍼즐이 완성되었는지 확인
        if check_completion():
            font = pygame.font.SysFont("malgungothic", 50)
            text = font.render("퍼즐 완성!", True, WHITE)
            # 메시지를 화면 중앙에 배치하기 위해 조정
            screen.blit(text, (160, 200))
            pygame.display.flip()
            pygame.time.wait(2000)  # 2초 대기
            get_randgame(list[step])
            return

        # 키 입력 받기
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            empty_pos = move_block(0, -1)
        elif keys[pygame.K_DOWN]:
            empty_pos = move_block(0, 1)
        elif keys[pygame.K_LEFT]:
            empty_pos = move_block(-1, 0)
        elif keys[pygame.K_RIGHT]:
            empty_pos = move_block(1, 0)

import pygame
import sys
import puzzle_1
import puzzle_2

# 색깔 정의
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# 퍼즐 게임 화면 구현
def puzzle_game(screen, step, list):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    # 키 입력 받기
    keys = pygame.key.get_pressed()

    def get_randgame(what):
        if what == "a":
            puzzle_1.puzzle_game(screen, step + 1, list)
        if what == "b":
            puzzle_2.puzzle_game(screen, step + 1, list)

    def check_completion():
        return True

    while True:
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
    
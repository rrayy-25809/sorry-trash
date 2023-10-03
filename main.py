import pygame
import sys
import puzzle_1
import puzzle_2
import random
import puzzle_3

# 초기화
pygame.init()

# 창 크기 설정
WINDOW_SIZE = (600, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("퍼즐 게임")

# 색깔 정의
WHITE = (255, 255, 255)

# 기본 폰트
font = pygame.font.SysFont("malgungothic", 40)

# 시작 화면 구현
def start_screen(screen):
    # 시작 화면 배경 설정
    background_color = (0, 0, 0)
    screen.fill(background_color)

    # 시작 버튼 디자인
    button_color = (50, 50, 200)
    button_rect = pygame.Rect(200, 250, 200, 100)
    pygame.draw.rect(screen, button_color, button_rect)
    
    text = font.render("시작", True, WHITE)
    text_rect = text.get_rect(center=button_rect.center)
    
    screen.blit(text, text_rect)
    pygame.display.flip()

    # "이스터에그" 출력을 위한 변수 및 폰트 설정
    easter_egg = False
    easter_egg_font = pygame.font.SysFont("malgungothic", 20)

    # 메인 게임 루프
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    screen.fill((0, 0, 0))
                    start_text = font.render("지금부터 나오는 랜덤한 세 개의 퍼즐을 모두 클리어하세요!", True, WHITE)
                    text_rect = start_text.get_rect(center=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2))
                    screen.blit(start_text, text_rect)
                    pygame.display.flip()
                    pygame.time.wait(2000)
                    waiting = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    easter_egg = True
            
        # 게임 화면 업데이트
        if easter_egg:
            screen.fill((0, 0, 0))
            easter_egg_text = easter_egg_font.render("축하합니다! 이스터에그를 발견하셨습니다!", True, WHITE)
            text_rect = easter_egg_text.get_rect(center=(WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2))
            screen.blit(easter_egg_text, text_rect)
            pygame.display.flip()
            pygame.time.wait(2000)

# 시작 화면 실행
start_screen(screen)

# 랜덤한 퍼즐 게임 실행
abc = ['a', 'b', 'c']
random.shuffle(abc)
print(abc)
if abc[0] == "a":
    puzzle_1.puzzle_game(screen, 1, abc)
elif abc[0] == "b":
    puzzle_2.puzzle_game(screen, 1, abc)
elif abc[0] == "c":
    puzzle_3.puzzle_game(screen, 1, abc)

pygame.quit()
sys.exit()

import pygame

pygame.init()

calc_img = pygame.image.load("calcu.png")

width = calc_img.get_width()
height = calc_img.get_height()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Random Calculator game")

button_0 = pygame.Rect()
button_9 = pygame.Rect()
button_8 = pygame.Rect()
button_7 = pygame.Rect(70, 600, 55, 55)
button_6 = pygame.Rect(280, 520, 55, 55)
button_5 = pygame.Rect()
button_4 = pygame.Rect()
button_3 = pygame.Rect()
button_2 = pygame.Rect()
button_1 = pygame.Rect()



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()

                if button_0.collidepoint(mouse_pos):
                                                    print("You clicked the 0 button!")

                if button_9.collidepoint(mouse_pos):
                                                    print("You clicked the 9 button!")


                if button_8.collidepoint(mouse_pos):
                                    print("You clicked the 8 button!")

                if button_7.collidepoint(mouse_pos):
                    print("You clicked the 7 button!")

                if button_6.collidepoint(mouse_pos):
                    print("You clicked the 6 button!")

                    if button_5.collidepoint(mouse_pos):
                                        print("You clicked the 5 button!")

                    if button_4.collidepoint(mouse_pos):
                                        print("You clicked the 4 button!")

                    if button_3.collidepoint(mouse_pos):
                                        print("You clicked the 3 button!")

                    if button_2.collidepoint(mouse_pos):
                                        print("You clicked the 2 button!")

                    if button_1.collidepoint(mouse_pos):
                                        print("You clicked the 1 button!")



    screen.blit(calc_img, (0, 0))
    pygame.draw.rect(screen, (0, 255, 0), button_0, 2)
    pygame.draw.rect(screen, (0, 255, 0), button_9, 2)
    pygame.draw.rect(screen, (0, 255, 0), button_8, 2)
    pygame.draw.rect(screen, (0, 255, 0), button_7, 2)
    pygame.draw.rect(screen, (0, 255, 0), button_6, 2)
    pygame.draw.rect(screen, (0, 255, 0), button_5, 2)
    pygame.draw.rect(screen, (0, 255, 0), button_4, 2)
    pygame.draw.rect(screen, (0, 255, 0), button_3, 2)
    pygame.draw.rect(screen, (0, 255, 0), button_2, 2)
    pygame.draw.rect(screen, (0, 255, 0), button_1, 2)
    pygame.display.flip()

pygame.quit()
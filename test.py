import pygame

pygame.init()

calc_img = pygame.image.load("calcu.png")

width = calc_img.get_width()
height = calc_img.get_height()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Random Calculator game")
font = pygame.font.SysFont("Minecraftia", 40, bold=True)
display_text = ""

#this is for the positioning of the buttons
button_0 = pygame.Rect(70, 690, 55, 55)
button_9 = pygame.Rect(280, 600, 55,55)
button_8 = pygame.Rect(178, 600, 55, 55)
button_7 = pygame.Rect(70, 600, 55, 55)
button_6 = pygame.Rect(280, 515, 55, 55)
button_5 = pygame.Rect(178, 515, 55, 55)
button_4 = pygame.Rect(70, 515, 55, 55)
button_3 = pygame.Rect(280,425, 55, 55 )
button_2 = pygame.Rect(178, 425, 55, 55)
button_1 = pygame.Rect(70, 425, 55, 55)
button_C = pygame.Rect(280, 690, 55, 55)
button_iws = pygame.Rect(385, 690, 55, 55)

#THIS IS JUST THE LOOP FOR HOW THE BUTTONS WORK
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
                                                    display_text += "0"

                if button_9.collidepoint(mouse_pos):
                                                    print("You clicked the 9 button!")
                                                    display_text += "9"


                if button_8.collidepoint(mouse_pos):
                                    print("You clicked the 8 button!")
                                    display_text += "8"

                if button_7.collidepoint(mouse_pos):
                    print("You clicked the 7 button!")
                    display_text += "7"

                if button_6.collidepoint(mouse_pos):
                    print("You clicked the 6 button!")
                    display_text += "6"

                if button_5.collidepoint(mouse_pos):
                                        print("You clicked the 5 button!")
                                        display_text += "5"

                if button_4.collidepoint(mouse_pos):
                                        print("You clicked the 4 button!")
                                        display_text += "4"

                if button_3.collidepoint(mouse_pos):
                                        print("You clicked the 3 button!")
                                        display_text += "3"

                if button_2.collidepoint(mouse_pos):
                                        print("You clicked the 2 button!")
                                        display_text += "2"

                if button_1.collidepoint(mouse_pos):
                                        print("You clicked the 1 button!")
                                        display_text += "1"

                if button_C.collidepoint(mouse_pos):
                                        print("Cleared")

                if button_iws.collidepoint(mouse_pos):
                                        print("=")
                        

                



    screen.blit(calc_img, (0, 0))
  #THIS IS THE GREEN HITBOX
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
    pygame.draw.rect(screen, (0, 255, 0), button_C, 2)
    pygame.draw.rect(screen, (0, 255, 0), button_iws, 2)

    text_surface = font.render(display_text, True, (0, 255, 0))  
    screen.blit(text_surface, (80, 90))
    
    pygame.display.flip()

pygame.quit()

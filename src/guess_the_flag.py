import pygame
import random
#on initiation:
    #PRINTS guess the flag at top
    #PRINTS white type box that handles keyboard entry
    #chooses RANDOM COUNTRY (make sure a new random is not selected every frame )
    #PRINTS flag from asscoiated random selected country
    #prints guess 1: and draws guess/type box for input
    #player puts in guess input
        #if input.strip == country
            #win
        #if input.strip =/ country
            #print hint, then give next guess

#class typebox
    #pygame.draw.rect(screen, color2, (300 - 25, 300 - 25, 90, 30))


def main():
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Guess The Flag")
    resolution = (600, 800)
    screen = pygame.display.set_mode(resolution)
    font = pygame.font.SysFont("Arial", 36)
    flag = pygame.image.load('cambodia_flag.png')
    #randomchoice country
    running = True
    while running:
     for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
     color = pygame.Color("White")
     screen.fill(color)
     #title:
     text_surface = font.render('Guess The Flag!', True, (255, 0, 0))
     screen.blit(text_surface, (0,0))
     #draw flag from randomly selected country
     screen.blit(flag, (50,100))
     #draw type box class
     pygame.display.flip()
     if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            pygame.QUIT()
    pygame.quit()
   





if __name__ == "__main__":
    main()
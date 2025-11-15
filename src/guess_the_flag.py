import pygame

#first page(start of game)
    #print/draw "welcome to guess the flag!
    #draw START button
    #start button INITIATES random selection, as well as 
#second page (main game loop)
    #PRINTS flag from random selected country
    #prints guess 1: and draws guess/type box for input
    #player puts in guess input
        #if input.strip == country
            #win
        #if input.strip =/ country
            #print hint, then give next guess

def main():
    pygame.init()
    pygame.display.set_caption("Guess The Flag")
    resolution = (600, 600)
    screen = pygame.display.set_mode(resolution)
    running = True
    while running:
     for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
     color = pygame.Color("White")
     color2 = pygame.Color("Black")
     screen.fill(color)
     pygame.draw.rect(screen, color2, (300 - 25, 300 - 25, 90, 30))
     #if pygame.mouse.get_pos(300 - 25, 300 - 25, 90, 30):
          #pygame.mouse.get_pressed()
          #return False
     
     
     pygame.display.flip()
     if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            pygame.QUIT()
    pygame.quit()
   





if __name__ == "__main__":
    main()
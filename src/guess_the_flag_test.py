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
                    
def check_guess(guess, country):
    font = pygame.font.SysFont("Arial", 36)
    global game_state
    if guess.strip() == country:
        game_state = "win"

    else: 
        guess = ''

    

def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.font.init()
    font = pygame.font.SysFont("Arial", 36)
    user_text = ''
    type_rect = pygame.Rect(150,500, 300, 45)
    rect_color = (0,0,0)
    pygame.display.set_caption("Guess The Flag")
    resolution = (600, 800)
    screen = pygame.display.set_mode(resolution)
    flag = pygame.image.load('cambodia_flag.png')
    country = "cambodia"
    color = pygame.Color("White")
    global game_state
    game_state= "playing"
    running = True
    while running:
     for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text =  user_text[0:-1]
                else:
                    user_text += event.unicode
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    check_guess(user_text,country)

     if game_state == "playing":
   
            screen.fill(color)

            pygame.draw.rect(screen, rect_color, type_rect, 2)
            type_text = font.render(user_text, True,(0,0,0))
            screen.blit(type_text, (155,500))

     #return user_text to guess function

     #title:
            text_surface = font.render('Guess The Flag!', True, (255, 0, 0))
            screen.blit(text_surface, (200, 0))
     
     #draw flag from randomly selected country
            screen.blit(flag, (50,100))
     
     #draw type box class
            pygame.display.flip()


     if game_state == "win":
            screen.fill(color) 
            text_surface = font.render('Congratulations, you are smart', True, (0, 214, 0))
            screen.blit(text_surface, (70, 400))

            pygame.display.flip()
         
     clock.tick(12)
     if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            pygame.QUIT()
    pygame.quit()
   



if __name__ == "__main__":
    main()
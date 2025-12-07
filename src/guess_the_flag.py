import pygame
import random
import json
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
                    
def check_guess(guess, answer):
    font = pygame.font.SysFont("Arial", 36)
    global game_state
    if guess.strip() == answer:
        game_state = "win"
        return True
    else: 
        return False

def hint(hints, hint_index):
     #choose hint from list of hint
     #draw (hint)
     global screen
     
     font = pygame.font.SysFont("Arial", 30)
     hint_print = font.render(hints[hint_index], True, (255, 0, 0))
     screen.blit(hint_print, (20,550))
     
     pygame.display.flip()
     

def main():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.font.init()
    font = pygame.font.SysFont("Arial", 36)
    user_text = ''
    type_rect = pygame.Rect(150,500, 300, 45)
    rect_color = (0,0,0)
    pygame.display.set_caption("Guess The Flag")
    global screen 
    resolution = (600, 800)
    screen = pygame.display.set_mode(resolution)
    hint_count = 0

    with open("countries.json") as countries:
        country = json.load(countries)
        country_list = list(country.keys())
        answer = random.choice(country_list)
        flag = country[answer]["flag"]
        hints = country[answer]["hints"]
    hint_index = 0 

    flag_pic = pygame.image.load(flag)
    color = (255,255,255)
    screen.fill(color)
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
                    pygame.display.update()
                else:
                    user_text += event.unicode
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    correct = check_guess(user_text, answer)
                    if not correct:
                         user_text = ""
                         screen.fill(color)
                         pygame.draw.rect(screen, rect_color, type_rect, 2)
                         type_text = font.render(user_text, True,(0,0,0))
                         screen.blit(type_text, (155,500))
                         hint(hints, hint_index)
                         hint_count += 1
                         text_surface = font.render('Guess The Flag!', True, (255, 0, 0))
                         screen.blit(text_surface, (200, 25))
                         screen.blit(flag_pic, (50,100))
                         hint_index += 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if restart_butt.collidepoint(mouse):
                      game_state = "playing"
                      hint_count == 0
                      main()
                      print("poop")
                 
     if hint_count == 6:
        game_state = "fail"

     if game_state == "playing":
            
            pygame.draw.rect(screen, rect_color, type_rect, 4)
            type_text = font.render(user_text, True,(0,0,0))
            screen.blit(type_text, (155,500))
     #title:
            text_surface = font.render('Guess The Flag!', True, (255, 0, 0))
            screen.blit(text_surface, (200, 25))
     #draw flag
            screen.blit(flag_pic, (50,100))
            
            pygame.display.flip()

     if game_state == "win":
            screen.fill(color) 
            text_surface = font.render('Congratulations, you are smart!!!', True, (0, 214, 0))
            screen.blit(text_surface, (80, 300))
            
            
            restart_butt = pygame.draw.rect(screen,(45, 217, 45), type_rect,)
            pygame.draw.rect(screen,(0,0,0), type_rect, 4)
            restart_text = font.render('Play Again', True, (255,255,255))
            screen.blit(restart_text,(225,500))
            mouse = pygame.mouse.get_pos()
            restart_butt.collidepoint(mouse)
            mouse = pygame.mouse.get_pos()
            restart_butt.collidepoint(mouse)
            pygame.display.flip()
     if game_state == "fail":
            
            screen.fill(color) 
            fail_one = font.render('Oops! You loose!', True, (255, 0, 0))
            screen.blit(fail_one, (155, 300))
            
            restart_butt = pygame.draw.rect(screen,(45, 217, 45), type_rect,)
            pygame.draw.rect(screen,(0,0,0), type_rect, 4)
            restart_text = font.render('Play Again', True, (255,255,255))
            screen.blit(restart_text,(225,500))
            mouse = pygame.mouse.get_pos()
            restart_butt.collidepoint(mouse)
            mouse = pygame.mouse.get_pos()
            restart_butt.collidepoint(mouse)

            pygame.display.flip()
          
         
     clock.tick(12)
     if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            pygame.QUIT()
    pygame.quit()
   



if __name__ == "__main__":
    main()
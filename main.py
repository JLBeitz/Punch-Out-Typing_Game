# the game itself
import keylogger
import pygame
import randomWord

pygame.init()

#setting up the select screen
screen = pygame.display.set_mode([1280, 651])
pygame.display.set_caption('Punch-Out Typing')

imp = pygame.image.load('RetroPie_Super_PunchOut.png')
 
screen.blit(imp, (0,0))

pygame.display.flip()

running = True
while running:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False

pygame.quit()

# keylogger.keylog()

# yes = randomWord.random_word()
# print(yes.rand_word())
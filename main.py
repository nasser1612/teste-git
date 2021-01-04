import pygame, sys, random
from pygame.image import load
from pygame.locals import *
from classes import *
pygame.init()


# screen
CLOCK = pygame.time.Clock()
WINDOW_SIZE = (600, 400)
DISPLAY_SIZE = (600, 400)
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
display = pygame.Surface(DISPLAY_SIZE)
pygame.display.set_caption("Konosuba")
true_scroll = [0,0]

# map
TILE_SIZE = 32
grass_image = pygame.image.load("images/map/grass.png").convert_alpha()
grass_image = pygame.transform.scale(grass_image, (TILE_SIZE,TILE_SIZE))
dirt_image = pygame.image.load("images/map/dirt.png").convert_alpha()
dirt_image = pygame.transform.scale(dirt_image, (TILE_SIZE,TILE_SIZE))

llama_sprites = []
for c in range(1,10):
    image = pygame.image.load(f"images/gold_llama/sprite_{c}.png").convert_alpha()
    image = pygame.transform.scale(image, (52, 82))
    llama_sprites.append(image)

llama = Statue(150, 28, llama_sprites, 12, 200, 0)

def load_map(path):
    f = open(path + '.txt','r')
    data = f.read()
    f.close()
    data = data.split('\n')
    game_map = []
    for row in data:
        game_map.append(list(row))
    return game_map

game_map = load_map("map")

while True:
    CLOCK.tick(60)
    print(CLOCK.get_fps())
    display.fill((146,244,255))

    tile_rects = []
    y = 0
    for layer in game_map:
        x = 0
        for tile in layer:
            if tile == '1':
                display.blit(dirt_image,(x*TILE_SIZE,y*TILE_SIZE))
            if tile == '2':
                display.blit(grass_image,(x*TILE_SIZE,y*TILE_SIZE))
            if tile != '0':
                tile_rects.append(pygame.Rect(x*TILE_SIZE,y*TILE_SIZE,TILE_SIZE,TILE_SIZE))
            x += 1
        y += 1


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.LEFT_KEY = True
            if event.key == pygame.K_RIGHT:
                player.RIGHT_KEY = True
            if event.key == pygame.K_SPACE:
                player.SPACE_KEY = True
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.LEFT_KEY = False
            if event.key == pygame.K_RIGHT:
                player.RIGHT_KEY = False
            if event.key == pygame.K_SPACE:
                player.SPACE_KEY = False

    llama.update()
    llama.draw(display)


    surf = pygame.transform.scale(display,(WINDOW_SIZE[0], WINDOW_SIZE[1]))
    screen.blit(surf, (0,0))
    pygame.display.update()
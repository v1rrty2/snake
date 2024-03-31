import pygame
import random
from os import path
dis_width = 800
dis_height = 600
pygame.init()
dis = pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption("Змейка")
clock = pygame.time.Clock()
FPS = 5
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

snake_list =[]
x1 = dis_width / 2
y1 = dis_height / 2

snake_block = 30
snake_step = 30
x1_change = 0
y1_change = 0
length = 1

img_dir = path.join(path.dirname(__file__),'img')

am = pygame.mixer.Sound(path.join(img_dir,'carrot_chew_munch_001_28556.mp3'))
am.set_volume(0.5)

foodx = random.randrange(0, dis_width - snake_block)
foody = random.randrange(0, dis_height - snake_block)

food_img = [pygame.image.load(path.join(img_dir,'камень.png')).convert(),
            pygame.image.load(path.join(img_dir,'железо.png')).convert(),
            pygame.image.load(path.join(img_dir,'серка.png')).convert()]

food = pygame.transform.scale(random.choice(food_img),(50,50))
food.set_colorkey(white)
food.set_colorkey(black)
food_rect = food.get_rect(x = foodx, y = foody)


bg = pygame.image.load(path.join(img_dir,'Фон.png')).convert()
bg = pygame.transform.scale(bg,(dis_width, dis_height))
bg_rect = bg.get_rect()


def eating_check(xcor, ycor, foodx, foody):
    if foodx-snake_block <= xcor <= foodx+snake_block:
        if foody-snake_block <= ycor <= foody+snake_block:
            return True
    else:
        return False

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_step
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_step
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -snake_step
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = snake_step
                x1_change = 0

    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
        run = False
    x1 += x1_change
    y1 += y1_change

    dis.fill(blue)
    dis.blit(bg, bg_rect)
    dis.blit(food, food_rect)
    # pygame.draw.rect(dis,green,[foodx,foody,snake_block, snake_block])
    snake_head =[x1,y1]
    snake_list.append(snake_head)

    if len(snake_list) > length:
        del snake_list[0]

    for x in snake_list[:-1]:
        if x == snake_head:
            run = False

    for x in snake_list:
        pygame.draw.rect(dis,black,[x[0],x[1],snake_block,snake_block])

    pygame.display.update()

    if eating_check(x1, y1, foodx, foody):
        foodx = random.randrange(0, dis_width - snake_block)
        foody = random.randrange(0, dis_height - snake_block)
        food_img = [pygame.image.load(path.join(img_dir, 'камень.png')).convert(),
                    pygame.image.load(path.join(img_dir, 'железо.png')).convert(),
                    pygame.image.load(path.join(img_dir, 'серка.png')).convert()]

        food = pygame.transform.scale(random.choice(food_img), (50, 50))
        food.set_colorkey(white)
        food.set_colorkey(black)
        food_rect = food.get_rect(x=foodx, y=foody)
        length += 1
        am.play()
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
quit()
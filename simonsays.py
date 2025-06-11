import pygame
import random
import time

#Variables
screen_size = 600
black = (0, 0, 0)
green = (0, 255, 0)
dark_green = (0, 70, 0)
grey = (120, 120, 120)
white = (255, 255, 255)
colour0 = grey
colour1 = grey
colour2 = grey
colour3 = grey
colour4 = grey
colour5 = grey
colour6 = grey
colour7 = grey
colour8 = grey
delay = 1
square = screen_size / 7
slot = (screen_size / 3) - square * 0.85
pg = pygame
order = []

pg.init()
screen = pg.display.set_mode((screen_size, screen_size))
pg.display.set_caption("simon says")
clock = pg.time.Clock()

#Font
font = pygame.font.Font(None, 64)
win = font.render("You Win!", True, (255, 255, 255))
win_pos = win.get_rect(centerx=screen.get_width() / 2, y= (screen_size/15))
lose = font.render("You Lose!", True, (255, 255, 255))
lose_pos = lose.get_rect(centerx=screen.get_width() / 2, y= (screen_size/15))

gaming = False

def draw_rect(x, y, colour):
    pg.draw.rect(screen, colour, ((slot * x), (slot * y), square, square))
def colour_box(number, delay):
    global colour0
    global colour1
    global colour2
    global colour3
    global colour4
    global colour5
    global colour6
    global colour7
    global colour8
    if number == 0:
        colour0 = white
        draw_rect(1, 1, colour0)
        pg.display.flip()
        time.sleep(delay)
        colour0 = grey
        draw_rect(1, 1, colour0)
        pg.display.flip()
    elif number == 1:
        colour1 = white
        draw_rect(2, 1, colour1)
        pg.display.flip()
        time.sleep(delay)
        colour1 = grey
        draw_rect(2, 1, colour1)
        pg.display.flip()
    elif number == 2:
        colour2 = white
        draw_rect(3, 1, colour2)
        pg.display.flip()
        time.sleep(delay)
        colour2 = grey
        draw_rect(3, 1, colour2)
        pg.display.flip()
    elif number == 3:
        colour3 = white
        draw_rect(1, 2, colour3)
        pg.display.flip()
        time.sleep(delay)
        colour3 = grey
        draw_rect(1, 2, colour3)
        pg.display.flip()
    elif number == 4:
        colour4 = white
        draw_rect(2, 2, colour4)
        pg.display.flip()
        time.sleep(delay)
        colour4 = grey
        draw_rect(2, 2, colour4)
        pg.display.flip()
    elif number == 5:
        colour5 = white
        draw_rect(3, 2, colour5)
        pg.display.flip()
        time.sleep(delay)
        colour5 = grey
        draw_rect(3, 2, colour5)
        pg.display.flip()
    elif number == 6:
        colour6 = white
        draw_rect(1, 3, colour6)
        pg.display.flip()
        time.sleep(delay)
        colour6 = grey
        draw_rect(1, 3, colour6)
        pg.display.flip()
    elif number == 7:
        colour7 = white
        draw_rect(2, 3, colour7)
        pg.display.flip()
        time.sleep(delay)
        colour7 = grey
        draw_rect(2, 3, colour7)
        pg.display.flip()
    elif number == 8:
        colour8 = white
        draw_rect(3, 3, colour8)
        pg.display.flip()
        time.sleep(delay)
        colour8 = grey
        draw_rect(3, 3, colour8)
        pg.display.flip()
def appendnum(number):
    global gaming
    if gaming == True:
        if len(order) <= 3:
            order.append(number)
            print(order)
        else:
            order.append(number)
            print(order)
            if order == answers:
                print("correct")
                screen.blit(win, win_pos)
                pg.display.flip()
                gaming = False
                time.sleep(3)
            else:
                print("incorrect")
                screen.blit(lose, lose_pos)
                pg.display.flip()
                gaming = False
                time.sleep(3)

running = True
patterning = False

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button ==1:
                if patterning == False:
                    mouse_pos = event.pos
                    if hitbox0.collidepoint(mouse_pos):
                        colour_box(0, (delay/2))
                        print("hitbox number 0 has been clicked")
                        appendnum(0)
                    elif hitbox1.collidepoint(mouse_pos):
                        colour_box(1, (delay/2))
                        print("hitbox number 1 has been clicked")
                        appendnum(1)
                    elif hitbox2.collidepoint(mouse_pos):
                        colour_box(2, (delay/2))
                        print("hitbox number 2 has been clicked")
                        appendnum(2)
                    elif hitbox3.collidepoint(mouse_pos):
                        colour_box(3, (delay/2))
                        print("hitbox number 3 has been clicked")
                        appendnum(3)
                    elif hitbox4.collidepoint(mouse_pos):
                        colour_box(4, (delay/2))
                        print("hitbox number 4 has been clicked")
                        appendnum(4)
                    elif hitbox5.collidepoint(mouse_pos):
                        colour_box(5, (delay/2))
                        print("hitbox number 5 has been clicked")
                        appendnum(5)
                    elif hitbox6.collidepoint(mouse_pos):
                        colour_box(6, (delay/2))
                        print("hitbox number 6 has been clicked")
                        appendnum(6)
                    elif hitbox7.collidepoint(mouse_pos):
                        colour_box(7, (delay/2))
                        print("hitbox number 7 has been clicked")
                        appendnum(7)
                    elif hitbox8.collidepoint(mouse_pos):
                        colour_box(8, (delay/2))
                        print("hitbox number 8 has been clicked")
                        appendnum(8)
                    elif startbox.collidepoint(mouse_pos):
                        print("start has been clicked")
                        playing = True                        
                        patterning = True
                        num0 = random.randint(0, 8)
                        num1 = random.randint(0, 8)
                        num2 = random.randint(0, 8)
                        num3 = random.randint(0, 8)
                        num4 = random.randint(0, 8)
                        pg.draw.rect(screen, dark_green, ((slot * 2), (slot * 4), square, (square/3)))
                        pg.display.flip()
                        time.sleep(delay)
                        pg.draw.rect(screen, green, ((slot * 2), (slot * 4), square, (square/3)))
                        pg.display.flip()
                        time.sleep(delay)
                        colour_box(num0, delay)
                        time.sleep((delay/2))
                        colour_box(num1, delay)
                        time.sleep((delay/2))
                        colour_box(num2, delay)
                        time.sleep((delay/2))
                        colour_box(num3, delay)
                        time.sleep((delay/2))
                        colour_box(num4, delay)
                        patterning = False
                        answers = []
                        answers.append(num0)
                        answers.append(num1)
                        answers.append(num2)
                        answers.append(num3)
                        answers.append(num4)
                        order = []
                        gaming = True
                    else:
                        print("no button has been clicked")
                
                    
    screen.fill(black)
    
    draw_rect(1, 1, colour0)
    draw_rect(2, 1, colour1)
    draw_rect(3, 1, colour2)
    draw_rect(1, 2, colour3)
    draw_rect(2, 2, colour4)
    draw_rect(3, 2, colour5)
    draw_rect(1, 3, colour6)
    draw_rect(2, 3, colour7)
    draw_rect(3, 3, colour8)
    pg.draw.rect(screen, green, ((slot * 2), (slot * 4), square, (square/3)))
    
    hitbox0 = pg.Rect(((slot * 1), (slot * 1), square, square))
    hitbox1 = pg.Rect(((slot * 2), (slot * 1), square, square))
    hitbox2 = pg.Rect(((slot * 3), (slot * 1), square, square))
    hitbox3 = pg.Rect(((slot * 1), (slot * 2), square, square))
    hitbox4 = pg.Rect(((slot * 2), (slot * 2), square, square))
    hitbox5 = pg.Rect(((slot * 3), (slot * 2), square, square))
    hitbox6 = pg.Rect(((slot * 1), (slot * 3), square, square))
    hitbox7 = pg.Rect(((slot * 2), (slot * 3), square, square))
    hitbox8 = pg.Rect(((slot * 3), (slot * 3), square, square))
    startbox = pg.Rect(((slot * 2), (slot * 4), square, (square/3)))

    pg.display.flip()
pygame.quit()
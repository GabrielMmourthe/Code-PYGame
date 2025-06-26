import pygame
import random
import sys

pygame.init()

#informacoes
font = pygame.font.SysFont("Lato", 45, True, True)
font2 = pygame.font.SysFont("Lato", 50, True, True)
font3 = pygame.font.SysFont("Arial", 30, True, True)
text_color = (200, 0, 0) #vermelho 
text_color2 = (0,0,0) #preto
text_color3 = (255,255,255) #branco
text_color4 = (0, 238, 255) #azul claro
text_color5 = (43, 255, 0) #verde

#Definicao de Texturas

    #menu
Menu = pygame.image.load('Menu/menu.png')

MenuBotao1 = pygame.image.load('Menu/botaoplay.png')
MenuBotao2 = pygame.image.load('Menu/botaocreditos.png')
MenuBotao3 = pygame.image.load('Menu/botaosaida.png')
MenuBotao4 = pygame.image.load('Menu/botaoback.png')

MenuBotao1 = pygame.transform.scale (MenuBotao1, (150,150))
MenuBotao2 = pygame.transform.scale (MenuBotao2, (150,150))
MenuBotao3 = pygame.transform.scale (MenuBotao3, (150,150))
MenuBotao4 = pygame.transform.scale (MenuBotao4, (150,150))
    #personages
PersonagemTextura1 = pygame.image.load('Sprites/Personagem1.png')
PersonagemTextura2 = pygame.image.load('Sprites/Personagem2.png')
    #bombas
bomba1 = pygame.image.load('Sprites/Bomba0.png')
bomba2 = pygame.image.load('Sprites/Bomba0.png')


    #mapa
Mapa = pygame.image.load('Map/Map.png')

    #vida
coracao = pygame.image.load('Sprites/coracao.png')     

#caixa
block_size = 50
box_rect = pygame.Rect((100, 100), (45, block_size))
# Caixa
box_positions = [
    (100, 100),
    (200, 100),
    (300, 100),
    (100, 200),
    (200, 200),
    (300, 200),
    (100, 300),
    (200, 300),
    (300, 300),
    (400, 100),
    (100, 400),
    (400, 200),
    (200, 400),
    (300, 400),
    (400, 300),
    (400, 400)
]

#adicionar caixas com posições fixas
boxes = [pygame.Rect(x, y, 45, block_size) for x, y in box_positions]

#range da explosao 

def get_explosion_range(bomb_x, bomb_y, walls):
    #converte a posicao da bomba para o grid de 11x11
    grid_x = bomb_x // 50
    grid_y = bomb_y // 50

    #tamanhos maximo para a explosao
    max_up = grid_y - 1
    max_down = 11 - grid_y - 2
    max_left = grid_x - 1
    max_right = 11 - grid_x - 2

    #verifica a quantidade de blocos disponiveis em cada direção
    up_range = 0
    for i in range(1, max_up + 1):
        if (grid_x, grid_y - i) in walls:
            break
        up_range += 1

    down_range = 0
    for i in range(1, max_down + 1):
        if (grid_x, grid_y + i) in walls:
            break
        down_range += 1

    left_range = 0
    for i in range(1, max_left + 1):
        if (grid_x - i, grid_y) in walls:
            break
        left_range += 1

    right_range = 0
    for i in range(1, max_right + 1):
        if (grid_x + i, grid_y) in walls:
            break
        right_range += 1

    return up_range, down_range, left_range, right_range

#range da explosao player2

def get_explosion_range_player2(bomb_x, bomb_y, walls):
    #converte a posição da bomba para o grid
    grid_x = bomb_x // 50
    grid_y = bomb_y // 50

    #tamanhos maximos para a explosão considerando 11x11 grid
    max_up = grid_y - 1
    max_down = 11 - grid_y - 2
    max_left = grid_x - 1
    max_right = 11 - grid_x - 2

    #verifica a quantidade de blocos disponíveis em cada direção
    up_range = 0
    for i in range(1, max_up + 1):
        if (grid_x, grid_y - i) in walls:
            break
        up_range += 1

    down_range = 0
    for i in range(1, max_down + 1):
        if (grid_x, grid_y + i) in walls:
            break
        down_range += 1

    left_range = 0
    for i in range(1, max_left + 1):
        if (grid_x - i, grid_y) in walls:
            break
        left_range += 1

    right_range = 0
    for i in range(1, max_right + 1):
        if (grid_x + i, grid_y) in walls:
            break
        right_range += 1

    #retorna o alcance da explosão nas quatro direções
    return {'up': up_range, 'down': down_range, 'left': left_range, 'right': right_range}

#definicao de pareda para o range da bomba

#definindo as paredes
walls = set()

for i in range(11):
    walls.add((i, 0))    #parede superior
    walls.add((i, 10))   #parede inferior
    walls.add((0, i))    #parede esquerda
    walls.add((10, i))   #parede direita

#blocos internos do mapa
    #fileira 1
walls.add((2, 2))
walls.add((2, 4))
walls.add((2, 6))
walls.add((2, 8))
    #fileira 2
walls.add((4, 2))
walls.add((4, 4))
walls.add((4, 6))
walls.add((4, 8))
    #fileira 3
walls.add((6, 2))
walls.add((6, 4))
walls.add((6, 6))
walls.add((6, 8))
    #fileira 4
walls.add((8, 2))
walls.add((8, 4))
walls.add((8, 6))
walls.add((8, 8))


#escala do personage
Personagem1 = pygame.transform.scale (PersonagemTextura1, (40,40))

Personagem2 = pygame.transform.scale (PersonagemTextura2, (40,40))

#Variaveis

animacaoperativa1 = 0
animacaoperativa2 = 0
animacaopersonagem1 = 0
animacaopersonagem2 = 0

localexplosao = 0
localexplosao2 = 0
iniciarbomba2 = 0
iniciarbomba1 = 0
bomba1time = 0
bomba2time = 0
bomba1ativa = 0
bomba2ativa = 0

danoplayer1 = 0
danoplayer2 = 0
timerdamege1 = 0
timerdamege2 = 0
danotimer1 = 0
danotimer2 = 0

Timetrigger = 0
TimeT = 0
Timetrigger2 = 0
TimeT2 = 0

creditos = 0

menuanimacao = 0
menutempoani = 0

MenuTimer = 0
Tempomenu = 0
Menupage = 0

Inicio = 0

Vidas = 3
Vidas2 = 3

Velocity = 2

Xscreen = 550
Yscreen = 550

trigger1 = 0
trigger2 = 0

correcao1 = 0
correcao2 = 0

#spawn
spawn2 = random.randint(1, 3)

spawn1 = random.randint(1, 3)

if spawn1 == 1:
    Xlocal = 55
    Ylocal = 55
if spawn1 == 2:
    Xlocal = 55
    Ylocal = 255   
if spawn1 == 3:
    Xlocal = 55 
    Ylocal = 455

if spawn2 == 1:
    Xlocal2 = 455
    Ylocal2 = 55
if spawn2 == 2:
    Xlocal2 = 455
    Ylocal2 = 255   
if spawn2 == 3:
    Xlocal2 = 455
    Ylocal2 = 455

#colicao

def handle_collision(rect, x_movement, y_movement, boxes):
    
    temp_rect = rect.move(x_movement, 0)
    for box in boxes:
        if temp_rect.colliderect(box):
            if x_movement > 0:  #movimento para a direita
                temp_rect.right = box.left
            elif x_movement < 0:  #movimento para a esquerda
                temp_rect.left = box.right
            x_movement = 0
            break

    temp_rect = rect.move(0, y_movement)
    for box in boxes:
        if temp_rect.colliderect(box):
            if y_movement > 0:  #movimento para baixo
                temp_rect.bottom = box.top
            elif y_movement < 0:  #movimento para cima
                temp_rect.top = box.bottom
            y_movement = 0
            break

    return x_movement, y_movement



sprite_center = pygame.image.load('explosao/explosao1.png')
sprite_middle = pygame.image.load('explosao/explosao2.png')
sprite_end = pygame.image.load('explosao/explosao3.png')

sprite_middle_up = pygame.transform.rotate(sprite_middle, 90)  
sprite_middle_down = pygame.transform.rotate(sprite_middle, -90)  

sprite_end_up = pygame.transform.rotate(sprite_end, 90)  
sprite_end_down = pygame.transform.rotate(sprite_end, -90)  

sprite_middle_left = pygame.transform.flip(sprite_middle, True, False)  
sprite_end_left = pygame.transform.flip(sprite_end, True, False)  


def draw_sprite(x, y, sprite):
    Screen.blit(sprite, (x, y))

def create_explosion(center_x, center_y, explosion_range):
    
    draw_sprite(center_x, center_y, sprite_center)

    def draw_explosion_in_direction(direction, explosion_length):
        for i in range(1, explosion_length + 1):
            if direction == 'up':
                new_x, new_y = center_x, center_y - i * 50
                if i == explosion_length:
                    draw_sprite(new_x, new_y, sprite_end_up)
                else:
                    draw_sprite(new_x, new_y, sprite_middle_up)
            elif direction == 'down':
                new_x, new_y = center_x, center_y + i * 50
                if i == explosion_length:
                    draw_sprite(new_x, new_y, sprite_end_down)
                else:
                    draw_sprite(new_x, new_y, sprite_middle_down)
            elif direction == 'left':
                new_x, new_y = center_x - i * 50, center_y
                if i == explosion_length:
                    draw_sprite(new_x, new_y, sprite_end_left)
                else:
                    draw_sprite(new_x, new_y, sprite_middle_left)
            elif direction == 'right':
                new_x, new_y = center_x + i * 50, center_y
                if i == explosion_length:
                    draw_sprite(new_x, new_y, sprite_end)
                else:
                    draw_sprite(new_x, new_y, sprite_middle)

    #desenhar a explosão nas quatro direções para o player 1
    draw_explosion_in_direction('up', explosion_range['up'])
    draw_explosion_in_direction('down', explosion_range['down'])
    draw_explosion_in_direction('left', explosion_range['left'])
    draw_explosion_in_direction('right', explosion_range['right'])

    #textura player 2

def create_explosion_player2(center_x, center_y, explosion_range_player2):
    #mostrar a textura na tela
    def draw_sprite(x, y, sprite, angle=0):
        rotated_sprite = pygame.transform.rotate(sprite, angle)
        Screen.blit(rotated_sprite, (x, y))

    #desenhar o centro da explosão
    draw_sprite(center_x, center_y, sprite_center)

    def draw_explosion_in_direction(direction, explosion_length):
        for i in range(1, explosion_length + 1):
            if direction == 'up':
                new_x, new_y = center_x, center_y - i * 50
                if i == explosion_length:
                    draw_sprite(new_x, new_y, sprite_end_up)
                else:
                    draw_sprite(new_x, new_y, sprite_middle_up)
            elif direction == 'down':
                new_x, new_y = center_x, center_y + i * 50
                if i == explosion_length:
                    draw_sprite(new_x, new_y, sprite_end_down)
                else:
                    draw_sprite(new_x, new_y, sprite_middle_down)
            elif direction == 'left':
                new_x, new_y = center_x - i * 50, center_y
                if i == explosion_length:
                    draw_sprite(new_x, new_y, sprite_end_left)
                else:
                    draw_sprite(new_x, new_y, sprite_middle_left)
            elif direction == 'right':
                new_x, new_y = center_x + i * 50, center_y
                if i == explosion_length:
                    draw_sprite(new_x, new_y, sprite_end)
                else:
                    draw_sprite(new_x, new_y, sprite_middle)

    #desenhar a explosão nas quatro direções para o player 2
    draw_explosion_in_direction('up', explosion_range_player2['up'])
    draw_explosion_in_direction('down', explosion_range_player2['down'])
    draw_explosion_in_direction('left', explosion_range_player2['left'])
    draw_explosion_in_direction('right', explosion_range_player2['right'])

    #definicao de explosao
BombaExplosao = False
BombaExplosao_Player2 = False
explosion_timer = 0
explosion_timer_player2 = 0
explosion_duration = 500

#spawn da bomba

Xlocalb = Xlocal
Ylocalb = Ylocal

Xlocalb2 = Xlocal2
Ylocalb2 = Ylocal2

#definir o dano da explosao

def check_player_in_explosion(player_x, player_y, explosion_range, bomb_x, bomb_y):
    
    grid_bomb_x, grid_bomb_y = bomb_x // 50, bomb_y // 50
    grid_player_x, grid_player_y = player_x // 50, player_y // 50
    
    if (grid_player_x == grid_bomb_x and grid_bomb_y - explosion_range['up'] <= grid_player_y <= grid_bomb_y) or \
       (grid_player_x == grid_bomb_x and grid_bomb_y <= grid_player_y <= grid_bomb_y + explosion_range['down']) or \
       (grid_player_y == grid_bomb_y and grid_bomb_x - explosion_range['left'] <= grid_player_x <= grid_bomb_x) or \
       (grid_player_y == grid_bomb_y and grid_bomb_x <= grid_player_x <= grid_bomb_x + explosion_range['right']):
        return True
    return False

Screen = pygame.display.set_mode((Xscreen, Yscreen))
pygame.display.set_caption("JogoBolivar BomberMan")

Screen_Open = True
while Screen_Open :

    pygame.time.delay(10)

    for event in pygame.event.get ():
        if event.type == pygame.QUIT:
            Screen_Open = False 
    
    Commands = pygame.key.get_pressed()

    #redefinir animacao
    animacaoperativa1 = 0
    animacaoperativa2 = 0

    #colicoes
    X_temp, Y_temp = 0, 0
    if Inicio == 1:
    
        if Commands[pygame.K_w]:
            Y_temp = -Velocity
            animacaopersonagem1 += 3
            animacaoperativa1 = 1
        if Commands[pygame.K_s]:
            Y_temp = Velocity
            animacaopersonagem1 += 3
            animacaoperativa1 = 1
        if Commands[pygame.K_a]:
            X_temp = -Velocity
            animacaopersonagem1 += 3
            animacaoperativa1 = 1
        if Commands[pygame.K_d]:
            X_temp = Velocity
            animacaopersonagem1 += 3
            animacaoperativa1 = 1

    # Temporário para verificar colisões
    temp_rect1 = pygame.Rect(Xlocal, Ylocal, 35, 40)
    X_temp, Y_temp = handle_collision(temp_rect1, X_temp, Y_temp, boxes)
    # Atualizar a posição do personagem 1
    Xlocal += X_temp
    Ylocal += Y_temp

    X_temp2, Y_temp2 = 0, 0
    if Inicio == 1:
        
        if Commands[pygame.K_UP]:
            Y_temp2 = -Velocity
            animacaopersonagem2 += 3
            animacaoperativa2 = 1        
        if Commands[pygame.K_DOWN]:
            Y_temp2 = Velocity
            animacaopersonagem2 += 3
            animacaoperativa2 = 1
        if Commands[pygame.K_LEFT]:
            X_temp2 = -Velocity
            animacaopersonagem2 += 3
            animacaoperativa2 = 1
        if Commands[pygame.K_RIGHT]:
            X_temp2 = Velocity
            animacaopersonagem2 += 3
            animacaoperativa2 = 1

    # Temporário para verificar colisões
    temp_rect2 = pygame.Rect(Xlocal2, Ylocal2, 35, 40)
    X_temp2, Y_temp2 = handle_collision(temp_rect2, X_temp2, Y_temp2, boxes)


    # Atualizar a posição do personagem 2
    Xlocal2 += X_temp2
    Ylocal2 += Y_temp2

        #personagem 1
            #parede da esquerda
    if Xlocal<= 43:
        if Ylocal>=0:
            if Ylocal<=550:
                if Xlocal>=40:
                    Xlocal+= 2
            #parede da esquerda
    if Xlocal>= 467:
        if Ylocal>=0:
            if Ylocal<=550:
                if Xlocal<=470:
                    Xlocal-= 2
            #chao cima
    if Xlocal>= 0:
        if Ylocal<=49:
            if Ylocal>=40:
                if Xlocal<=550:
                    Ylocal+= 2
            #chao baixo
    if Xlocal>= 0:
        if Ylocal>=460:
            if Ylocal<=470:
                if Xlocal<=550:
                    Ylocal-= 2                                            

        #personagem 2
            #parede da esquerda
    if Xlocal2<= 43:
        if Ylocal2>=0:
            if Ylocal2<=550:
                if Xlocal2>=40:
                    Xlocal2+= 2   
            #parede da direita
    if Xlocal2>= 467:
        if Ylocal2>=0:
            if Ylocal2<=550:
                if Xlocal2<=470:
                    Xlocal2-= 2                    
            #chao cima
    if Xlocal2>= 0:
        if Ylocal2<=49:
            if Ylocal2>=40:
                if Xlocal2<=550:
                    Ylocal2+= 2
            #chao baixo
    if Xlocal2>= 0:
        if Ylocal2>=460:
            if Ylocal2<=470:
                if Xlocal2<=550:
                    Ylocal2-= 2   

    #inicio do jogo    
    if Inicio == 2:
        #personagem1
        if Commands[pygame.K_w]:
            Ylocal-= Velocity 
            animacaopersonagem1 += 1
            animacaoperativa1 = 1

        if Commands[pygame.K_s]:
            Ylocal+= Velocity
            animacaopersonagem1 += 1
            animacaoperativa1 = 1

        if Commands[pygame.K_a]:
            Xlocal-= Velocity
            animacaopersonagem1 += 1
            animacaoperativa1 = 1

        if Commands[pygame.K_d]:
            Xlocal+= Velocity
            animacaopersonagem1 += 1
            animacaoperativa1 = 1

            #animacao do personagem 1
    
    if animacaoperativa1 == 0:
        PersonagemTextura1 = pygame.image.load('Sprites/Personagem1.png')
        Personagem1 = pygame.transform.scale (PersonagemTextura1, (40,40))

    if animacaoperativa1 == 1:
        if animacaopersonagem1 >= 25:
            PersonagemTextura1 = pygame.image.load('Sprites/Personagem1.1.png')
            Personagem1 = pygame.transform.scale (PersonagemTextura1, (40,40))

        if animacaopersonagem1 >= 50:
            PersonagemTextura1 = pygame.image.load('Sprites/Personagem1.2.png')
            Personagem1 = pygame.transform.scale (PersonagemTextura1, (40,40))

        if animacaopersonagem1 >= 75:
            PersonagemTextura1 = pygame.image.load('Sprites/Personagem1.3.png')
            Personagem1 = pygame.transform.scale (PersonagemTextura1, (40,40))

        if animacaopersonagem1 >= 100:
            PersonagemTextura1 = pygame.image.load('Sprites/Personagem1.4.png')
            Personagem1 = pygame.transform.scale (PersonagemTextura1, (40,40))
            animacaopersonagem1 = 0

            #animacao do personagem 2

    if animacaoperativa2 == 0:
        PersonagemTextura2 = pygame.image.load('Sprites/Personagem2.png')
        Personagem2 = pygame.transform.scale (PersonagemTextura2, (40,40))

    if animacaoperativa2 == 1:
        if animacaopersonagem2 >= 25:
            PersonagemTextura2 = pygame.image.load('Sprites/Personagem2.1.png')
            Personagem2 = pygame.transform.scale (PersonagemTextura2, (40,40))

        if animacaopersonagem2 >= 50:
            PersonagemTextura2 = pygame.image.load('Sprites/Personagem2.2.png')
            Personagem2 = pygame.transform.scale (PersonagemTextura2, (40,40))

        if animacaopersonagem2 >= 75:
            PersonagemTextura2 = pygame.image.load('Sprites/Personagem2.3.png')
            Personagem2 = pygame.transform.scale (PersonagemTextura2, (40,40))

        if animacaopersonagem2 >= 100:
            PersonagemTextura2 = pygame.image.load('Sprites/Personagem2.4.png')
            Personagem2 = pygame.transform.scale (PersonagemTextura2, (40,40))
            animacaopersonagem2 = 0

        if Inicio == 2: #personagem2
            if Commands[pygame.K_UP]:
                Ylocal2-= Velocity 

            if Commands[pygame.K_DOWN]:
                Ylocal2+= Velocity

            if Commands[pygame.K_LEFT]:
                Xlocal2-= Velocity

            if Commands[pygame.K_RIGHT]:
                Xlocal2+= Velocity

    #menu

    #exibicao do menu

    if Inicio == 0:

        Screen.blit(Menu,(0,0))   

        if creditos == 0:
            Screen.blit(MenuBotao1,(198,154))              
            Screen.blit(MenuBotao2,(198,254))   
            Screen.blit(MenuBotao3,(198,354))
        if creditos == 1:
            Screen.blit(MenuBotao4,(198,354))
            CreditosIntro = font3.render(f'Criado Por:', False, text_color5)
            Creditosnome1 = font3.render(f'Gabriel Meirelles', False, text_color3) 
            Creditosnome2 = font3.render(f'Lucas Eduardo', False, text_color3) 
            Creditosprog = font3.render(f'Programador:', False, text_color) 
            Creditosdesig = font3.render(f'Designer:', False, text_color4) 
            Screen.blit(CreditosIntro, (193, 50))
            Screen.blit(Creditosnome1, (150, 85))
            Screen.blit(Creditosnome2, (165, 115))
            Screen.blit(Creditosprog, (175, 150))
            Screen.blit(Creditosnome1, (150, 185))
            Screen.blit(Creditosdesig, (202, 225))
            Screen.blit(Creditosnome1, (150, 265))
            Screen.blit(Creditosnome2, (165, 295))
    #selecao de menu

    if Menupage == 0:
        if MenuTimer == 0:
            if Commands[pygame.K_DOWN]:
                menuanimacao = 1
                MenuTimer = 1
                Menupage = 1
                MenuBotao1 = pygame.image.load('Menu/botaoplay2.png')
                MenuBotao1 = pygame.transform.scale (MenuBotao1, (150,150))
                


    if Menupage == 1:
        if menuanimacao == 1:
            menutempoani += 10
            if menutempoani <= 400:
                MenuBotao1 = pygame.image.load('Menu/botaoplay2.png')
                MenuBotao1 = pygame.transform.scale (MenuBotao1, (150,150))
            if menutempoani >= 400:
                MenuBotao1 = pygame.image.load('Menu/botaoplay.png')
                MenuBotao1 = pygame.transform.scale (MenuBotao1, (150,150))
            if menutempoani >= 800:
                menutempoani = 0

        if Commands[pygame.K_SPACE]:
            Inicio = 1
            Menupage = 10

        if MenuTimer == 0:
            if Commands[pygame.K_DOWN]:
                menutempoani = 0
                MenuTimer = 1
                Menupage = 2
                MenuBotao1 = pygame.image.load('Menu/botaoplay.png')
                MenuBotao1 = pygame.transform.scale (MenuBotao1, (150,150))
                MenuBotao2 = pygame.image.load('Menu/botaocreditos2.png')
                MenuBotao2 = pygame.transform.scale (MenuBotao2, (150,150))



    if Menupage == 2:
        if menuanimacao == 1:
            menutempoani += 10
            if menutempoani <= 400:
                MenuBotao2 = pygame.image.load('Menu/botaocreditos2.png')
                MenuBotao2 = pygame.transform.scale (MenuBotao2, (150,150))
            if menutempoani >= 400:
                MenuBotao2 = pygame.image.load('Menu/botaocreditos.png')
                MenuBotao2 = pygame.transform.scale (MenuBotao2, (150,150))
            if menutempoani >= 800:
                menutempoani = 0

        if Commands[pygame.K_SPACE]:
            creditos = 1
            Menupage = 4
            MenuBotao2 = pygame.image.load('Menu/botaocreditos.png')
            MenuBotao2 = pygame.transform.scale (MenuBotao2, (150,150))

        if MenuTimer == 0:
            if Commands[pygame.K_DOWN]:
                menutempoani = 0
                Menupage = 3
                MenuTimer = 1
                MenuBotao2 = pygame.image.load('Menu/botaocreditos.png')
                MenuBotao2 = pygame.transform.scale (MenuBotao2, (150,150))
                MenuBotao3 = pygame.image.load('Menu/botaosaida2.png')
                MenuBotao3 = pygame.transform.scale (MenuBotao3, (150,150))
            if Commands[pygame.K_UP]:
                menutempoani = 0
                Menupage = 1
                MenuTimer = 1
                MenuBotao1 = pygame.image.load('Menu/botaoplay2.png')
                MenuBotao1 = pygame.transform.scale (MenuBotao1, (150,150))
                MenuBotao2 = pygame.image.load('Menu/botaocreditos.png')
                MenuBotao2 = pygame.transform.scale (MenuBotao2, (150,150))        



    if Menupage == 3:
        if menuanimacao == 1:
            menutempoani += 10
            if menutempoani <= 400:
                MenuBotao3 = pygame.image.load('Menu/botaosaida2.png')
                MenuBotao3 = pygame.transform.scale (MenuBotao3, (150,150))
            if menutempoani >= 400:
                MenuBotao3 = pygame.image.load('Menu/botaosaida.png')
                MenuBotao3 = pygame.transform.scale (MenuBotao3, (150,150))
            if menutempoani >= 800:
                menutempoani = 0

        if Commands[pygame.K_UP]:
            menutempoani = 0
            Menupage = 2
            MenuTimer = 1
            MenuBotao2 = pygame.image.load('Menu/botaocreditos2.png')
            MenuBotao2 = pygame.transform.scale (MenuBotao2, (150,150))
            MenuBotao3 = pygame.image.load('Menu/botaosaida.png')
            MenuBotao3 = pygame.transform.scale (MenuBotao3, (150,150))
        if Commands[pygame.K_SPACE]:
            Screen_Open = False     

    if Menupage == 4:
        if MenuTimer == 0:
            if Commands[pygame.K_DOWN]:
                menuanimacao = 1
                menutempoani = 0
                Menupage = 5
                MenuBotao4= pygame.image.load('Menu/botaoback.png')
                MenuBotao4 = pygame.transform.scale (MenuBotao4, (150,150)) 

    if Menupage == 5:
        if menuanimacao == 1:
            menutempoani += 10
            if menutempoani <= 400:
                MenuBotao4 = pygame.image.load('Menu/botaoback2.png')
                MenuBotao4 = pygame.transform.scale (MenuBotao4, (150,150))
            if menutempoani >= 400:
                MenuBotao4 = pygame.image.load('Menu/botaoback.png')
                MenuBotao4 = pygame.transform.scale (MenuBotao4, (150,150))
            if menutempoani >= 800:
                menutempoani = 0
        if Commands[pygame.K_SPACE]:
            Menupage = 0
            creditos = 0
            MenuBotao4 = pygame.image.load('Menu/botaoback.png')
            MenuBotao4 = pygame.transform.scale (MenuBotao4, (150,150))

    #timer do menu

    if MenuTimer == 1:
       Tempomenu+= 10
       if Tempomenu >= 150:
           MenuTimer = 0
           Tempomenu = 0


    #mapa
    if Inicio == 1:
        Screen.blit(Mapa,(0,0))


    #definicao de spawn da bomba do jogador 1
    def get_square(Xlocalb, Ylocalb):
        if 40 <= Xlocalb < 500 and 40 <= Ylocalb < 500:

            coluna = (Xlocalb - 25) // 50

            row = (Ylocalb - 25) // 50

            local = row * 9 + coluna + 1

            return local

    local = get_square(Xlocalb, Ylocalb)

    def get_spawn_coordinates(local):

        row = (local - 1) // 9
        column = (local - 1) % 9
    
        spawn_x = 50 + column * 50
        spawn_y = 50 + row * 50
    
        return spawn_x, spawn_y

    current_square = get_square(Xlocalb, Ylocalb)
    spawn_x, spawn_y = get_spawn_coordinates(current_square)

    #definicao do spawn da bomba do jogador 2
    def get_square(Xlocalb2, Ylocalb2):
        if 40 <= Xlocalb2 < 500 and 40 <= Ylocalb2 < 500:

            coluna = (Xlocalb2 - 25) // 50

            row = (Ylocalb2 - 25) // 50

            local2 = row * 9 + coluna + 1

            return local2

    local2 = get_square(Xlocalb2, Ylocalb2)

    def get_spawn_coordinates(local2):

        row = (local2 - 1) // 9
        column = (local2 - 1) % 9
    
        spawn_x2 = 50 + column * 50
        spawn_y2 = 50 + row * 50
    
        return spawn_x2, spawn_y2

    current_square = get_square(Xlocalb2, Ylocalb2)
    spawn_x2, spawn_y2 = get_spawn_coordinates(current_square)

    #bomba

    if  Inicio == 1:

        if trigger1 == 0:
            Xlocalb = Xlocal
            Ylocalb = Ylocal

        if trigger2 == 0:
            Xlocalb2 = Xlocal2
            Ylocalb2 = Ylocal2


        if correcao1 == 1:
            correcao1 = 0
            bomba1 = pygame.image.load('Sprites/Bomba.png')
            bomba1 = pygame.transform.scale (bomba1, (48,48))    

        if correcao2 == 1:
            correcao2 = 0
            bomba2 = pygame.image.load('Sprites/Bomba.png')
            bomba2 = pygame.transform.scale (bomba2, (48,48))   

    if Inicio == 1:
        # tempo para a bomba explodir
        if bomba1ativa == 1:
            bomba1time += 1
            if bomba1time >= 100:
                bomba1ativa = 0
                bomba1time = 0
                bomba1 = pygame.image.load('Sprites/Bomba0.png')
                iniciarbomba1 = 1

        if bomba2ativa == 1:  
            bomba2time += 1
            if bomba2time >= 100:
                bomba2ativa =0
                bomba2time = 0
                bomba2 = pygame.image.load('Sprites/Bomba0.png')
                iniciarbomba2 = 1

        if trigger1 == 0:
            if Commands[pygame.K_g]:
                localexplosao = 1
                trigger1 = 1
                bomba1ativa = 1
                correcao1 = 1

        if trigger2 == 0:
            if Commands[pygame.K_BACKSPACE]:
                localexplosao2 = 1
                bomba2ativa = 1
                trigger2 = 1
                correcao2 = 1

    #range da explosao
    bomb_x = Xlocal + 25
    bomb_y = Ylocal + 25

    bomb_x2 = Xlocal2 + 25
    bomb_y2 = Ylocal2 + 25
    
    #alcance da bomba
    up, down, left, right = get_explosion_range(bomb_x, bomb_y, walls)

    up2, down2, left2, right2 = get_explosion_range_player2(bomb_x2, bomb_y2, walls)

    MostraEstatisticaDeRange = 0
    if MostraEstatisticaDeRange == 1:
        alcance = font.render(f'up:{up},down:{down},esquerda:{left},direita:{right}', False, text_color3)
        Screen.blit(alcance, (0, 50))

    #sprites da bomba

    if iniciarbomba1 == 1:
        BombaExplosao = True
        explosion_timer = pygame.time.get_ticks()
        iniciarbomba1 = 0

    if iniciarbomba2 == 1:
        BombaExplosao_Player2 = True
        explosion_timer_player2 = pygame.time.get_ticks()
        iniciarbomba2 = 0

    #bomba player 1

    bomb_position = (spawn_x, spawn_y)

    #bomba player 2

    bomb_position_player2 = (spawn_x2, spawn_y2)

    if localexplosao == 0:
        explosion_range = {
        'up': up,
        'down': down,
        'left': left,
        'right': right
        }

    #verificar se a bomba explodiu
    if BombaExplosao:
        current_time = pygame.time.get_ticks()
        if current_time - explosion_timer <= explosion_duration:
            # Renderizar a explosão
            create_explosion(bomb_position[0], bomb_position[1], explosion_range)
        else:
            # Reseta a explosão depois que o tempo acabar
            BombaExplosao = False
            Timetrigger = 1
            localexplosao = 0

    if Timetrigger == 1:
        TimeT += 1
        if TimeT == 10:
            trigger1 = 0
            Timetrigger = 0
            TimeT = 0

    if Timetrigger2 == 1:
        TimeT2 += 1
        if TimeT2 == 10:
            trigger2 = 0
            Timetrigger2 = 0
            TimeT2 = 0

    # Verificar se a bomba do Player 2 explodiu
    if BombaExplosao_Player2:
        current_time = pygame.time.get_ticks()
        if current_time - explosion_timer_player2 <= explosion_duration:
            # Calcular o intervalo da explosão para o Player 2
            explosion_range_player2 = get_explosion_range_player2(bomb_position_player2[0], bomb_position_player2[1], walls)
            # Renderizar a explosão do Player 2
            create_explosion_player2(bomb_position_player2[0], bomb_position_player2[1], explosion_range_player2)
        else:
            # Reseta a explosão depois que o tempo acabar
            BombaExplosao_Player2 = False
            Timetrigger2 = 1
            localexplosao2 = 0

    if localexplosao2 == 0:
        explosion_range_player2 = {
        'up': up2,
        'down': down2,
        'left': left2,
        'right': right2
        }

    #dano da explosao da bomba para todos os player

    if BombaExplosao:
    
        if danoplayer1 == 0:

            if check_player_in_explosion(Xlocal, Ylocal, explosion_range, bomb_position[0], bomb_position[1]):
                danoplayer1 = 1

        if danoplayer2 == 0:

            if check_player_in_explosion(Xlocal2, Ylocal2, explosion_range, bomb_position[0], bomb_position[1]):
                danoplayer2 = 1

    if BombaExplosao_Player2:
        
        if danoplayer1 == 0:

            if check_player_in_explosion(Xlocal, Ylocal, explosion_range_player2, bomb_position_player2[0], bomb_position_player2[1]):
                danoplayer1 = 1

        if danoplayer2 == 0:

            if check_player_in_explosion(Xlocal2, Ylocal2, explosion_range_player2, bomb_position_player2[0], bomb_position_player2[1]):
                danoplayer2 = 1

    if danoplayer1 == 1:
        Vidas -= 1
        timerdamege1 = 1
        danoplayer1 = 2

    if danoplayer2 == 1:
        Vidas2 -= 1
        timerdamege2 = 1
        danoplayer2 = 2
    
    if timerdamege1 == 1:
        danotimer1 += 1
        if danotimer1 == 50:
            danoplayer1 = 0
            timerdamege1 = 0
            danotimer1 = 0

    if timerdamege2 == 1:
        danotimer2 += 1
        if danotimer2 == 50:
            danoplayer2 = 0
            timerdamege2 = 0
            danotimer2 = 0

    #personagem
    if Inicio == 1: 

        test = 0
        if test == 1:
            test = font.render(f'local:{local}', False, text_color)
            Screen.blit(test, (380, 50))

        if trigger1 == 0:
            Screen.blit(bomba1,(Xlocalb,Ylocalb))
        if trigger1 == 1:
            Screen.blit(bomba1,(spawn_x -2,spawn_y - 2))

        if trigger2 == 0:
            Screen.blit(bomba2,(Xlocalb2,Ylocalb2))
        if trigger2 == 1:
            Screen.blit(bomba2,(spawn_x2 -2,spawn_y2 - 2))

        Screen.blit(Personagem1,(Xlocal,Ylocal))
        Screen.blit(Personagem2,(Xlocal2,Ylocal2))

        #ver hit box
        showhitbox = False
        if showhitbox == True:
            for box in boxes:
                pygame.draw.rect(Screen, (255, 0, 0), box)

        #vidas

            #borda
        VidasInfo1 = font2.render(f'P1:', False, text_color2)
        Screen.blit(VidasInfo1, (2.5, 2.5))

        VidasInfo2 = font2.render(f'P2:', False, text_color2)
        Screen.blit(VidasInfo2, (377.5, 2.5))

            #escrita
        VidasInfo1 = font.render(f'P1:', False, text_color)
        Screen.blit(VidasInfo1, (5, 5))

        VidasInfo2 = font.render(f'P2:', False, text_color)
        Screen.blit(VidasInfo2, (380, 5))
            #coracoes
        if Vidas2 >= 1:    
            Screen.blit(coracao, (440, 5))
        if Vidas >= 1:
            Screen.blit(coracao, (65, 5))


        if Vidas2 >= 2:
            Screen.blit(coracao, (475, 5))
        if Vidas >= 2:
            Screen.blit(coracao, (100, 5))  


        if Vidas2 == 3:
            Screen.blit(coracao, (510, 5))
        if Vidas == 3:
            Screen.blit(coracao, (135, 5))

    pygame.display.update()

pygame.quit ()

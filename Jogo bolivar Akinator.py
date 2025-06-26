import pygame
import math
import random
import sys

pygame.init()
pygame.display.set_caption("Akinator")

#variaveis

PerguntaAtual = 1
triggerpergunta = 0
PerguntaTempo = 0
PerguntaTempo1 = 0
triggerpergunta1 = 0

pergunta1mulher = 0
pergunta1homen = 0
pergunta9nao = 0
pergunta9sim = 0

    #definicao de tamanho de tela

Xscreen = 512
Yscreen = 512

#informacoes
font = pygame.font.SysFont("Lato", 45, True, True)
font2 = pygame.font.SysFont("Lato", 50, True, True)
font3 = pygame.font.SysFont("Arial", 30, True, True)
text_color = (200, 0, 0) #vermelho 
text_color2 = (0,0,0) #preto
text_color3 = (255,255,255) #branco
text_color4 = (0, 238, 255) #azul claro
text_color5 = (43, 255, 0) #verde

    #MENU

Mapa = pygame.image.load('Menu/menuakinator.png')
Menu = pygame.image.load('Menu/menuakinator.png')

MenuBotao1 = pygame.image.load('Menu/2botaoplay.png')
MenuBotao2 = pygame.image.load('Menu/2botaocreditos.png')
MenuBotao3 = pygame.image.load('Menu/2botaosaida.png')
MenuBotao4 = pygame.image.load('Menu/2botaoback.png')
Fantasma = pygame.image.load('Sprites/Fantasma.png')

Fantasma = pygame.transform.scale (Fantasma, (225,225))
MenuBotao1 = pygame.transform.scale (MenuBotao1, (150,150))
MenuBotao2 = pygame.transform.scale (MenuBotao2, (150,150))
MenuBotao3 = pygame.transform.scale (MenuBotao3, (150,150))
MenuBotao4 = pygame.transform.scale (MenuBotao4, (150,150))

    #MENU MECANICAS

creditos = 0

menuanimacao = 0
menutempoani = 0

MenuTimer = 0
Tempomenu = 0
Menupage = 0

Inicio = 0

#tamanho do jogo e inicializacao
Screen = pygame.display.set_mode((Xscreen, Yscreen))

#Fantasma

clock = pygame.time.Clock()

x, y = 420, 250  

A, B = 50, 50  

speed = 0.020  
animacao_fantasma = 1  
time = 0


sprite_width, sprite_height = Fantasma.get_size()

def desenha_fantasma(x, y):

    Screen.blit(Fantasma, (x - sprite_width // 2, y - sprite_height // 2))


font = pygame.font.Font(None, 35)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class TriggerSystem:
    def __init__(self):
        self.codigo = "" 
        self.triggerValor = False  
        self.valorAtual = None 
    
    def ativar_trigger(self, valorAtual):
        if self.triggerValor:  
            self.codigo += str(valorAtual)  
            self.triggerValor = False  
    
    def ligar_trigger(self):
        self.triggerValor = True  


sistema = TriggerSystem()

def display_text(text, x, y):
    text_surface = font.render(text, True, BLACK)
    Screen.blit(text_surface, (x, y))
    pygame.display.flip()  

codigo_comparacao = 111

Screen_Open = True
while Screen_Open :
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Screen_Open = False
        if Inicio == 1:
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_1 and sistema.triggerValor:
                    sistema.ativar_trigger(1)  

                if event.key == pygame.K_2 and sistema.triggerValor:
                    sistema.ativar_trigger(2)

                if event.key == pygame.K_3 and sistema.triggerValor:
                    sistema.ativar_trigger(3) 

                if event.key == pygame.K_4 and sistema.triggerValor:
                    sistema.ativar_trigger(4)
                    
                if event.key == pygame.K_0 and sistema.triggerValor:
                    sistema.ativar_trigger(0)  

    Commands = pygame.key.get_pressed()

    #exibicao do menu

    if Inicio == 0:

        Screen.blit(Menu,(0,0))   

        if creditos == 0:

            if animacao_fantasma == 1:
            
                offset_y = A * math.sin(time)  
                y_fantasma = y - offset_y  
        
            time += speed
        
            if time >= 2 * math.pi:
                time = 0

            desenha_fantasma(x, y_fantasma)
    
            Screen.blit(MenuBotao1,(178,154))
            Screen.blit(MenuBotao2,(178,254))   
            Screen.blit(MenuBotao3,(178,354))
            
        if creditos == 1:

            if animacao_fantasma == 1:
            
                offset_y = A * math.sin(time)  
                y_fantasma = y - offset_y  
        
            time += speed
        
            if time >= 2 * math.pi:
                time = 0

            desenha_fantasma(x, y_fantasma)

            Screen.blit(MenuBotao4,(178,354))
            CreditosIntro = font3.render(f'Criado Por:', False, text_color5)
            Creditosnome1 = font3.render(f'Gabriel Meirelles', False, text_color3) 
            Creditosnome2 = font3.render(f'Lucas Eduardo', False, text_color3) 
            Creditosprog = font3.render(f'Programador:', False, text_color) 
            Creditosdesig = font3.render(f'Designer:', False, text_color4) 
            Screen.blit(CreditosIntro, (173, 50))
            Screen.blit(Creditosnome1, (130, 85))
            Screen.blit(Creditosnome2, (145, 115))
            Screen.blit(Creditosprog, (155, 150))
            Screen.blit(Creditosnome1, (130, 185))
            Screen.blit(Creditosdesig, (182, 225))
            Screen.blit(Creditosnome1, (130, 265))
            Screen.blit(Creditosnome2, (145, 295))
    #selecao de menu

    if Menupage == 0:
        if MenuTimer == 0:
            if Commands[pygame.K_DOWN]:
                menuanimacao = 1
                MenuTimer = 1
                Menupage = 1
                MenuBotao1 = pygame.image.load('Menu/2botaoplay2.png')
                MenuBotao1 = pygame.transform.scale (MenuBotao1, (150,150))
                


    if Menupage == 1:
        if menuanimacao == 1:
            menutempoani += 10
            if menutempoani <= 400:
                MenuBotao1 = pygame.image.load('Menu/2botaoplay2.png')
                MenuBotao1 = pygame.transform.scale (MenuBotao1, (150,150))
            if menutempoani >= 400:
                MenuBotao1 = pygame.image.load('Menu/2botaoplay.png')
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
                MenuBotao1 = pygame.image.load('Menu/2botaoplay.png')
                MenuBotao1 = pygame.transform.scale (MenuBotao1, (150,150))
                MenuBotao2 = pygame.image.load('Menu/2botaocreditos2.png')
                MenuBotao2 = pygame.transform.scale (MenuBotao2, (150,150))



    if Menupage == 2:
        if menuanimacao == 1:
            menutempoani += 10
            if menutempoani <= 400:
                MenuBotao2 = pygame.image.load('Menu/2botaocreditos2.png')
                MenuBotao2 = pygame.transform.scale (MenuBotao2, (150,150))
            if menutempoani >= 400:
                MenuBotao2 = pygame.image.load('Menu/2botaocreditos.png')
                MenuBotao2 = pygame.transform.scale (MenuBotao2, (150,150))
            if menutempoani >= 800:
                menutempoani = 0

        if Commands[pygame.K_SPACE]:
            creditos = 1
            Menupage = 4
            MenuBotao2 = pygame.image.load('Menu/2botaocreditos.png')
            MenuBotao2 = pygame.transform.scale (MenuBotao2, (150,150))

        if MenuTimer == 0:
            if Commands[pygame.K_DOWN]:
                menutempoani = 0
                Menupage = 3
                MenuTimer = 1
                MenuBotao2 = pygame.image.load('Menu/2botaocreditos.png')
                MenuBotao2 = pygame.transform.scale (MenuBotao2, (150,150))
                MenuBotao3 = pygame.image.load('Menu/2botaosaida2.png')
                MenuBotao3 = pygame.transform.scale (MenuBotao3, (150,150))
            if Commands[pygame.K_UP]:
                menutempoani = 0
                Menupage = 1
                MenuTimer = 1
                MenuBotao1 = pygame.image.load('Menu/2botaoplay2.png')
                MenuBotao1 = pygame.transform.scale (MenuBotao1, (150,150))
                MenuBotao2 = pygame.image.load('Menu/2botaocreditos.png')
                MenuBotao2 = pygame.transform.scale (MenuBotao2, (150,150))        



    if Menupage == 3:
        if menuanimacao == 1:
            menutempoani += 10
            if menutempoani <= 400:
                MenuBotao3 = pygame.image.load('Menu/2botaosaida2.png')
                MenuBotao3 = pygame.transform.scale (MenuBotao3, (150,150))
            if menutempoani >= 400:
                MenuBotao3 = pygame.image.load('Menu/2botaosaida.png')
                MenuBotao3 = pygame.transform.scale (MenuBotao3, (150,150))
            if menutempoani >= 800:
                menutempoani = 0

        if Commands[pygame.K_UP]:
            menutempoani = 0
            Menupage = 2
            MenuTimer = 1
            MenuBotao2 = pygame.image.load('Menu/2botaocreditos2.png')
            MenuBotao2 = pygame.transform.scale (MenuBotao2, (150,150))
            MenuBotao3 = pygame.image.load('Menu/2botaosaida.png')
            MenuBotao3 = pygame.transform.scale (MenuBotao3, (150,150))
        if Commands[pygame.K_SPACE]:
            Screen_Open = False     

    if Menupage == 4:
        if MenuTimer == 0:
            if Commands[pygame.K_DOWN]:
                menuanimacao = 1
                menutempoani = 0
                Menupage = 5
                MenuBotao4= pygame.image.load('Menu/2botaoback.png')
                MenuBotao4 = pygame.transform.scale (MenuBotao4, (150,150)) 

    if Menupage == 5:
        if menuanimacao == 1:
            menutempoani += 10
            if menutempoani <= 400:
                MenuBotao4 = pygame.image.load('Menu/2botaoback2.png')
                MenuBotao4 = pygame.transform.scale (MenuBotao4, (150,150))
            if menutempoani >= 400:
                MenuBotao4 = pygame.image.load('Menu/2botaoback.png')
                MenuBotao4 = pygame.transform.scale (MenuBotao4, (150,150))
            if menutempoani >= 800:
                menutempoani = 0
        if Commands[pygame.K_SPACE]:
            Menupage = 0
            creditos = 0
            MenuBotao4 = pygame.image.load('Menu/2botaoback.png')
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
        
        if animacao_fantasma == 1:
            
            offset_y = A * math.sin(time)  
            y_fantasma = y - offset_y  
        
        time += speed
        
        if time >= 2 * math.pi:
            time = 0

        desenha_fantasma(x, y_fantasma)

        #display_text(f"Código: {sistema.codigo}", 10, 0)

        if triggerpergunta == 1:
            PerguntaTempo += 5
        if triggerpergunta1 == 1:
            PerguntaTempo1 += 5
            if PerguntaTempo1 >= 50:
                PerguntaTempo = 0
                triggerpergunta = 0
                triggerpergunta1 = 0
                PerguntaTempo1 = 0

        if PerguntaAtual == 1:
            sistema.ligar_trigger()
            display_text(f"Qual é o Gênero da Pessoa?", 25, 25)
            display_text(f"1 . Mulher", 25, 75)
            display_text(f"2 . Homen", 25, 125)
            if Commands[pygame.K_1]:
                pergunta1mulher = 1 
                triggerpergunta = 1

            if Commands[pygame.K_2]:
                pergunta1homen = 1 
                triggerpergunta = 1

            if PerguntaTempo >= 50:
                PerguntaAtual = 2
                PerguntaTempo = 0
                triggerpergunta1 = 1

        if PerguntaAtual == 2:
            sistema.ligar_trigger()
            display_text(f"Qual é a Cor do Cabelo?", 25, 25)
            display_text(f"1 . Castanho", 25, 75)
            display_text(f"2 . Loiro", 25, 125)
            display_text(f"3 . Preto", 25, 175)
            display_text(f"4 . Ruivo", 25, 225)

            if Commands[pygame.K_1] or Commands[pygame.K_2] or Commands[pygame.K_3] or Commands[pygame.K_4]:
                triggerpergunta = 1
            if PerguntaTempo >= 50:
                PerguntaAtual = 3
                PerguntaTempo = 0
                triggerpergunta1 = 1

        if PerguntaAtual == 3:
            sistema.ligar_trigger()
            display_text(f"Qual é o Tipo de Cabelo?", 25, 25)
            display_text(f"1 . Ondulado", 25, 75)
            display_text(f"2 . Liso", 25, 125)
            display_text(f"3 . Cacheado", 25, 175)
            if Commands[pygame.K_1] or Commands[pygame.K_2] or Commands[pygame.K_3]:
                triggerpergunta = 1
            if PerguntaTempo >= 50:
                PerguntaAtual = 4
                PerguntaTempo = 0
                triggerpergunta1 = 1 

        if PerguntaAtual == 4:
            sistema.ligar_trigger()
            display_text(f"Qual é o Comprimento do Cabelo?", 25, 25)
            display_text(f"1 . Longo", 25, 75)
            display_text(f"2 . Curto", 25, 125)
            if Commands[pygame.K_1] or Commands[pygame.K_2]:
                triggerpergunta = 1
            if PerguntaTempo >= 50:
                PerguntaAtual = 5
                PerguntaTempo = 0
                triggerpergunta1 = 1 

        if PerguntaAtual == 5:
            sistema.ligar_trigger()
            display_text(f"Tem o Cabelo pintado?", 25, 25)
            display_text(f"1 . Não", 25, 75)
            display_text(f"2 . Sim", 25, 125)
            if Commands[pygame.K_1] or Commands[pygame.K_2]:
                triggerpergunta = 1
            if PerguntaTempo >= 50:
                PerguntaAtual = 6
                PerguntaTempo = 0
                triggerpergunta1 = 1 

        if PerguntaAtual == 6:
            sistema.ligar_trigger()
            display_text(f"Usa Oculos ?", 25, 25)
            display_text(f"1 . Não", 25, 75)
            display_text(f"2 . Sim", 25, 125)
            if Commands[pygame.K_1] or Commands[pygame.K_2]:
                triggerpergunta = 1
            if PerguntaTempo >= 50:
                PerguntaAtual = 7
                PerguntaTempo = 0
                triggerpergunta1 = 1 

        if PerguntaAtual == 7:
            sistema.ligar_trigger()
            display_text(f"Qual é a altura ?", 25, 25)
            display_text(f"1 . Baixo", 25, 75)
            display_text(f"2 . Alto", 25, 125)
            if Commands[pygame.K_1] or Commands[pygame.K_2]:
                triggerpergunta = 1
            if PerguntaTempo >= 50:
                PerguntaAtual = 8
                PerguntaTempo = 0
                triggerpergunta1 =1 

        if PerguntaAtual == 8:
            sistema.ligar_trigger()
            display_text(f"Essa pessoa Trabalha ?", 25, 25)
            display_text(f"1 . Não", 25, 75)
            display_text(f"2 . Sim", 25, 125)
            if Commands[pygame.K_1] or Commands[pygame.K_2]:
                triggerpergunta = 1
            if PerguntaTempo >= 50:
                PerguntaAtual = 9
                PerguntaTempo = 0
                triggerpergunta1 = 1

        if PerguntaAtual == 9:
            sistema.ligar_trigger()
            display_text(f"Essa pessoa é atleta ?", 25, 25)
            display_text(f"1 . Não", 25, 75)
            display_text(f"2 . Sim", 25, 125)
            if Commands[pygame.K_1]:
                triggerpergunta = 1
                pergunta9nao = 1
            if Commands[pygame.K_2]:
                triggerpergunta = 1
                pergunta9sim = 1

            if pergunta9sim == 1:
                PerguntaAtual = 10
                PerguntaTempo = 0
                triggerpergunta1 = 1

            if  pergunta9nao == 1:
                if PerguntaTempo >= 50:
                    if pergunta1homen == 1:
                        sistema.ativar_trigger(0)
                        PerguntaAtual = 11
                        PerguntaTempo = 0
                        triggerpergunta1 = 1
                        pergunta1homen = 0
                    if pergunta1mulher == 1:
                        sistema.ativar_trigger(0)
                        pergunta1mulher = 0
                        pergunta9sim = 0
                        PerguntaTempo = 0
                        triggerpergunta1 = 1
                        PerguntaAtual = 0

        if PerguntaAtual == 10:
            sistema.ligar_trigger()
            display_text(f"Qual esporte Eessa pessoa faz?", 25, 25)
            display_text(f"1 . Volei", 25, 75)
            display_text(f"2 . Dança", 25, 125)
            display_text(f"3 . Handboll", 25, 175)
            if Commands[pygame.K_1] or Commands[pygame.K_2] or Commands[pygame.K_3]:
                triggerpergunta = 1
            if PerguntaTempo >= 50:
                if pergunta1homen == 1:
                    PerguntaAtual = 11
                    PerguntaTempo = 0
                    triggerpergunta1 = 1
                    pergunta1homen = 0
                if pergunta1mulher == 1:
                    pergunta1mulher = 0
                    PerguntaAtual = 0
                    PerguntaTempo = 0
                    triggerpergunta1 = 1
            
        if PerguntaAtual == 11:
            sistema.ligar_trigger()
            display_text(f"Ela tem barba ?", 25, 25)
            display_text(f"1 . Não", 25, 75)
            display_text(f"2 . Sim", 25, 125)
            if Commands[pygame.K_1] or Commands[pygame.K_2]:
                triggerpergunta = 1
            if PerguntaTempo >= 50:
                PerguntaAtual = 11
                PerguntaTempo = 0
                triggerpergunta1 = 1 

        banco_de_dados = {
        "21211121102": "João",
        "21221112211": "Gabriel",
        }

        #| Gênero  | Cor do Cabelo | Tipo de Cabelo | Comprimento do Cabelo | Cabelo Pintado | Usa Óculos | Altura | Trabalha | Atleta   | Esporte     | Barba  |

        #| Mulher 1| Castanho    1 | Ondulado     1 | Longo              1  | Não          1 | Não      1 | Baixa1 | Nao    1 | Não    1 | vôlei     1 | Nao 1  |
        #| Homen  2| Loira       2 | Liso         2 | Curto              2  | Sim          2 | Sim      2 | Alto 2 | Sim    2 | Sim    2 | Dança     2 | Sim 2  |
        #|         | Preto       3 | Cacheado     3 |                       |                |            |        |          |          | Handboll  3 | Nada 0 |
        #|         | Ruiva       4 |                |                       |                |            |        |          |          | Nada      0 |        |


        if sistema.codigo in banco_de_dados:
            nome = banco_de_dados[sistema.codigo]  # Puxa o nome associado ao código
            #display_text(f"Código: {sistema.codigo}, Nome: {nome}", 0, 200)
            display_text(f"Nome: {nome}", 25, 200)


    pygame.display.flip()

pygame.quit()

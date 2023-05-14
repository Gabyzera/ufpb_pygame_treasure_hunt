import pygame, random 

pygame.init()

#tabela de cores
azul_escuro = (0,0,128)
azul = (65,105,225)
azul_claro = (135,206,250) 

#medidas 
tamanho = 114
linhas_colunas = 6 

#tela de jogo
tela = pygame.display.set_mode(((linhas_colunas) * tamanho, (linhas_colunas) * tamanho)) #684 x 684
nome = pygame.display.set_caption("Caça ao tesouro")

#tela
tela.fill(azul_escuro)

#tabuleiro
pygame.draw.rect(tela, azul, (114, 114, tamanho * 4, tamanho * 4)) #475 x 475
for i in range (2, 5):
    pygame.draw.line(tela, azul_claro, (tamanho * i,  342), ((tamanho * i) + 5, 342), 455) #linhas verticais
    pygame.draw.line(tela, azul_claro, (114, tamanho * i), (570, (tamanho * i)), 5) #linhas horizontais

pygame.display.update()

#variaveis de quantidade
num_tesouros = 0
num_buracos = 0
jogador_1 = 0 
jogador_2 = 0
num_numeros_escolhidos = 0
num_tesouros_escolhidos = 0
num_buracos_escolhidos = 0


#fonte que sera' utilizada nas palavras
fonte = pygame.font.Font(None, 50)

#adicionando o valor da pontucao inicial de cada jogador
tela.blit(fonte.render("Pontuação: "+ str(jogador_1), True, azul_claro), [15, 15])
tela.blit(fonte.render("Pontuação: "+ str(jogador_2), True, azul_claro), [400, 15])
                
#iniciando o jogo pelo jogador_1
vez = jogador_1

#matriz que tera' as posicoes dos tesouros
casa_escolhida = [[None for i in range (linhas_colunas)] for j in range(linhas_colunas)] 
#matriz que mostra a casa revelada
casa_revelada = [[False for i in range(linhas_colunas)] for j in range(linhas_colunas)]

#coloca os tesouros em casas aleatorias
while (num_tesouros < (linhas_colunas)):
    i = random.randint(1, linhas_colunas - 2)
    j = random.randint(1, linhas_colunas - 2)     

    if (casa_escolhida[i][j] == None):
        casa_escolhida[i][j] = "*"
        num_tesouros += 1       

#coloca os buracos em casas aleatorios
while (num_buracos < (linhas_colunas / 2)):
    i = random.randint(1, linhas_colunas / 3)
    j = random.randint(1, linhas_colunas / 3)

    if (casa_escolhida[i][j] == None):
        casa_escolhida[i][j] = "@"
        num_buracos += 1 

for i in range (1,5):
    for j in range (1,5):
        if (casa_escolhida[i][j] != "*" and casa_escolhida[i][j] != "@"):
            cont = 0
            if (i < 4) and (casa_escolhida[i+1][j] == "*"):
                cont += 1
            if (j < 4) and (casa_escolhida[i][j+1] == "*"):
                cont += 1
            if (i > 1) and (casa_escolhida[i-1][j] == "*"):
                cont += 1
            if (j > 1) and (casa_escolhida[i][j-1] == "*"):
                cont += 1
            casa_escolhida[i][j] = str(cont)

#loop para o jogo só fechar quando aperta o 'x'
deve_continuar = True 
while deve_continuar:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            deve_continuar = False

        #tela so' sera' atualizada quando "tela_mundou" for igual a "True"
        tela_mudou = False
        
        #iniciando o jogo pelo jogador_1
        if vez == jogador_1:
            elipse = pygame.draw.ellipse(tela, azul_claro, [15, (tamanho - 66), 40, 40]) #mostrando de quem e' a vez
    
        #quando o jogador clicar em algum lugar         
        if (event.type == pygame.MOUSEBUTTONDOWN):
            mouse_x, mouse_y = event.pos #tornando as coordenadas do ponto que clicou em um evento
          
            #divisao inteira das coordenadas pelo tamanho da casa para 
            casa_x = mouse_x // tamanho 
            casa_y = mouse_y // tamanho
           
            #se cliquou no tabuleiro
            if (casa_y > linhas_colunas-1):
                continue #quando a casa e' clicada pela primeira vez
            if (not casa_revelada[casa_x][casa_y]):
                tela_mudou = True
                casa_revelada[casa_x][casa_y] = True

                if (tela_mudou):
                    i, j = casa_x, casa_y
                    num_casas_abertas = 0

                    # Verifica se apertou na casa que tem o tesouro
                    if (casa_escolhida[casa_x][casa_y] == "*"):
                        #mostrar a imagem do tesouro no tabuleiro
                        tesouro = pygame.image.load("tesouro.png")
                        #adequa o tamanho da imagem
                        tesouro = pygame.transform.scale(tesouro, (tamanho - 2, tamanho - 2))            
                        #posiciona a imagem na casa
                        tela.blit(tesouro, (tamanho*i + 1, tamanho*j + 1))   
                        num_tesouros_escolhidos +=1 

                        #os jogadores ganham 100 pontos
                        if vez == jogador_1:
                            jogador_1 += 100
                            retangulo_pontuacao = pygame.draw.rect(tela,azul_escuro,(0,0,350,45))
                            tela.blit(fonte.render("Pontuação: "+ str(jogador_1), True, azul_claro), [15, 15])
                            retangulo_epipse = pygame.draw.rect(tela,azul_escuro,(15,48,40,40))
                            elipse = pygame.draw.ellipse(tela, azul_claro, [(tamanho * 4 - 56), (tamanho - 66), 40, 40])
                            vez = jogador_2 #mudando de turno
                            break

                        else:
                            jogador_2 += 100
                            retangulo_pontuacao = pygame.draw.rect(tela,azul_escuro,(400,0,350,45))
                            tela.blit(fonte.render("Pontuação: "+ str(jogador_2), True, azul_claro), [400, 15])
                            retangulo_epipse = pygame.draw.rect(tela,azul_escuro,(400,48,40,40))
                            elipse = pygame.draw.ellipse(tela, azul_claro, [15, (tamanho - 66), 40, 40])
                            vez = jogador_1
                            break                                 
                        

                    #verifica se apertou no buraco
                    if (casa_escolhida[casa_x][casa_y] == "@"):
                        #mostra a imagem do buracono tabuleiro
                        buraco = pygame.image.load("buraco.png")
                        #adequa o tamanho da imagem
                        buraco = pygame.transform.scale(buraco, (tamanho - 5, tamanho - 5))         
                        #posiciona a imagem na casa 
                        tela.blit(buraco, (tamanho*i + 1, tamanho*j + 1))  
                        num_buracos_escolhidos += 1

                        #os jogadores perdem 50 pontos
                        if (vez == jogador_1):
                            retangulo_epipse = pygame.draw.rect(tela,azul_escuro,(15,48,40,40))
                            elipse = pygame.draw.ellipse(tela, azul_claro, [(tamanho * 4 - 56), (tamanho - 66), 40, 40])
                            if (jogador_1 > 0):
                                jogador_1 -= 50
                                retangulo_pontuacao = pygame.draw.rect(tela,azul_escuro,(0,0,350,45))
                                tela.blit(fonte.render("Pontuação: "+ str(jogador_1), True, azul_claro), [15, 15])
                            vez = jogador_2 #mudando de vez
                            break
                            

                        if (vez == jogador_2):
                            retangulo_epipse = pygame.draw.rect(tela,azul_escuro,(400,48,40,40))
                            elipse = pygame.draw.ellipse(tela, azul_claro, [15, (tamanho - 66), 40, 40])
                            if (jogador_2 > 0):
                                jogador_2 -= 50
                                retangulo_pontuacao = pygame.draw.rect(tela,azul_escuro,(400,0,350,45))
                                tela.blit(fonte.render("Pontuação: "+ str(jogador_2), True, azul_claro), [400, 15])
                            vez = jogador_1
                            break
                            
                    
                    
                    else:
                        texto = fonte.render((str(casa_escolhida[i][j])), True, azul_escuro)    
                        tela.blit(texto, (tamanho*i + 0.4*tamanho, tamanho*j + 0.4*tamanho))
                        num_numeros_escolhidos += 1

                        if vez == jogador_1:
                            retangulo_epipse = pygame.draw.rect(tela,azul_escuro,(15,48,40,40))
                            elipse = pygame.draw.ellipse(tela, azul_claro, [(tamanho * 4 - 56), (tamanho - 66), 40, 40])
                            vez = jogador_2 #mudando de turno
                            break

                        else:
                            retangulo_epipse = pygame.draw.rect(tela,azul_escuro,(400,48,40,40))
                            elipse = pygame.draw.ellipse(tela, azul_claro, [15, (tamanho - 66), 40, 40])
                            vez = jogador_1
                            break

                             
                if (num_numeros_escolhidos == 7) and (num_buracos_escolhidos == 3) and (num_tesouros_escolhidos == 6):
                    print("f")
                    if (jogador_1 > jogador_2):
                        tela.fill(azul_escuro) 
                        tela.blit(pygame.font.SysFont(None, 60).render(("O jogador 1 venceu."), False, azul_claro), (45, 140))
                        tela.blit(pygame.font.SysFont(None, 60).render(("Parabéns!"), False, azul_claro), (115, 185))

                    else:
                        tela.fill(azul_escuro) 
                        tela.blit(pygame.font.SysFont(None, 60).render(("O jogador 2 venceu."), False, azul_claro), (45, 140))
                        tela.blit(pygame.font.SysFont(None, 60).render(("Parabéns!"), False, azul_claro), (115, 140))

        pygame.display.update()

pygame.quit() 
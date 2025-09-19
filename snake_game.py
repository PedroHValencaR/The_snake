import pygame
import random

# --- 1. Inicialização e Configurações Globais ---

pygame.init()
pygame.mixer.init()

# Cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE_CLARO = (0, 255, 0)
VERDE_ESCURO = (0, 155, 0)
COR_GRID = (40, 40, 40)

# Tela
LARGURA_TELA = 600
ALTURA_TELA = 400
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption('The snake')

# Controle de FPS
clock = pygame.time.Clock()

# Configurações da Cobra e Fontes
TAMANHO_BLOCO = 20
VELOCIDADE_INICIAL = 10
ACELERACAO = 0.5
fonte_estilo = pygame.font.SysFont("bahnschrift", 25)

# --- CARREGAMENTO DE SONS E IMAGENS ---
try:
    som_comida = pygame.mixer.Sound('sons/comer.mp3')
    som_game_over = pygame.mixer.Sound('sons/game_over.mp3')
except pygame.error:
    print("Aviso: Arquivos de som não encontrados na pasta 'sons'. O jogo rodará sem som.")
    som_comida = som_game_over = None

try:
    apple_img_original = pygame.image.load('imagens/apple.png').convert_alpha()
    snake_head_original = pygame.image.load('imagens/snake_head.png').convert_alpha()
    snake_body_original = pygame.image.load('imagens/snake_body.png').convert_alpha()  # Carrega o corpo

    # Redimensiona as imagens
    apple_img = pygame.transform.scale(apple_img_original, (TAMANHO_BLOCO, TAMANHO_BLOCO))
    snake_head_img = pygame.transform.scale(snake_head_original, (TAMANHO_BLOCO, TAMANHO_BLOCO))
    snake_body_img = pygame.transform.scale(snake_body_original, (TAMANHO_BLOCO, TAMANHO_BLOCO))  # Redimensiona o corpo
except pygame.error:
    print("Aviso: Arquivos de imagem não encontrados na pasta 'imagens'. O jogo rodará com retângulos.")
    apple_img = snake_head_img = snake_body_img = None


# --- 2. Funções do Jogo ---

def salvar_highscore(pontuacao):
    with open("highscore.txt", "w") as f:
        f.write(str(pontuacao))


def carregar_highscore():
    try:
        with open("highscore.txt", "r") as f:
            return int(f.read())
    except (FileNotFoundError, ValueError):
        return 0


def exibir_pontuacao(pontuacao):
    valor = fonte_estilo.render("Pontuação: " + str(pontuacao), True, BRANCO)
    tela.blit(valor, [10, 10])


def desenhar_grid():
    for x in range(0, LARGURA_TELA, TAMANHO_BLOCO):
        pygame.draw.line(tela, COR_GRID, (x, 0), (x, ALTURA_TELA))
    for y in range(0, ALTURA_TELA, TAMANHO_BLOCO):
        pygame.draw.line(tela, COR_GRID, (0, y), (LARGURA_TELA, y))


def desenhar_cobra(tamanho_bloco, lista_cobra, direcao):
    """Desenha a cobra, usando imagens para o corpo e a cabeça rotacionada."""
    if not lista_cobra: return

    # Desenha o corpo (todos os segmentos, exceto o último)
    for segmento in lista_cobra[:-1]:
        if snake_body_img:
            tela.blit(snake_body_img, (segmento[0], segmento[1]))
        else:  # Fallback para retângulos
            pygame.draw.rect(tela, VERDE_CLARO, [segmento[0], segmento[1], tamanho_bloco, tamanho_bloco])

    # Desenha a cabeça
    cabeca_pos = lista_cobra[-1]
    if snake_head_img:
        cabeca_rotacionada = snake_head_img
        if direcao == "CIMA":
            cabeca_rotacionada = pygame.transform.rotate(snake_head_img, 90)
        elif direcao == "BAIXO":
            cabeca_rotacionada = pygame.transform.rotate(snake_head_img, -90)
        elif direcao == "ESQUERDA":
            cabeca_rotacionada = pygame.transform.rotate(snake_head_img, 180)
        tela.blit(cabeca_rotacionada, (cabeca_pos[0], cabeca_pos[1]))
    else:
        pygame.draw.rect(tela, VERDE_ESCURO, [cabeca_pos[0], cabeca_pos[1], tamanho_bloco, tamanho_bloco])


def tela_de_inicio(highscore):
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                intro = False

        tela.fill(PRETO)
        desenhar_grid()

        # Título com sombra
        fonte_titulo = pygame.font.SysFont("comicsansms", 80)
        titulo_surface = fonte_titulo.render("SNAKE", True, VERDE_CLARO)
        titulo_sombra_surface = fonte_titulo.render("SNAKE", True, VERDE_ESCURO)
        titulo_rect = titulo_surface.get_rect(center=(LARGURA_TELA / 2, ALTURA_TELA / 3))
        tela.blit(titulo_sombra_surface, (titulo_rect.x + 4, titulo_rect.y + 4))
        tela.blit(titulo_surface, titulo_rect)

        # Imagens decorativas
        if snake_head_img:
            tela.blit(snake_head_img, (titulo_rect.left - TAMANHO_BLOCO - 10, titulo_rect.centery - TAMANHO_BLOCO / 2))
        if apple_img:
            tela.blit(apple_img, (titulo_rect.right + 10, titulo_rect.centery - TAMANHO_BLOCO / 2))

        fonte_instrucao = pygame.font.SysFont("bahnschrift", 20)
        instrucao = fonte_instrucao.render("Pressione qualquer tecla para iniciar", True, BRANCO)
        instrucao_rect = instrucao.get_rect(center=(LARGURA_TELA / 2, ALTURA_TELA / 2 + 40))
        tela.blit(instrucao, instrucao_rect)

        texto_highscore = fonte_estilo.render(f"Pontuação Máxima: {highscore}", True, BRANCO)
        highscore_rect = texto_highscore.get_rect(center=(LARGURA_TELA / 2, ALTURA_TELA - 50))
        tela.blit(texto_highscore, highscore_rect)

        pygame.display.update()
        clock.tick(15)


def loop_do_jogo():
    highscore = carregar_highscore()
    velocidade_atual = VELOCIDADE_INICIAL
    game_over = False
    game_close = False

    x1, y1 = LARGURA_TELA / 2, ALTURA_TELA / 2
    x1_change, y1_change = 0, 0
    direcao = "DIREITA"
    lista_cobra = []
    comprimento_cobra = 1

    comida_x = round(random.randrange(0, LARGURA_TELA - TAMANHO_BLOCO) / float(TAMANHO_BLOCO)) * float(TAMANHO_BLOCO)
    comida_y = round(random.randrange(0, ALTURA_TELA - TAMANHO_BLOCO) / float(TAMANHO_BLOCO)) * float(TAMANHO_BLOCO)

    while not game_over:
        while game_close:
            # ... (código da tela de game over permanece o mesmo) ...
            pontuacao_atual = comprimento_cobra - 1
            if pontuacao_atual > highscore:
                highscore = pontuacao_atual
                salvar_highscore(highscore)

            tela.fill(PRETO)
            fonte_game_over = pygame.font.SysFont("comicsansms", 40)
            linha1_surface = fonte_game_over.render("Você Perdeu!", True, VERMELHO)
            linha2_surface = fonte_estilo.render("Pressione C para Continuar ou S para Sair", True, BRANCO)
            linha1_rect = linha1_surface.get_rect(center=(LARGURA_TELA / 2, ALTURA_TELA / 3))
            linha2_rect = linha2_surface.get_rect(center=(LARGURA_TELA / 2, ALTURA_TELA / 2))

            tela.blit(linha1_surface, linha1_rect)
            tela.blit(linha2_surface, linha2_rect)

            texto_highscore_final = fonte_estilo.render("Pontuação Máxima: " + str(highscore), True, BRANCO)
            tela.blit(texto_highscore_final,
                      [LARGURA_TELA / 2 - texto_highscore_final.get_width() / 2, ALTURA_TELA / 2 + 50])
            exibir_pontuacao(pontuacao_atual)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        game_over, game_close = True, False
                    if event.key == pygame.K_c:
                        loop_do_jogo()
                if event.type == pygame.QUIT:
                    game_over, game_close = True, False

        for event in pygame.event.get():
            if event.type == pygame.QUIT: game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change, y1_change, direcao = -TAMANHO_BLOCO, 0, "ESQUERDA"
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change, y1_change, direcao = TAMANHO_BLOCO, 0, "DIREITA"
                elif event.key == pygame.K_UP and y1_change == 0:
                    x1_change, y1_change, direcao = 0, -TAMANHO_BLOCO, "CIMA"
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    x1_change, y1_change, direcao = 0, TAMANHO_BLOCO, "BAIXO"

        if x1 >= LARGURA_TELA or x1 < 0 or y1 >= ALTURA_TELA or y1 < 0:
            if som_game_over: som_game_over.play()
            game_close = True

        x1 += x1_change
        y1 += y1_change

        tela.fill(PRETO)
        desenhar_grid()

        if apple_img:
            tela.blit(apple_img, (comida_x, comida_y))
        else:
            pygame.draw.rect(tela, VERMELHO, [comida_x, comida_y, TAMANHO_BLOCO, TAMANHO_BLOCO])

        cabeca_cobra = [x1, y1]
        lista_cobra.append(cabeca_cobra)
        if len(lista_cobra) > comprimento_cobra:
            del lista_cobra[0]

        for x in lista_cobra[:-1]:
            if x == cabeca_cobra:
                if som_game_over: som_game_over.play()
                game_close = True

        desenhar_cobra(TAMANHO_BLOCO, lista_cobra, direcao)
        exibir_pontuacao(comprimento_cobra - 1)
        pygame.display.update()

        if x1 == comida_x and y1 == comida_y:
            comida_x = round(random.randrange(0, LARGURA_TELA - TAMANHO_BLOCO) / float(TAMANHO_BLOCO)) * float(
                TAMANHO_BLOCO)
            comida_y = round(random.randrange(0, ALTURA_TELA - TAMANHO_BLOCO) / float(TAMANHO_BLOCO)) * float(
                TAMANHO_BLOCO)
            comprimento_cobra += 1
            velocidade_atual += ACELERACAO
            if som_comida: som_comida.play()

        clock.tick(velocidade_atual)

    pygame.quit()
    quit()


# --- Inicia o Jogo ---
if __name__ == '__main__':
    highscore_inicial = carregar_highscore()
    tela_de_inicio(highscore_inicial)
    loop_do_jogo()

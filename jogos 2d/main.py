from dataclasses import dataclass
import math
import random
from typing import Optional
import arcade


# CONFIGURACOES GERAIS

LARGURA_TELA = 1180
ALTURA_TELA = 720
TITULO_TELA = "Demonstrção - Utility AI Simplificada"

ARENA_ESQUERDA = 24
ARENA_DIREITA = 856
ARENA_BAIXO = 40
ARENA_CIMA = 680
PAINEL_ESQUERDA = 890

TAMANHO_TILE = 64

VELOCIDADE_JOGADOR = 260
VELOCIDADE_TIRO_JOGADOR = 540
DANO_TIRO_JOGADOR = 18
RECARGA_TIRO_JOGADOR = 0.45

VELOCIDADE_PATRULHA_NPC = 115
VELOCIDADE_ATAQUE_NPC = 170
VELOCIDADE_FUGA_NPC = 195
VELOCIDADE_BUSCAR_VIDA_NPC = 155
VELOCIDADE_TIRO_NPC = 430
DANO_TIRO_NPC = 12
ALCANCE_TIRO_NPC = 285
DISTANCIA_SEGURA_NPC = 180
RECARGA_TIRO_NPC = 0.90

VIDA_MAXIMA = 100

# Assets da propria biblioteca Arcade.
TEXTURA_JOGADOR = ":resources:images/topdown_tanks/tankBody_blue_outline.png"
TEXTURA_NPC = ":resources:images/topdown_tanks/tankBody_red_outline.png"
TEXTURA_VIDA = ":resources:images/items/gemGreen.png"
TEXTURA_CAIXA = ":resources:images/tiles/boxCrate_double.png"
TEXTURA_GRAMA_1 = ":resources:images/topdown_tanks/tileGrass1.png"
TEXTURA_GRAMA_2 = ":resources:images/topdown_tanks/tileGrass2.png"
TEXTURA_RUA_HORIZONTAL = ":resources:images/topdown_tanks/tileGrass_roadEast.png"
TEXTURA_RUA_VERTICAL = ":resources:images/topdown_tanks/tileGrass_roadNorth.png"
TEXTURA_CRUZAMENTO = ":resources:images/topdown_tanks/tileGrass_roadCrossing.png"

COR_FUNDO = (12, 16, 24)
COR_PAINEL = (18, 23, 33)
COR_BORDA_PAINEL = (72, 86, 108)
BRANCO = (238, 242, 250)
CINZA_TEXTO = (157, 169, 188)
CINZA_FRACO = (92, 106, 128)
COR_JOGADOR = (75, 151, 255)
COR_NPC = (238, 86, 76)
COR_VIDA = (76, 211, 126)
COR_ATAQUE = (255, 188, 72)
COR_FUGA = (96, 217, 255)
COR_PATRULHA = (178, 126, 255)
COR_PERIGO = (255, 94, 94)


# FUNCOES AUXILIARES

# Mantem um valor dentro de um intervalo.
def limitar(valor: float, minimo: float, maximo: float) -> float:
    return max(minimo, min(maximo, valor))

# Calcula a distancia entre dois pontos do plano 2D.
def calcular_distancia(x1: float, y1: float, x2: float, y2: float) -> float:
    return math.hypot(x2 - x1, y2 - y1)

# Transforma um vetor em direcao com tamanho 1.
def normalizar(vetor_x: float, vetor_y: float) -> tuple[float, float]:
    tamanho = math.hypot(vetor_x, vetor_y)
    if tamanho == 0:
        return 0, 0
    return vetor_x / tamanho, vetor_y / tamanho

# Converte uma direcao em angulo para girar o sprite.
def angulo_do_vetor(vetor_x: float, vetor_y: float) -> float:
    # Pequenos desvios aparecem por causa do movimento com delta_time.
    # Se um dos eixos for quase zero, tratamos como movimento reto.
    if abs(vetor_x) < 0.20:
        vetor_x = 0
    if abs(vetor_y) < 0.20:
        vetor_y = 0

    angulo = math.degrees(math.atan2(vetor_y, vetor_x)) - 90

    # Nas diagonais, o sprite do tanque ficava visualmente de lado.
    # Esta correcao so acontece quando existe movimento nos dois eixos.
    if vetor_x != 0 and vetor_y != 0:
        angulo += 90

    return angulo

# Cria um Rect da Arcade a partir do centro, largura e altura desejados.
# Isso facilita o desenho de efeitos centralizados.
def retangulo_centralizado(x: float, y: float, largura: float, altura: float) -> arcade.Rect:
    return arcade.Rect(
        left=x - largura / 2,
        right=x + largura / 2,
        bottom=y - altura / 2,
        top=y + altura / 2,
        width=largura,
        height=altura,
        x=x,
        y=y,
    )

# Impede que jogador ou NPC saiam da area jogavel.
# O centro do sprite permanece dentro dos limites da arena.
def manter_dentro_da_arena(sprite: arcade.Sprite) -> None:
    metade_largura = sprite.width / 2
    metade_altura = sprite.height / 2
    sprite.center_x = limitar(sprite.center_x, ARENA_ESQUERDA + metade_largura, ARENA_DIREITA - metade_largura)
    sprite.center_y = limitar(sprite.center_y, ARENA_BAIXO + metade_altura, ARENA_CIMA - metade_altura)

# Move um sprite em direcao a um alvo usando delta_time.
def mover_em_direcao(sprite: arcade.Sprite, alvo_x: float, alvo_y: float, velocidade: float, delta_time: float) -> None:
    direcao_x, direcao_y = normalizar(alvo_x - sprite.center_x, alvo_y - sprite.center_y)
    sprite.center_x += direcao_x * velocidade * delta_time
    sprite.center_y += direcao_y * velocidade * delta_time

    # Gira o sprite para apontar para onde esta andando.
    if direcao_x != 0 or direcao_y != 0:
        sprite.angle = angulo_do_vetor(direcao_x, direcao_y)

    manter_dentro_da_arena(sprite)


# Guarda o nome, o valor e a cor de uma acao da Utility AI.
@dataclass
class PontuacaoUtilidade:
    nome: str
    valor: float
    cor: tuple[int, int, int]

# Cria um efeito visual simples usado quando ha tiro, dano ou troca de acao.
class ParticulaFlutuante(arcade.Sprite):
    # Inicializa a particula com cor, velocidade e tempo de vida aleatorios.
    def __init__(self, x: float, y: float, cor: tuple[int, int, int], velocidade: float = 160) -> None:
        super().__init__()

        self.texture = arcade.make_soft_circle_texture(
            diameter=random.randint(8, 14),
            color=(cor[0], cor[1], cor[2], 255),
            center_alpha=255,
            outer_alpha=0,
        )

        angulo = random.uniform(0, math.tau)
        velocidade_particula = random.uniform(velocidade * 0.35, velocidade)
        self.center_x = x
        self.center_y = y
        self.change_x = math.cos(angulo) * velocidade_particula
        self.change_y = math.sin(angulo) * velocidade_particula
        self.vida = random.uniform(0.28, 0.58)
        self.vida_inicial = self.vida

    # Atualiza a posicao e reduz a transparencia da particula ate ela sumir.
    def update(self, delta_time: float = 1 / 60) -> None:
        self.center_x += self.change_x * delta_time
        self.center_y += self.change_y * delta_time
        self.change_x *= 0.90
        self.change_y *= 0.90
        self.vida -= delta_time

        # O alpha diminui com o tempo, criando efeito de desaparecer.
        self.alpha = int(255 * limitar(self.vida / self.vida_inicial, 0, 1))

        if self.vida <= 0:
            self.remove_from_sprite_lists()

# Representa os tiros do jogador e do NPC.
class Tiro(arcade.Sprite):
    # Cria o tiro apontando para o alvo indicado.
    def __init__(
        self,
        x: float,
        y: float,
        alvo_x: float,
        alvo_y: float,
        velocidade: float,
        dano: float,
        cor: tuple[int, int, int],
        dono: str,
    ) -> None:
        super().__init__()

        direcao_x, direcao_y = normalizar(alvo_x - x, alvo_y - y)
        if direcao_x == 0 and direcao_y == 0:
            direcao_y = 1

        self.texture = arcade.make_soft_circle_texture(
            diameter=16,
            color=(cor[0], cor[1], cor[2], 255),
            center_alpha=255,
            outer_alpha=20,
        )
        self.center_x = x + direcao_x * 34
        self.center_y = y + direcao_y * 34
        self.change_x = direcao_x * velocidade
        self.change_y = direcao_y * velocidade
        self.angle = angulo_do_vetor(direcao_x, direcao_y)
        self.dano = dano
        self.dono = dono
        self.tempo_de_vida = 1.9

    # Move o tiro e remove quando ele sai da arena ou perde a validade.
    def update(self, delta_time: float = 1 / 60) -> None:
        self.center_x += self.change_x * delta_time
        self.center_y += self.change_y * delta_time
        self.tempo_de_vida -= delta_time

        saiu_da_arena = (
            self.center_x < ARENA_ESQUERDA - 40
            or self.center_x > ARENA_DIREITA + 40
            or self.center_y < ARENA_BAIXO - 40
            or self.center_y > ARENA_CIMA + 40
        )

        if saiu_da_arena or self.tempo_de_vida <= 0:
            self.remove_from_sprite_lists()

# Representa o item que recupera vida do NPC quando a acao Buscar Vida vence.
class KitVida:
    # Guarda a posicao, textura e estado inicial do kit de vida.
    def __init__(self, x: float, y: float, textura: arcade.Texture) -> None:
        self.x = x
        self.y = y
        self.textura = textura
        self.ativo = True
        self.tempo_respawn = 0.0
        self.pulso = random.uniform(0, math.tau)

    # Atualiza o pulso visual e controla o tempo de respawn.
    def atualizar(self, delta_time: float) -> None:
        self.pulso += delta_time * 4

        if self.ativo:
            return

        self.tempo_respawn -= delta_time
        if self.tempo_respawn <= 0:
            self.ativo = True

    # Desativa o kit e inicia a contagem para ele aparecer novamente.
    def coletar(self) -> None:
        self.ativo = False
        self.tempo_respawn = 7.0

    # Desenha o kit ativo ou o marcador vazio quando ele esta em respawn.
    def desenhar(self) -> None:
        raio_pulso = 28 + math.sin(self.pulso) * 4

        if self.ativo:
            arcade.draw_circle_filled(self.x, self.y, raio_pulso, (42, 121, 78, 90))
            arcade.draw_texture_rect(
                texture=self.textura,
                rect=retangulo_centralizado(self.x, self.y + math.sin(self.pulso) * 2, 44, 44),
            )
            arcade.draw_line(self.x - 12, self.y, self.x + 12, self.y, BRANCO, 4)
            arcade.draw_line(self.x, self.y - 12, self.x, self.y + 12, BRANCO, 4)
            arcade.draw_circle_outline(self.x, self.y, raio_pulso, COR_VIDA, 2)
        else:
            arcade.draw_circle_outline(self.x, self.y, 19, (66, 78, 92), 2)

# Controla o tanque azul do jogador, suas vidas, tiros e movimento.
# O jogador e controlado por teclado e mouse.
class Jogador:
    # Inicializa o sprite, a vida, os temporizadores e o estado das teclas.
    def __init__(self) -> None:
        self.sprite = arcade.Sprite(TEXTURA_JOGADOR, scale=1.15)
        self.vida = VIDA_MAXIMA
        self.tempo_flash_tiro = 0.0
        self.recarga_tiro = 0.0

        # Guardamos o estado das teclas para permitir movimento continuo.
        self.teclas = {
            arcade.key.RIGHT: False,
            arcade.key.LEFT: False,
            arcade.key.UP: False,
            arcade.key.DOWN: False,
            arcade.key.D: False,
            arcade.key.A: False,
            arcade.key.W: False,
            arcade.key.S: False,
        }

    # Define a posicao inicial e reinicia os estados do jogador.
    def configurar(self) -> None:
        self.sprite.center_x = 160
        self.sprite.center_y = 360
        self.sprite.angle = -90
        self.sprite.change_x = 0
        self.sprite.change_y = 0
        self.vida = VIDA_MAXIMA
        self.tempo_flash_tiro = 0.0
        self.recarga_tiro = 0.0

        for tecla in self.teclas:
            self.teclas[tecla] = False

    # Marca uma tecla como pressionada e recalcula a velocidade.
    def pressionar_tecla(self, tecla: int) -> None:
        if tecla in self.teclas:
            self.teclas[tecla] = True
            self.atualizar_velocidade()

    # Marca uma tecla como solta e recalcula a velocidade.
    def soltar_tecla(self, tecla: int) -> None:
        if tecla in self.teclas:
            self.teclas[tecla] = False
            self.atualizar_velocidade()

    # Calcula a direcao do movimento a partir das teclas pressionadas.
    def atualizar_velocidade(self) -> None:
        movimento_x = 0
        movimento_y = 0

        if self.teclas[arcade.key.RIGHT] or self.teclas[arcade.key.D]:
            movimento_x += 1
        if self.teclas[arcade.key.LEFT] or self.teclas[arcade.key.A]:
            movimento_x -= 1
        if self.teclas[arcade.key.UP] or self.teclas[arcade.key.W]:
            movimento_y += 1
        if self.teclas[arcade.key.DOWN] or self.teclas[arcade.key.S]:
            movimento_y -= 1

        direcao_x, direcao_y = normalizar(movimento_x, movimento_y)
        self.sprite.change_x = direcao_x * VELOCIDADE_JOGADOR
        self.sprite.change_y = direcao_y * VELOCIDADE_JOGADOR

        if direcao_x != 0 or direcao_y != 0:
            self.sprite.angle = angulo_do_vetor(direcao_x, direcao_y)

    # Tenta criar um tiro em direcao ao alvo, respeitando a recarga.
    def atirar_para(self, alvo_x: float, alvo_y: float) -> Optional[Tiro]:
        if self.recarga_tiro > 0:
            return None

        self.tempo_flash_tiro = 0.12
        self.recarga_tiro = RECARGA_TIRO_JOGADOR
        direcao_x, direcao_y = normalizar(alvo_x - self.sprite.center_x, alvo_y - self.sprite.center_y)

        if direcao_x != 0 or direcao_y != 0:
            self.sprite.angle = angulo_do_vetor(direcao_x, direcao_y)

        return Tiro(
            self.sprite.center_x,
            self.sprite.center_y,
            alvo_x,
            alvo_y,
            VELOCIDADE_TIRO_JOGADOR,
            DANO_TIRO_JOGADOR,
            COR_JOGADOR,
            "jogador",
        )

    # Atualiza a posicao do jogador e os temporizadores de tiro.
    def atualizar(self, delta_time: float) -> None:
        self.sprite.center_x += self.sprite.change_x * delta_time
        self.sprite.center_y += self.sprite.change_y * delta_time
        manter_dentro_da_arena(self.sprite)

        self.tempo_flash_tiro = max(0, self.tempo_flash_tiro - delta_time)
        self.recarga_tiro = max(0, self.recarga_tiro - delta_time)

    # Desenha o brilho rapido que aparece quando o jogador atira.
    def desenhar_flash_tiro(self) -> None:
        if self.tempo_flash_tiro <= 0:
            return

        arcade.draw_circle_filled(self.sprite.center_x, self.sprite.center_y, 36, (255, 196, 82, 42))
        arcade.draw_circle_outline(self.sprite.center_x, self.sprite.center_y, 36, COR_ATAQUE, 3)


# Controla o NPC vermelho usando Utility AI para decidir a melhor acao.
class NpcUtilidade:
    PATRULHAR = "Patrulhar"
    ATACAR = "Atacar"
    FUGIR = "Fugir"
    BUSCAR_VIDA = "Buscar vida"

    # Inicializa o sprite, a vida, os alvos, as pontuacoes e os temporizadores.
    def __init__(self) -> None:
        self.sprite = arcade.Sprite(TEXTURA_NPC, scale=1.18)
        self.vida = VIDA_MAXIMA
        self.acao_atual = self.PATRULHAR
        self.alvo_x = 0.0
        self.alvo_y = 0.0
        self.indice_patrulha = 0
        self.pontuacoes: list[PontuacaoUtilidade] = []
        self.tempo_flash_ataque = 0.0
        self.tempo_troca_acao = 0.0
        self.recarga_tiro = 0.0
        self.acao_anterior = self.PATRULHAR

        # Pontos roxos da patrulha. Eles ficam sobre os cruzamentos da estrada.
        self.pontos_patrulha = [
            (248, 584),
            (760, 584),
            (760, 136),
            (248, 136),
        ]

    # Define o estado inicial do NPC e prepara o primeiro ponto de patrulha.
    def configurar(self) -> None:
        ponto_inicial = 1
        self.sprite.center_x, self.sprite.center_y = self.pontos_patrulha[ponto_inicial]
        self.indice_patrulha = (ponto_inicial + 1) % len(self.pontos_patrulha)
        self.alvo_x, self.alvo_y = self.pontos_patrulha[self.indice_patrulha]
        direcao_x, direcao_y = normalizar(self.alvo_x - self.sprite.center_x, self.alvo_y - self.sprite.center_y)
        self.sprite.angle = angulo_do_vetor(direcao_x, direcao_y)
        self.vida = VIDA_MAXIMA
        self.acao_atual = self.PATRULHAR
        self.acao_anterior = self.PATRULHAR
        self.tempo_flash_ataque = 0.0
        self.tempo_troca_acao = 0.0
        self.recarga_tiro = 0.0

    # Recalcula a Utility AI, escolhe a acao atual e executa o comportamento do NPC.
    def atualizar(self, jogador: Jogador, kits_vida: list[KitVida], delta_time: float) -> Optional[Tiro]:
        # A cada quadro o NPC recalcula as utilidades, escolhe a melhor acao
        # e executa essa acao.
        self.recarga_tiro = max(0, self.recarga_tiro - delta_time)
        self.calcular_utilidades(jogador, kits_vida)
        self.escolher_acao()
        tiro = self.executar_acao(jogador, kits_vida, delta_time)
        self.tempo_flash_ataque = max(0, self.tempo_flash_ataque - delta_time)
        self.tempo_troca_acao = max(0, self.tempo_troca_acao - delta_time)
        return tiro

    # Calcula quanto cada acao vale no momento atual.
    def calcular_utilidades(self, jogador: Jogador, kits_vida: list[KitVida]) -> None:
        distancia_jogador = calcular_distancia(
            self.sprite.center_x,
            self.sprite.center_y,
            jogador.sprite.center_x,
            jogador.sprite.center_y,
        )

        # Valores normalizados entre 0 e 1.
        # jogador_perto cresce quando o jogador se aproxima do NPC.
        jogador_perto = 1 - limitar((distancia_jogador - 60) / 220, 0, 1)
        jogador_longe = limitar((distancia_jogador - 170) / 360, 0, 1)
        porcentagem_vida = self.vida / VIDA_MAXIMA
        vida_baixa = 1 - porcentagem_vida
        jogador_fraco = 1 - (jogador.vida / VIDA_MAXIMA)

        kit_mais_perto = self.encontrar_kit_vida_mais_perto(kits_vida)
        pontuacao_kit = 0
        if kit_mais_perto is not None:
            distancia_kit = calcular_distancia(self.sprite.center_x, self.sprite.center_y, kit_mais_perto.x, kit_mais_perto.y)
            pontuacao_kit = 1 - limitar(distancia_kit / 520, 0, 1)

        # Formula da Utility AI:
        # cada acao recebe uma pontuacao. A maior pontuacao vence.
        pontuacao_atacar = limitar(
            0.08 + jogador_perto * 0.76 + porcentagem_vida * 0.18 + jogador_fraco * 0.18 - vida_baixa * 0.38,
            0,
            1,
        )
        pontuacao_fugir = limitar(
            vida_baixa * 0.70 + jogador_perto * 0.38 - pontuacao_kit * 0.18,
            0,
            1,
        )
        pontuacao_buscar_vida = limitar(
            vida_baixa * 0.82 + pontuacao_kit * 0.24 - jogador_perto * 0.16,
            0,
            1,
        )
        if kit_mais_perto is None or self.vida >= 92:
            pontuacao_buscar_vida = 0

        pontuacao_patrulhar = limitar(
            0.18 + jogador_longe * 0.42 + porcentagem_vida * 0.30 - vida_baixa * 0.22 - jogador_perto * 0.30,
            0,
            1,
        )

        self.pontuacoes = [
            PontuacaoUtilidade(self.ATACAR, pontuacao_atacar, COR_ATAQUE),
            PontuacaoUtilidade(self.FUGIR, pontuacao_fugir, COR_FUGA),
            PontuacaoUtilidade(self.BUSCAR_VIDA, pontuacao_buscar_vida, COR_VIDA),
            PontuacaoUtilidade(self.PATRULHAR, pontuacao_patrulhar, COR_PATRULHA),
        ]

    # Escolhe a acao com maior pontuacao de utilidade.
    def escolher_acao(self) -> None:
        melhor = max(self.pontuacoes, key=lambda item: item.valor)
        self.acao_atual = melhor.nome

        if self.acao_atual != self.acao_anterior:
            self.tempo_troca_acao = 0.45
            self.acao_anterior = self.acao_atual

    # Executa o comportamento correspondente a acao escolhida pela Utility AI.
    def executar_acao(self, jogador: Jogador, kits_vida: list[KitVida], delta_time: float) -> Optional[Tiro]:
        if self.acao_atual == self.ATACAR:
            self.alvo_x = jogador.sprite.center_x
            self.alvo_y = jogador.sprite.center_y
            distancia_jogador = calcular_distancia(
                self.sprite.center_x,
                self.sprite.center_y,
                jogador.sprite.center_x,
                jogador.sprite.center_y,
            )

            # Se estiver longe, o NPC se aproxima. Se estiver perto, ele para
            # e apenas mira/atira.
            if distancia_jogador > DISTANCIA_SEGURA_NPC:
                mover_em_direcao(self.sprite, self.alvo_x, self.alvo_y, VELOCIDADE_ATAQUE_NPC, delta_time)
            else:
                direcao_x, direcao_y = normalizar(
                    jogador.sprite.center_x - self.sprite.center_x,
                    jogador.sprite.center_y - self.sprite.center_y,
                )
                if direcao_x != 0 or direcao_y != 0:
                    self.sprite.angle = angulo_do_vetor(direcao_x, direcao_y)

            return self.atirar_no_jogador(jogador)

        if self.acao_atual == self.FUGIR:
            self.alvo_x, self.alvo_y = self.encontrar_ponto_de_fuga(jogador)
            mover_em_direcao(self.sprite, self.alvo_x, self.alvo_y, VELOCIDADE_FUGA_NPC, delta_time)
            return None

        if self.acao_atual == self.BUSCAR_VIDA:
            kit = self.encontrar_kit_vida_mais_perto(kits_vida)
            if kit is None:
                return None

            self.alvo_x = kit.x
            self.alvo_y = kit.y
            mover_em_direcao(self.sprite, self.alvo_x, self.alvo_y, VELOCIDADE_BUSCAR_VIDA_NPC, delta_time)
            if calcular_distancia(self.sprite.center_x, self.sprite.center_y, kit.x, kit.y) <= 30:
                self.vida = limitar(self.vida + 48, 0, VIDA_MAXIMA)
                kit.coletar()
            return None

        self.patrulhar(delta_time)
        return None

    # Cria um tiro do NPC contra o jogador quando alcance e recarga permitem.
    def atirar_no_jogador(self, jogador: Jogador) -> Optional[Tiro]:
        distancia_tiro = calcular_distancia(
            self.sprite.center_x,
            self.sprite.center_y,
            jogador.sprite.center_x,
            jogador.sprite.center_y,
        )

        if self.recarga_tiro > 0 or distancia_tiro > ALCANCE_TIRO_NPC:
            return None

        self.recarga_tiro = RECARGA_TIRO_NPC
        self.tempo_flash_ataque = 0.14

        return Tiro(
            self.sprite.center_x,
            self.sprite.center_y,
            jogador.sprite.center_x,
            jogador.sprite.center_y,
            VELOCIDADE_TIRO_NPC,
            DANO_TIRO_NPC,
            COR_NPC,
            "npc",
        )

    # Move o NPC entre os pontos fixos da rota de patrulha.
    def patrulhar(self, delta_time: float) -> None:
        self.alvo_x, self.alvo_y = self.pontos_patrulha[self.indice_patrulha]

        if calcular_distancia(self.sprite.center_x, self.sprite.center_y, self.alvo_x, self.alvo_y) <= 18:
            # Encaixa exatamente no cruzamento antes de escolher o proximo alvo.
            # Isso evita que pequenos desvios facam o tanque parecer andar de lado.
            self.sprite.center_x = self.alvo_x
            self.sprite.center_y = self.alvo_y
            self.indice_patrulha = (self.indice_patrulha + 1) % len(self.pontos_patrulha)
            self.alvo_x, self.alvo_y = self.pontos_patrulha[self.indice_patrulha]

        mover_em_direcao(self.sprite, self.alvo_x, self.alvo_y, VELOCIDADE_PATRULHA_NPC, delta_time)

    # Procura o kit de vida ativo mais proximo do NPC.
    def encontrar_kit_vida_mais_perto(self, kits_vida: list[KitVida]) -> Optional[KitVida]:
        kits_ativos = [kit for kit in kits_vida if kit.ativo]
        if not kits_ativos:
            return None

        return min(
            kits_ativos,
            key=lambda kit: calcular_distancia(self.sprite.center_x, self.sprite.center_y, kit.x, kit.y),
        )

    # Escolhe o ponto de fuga mais distante do jogador.
    def encontrar_ponto_de_fuga(self, jogador: Jogador) -> tuple[float, float]:
        pontos_possiveis = [
            (ARENA_ESQUERDA + 82, ARENA_BAIXO + 82),
            (ARENA_ESQUERDA + 82, ARENA_CIMA - 82),
            (ARENA_DIREITA - 82, ARENA_BAIXO + 82),
            (ARENA_DIREITA - 82, ARENA_CIMA - 82),
        ]

        return max(
            pontos_possiveis,
            key=lambda ponto: calcular_distancia(ponto[0], ponto[1], jogador.sprite.center_x, jogador.sprite.center_y),
        )

    # Retorna a cor usada para representar a acao atual do NPC.
    def cor_da_acao(self) -> tuple[int, int, int]:
        if self.acao_atual == self.ATACAR:
            return COR_ATAQUE
        if self.acao_atual == self.FUGIR:
            return COR_FUGA
        if self.acao_atual == self.BUSCAR_VIDA:
            return COR_VIDA
        return COR_PATRULHA

    # Desenha a linha ate o alvo e o estado atual da IA.
    def desenhar_debug(self) -> None:
        cor = self.cor_da_acao()
        espessura_anel = 5 if self.tempo_troca_acao > 0 else 3

        arcade.draw_line(self.sprite.center_x, self.sprite.center_y, self.alvo_x, self.alvo_y, cor, 4)
        arcade.draw_circle_filled(self.alvo_x, self.alvo_y, 18, (cor[0], cor[1], cor[2], 48))
        arcade.draw_circle_outline(self.alvo_x, self.alvo_y, 18, cor, 3)
        arcade.draw_circle_outline(self.sprite.center_x, self.sprite.center_y, 36, cor, espessura_anel)

        if self.acao_atual == self.ATACAR:
            arcade.draw_circle_outline(self.sprite.center_x, self.sprite.center_y, ALCANCE_TIRO_NPC, COR_PERIGO, 2)

        if self.tempo_flash_ataque > 0:
            arcade.draw_circle_filled(self.sprite.center_x, self.sprite.center_y, 48, (255, 88, 66, 42))

        if self.acao_atual == self.BUSCAR_VIDA:
            icone_x = self.sprite.center_x
            icone_y = self.sprite.center_y + 70
            arcade.draw_circle_filled(icone_x, icone_y, 15, (35, 118, 73, 220))
            arcade.draw_line(icone_x - 8, icone_y, icone_x + 8, icone_y, BRANCO, 4)
            arcade.draw_line(icone_x, icone_y - 8, icone_x, icone_y + 8, BRANCO, 4)
            arcade.draw_circle_outline(icone_x, icone_y, 16, COR_VIDA, 2)

        arcade.draw_text(self.acao_atual, self.sprite.center_x, self.sprite.center_y + 48, BRANCO, 12, anchor_x="center")


# Controla a janela principal e organiza desenho, atualizacao e eventos.
class Jogo(arcade.Window):
    # Inicializa a janela, os personagens, as listas de sprites e as texturas.
    def __init__(self) -> None:
        super().__init__(LARGURA_TELA, ALTURA_TELA, TITULO_TELA)
        arcade.set_background_color(COR_FUNDO)

        self.jogador = Jogador()
        self.npc = NpcUtilidade()

        self.lista_jogador = arcade.SpriteList()
        self.lista_npc = arcade.SpriteList()
        self.lista_cenario = arcade.SpriteList()
        self.lista_particulas = arcade.SpriteList()
        self.lista_tiros_jogador = arcade.SpriteList()
        self.lista_tiros_npc = arcade.SpriteList()
        self.kits_vida: list[KitVida] = []

        self.tiles_chao: list[tuple[float, float, arcade.Texture]] = []
        self.textura_vida = arcade.load_texture(TEXTURA_VIDA)
        self.textura_icone_jogador = arcade.load_texture(TEXTURA_JOGADOR)
        self.textura_icone_npc = arcade.load_texture(TEXTURA_NPC)
        self.textura_grama_1 = arcade.load_texture(TEXTURA_GRAMA_1)
        self.textura_grama_2 = arcade.load_texture(TEXTURA_GRAMA_2)
        self.textura_rua_horizontal = arcade.load_texture(TEXTURA_RUA_HORIZONTAL)
        self.textura_rua_vertical = arcade.load_texture(TEXTURA_RUA_VERTICAL)
        self.textura_cruzamento = arcade.load_texture(TEXTURA_CRUZAMENTO)

    # Prepara ou reinicia o jogo.
    def setup(self) -> None:
        self.jogador.configurar()
        self.npc.configurar()

        self.lista_jogador = arcade.SpriteList()
        self.lista_npc = arcade.SpriteList()
        self.lista_cenario = arcade.SpriteList()
        self.lista_particulas = arcade.SpriteList()
        self.lista_tiros_jogador = arcade.SpriteList()
        self.lista_tiros_npc = arcade.SpriteList()

        self.lista_jogador.append(self.jogador.sprite)
        self.lista_npc.append(self.npc.sprite)

        self.criar_tiles_da_arena()
        self.criar_objetos_do_cenario()

        self.kits_vida = [
            KitVida(116, 292, self.textura_vida),
            KitVida(520, 360, self.textura_vida),
            KitVida(820, 448, self.textura_vida),
        ]

        self.npc.calcular_utilidades(self.jogador, self.kits_vida)

    # Monta o chao com grama e ruas em formato de malha.
    def criar_tiles_da_arena(self) -> None:
        self.tiles_chao = []
        colunas = int((ARENA_DIREITA - ARENA_ESQUERDA) / TAMANHO_TILE)
        linhas = int((ARENA_CIMA - ARENA_BAIXO) / TAMANHO_TILE)
        coluna_rua_esquerda = 3
        coluna_rua_direita = 11
        linha_rua_baixo = 1
        linha_rua_cima = 8

        for linha in range(linhas):
            for coluna in range(colunas):
                x = ARENA_ESQUERDA + TAMANHO_TILE / 2 + coluna * TAMANHO_TILE
                y = ARENA_BAIXO + TAMANHO_TILE / 2 + linha * TAMANHO_TILE

                tem_rua_vertical = coluna in (coluna_rua_esquerda, coluna_rua_direita)
                tem_rua_horizontal = linha in (linha_rua_baixo, linha_rua_cima)

                if tem_rua_vertical and tem_rua_horizontal:
                    textura = self.textura_cruzamento
                elif tem_rua_horizontal:
                    textura = self.textura_rua_horizontal
                elif tem_rua_vertical:
                    textura = self.textura_rua_vertical
                elif (linha + coluna) % 4 == 0:
                    textura = self.textura_grama_2
                else:
                    textura = self.textura_grama_1

                self.tiles_chao.append((x, y, textura))

    # Adiciona caixas e objetos decorativos para deixar o mapa mais vivo.
    def criar_objetos_do_cenario(self) -> None:
        objetos = [
            (96, 484, TEXTURA_CAIXA, 0.34, 8),
            (160, 484, TEXTURA_CAIXA, 0.28, -4),
            (536, 488, TEXTURA_CAIXA, 0.30, -12),
            (604, 248, TEXTURA_CAIXA, 0.28, 18),
        ]

        for x, y, textura, escala, angulo in objetos:
            objeto = arcade.Sprite(textura, scale=escala)
            objeto.center_x = x
            objeto.center_y = y
            objeto.angle = angulo
            self.lista_cenario.append(objeto)

    # Desenha a tela a cada quadro chamado pela Arcade.
    def on_draw(self) -> None:
        self.clear()
        self.desenhar_arena()
        self.desenhar_rota_patrulha()

        for kit in self.kits_vida:
            kit.desenhar()

        self.jogador.desenhar_flash_tiro()
        self.npc.desenhar_debug()

        self.lista_cenario.draw()
        self.lista_tiros_jogador.draw()
        self.lista_tiros_npc.draw()
        self.lista_jogador.draw()
        self.lista_npc.draw()
        self.lista_particulas.draw()

        self.desenhar_painel()

    # Atualiza a logica do jogo a cada quadro chamado pela Arcade.
    def on_update(self, delta_time: float) -> None:
        for kit in self.kits_vida:
            kit.atualizar(delta_time)

        self.lista_particulas.update(delta_time)
        self.lista_tiros_jogador.update(delta_time)
        self.lista_tiros_npc.update(delta_time)
        self.verificar_colisoes_dos_tiros()

        if self.jogador.vida > 0 and self.npc.vida > 0:
            self.jogador.atualizar(delta_time)
            acao_antiga = self.npc.acao_atual
            tiro_npc = self.npc.atualizar(self.jogador, self.kits_vida, delta_time)

            if tiro_npc is not None:
                self.lista_tiros_npc.append(tiro_npc)
                self.criar_particulas(self.npc.sprite.center_x, self.npc.sprite.center_y, COR_NPC, 8, 90)

            if self.npc.acao_atual != acao_antiga:
                self.criar_particulas(self.npc.sprite.center_x, self.npc.sprite.center_y, self.npc.cor_da_acao(), 18, 120)

    # Trata eventos de teclado para mover, atirar e reiniciar.
    def on_key_press(self, key: int, modifiers: int) -> None:
        if key == arcade.key.R:
            self.setup()
            return

        if key == arcade.key.SPACE:
            tiro = self.jogador.atirar_para(self.npc.sprite.center_x, self.npc.sprite.center_y)
            if tiro is not None:
                self.lista_tiros_jogador.append(tiro)
                self.criar_particulas(self.jogador.sprite.center_x, self.jogador.sprite.center_y, COR_JOGADOR, 8, 95)
            else:
                self.criar_particulas(self.jogador.sprite.center_x, self.jogador.sprite.center_y, CINZA_FRACO, 10, 80)
            return

        self.jogador.pressionar_tecla(key)

    # Trata a tecla solta para interromper movimentos do jogador.
    def on_key_release(self, key: int, modifiers: int) -> None:
        self.jogador.soltar_tecla(key)

    # Cria varias particulas flutuantes em uma posicao da arena.
    def criar_particulas(self, x: float, y: float, cor: tuple[int, int, int], quantidade: int, velocidade: float) -> None:
        for _ in range(quantidade):
            self.lista_particulas.append(ParticulaFlutuante(x, y, cor, velocidade))

    # Aplica dano quando tiros acertam o alvo.
    def verificar_colisoes_dos_tiros(self) -> None:
        tiros_que_acertaram_npc = arcade.check_for_collision_with_list(self.npc.sprite, self.lista_tiros_jogador)
        for tiro in tiros_que_acertaram_npc:
            tiro.remove_from_sprite_lists()
            self.npc.vida = limitar(self.npc.vida - tiro.dano, 0, VIDA_MAXIMA)
            self.criar_particulas(self.npc.sprite.center_x, self.npc.sprite.center_y, COR_ATAQUE, 22, 190)

        tiros_que_acertaram_jogador = arcade.check_for_collision_with_list(self.jogador.sprite, self.lista_tiros_npc)
        for tiro in tiros_que_acertaram_jogador:
            tiro.remove_from_sprite_lists()
            self.jogador.vida = limitar(self.jogador.vida - tiro.dano, 0, VIDA_MAXIMA)
            self.criar_particulas(self.jogador.sprite.center_x, self.jogador.sprite.center_y, COR_PERIGO, 18, 175)

    # Desenha o fundo, os tiles e a borda da arena.
    def desenhar_arena(self) -> None:
        arcade.draw_lrbt_rectangle_filled(
            left=ARENA_ESQUERDA - 10,
            right=ARENA_DIREITA + 10,
            bottom=ARENA_BAIXO - 10,
            top=ARENA_CIMA + 10,
            color=(8, 12, 18),
        )

        for x, y, textura in self.tiles_chao:
            arcade.draw_texture_rect(texture=textura, rect=retangulo_centralizado(x, y, TAMANHO_TILE, TAMANHO_TILE))

        arcade.draw_lrbt_rectangle_filled(
            left=ARENA_ESQUERDA,
            right=ARENA_DIREITA,
            bottom=ARENA_BAIXO,
            top=ARENA_CIMA,
            color=(8, 12, 18, 28),
        )

        arcade.draw_lrbt_rectangle_outline(
            left=ARENA_ESQUERDA,
            right=ARENA_DIREITA,
            bottom=ARENA_BAIXO,
            top=ARENA_CIMA,
            color=(94, 109, 132),
            border_width=4,
        )
        arcade.draw_lrbt_rectangle_outline(
            left=ARENA_ESQUERDA + 8,
            right=ARENA_DIREITA - 8,
            bottom=ARENA_BAIXO + 8,
            top=ARENA_CIMA - 8,
            color=(28, 39, 55),
            border_width=2,
        )

    # Mostra no mapa o caminho que o NPC usa enquanto patrulha.
    def desenhar_rota_patrulha(self) -> None:
        pontos = self.npc.pontos_patrulha
        for indice, ponto in enumerate(pontos):
            proximo_ponto = pontos[(indice + 1) % len(pontos)]
            arcade.draw_line(ponto[0], ponto[1], proximo_ponto[0], proximo_ponto[1], (118, 85, 179, 130), 3)
            arcade.draw_circle_filled(ponto[0], ponto[1], 9, (178, 126, 255, 70))
            arcade.draw_circle_outline(ponto[0], ponto[1], 12, COR_PATRULHA, 2)

    # Desenha o painel lateral com vida, acao atual, utilidades e controles.
    def desenhar_painel(self) -> None:
        arcade.draw_lrbt_rectangle_filled(
            left=PAINEL_ESQUERDA - 18,
            right=LARGURA_TELA - 24,
            bottom=40,
            top=ALTURA_TELA - 40,
            color=COR_PAINEL,
        )
        arcade.draw_lrbt_rectangle_outline(
            left=PAINEL_ESQUERDA - 18,
            right=LARGURA_TELA - 24,
            bottom=40,
            top=ALTURA_TELA - 40,
            color=COR_BORDA_PAINEL,
            border_width=2,
        )

        arcade.draw_text("Utility AI Simplificada", PAINEL_ESQUERDA, 648, BRANCO, 23)
        arcade.draw_text("DEMONSTRAÇÃO", PAINEL_ESQUERDA, 622, CINZA_TEXTO, 14)

        self.desenhar_status_vida(
            PAINEL_ESQUERDA,
            558,
            220,
            self.jogador.vida / VIDA_MAXIMA,
            COR_JOGADOR,
            "Vida jogador",
            self.textura_icone_jogador,
        )
        self.desenhar_status_vida(
            PAINEL_ESQUERDA,
            512,
            220,
            self.npc.vida / VIDA_MAXIMA,
            COR_NPC,
            "Vida NPC",
            self.textura_icone_npc,
        )

        cor_acao = self.npc.cor_da_acao()
        arcade.draw_lrbt_rectangle_filled(
            left=PAINEL_ESQUERDA,
            right=PAINEL_ESQUERDA + 238,
            bottom=450,
            top=482,
            color=(28, 35, 49),
        )
        arcade.draw_lrbt_rectangle_outline(
            left=PAINEL_ESQUERDA,
            right=PAINEL_ESQUERDA + 238,
            bottom=450,
            top=482,
            color=cor_acao,
            border_width=2,
        )
        arcade.draw_text("Acao atual", PAINEL_ESQUERDA + 12, 460, CINZA_TEXTO, 11)
        arcade.draw_text(self.npc.acao_atual, PAINEL_ESQUERDA + 95, 457, BRANCO, 16)

        arcade.draw_text("Matriz de utilidade", PAINEL_ESQUERDA, 416, BRANCO, 15)

        y = 382
        pontuacoes_ordenadas = sorted(self.npc.pontuacoes, key=lambda item: item.valor, reverse=True)
        for indice, pontuacao in enumerate(pontuacoes_ordenadas):
            marcador = ">" if indice == 0 else " "
            self.desenhar_linha_utilidade(PAINEL_ESQUERDA, y, 238, pontuacao, marcador)
            y -= 50

        arcade.draw_line(PAINEL_ESQUERDA, 178, LARGURA_TELA - 48, 178, (50, 60, 78), 2)
        arcade.draw_text("Controles", PAINEL_ESQUERDA, 148, BRANCO, 14)
        arcade.draw_text("WASD / setas    mover", PAINEL_ESQUERDA, 124, CINZA_TEXTO, 12)
        arcade.draw_text("Espaco          atirar", PAINEL_ESQUERDA, 102, CINZA_TEXTO, 12)
        arcade.draw_text("R               reiniciar", PAINEL_ESQUERDA, 80, CINZA_TEXTO, 12)

        if self.jogador.vida <= 0:
            arcade.draw_text("Jogador derrotado", PAINEL_ESQUERDA, 55, COR_PERIGO, 14)
        elif self.npc.vida <= 0:
            arcade.draw_text("NPC desativado", PAINEL_ESQUERDA, 55, COR_ATAQUE, 14)

    # Desenha uma barra horizontal usada para vida e valores proporcionais.
    def desenhar_barra(
        self,
        x: float,
        y: float,
        largura: float,
        altura: float,
        porcentagem: float,
        cor: tuple[int, int, int],
        texto: str,
    ) -> None:
        porcentagem = limitar(porcentagem, 0, 1)
        arcade.draw_text(texto, x, y + altura + 6, CINZA_TEXTO, 12)
        arcade.draw_lbwh_rectangle_filled(x, y, largura, altura, (45, 54, 69))
        arcade.draw_lbwh_rectangle_filled(x, y, largura * porcentagem, altura, cor)
        arcade.draw_lrbt_rectangle_outline(
            left=x,
            right=x + largura,
            bottom=y,
            top=y + altura,
            color=(94, 105, 124),
            border_width=1,
        )

    # Desenha o icone e a barra de vida de um personagem.
    def desenhar_status_vida(
        self,
        x: float,
        y: float,
        largura: float,
        porcentagem: float,
        cor: tuple[int, int, int],
        texto: str,
        textura_icone: arcade.Texture,
    ) -> None:
        icone_x = x + 12
        icone_y = y + 8
        barra_x = x + 34
        largura_barra = largura - 34

        arcade.draw_texture_rect(texture=textura_icone, rect=retangulo_centralizado(icone_x, icone_y, 24, 24))
        self.desenhar_barra(barra_x, y, largura_barra, 17, porcentagem, cor, texto)

    # Desenha uma linha da matriz de utilidade do NPC.
    def desenhar_linha_utilidade(
        self,
        x: float,
        y: float,
        largura: float,
        pontuacao: PontuacaoUtilidade,
        marcador: str,
    ) -> None:
        texto_x = x
        if pontuacao.nome == self.npc.BUSCAR_VIDA:
            icone_x = x + 9
            icone_y = y + 27
            arcade.draw_circle_filled(icone_x, icone_y, 7, (35, 118, 73, 230))
            arcade.draw_line(icone_x - 4, icone_y, icone_x + 4, icone_y, BRANCO, 2)
            arcade.draw_line(icone_x, icone_y - 4, icone_x, icone_y + 4, BRANCO, 2)
            arcade.draw_circle_outline(icone_x, icone_y, 8, COR_VIDA, 1)
            texto_x = x + 22

        arcade.draw_text(f"{marcador} {pontuacao.nome}", texto_x, y + 20, BRANCO, 12)
        arcade.draw_text(f"{pontuacao.valor:.2f}", x + largura - 34, y + 20, CINZA_TEXTO, 12)
        arcade.draw_lbwh_rectangle_filled(x, y, largura, 15, (43, 51, 65))
        arcade.draw_lbwh_rectangle_filled(x, y, largura * pontuacao.valor, 15, pontuacao.cor)
        arcade.draw_lrbt_rectangle_outline(
            left=x,
            right=x + largura,
            bottom=y,
            top=y + 15,
            color=(84, 96, 116),
            border_width=1,
        )


# Cria a janela, prepara o jogo e inicia o loop principal da Arcade.
def main() -> None:
    jogo = Jogo()
    jogo.setup()
    arcade.run()


if __name__ == "__main__":
    main()

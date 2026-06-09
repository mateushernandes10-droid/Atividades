# ####################################
# #   CÓDIGO 001 - Estrutura básica
# ####################################
# import arcade

# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600
# SCREEN_TITLE = "Estrutura básica"

# class Game(arcade.Window):
#     # Método executado uma vez, ao criar a janela
#     def __init__(self):
#         # A função super() chama o construtor da classe base (arcade.Window),
#         # configurando efetivamente as dimensões e título no sistema operacional.
#         super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
#         arcade.set_background_color(arcade.color.DARK_BLUE)
#     # Método para preparar variáveis, jogadores e listas (reiniciável)
#     def setup(self):
#         pass
#     # Método chamado cerca de 60 vezes por segundo EXCLUSIVAMENTE para desenhar
#     def on_draw(self):
#         self.clear() # Limpa o quadro anterior
#     # Método chamado cerca de 60 vezes por segundo para LÓGICA (física, movimento)
#     def on_update(self, delta_time):
#         pass

# if __name__ == "__main__":
#     game = Game()
#     game.setup()
#     # Inicia o laço infinito interno da biblioteca (substitui o 'while True')
#     arcade.run()


####################################
#   CÓDIGO 002 - Primitivas
####################################

# import arcade
# class Game(arcade.Window):
#    def __init__(self):
#        # Inicializa a janela da Arcade
#        # super().__init__ prepara internamente
#        # toda a estrutura da janela
#        super().__init__(800, 600, "Retângulos")
#    def on_draw(self):
#        # Limpa a tela antes de desenhar
#        self.clear()
#        # Desenha um retângulo preenchido
#        # usando left, bottom, width e height
#        arcade.draw_lbwh_rectangle_filled(
#            # Distância da esquerda
#            left=100,

#            # Distância da parte inferior
#            bottom=100,
#            # Largura do retângulo
#            width=200,
#            # Altura do retângulo
#            height=80,
#            # Cor do preenchimento
#            color=arcade.color.RED
#        )
#        # Desenha apenas o contorno
#        # usando left, right, bottom e top
#        arcade.draw_lrbt_rectangle_outline(
#            # Limite esquerdo
#            left=400,
#            # Limite direito
#            right=650,
#            # Limite inferior
#            bottom=150,
#            # Limite superior
#            top=260,
#            # Cor do contorno
#            color=arcade.color.WHITE,
#            # Espessura da borda
#            border_width=3
#        )
# # Cria a janela do jogo
# Game()
# # Inicia o game loop da Arcade
# arcade.run()


####################################
#   CÓDIGO 003 - Plano 2D
####################################

# import arcade

# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600
# SCREEN_TITLE = "Coordenadas"

# class Game(arcade.Window):
#     def __init__(self):
#         super().__init__(
#             SCREEN_WIDTH,
#             SCREEN_HEIGHT,
#             SCREEN_TITLE
#         )

#         self.player = arcade.SpriteSolidColor(
#             width=64,
#             height=64,
#             color=arcade.color.BLUE
#         )

#         self.player.center_x = 400
#         self.player.center_y = 300

#         self.player_list = arcade.SpriteList()
#         self.player_list.append(self.player)

#     def on_draw(self):
#         self.clear()

#         self.player_list.draw()

#         # Desenha linhas centrais
#         arcade.draw_line(
#             0,
#             SCREEN_HEIGHT / 2,
#             SCREEN_WIDTH,
#             SCREEN_HEIGHT / 2,
#             arcade.color.RED,
#             2
#         )

#         arcade.draw_line(
#             SCREEN_WIDTH / 2,
#             0,
#             SCREEN_WIDTH / 2,
#             SCREEN_HEIGHT,
#             arcade.color.GREEN,
#             2
#         )

#         # Mostra coordenadas
#         arcade.draw_text(
#             f"X: {self.player.center_x}",
#             10,
#             40,
#             arcade.color.WHITE,
#             18
#         )

#         arcade.draw_text(
#             f"Y: {self.player.center_y}",
#             10,
#             10,
#             arcade.color.WHITE,
#             18
#         )

# game = Game()
# arcade.run()





####################################
#   CÓDIGO 004 - Delta time
####################################


# import arcade


# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600

# # Velocidade em pixels por segundo
# MOVE_SPEED = 300


# class Game(arcade.Window):

#     def __init__(self):

#         super().__init__(
#             SCREEN_WIDTH,
#             SCREEN_HEIGHT,
#             "Delta Time"
#         )

#         self.player = arcade.SpriteSolidColor(
#             width=50,
#             height=50,
#             color=arcade.color.BLUE
#         )

#         self.player.center_x = 400
#         self.player.center_y = 300

#         self.player_list = arcade.SpriteList()
#         self.player_list.append(self.player)

#     def on_key_press(self, key, modifiers):

#         if key == arcade.key.RIGHT:
#             self.player.change_x = MOVE_SPEED

#         elif key == arcade.key.LEFT:
#             self.player.change_x = -MOVE_SPEED

#     def on_key_release(self, key, modifiers):

#         if key == arcade.key.RIGHT:
#             self.player.change_x = 0

#         elif key == arcade.key.LEFT:
#             self.player.change_x = 0

#     def on_update(self, delta_time):

#         # Mostra o tempo entre os frames
#         print(delta_time)

#         # Movimento baseado em tempo
#         self.player.center_x += self.player.change_x * delta_time

#     def on_draw(self):

#         self.clear()

#         self.player_list.draw()


# game = Game()
# arcade.run()




####################################
#   CÓDIGO 005
####################################
# import arcade


# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600

# # Velocidade em pixels por segundo
# MOVE_SPEED = 300


# class Game(arcade.Window):

#     def __init__(self):

#         super().__init__(
#             SCREEN_WIDTH,
#             SCREEN_HEIGHT,
#             "Game Loop"
#         )

#         self.player = arcade.SpriteSolidColor(
#             width=50,
#             height=50,
#             color=arcade.color.BLUE
#         )

#         self.player.center_x = 400
#         self.player.center_y = 300

#         self.player_list = arcade.SpriteList()
#         self.player_list.append(self.player)

#     def on_key_press(self, key, modifiers):

#         print("KEY PRESS")

#         if key == arcade.key.RIGHT:
#             self.player.change_x = MOVE_SPEED

#         elif key == arcade.key.LEFT:
#             self.player.change_x = -MOVE_SPEED

#     def on_key_release(self, key, modifiers):

#         print("KEY RELEASE")

#         if (
#             key == arcade.key.RIGHT
#             or key == arcade.key.LEFT
#         ):
#             self.player.change_x = 0

#     def on_update(self, delta_time):

#         print(
#             f"UPDATE - delta_time: "
#             f"{delta_time:.4f}"
#         )

#         # Movimento baseado em tempo
#         self.player.center_x += (
#             self.player.change_x * delta_time
#         )

#     def on_draw(self):

#         print("DRAW")

#         self.clear()

#         self.player_list.draw()


# game = Game()
# arcade.run()



####################################
#   CÓDIGO 006 - Sprites/Colisão
####################################

# import arcade
# import random
# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600
# SCREEN_TITLE = "Sprites, SpriteLists e Colisão"

# class Game(arcade.Window):
#    def __init__(self):
#        # Inicializa a janela principal da Arcade
#        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
#        # Lista onde ficará o jogador
#        self.player_list = arcade.SpriteList()
#        # Lista onde ficarão as moedas
#        self.coin_list = arcade.SpriteList()
#        # Referência direta ao jogador
#        self.player = None
#        # Pontuação inicial
#        self.score = 0

#    def setup(self):
#        # Cria o sprite do jogador usando imagem interna da Arcade
#        self.player = arcade.Sprite(
#            ":resources:images/animated_characters/male_person/malePerson_idle.png",
#            scale=0.5
#        )
#        # Define posição inicial do jogador
#        self.player.center_x = 400
#        self.player.center_y = 300
#        # Adiciona jogador à SpriteList
#        self.player_list.append(self.player)
#        # Cria 10 moedas em posições aleatórias
#        for i in range(10):
#            coin = arcade.Sprite(
#                ":resources:images/items/coinGold.png",
#                scale=0.5
#            )
#            # Sorteia posição horizontal
#            coin.center_x = random.randint(50, 750)
#            # Sorteia posição vertical
#            coin.center_y = random.randint(50, 550)
#            # Adiciona moeda à lista de moedas
#            self.coin_list.append(coin)
#    def on_draw(self):
#        # Limpa a tela
#        self.clear()
#        # Desenha primeiro as moedas
#        self.coin_list.draw()
#        # Desenha depois o jogador
#        self.player_list.draw()
#        # Desenha a pontuação na tela
#        arcade.draw_text(
#            f"Pontos: {self.score}",
#            10,
#            10,
#            arcade.color.WHITE,
#            18
#        )
#    def on_mouse_motion(self, x, y, dx, dy):
#        # Move o jogador para a posição do mouse
#        self.player.center_x = x
#        self.player.center_y = y

#    def on_update(self, delta_time):
#        # Verifica quais moedas colidiram com o jogador
#        hit_list = arcade.check_for_collision_with_list(
#            self.player,
#            self.coin_list
#        )
#        # Para cada moeda tocada
#        for coin in hit_list:
#            # Remove a moeda de todas as SpriteLists
#            coin.remove_from_sprite_lists()
#            # Soma um ponto
#            self.score += 1
# game = Game()
# game.setup()
# arcade.run()



####################################
#   CÓDIGO 007 - Tiros
####################################

# import arcade


# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600
# SCREEN_TITLE = "Tiros do jogador e dos inimigos"

# # Velocidades em pixels por segundo
# PLAYER_SPEED = 300
# BULLET_SPEED = 600


# class Bullet(arcade.Sprite):

#     def __init__(self, direction, color):

#         super().__init__()

#         self.texture = arcade.make_soft_square_texture(
#             size=12,
#             color=color,
#             outer_alpha=255
#         )

#         self.change_x = BULLET_SPEED * direction

#     def update_bullet(self, delta_time):

#         self.center_x += self.change_x * delta_time

#         if self.center_x < 0 or self.center_x > SCREEN_WIDTH:
#             self.remove_from_sprite_lists()


# class Game(arcade.Window):

#     def __init__(self):

#         super().__init__(
#             SCREEN_WIDTH,
#             SCREEN_HEIGHT,
#             SCREEN_TITLE
#         )

#         arcade.set_background_color(arcade.color.DARK_BLUE)

#         self.player = None
#         self.player_list = arcade.SpriteList()

#         self.enemy_list = arcade.SpriteList()

#         self.player_bullet_list = arcade.SpriteList()
#         self.enemy_bullet_list = arcade.SpriteList()

#         self.player_life = 3
#         self.score = 0

#         self.enemy_shoot_timer = 0

#     def setup(self):

#         self.player = arcade.SpriteSolidColor(
#             width=50,
#             height=50,
#             color=arcade.color.BLUE
#         )

#         self.player.center_x = 100
#         self.player.center_y = 300
#         self.player_list.append(self.player)

#         for x in range(500, 751, 100):

#             enemy = arcade.SpriteSolidColor(
#                 width=40,
#                 height=40,
#                 color=arcade.color.RED
#             )

#             enemy.center_x = x
#             enemy.center_y = 300
#             self.enemy_list.append(enemy)

#     def shoot_player_bullet(self):

#         bullet = Bullet(
#             direction=1,
#             color=arcade.color.YELLOW
#         )

#         bullet.center_x = self.player.center_x + 30
#         bullet.center_y = self.player.center_y

#         self.player_bullet_list.append(bullet)

#     def shoot_enemy_bullet(self, enemy):

#         bullet = Bullet(
#             direction=-1,
#             color=arcade.color.ORANGE
#         )

#         bullet.center_x = enemy.center_x - 30
#         bullet.center_y = enemy.center_y

#         self.enemy_bullet_list.append(bullet)

#     def on_key_press(self, key, modifiers):

#         if key == arcade.key.UP:
#             self.player.change_y = PLAYER_SPEED

#         elif key == arcade.key.DOWN:
#             self.player.change_y = -PLAYER_SPEED

#         elif key == arcade.key.SPACE:
#             self.shoot_player_bullet()

#     def on_key_release(self, key, modifiers):

#         if key in (arcade.key.UP, arcade.key.DOWN):
#             self.player.change_y = 0

#     def on_update(self, delta_time):

#         # Movimento do jogador baseado em tempo
#         self.player.center_y += (
#             self.player.change_y * delta_time
#         )

#         # Atualiza os tiros usando delta_time
#         for bullet in self.player_bullet_list:
#             bullet.update_bullet(delta_time)

#         for bullet in self.enemy_bullet_list:
#             bullet.update_bullet(delta_time)

#         # Colisão entre tiros do jogador e inimigos
#         for bullet in self.player_bullet_list:

#             hit_list = arcade.check_for_collision_with_list(
#                 bullet,
#                 self.enemy_list
#             )

#             for enemy in hit_list:
#                 enemy.remove_from_sprite_lists()
#                 bullet.remove_from_sprite_lists()
#                 self.score += 1

#         # Colisão entre tiros inimigos e jogador
#         hit_list = arcade.check_for_collision_with_list(
#             self.player,
#             self.enemy_bullet_list
#         )

#         for bullet in hit_list:
#             bullet.remove_from_sprite_lists()
#             self.player_life -= 1

#         # Temporizador dos disparos inimigos
#         self.enemy_shoot_timer += delta_time

#         if self.enemy_shoot_timer >= 2.0:

#             for enemy in self.enemy_list:
#                 self.shoot_enemy_bullet(enemy)

#             self.enemy_shoot_timer = 0

#     def on_draw(self):

#         self.clear()

#         self.player_list.draw()
#         self.enemy_list.draw()

#         self.player_bullet_list.draw()
#         self.enemy_bullet_list.draw()

#         arcade.draw_text(
#             f"Pontos: {self.score}",
#             10,
#             570,
#             arcade.color.WHITE,
#             18
#         )

#         arcade.draw_text(
#             f"Vida: {self.player_life}",
#             10,
#             540,
#             arcade.color.WHITE,
#             18
#         )


# game = Game()
# game.setup()
# arcade.run()



####################################
#   CÓDIGO 008 - Debug
####################################

# import arcade


# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600
# SCREEN_TITLE = "Debug"

# # Ativa a coleta de informações de desempenho
# arcade.enable_timings()


# class Game(arcade.Window):

#     def __init__(self):

#         super().__init__(
#             SCREEN_WIDTH,
#             SCREEN_HEIGHT,
#             SCREEN_TITLE
#         )

#         self.player = arcade.SpriteSolidColor(
#             width=64,
#             height=64,
#             color=arcade.color.BLUE
#         )

#         self.player.center_x = 400
#         self.player.center_y = 300

#         self.player_list = arcade.SpriteList()
#         self.player_list.append(self.player)

#     def on_draw(self):

#         self.clear()

#         self.player_list.draw()

#         self.player.draw_hit_box(
#             color=arcade.color.RED,
#             line_thickness=2
#         )

#         arcade.draw_text(
#             f"X: {self.player.center_x}",
#             10,
#             40,
#             arcade.color.WHITE,
#             18
#         )

#         arcade.draw_text(
#             f"Y: {self.player.center_y}",
#             10,
#             10,
#             arcade.color.WHITE,
#             18
#         )

#         fps = arcade.get_fps()

#         arcade.draw_text(
#             f"FPS: {fps:.0f}",
#             10,
#             70,
#             arcade.color.YELLOW,
#             18
#         )


# game = Game()
# arcade.run()


####################################
#   CÓDIGO 009 - Física básica
####################################
# import arcade


# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600
# SCREEN_TITLE = "Física básica com Arcade"

# GRAVITY = 1.0
# MOVE_SPEED = 5
# JUMP_FORCE = 23


# class Game(arcade.Window):

#     def __init__(self):

#         super().__init__(
#             SCREEN_WIDTH,
#             SCREEN_HEIGHT,
#             SCREEN_TITLE
#         )

#         self.player_list = arcade.SpriteList()
#         self.wall_list = arcade.SpriteList()

#         self.player = None
#         self.physics_engine = None

#     def setup(self):

#         self.player = arcade.Sprite(
#             ":resources:images/animated_characters/male_person/malePerson_idle.png",
#             scale=0.5
#         )

#         self.player.center_x = 100
#         self.player.center_y = 200

#         self.player_list.append(self.player)

#         # Cria o chão
#         for x in range(0, SCREEN_WIDTH, 64):

#             wall = arcade.SpriteSolidColor(
#                 width=64,
#                 height=32,
#                 color=arcade.color.DARK_GREEN
#             )

#             wall.center_x = x + 32
#             wall.center_y = 16

#             self.wall_list.append(wall)

#         # Cria uma plataforma elevada
#         for x in range(300, 600, 64):

#             wall = arcade.SpriteSolidColor(
#                 width=64,
#                 height=32,
#                 color=arcade.color.DARK_GREEN
#             )

#             wall.center_x = x + 32
#             wall.center_y = 220

#             self.wall_list.append(wall)

#         self.physics_engine = arcade.PhysicsEnginePlatformer(
#             self.player,
#             walls=self.wall_list,
#             gravity_constant=GRAVITY
#         )

#     def on_draw(self):

#         self.clear()

#         self.wall_list.draw()
#         self.player_list.draw()

#     def on_update(self, delta_time):

#         self.physics_engine.update()

#     def on_key_press(self, key, modifiers):

#         if key == arcade.key.RIGHT:
#             self.player.change_x = MOVE_SPEED

#         elif key == arcade.key.LEFT:
#             self.player.change_x = -MOVE_SPEED

#         elif key == arcade.key.UP:

#             if self.physics_engine.can_jump():
#                 self.player.change_y = JUMP_FORCE

#     def on_key_release(self, key, modifiers):

#         if key in (arcade.key.RIGHT, arcade.key.LEFT):
#             self.player.change_x = 0


# game = Game()
# game.setup()
# arcade.run()




####################################
#   CÓDIGO 010 - HUD vs Scroll
####################################

# import arcade


# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600
# SCREEN_TITLE = "HUD e múltiplas câmeras"

# WORLD_WIDTH = 2000

# # Velocidade em pixels por segundo
# MOVE_SPEED = 300


# class Game(arcade.Window):

#     def __init__(self):

#         super().__init__(
#             SCREEN_WIDTH,
#             SCREEN_HEIGHT,
#             SCREEN_TITLE
#         )

#         self.player_list = arcade.SpriteList()
#         self.wall_list = arcade.SpriteList()

#         self.player = None

#         self.camera_sprites = arcade.Camera2D()
#         self.camera_gui = arcade.Camera2D()

#         self.score = 0

#         self.score_text = arcade.Text(
#             "Pontos: 0",
#             10,
#             10,
#             arcade.color.WHITE,
#             18
#         )

#     def setup(self):

#         self.player = arcade.SpriteSolidColor(
#             width=50,
#             height=50,
#             color=arcade.color.BLUE
#         )

#         self.player.center_x = 100
#         self.player.center_y = 150
#         self.player.change_x = 0

#         self.player_list.append(self.player)

#         # Chão ao longo do mundo
#         for x in range(0, WORLD_WIDTH, 64):

#             wall = arcade.SpriteSolidColor(
#                 width=64,
#                 height=32,
#                 color=arcade.color.DARK_GREEN
#             )

#             wall.center_x = x + 32
#             wall.center_y = 16

#             self.wall_list.append(wall)

#         # Plataforma central como referência visual
#         for x in range(600, 1450, 64):

#             platform = arcade.SpriteSolidColor(
#                 width=64,
#                 height=32,
#                 color=arcade.color.BROWN
#             )

#             platform.center_x = x + 32
#             platform.center_y = 250

#             self.wall_list.append(platform)

#         self.camera_sprites.position = (
#             SCREEN_WIDTH / 2,
#             SCREEN_HEIGHT / 2
#         )

#         self.camera_gui.position = (
#             SCREEN_WIDTH / 2,
#             SCREEN_HEIGHT / 2
#         )

#     def on_draw(self):

#         self.clear()

#         # Câmera do mundo
#         self.camera_sprites.use()

#         self.wall_list.draw()
#         self.player_list.draw()

#         # Câmera do HUD
#         self.camera_gui.use()

#         self.score_text.draw()

#     def on_update(self, delta_time):

#         # Move o jogador com base no tempo
#         self.player.center_x += (
#             self.player.change_x * delta_time
#         )

#         # Limita jogador ao mundo
#         if self.player.center_x < 25:
#             self.player.center_x = 25

#         if self.player.center_x > WORLD_WIDTH - 25:
#             self.player.center_x = WORLD_WIDTH - 25

#         # Calcula centro da câmera
#         camera_x = self.player.center_x

#         # Limita câmera para não mostrar fora do mundo
#         min_camera_x = SCREEN_WIDTH / 2
#         max_camera_x = WORLD_WIDTH - SCREEN_WIDTH / 2

#         camera_x = max(
#             min_camera_x,
#             min(camera_x, max_camera_x)
#         )

#         # Atualiza câmera do mundo
#         self.camera_sprites.position = (
#             camera_x,
#             SCREEN_HEIGHT / 2
#         )

#         # Atualiza texto do HUD
#         self.score_text.text = f"Pontos: {self.score}"

#     def on_key_press(self, key, modifiers):

#         if key == arcade.key.RIGHT:
#             self.player.change_x = MOVE_SPEED

#         elif key == arcade.key.LEFT:
#             self.player.change_x = -MOVE_SPEED

#     def on_key_release(self, key, modifiers):

#         if key in (arcade.key.RIGHT, arcade.key.LEFT):
#             self.player.change_x = 0


# game = Game()
# game.setup()
# arcade.run()


####################################
#   CÓDIGO 011 - Tile map (matriz)
#####################################
# import arcade

# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600
# SCREEN_TITLE = "Mapa com Matriz"
# TILE_SIZE = 64

# class Game(arcade.Window):
#    def __init__(self):
#        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

#        # Lista das paredes e plataformas
#        self.wall_list = arcade.SpriteList()
#        # Lista das moedas
#        self.coin_list = arcade.SpriteList()
#        # Lista do jogador
#        self.player_list = arcade.SpriteList()
#        # Sprite do jogador
#        self.player = None

#    def setup(self):
#        # Cria o jogador
#        self.player = arcade.SpriteSolidColor(
#            width=40,
#            height=50,
#            color=arcade.color.BLUE
#        )
#        self.player_list.append(self.player)
#        # W = parede/chão
#        # C = moeda
#        # P = posição inicial do jogador
#        # . = vazio
#        mapa = [
#            "WWWWWWWWWWWW",
#            "W..........W",
#            "W....C.....W",
#            "W...WWW....W",
#            "W.P........W",
#            "WWWWWWWWWWWW"
#        ]
#        # Percorre cada linha do mapa
#        for linha_idx, linha in enumerate(mapa):
#            # Percorre cada caractere da linha
#            for col_idx, caractere in enumerate(linha):
#                # Calcula posição X com base na coluna
#                x = (col_idx * TILE_SIZE) + (TILE_SIZE / 2)
#                # Calcula posição Y invertendo a ordem das linhas
#                y = (len(mapa) - 1 - linha_idx) * TILE_SIZE + (TILE_SIZE / 2)
#                # Se o caractere for W, cria parede
#                if caractere == "W":
#                    wall = arcade.SpriteSolidColor(
#                        width=TILE_SIZE,
#                        height=TILE_SIZE,
#                        color=arcade.color.DARK_GREEN
#                    )
#                    wall.center_x = x
#                    wall.center_y = y

#                    self.wall_list.append(wall)
#                # Se o caractere for C, cria moeda
#                elif caractere == "C":
#                    coin = arcade.SpriteSolidColor(
#                        width=24,
#                        height=24,
#                        color=arcade.color.YELLOW
#                    )
#                    coin.center_x = x
#                    coin.center_y = y
#                    self.coin_list.append(coin)
#                # Se o caractere for P, posiciona jogador
#                elif caractere == "P":
#                    self.player.center_x = x
#                    self.player.center_y = y

#    def on_draw(self):
#        self.clear()
#        self.wall_list.draw()
#        self.coin_list.draw()
#        self.player_list.draw()

# game = Game()
# game.setup()
# arcade.run()




####################################
#   CÓDIGO 012 - Arquivo Tiled
#####################################
# import arcade
# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600
# SCREEN_TITLE = "Mapa com Tiled"
# TILE_SCALING = 1.0

# class Game(arcade.Window):
#    def __init__(self):
#        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
#        self.tile_map = None
#        self.scene = None

#    def setup(self):
#        # Opções das camadas do mapa
#        layer_options = {
#            # Camadas estáticas podem usar spatial hash
#            "Platforms": {
#                "use_spatial_hash": True
#            },
#            "Coins": {
#                "use_spatial_hash": True
#            }
#        }
#        # Carrega o arquivo exportado pelo Tiled
#        self.tile_map = arcade.load_tilemap(
#            "./DJ2D/fase1.tmj",
#            scaling=TILE_SCALING,
#            layer_options=layer_options
#        )
#        # Converte o mapa em uma Scene
#        self.scene = arcade.Scene.from_tilemap(self.tile_map)
#    def on_draw(self):
#        self.clear()

#        # Desenha todas as camadas da Scene
#        self.scene.draw()

# game = Game()
# game.setup()
# arcade.run()





####################################
#   CÓDIGO 013 - Folha de Sprites
#####################################
# import arcade
# import os
# import math


# BASE_DIR = os.path.dirname(__file__)

# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600
# SCREEN_TITLE = "Sprite Sheet - 4 Direções"

# MOVE_SPEED = 200


# class Direction:
#     DOWN = "down"
#     RIGHT = "right"
#     UP = "up"
#     LEFT = "left"


# class Player(arcade.Sprite):

#     def __init__(self):

#         super().__init__()

#         spritesheet = arcade.load_spritesheet(
#             os.path.join(
#                 BASE_DIR,
#                 "esqueleto.png"
#             )
#         )

#         self.texturas = spritesheet.get_texture_grid(
#             size=(64, 64),
#             columns=9,
#             count=36
#         )

#         self.walk_up = self.texturas[0:9]
#         self.walk_left = self.texturas[9:18]
#         self.walk_down = self.texturas[18:27]
#         self.walk_right = self.texturas[27:36]

#         self.direction = Direction.DOWN

#         self.current_texture = 0
#         self.frame_timer = 0
#         self.animation_speed = 0.1

#         self.texture = self.walk_down[0]

#         self.center_x = 400
#         self.center_y = 300

#         self.change_x = 0
#         self.change_y = 0

#     def update_animation(self, delta_time):

#         if self.direction == Direction.DOWN:
#             animation = self.walk_down

#         elif self.direction == Direction.RIGHT:
#             animation = self.walk_right

#         elif self.direction == Direction.UP:
#             animation = self.walk_up

#         elif self.direction == Direction.LEFT:
#             animation = self.walk_left

#         else:
#             animation = self.walk_down

#         if self.change_x == 0 and self.change_y == 0:
#             self.texture = animation[0]
#             return

#         self.frame_timer += delta_time

#         if self.frame_timer < self.animation_speed:
#             return

#         self.frame_timer = 0
#         self.current_texture += 1

#         if self.current_texture >= len(animation):
#             self.current_texture = 0

#         self.texture = animation[self.current_texture]


# class Game(arcade.Window):

#     def __init__(self):

#         super().__init__(
#             SCREEN_WIDTH,
#             SCREEN_HEIGHT,
#             SCREEN_TITLE
#         )

#         self.player_list = arcade.SpriteList()
#         self.player = None

#         self.right_pressed = False
#         self.left_pressed = False
#         self.up_pressed = False
#         self.down_pressed = False

#     def setup(self):

#         self.player = Player()
#         self.player_list.append(self.player)

#     def update_player_speed(self):

#         self.player.change_x = 0
#         self.player.change_y = 0

#         if self.right_pressed:
#             self.player.change_x = MOVE_SPEED
#             self.player.direction = Direction.RIGHT

#         elif self.left_pressed:
#             self.player.change_x = -MOVE_SPEED
#             self.player.direction = Direction.LEFT

#         if self.up_pressed:
#             self.player.change_y = MOVE_SPEED
#             self.player.direction = Direction.UP

#         elif self.down_pressed:
#             self.player.change_y = -MOVE_SPEED
#             self.player.direction = Direction.DOWN

#         if self.player.change_x != 0 and self.player.change_y != 0:
#             self.player.change_x /= math.sqrt(2)
#             self.player.change_y /= math.sqrt(2)

#     def on_draw(self):

#         self.clear()
#         self.player_list.draw()

#     def on_update(self, delta_time):

#         self.player.center_x += (
#             self.player.change_x * delta_time
#         )

#         self.player.center_y += (
#             self.player.change_y * delta_time
#         )

#         self.player_list.update_animation(delta_time)

#     def on_key_press(self, key, modifiers):

#         if key == arcade.key.RIGHT:
#             self.right_pressed = True

#         elif key == arcade.key.LEFT:
#             self.left_pressed = True

#         elif key == arcade.key.UP:
#             self.up_pressed = True

#         elif key == arcade.key.DOWN:
#             self.down_pressed = True

#         self.update_player_speed()

#     def on_key_release(self, key, modifiers):

#         if key == arcade.key.RIGHT:
#             self.right_pressed = False

#         elif key == arcade.key.LEFT:
#             self.left_pressed = False

#         elif key == arcade.key.UP:
#             self.up_pressed = False

#         elif key == arcade.key.DOWN:
#             self.down_pressed = False

#         self.update_player_speed()


# game = Game()
# game.setup()
# arcade.run()





####################################
#   CÓDIGO 014 - Máq. Estados
#####################################

# import arcade


# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600
# SCREEN_TITLE = "Máquina de Estados do Personagem"

# # Velocidades em pixels por segundo
# MOVE_SPEED = 300
# JUMP_FORCE = 600

# # Gravidade em pixels por segundo ao quadrado
# GRAVITY = 1200


# class PlayerState:

#     IDLE = "idle"
#     WALKING = "walking"
#     JUMPING = "jumping"
#     FALLING = "falling"
#     ATTACKING = "attacking"


# class Player(arcade.Sprite):

#     def __init__(self):

#         super().__init__()

#         self.texture = arcade.make_soft_square_texture(
#             size=50,
#             color=arcade.color.BLUE,
#             outer_alpha=255
#         )

#         self.center_x = 400
#         self.center_y = 300

#         self.change_x = 0
#         self.change_y = 0

#         self.state = PlayerState.IDLE

#         self.attack_timer = 0
#         self.attack_duration = 0.3

#         self.ground_y = 300

#     def attack(self):

#         self.state = PlayerState.ATTACKING
#         self.attack_timer = self.attack_duration

#     def update_state(self, delta_time):

#         if self.attack_timer > 0:
#             self.attack_timer -= delta_time
#             self.state = PlayerState.ATTACKING
#             return

#         if self.change_y > 0:
#             self.state = PlayerState.JUMPING

#         elif self.change_y < 0:
#             self.state = PlayerState.FALLING

#         elif self.change_x != 0:
#             self.state = PlayerState.WALKING

#         else:
#             self.state = PlayerState.IDLE


# class Game(arcade.Window):

#     def __init__(self):

#         super().__init__(
#             SCREEN_WIDTH,
#             SCREEN_HEIGHT,
#             SCREEN_TITLE
#         )

#         self.player = Player()

#         self.player_list = arcade.SpriteList()
#         self.player_list.append(self.player)

#     def on_draw(self):

#         self.clear()

#         self.player_list.draw()

#         arcade.draw_text(
#             f"Estado: {self.player.state}",
#             10,
#             10,
#             arcade.color.WHITE,
#             18
#         )

#     def on_update(self, delta_time):

#         # Aplica gravidade quando o jogador está acima do chão
#         if self.player.center_y > self.player.ground_y:
#             self.player.change_y -= GRAVITY * delta_time

#         # Movimento baseado em tempo
#         self.player.center_x += (
#             self.player.change_x * delta_time
#         )

#         self.player.center_y += (
#             self.player.change_y * delta_time
#         )

#         # Impede o jogador de cair abaixo do chão
#         if self.player.center_y < self.player.ground_y:
#             self.player.center_y = self.player.ground_y
#             self.player.change_y = 0

#         self.player.update_state(delta_time)

#     def on_key_press(self, key, modifiers):

#         if key == arcade.key.RIGHT:
#             self.player.change_x = MOVE_SPEED

#         elif key == arcade.key.LEFT:
#             self.player.change_x = -MOVE_SPEED

#         elif key == arcade.key.UP:

#             if self.player.center_y == self.player.ground_y:
#                 self.player.change_y = JUMP_FORCE

#         elif key == arcade.key.SPACE:
#             self.player.attack()

#     def on_key_release(self, key, modifiers):

#         if key in (
#             arcade.key.RIGHT,
#             arcade.key.LEFT
#         ):
#             self.player.change_x = 0


# game = Game()
# arcade.run()




####################################
#   CÓDIGO 015 - BFS
#####################################

# from collections import deque


# def bfs(grid, start, goal):

#     # Fila utilizada pela BFS
#     queue = deque()

#     # Adiciona posição inicial
#     queue.append(start)

#     # Dicionário usado para reconstruir o caminho
#     came_from = {}

#     # O ponto inicial não veio de lugar algum
#     came_from[start] = None

#     # Enquanto houver posições para explorar
#     while queue:

#         # Remove a primeira posição da fila
#         current = queue.popleft()

#         # Se chegou ao objetivo, encerra
#         if current == goal:
#             break

#         row, col = current

#         # Movimentos possíveis
#         neighbors = [
#             (row - 1, col),
#             (row + 1, col),
#             (row, col - 1),
#             (row, col + 1)
#         ]

#         # Analisa vizinhos
#         for next_cell in neighbors:

#             r, c = next_cell

#             # Verifica limites do mapa
#             if r < 0 or c < 0:
#                 continue

#             if r >= len(grid):
#                 continue

#             if c >= len(grid[0]):
#                 continue

#             # Ignora paredes
#             if grid[r][c] == "#":
#                 continue

#             # Evita revisitar células
#             if next_cell not in came_from:

#                 queue.append(next_cell)

#                 # Guarda de onde veio
#                 came_from[next_cell] = current

#     # Se o objetivo não foi encontrado
#     if goal not in came_from:
#         return []

#     # Reconstrução do caminho
#     path = []

#     current = goal

#     while current is not None:

#         path.append(current)

#         current = came_from[current]

#     # Inverte ordem
#     path.reverse()

#     return path


# # Exemplo de uso
# grid = [
#     "S...",
#     ".##.",
#     "....",
#     "...G"
# ]

# start = (0, 3)
# goal = (3, 0)

# path = bfs(grid, start, goal)

# print(path)




####################################
#   CÓDIGO 016 - A*
#####################################
# import heapq

# def heuristica(a, b):
#     """
#     Calcula a distância Manhattan entre dois pontos.
#     Cada ponto é representado como uma tupla (linha, coluna).
#     """

#     linha_a, coluna_a = a
#     linha_b, coluna_b = b

#     return abs(linha_a - linha_b) + abs(coluna_a - coluna_b)


# def obter_vizinhos(posicao, mapa):
#     """
#     Retorna as células vizinhas válidas.
#     Considera movimento em quatro direções:
#     cima, baixo, esquerda e direita.
#     """

#     linha, coluna = posicao

#     candidatos = [
#         (linha - 1, coluna),  # cima
#         (linha + 1, coluna),  # baixo
#         (linha, coluna - 1),  # esquerda
#         (linha, coluna + 1)   # direita
#     ]

#     vizinhos = []

#     for nova_linha, nova_coluna in candidatos:

#         # Verifica se está dentro dos limites do mapa
#         if nova_linha < 0 or nova_linha >= len(mapa):
#             continue

#         if nova_coluna < 0 or nova_coluna >= len(mapa[0]):
#             continue

#         # Ignora paredes
#         if mapa[nova_linha][nova_coluna] == "#":
#             continue

#         vizinhos.append((nova_linha, nova_coluna))

#     return vizinhos


# def reconstruir_caminho(came_from, inicio, objetivo):
#     """
#     Reconstrói o caminho final voltando do objetivo até o início.
#     """

#     atual = objetivo
#     caminho = []

#     while atual != inicio:

#         caminho.append(atual)
#         atual = came_from[atual]

#     caminho.append(inicio)
#     caminho.reverse()

#     return caminho


# def astar(mapa, inicio, objetivo):
#     """
#     Implementação básica do algoritmo A*.
#     """

#     # Fila de prioridade.
#     # O heap sempre remove primeiro o item com menor prioridade.
#     fila_aberta = []

#     heapq.heappush(fila_aberta, (0, inicio))

#     # Guarda de onde cada célula veio
#     came_from = {}

#     # Guarda o custo real até cada célula
#     custo_ate_agora = {}

#     came_from[inicio] = None
#     custo_ate_agora[inicio] = 0

#     while fila_aberta:

#         # Pega a célula mais promissora
#         prioridade_atual, atual = heapq.heappop(fila_aberta)

#         # Se chegou ao objetivo, pode parar
#         if atual == objetivo:
#             break

#         # Analisa vizinhos válidos
#         for vizinho in obter_vizinhos(atual, mapa):

#             novo_custo = custo_ate_agora[atual] + 1

#             # Se ainda não visitou ou achou caminho melhor
#             if vizinho not in custo_ate_agora or novo_custo < custo_ate_agora[vizinho]:

#                 custo_ate_agora[vizinho] = novo_custo

#                 prioridade = novo_custo + heuristica(vizinho, objetivo)

#                 heapq.heappush(fila_aberta, (prioridade, vizinho))

#                 came_from[vizinho] = atual

#     # Se não encontrou caminho
#     if objetivo not in came_from:
#         return []

#     return reconstruir_caminho(came_from, inicio, objetivo)


# # Exemplo de mapa
# mapa = [
#     "S...#",
#     ".#..#",
#     ".#...",
#     "...#G"
# ]

# inicio = (0, 0)
# objetivo = (3, 4)

# caminho = astar(mapa, inicio, objetivo)

# print("Caminho encontrado:")
# print(caminho)




####################################
#   CÓDIGO 017 - camera shake
#####################################

# import random


# def start_screen_shake(
#     self,
#     intensity,
#     duration
# ):

#     # Intensidade do tremor
#     self.shake_intensity = intensity

#     # Duração em segundos
#     self.shake_duration = duration


# def update_screen_shake(self, delta_time):

#     if self.shake_duration > 0:

#         offset_x = random.uniform(
#             -self.shake_intensity,
#             self.shake_intensity
#         )

#         offset_y = random.uniform(
#             -self.shake_intensity,
#             self.shake_intensity
#         )

#         self.camera.position = (
#             self.camera_x + offset_x,
#             self.camera_y + offset_y
#         )

#         # Reduz duração usando delta_time
#         self.shake_duration -= delta_time

#     else:

#         # Retorna câmera à posição normal
#         self.camera.position = (
#             self.camera_x,
#             self.camera_y
#         )




####################################
#   CÓDIGO 018 - Dead Zone
#####################################
# import arcade


# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600
# SCREEN_TITLE = "Dead Zone"

# WORLD_WIDTH = 3000

# # Velocidade em pixels por segundo
# MOVE_SPEED = 300


# class Game(arcade.Window):

#     def __init__(self):

#         super().__init__(
#             SCREEN_WIDTH,
#             SCREEN_HEIGHT,
#             SCREEN_TITLE
#         )

#         self.player_list = arcade.SpriteList()
#         self.wall_list = arcade.SpriteList()

#         self.player = None

#         self.camera = arcade.Camera2D()

#         self.camera_x = SCREEN_WIDTH / 2

#     def setup(self):

#         self.player = arcade.SpriteSolidColor(
#             width=50,
#             height=50,
#             color=arcade.color.BLUE
#         )

#         self.player.center_x = 100
#         self.player.center_y = 120

#         self.player_list.append(self.player)

#         for x in range(0, WORLD_WIDTH, 64):

#             wall = arcade.SpriteSolidColor(
#                 width=64,
#                 height=32,
#                 color=arcade.color.DARK_GREEN
#             )

#             wall.center_x = x + 32
#             wall.center_y = 32

#             self.wall_list.append(wall)

#         for x in range(1200, 1600, 64):

#             platform = arcade.SpriteSolidColor(
#                 width=64,
#                 height=32,
#                 color=arcade.color.BROWN
#             )

#             platform.center_x = x + 32
#             platform.center_y = 250

#             self.wall_list.append(platform)

#     def update_camera_dead_zone(self):

#         player_screen_x = self.player.center_x - (
#             self.camera_x - SCREEN_WIDTH / 2
#         )

#         if player_screen_x > 500:

#             diff = player_screen_x - 500
#             self.camera_x += diff

#         elif player_screen_x < 300:

#             diff = 300 - player_screen_x
#             self.camera_x -= diff

#         min_x = SCREEN_WIDTH / 2
#         max_x = WORLD_WIDTH - SCREEN_WIDTH / 2

#         self.camera_x = max(
#             min_x,
#             min(self.camera_x, max_x)
#         )

#         self.camera.position = (
#             self.camera_x,
#             SCREEN_HEIGHT / 2
#         )

#     def on_draw(self):

#         self.clear()

#         self.camera.use()

#         self.wall_list.draw()
#         self.player_list.draw()

#         arcade.draw_line(
#             300 + self.camera_x - SCREEN_WIDTH / 2,
#             0,
#             300 + self.camera_x - SCREEN_WIDTH / 2,
#             SCREEN_HEIGHT,
#             arcade.color.YELLOW,
#             2
#         )

#         arcade.draw_line(
#             500 + self.camera_x - SCREEN_WIDTH / 2,
#             0,
#             500 + self.camera_x - SCREEN_WIDTH / 2,
#             SCREEN_HEIGHT,
#             arcade.color.YELLOW,
#             2
#         )

#     def on_update(self, delta_time):

#         self.player.center_x += (
#             self.player.change_x * delta_time
#         )

#         self.update_camera_dead_zone()

#     def on_key_press(self, key, modifiers):

#         if key == arcade.key.RIGHT:
#             self.player.change_x = MOVE_SPEED

#         elif key == arcade.key.LEFT:
#             self.player.change_x = -MOVE_SPEED

#     def on_key_release(self, key, modifiers):

#         if key in (
#             arcade.key.RIGHT,
#             arcade.key.LEFT
#         ):
#             self.player.change_x = 0


# game = Game()
# game.setup()
# arcade.run()






####################################
#   CÓDIGO 019 - Parallax
#####################################
# import arcade
# import os


# BASE_DIR = os.path.dirname(__file__)
# BACKGROUND_DIR = os.path.join(BASE_DIR, "backgrounds")

# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600
# SCREEN_TITLE = "Parallax"

# WORLD_WIDTH = 4000

# # Velocidade em pixels por segundo
# MOVE_SPEED = 300


# class ParallaxLayer:

#     def __init__(
#         self,
#         texture_path,
#         speed_factor,
#         y,
#         width,
#         height
#     ):

#         # Carrega textura da camada
#         self.texture = arcade.load_texture(
#             texture_path
#         )

#         self.speed_factor = speed_factor
#         self.y = y
#         self.width = width
#         self.height = height

#     def draw(self, camera_x):

#         offset = (
#             -(camera_x * self.speed_factor)
#             % self.width
#         )

#         for i in range(-1, 3):

#             pos_x = (
#                 offset
#                 + (i * self.width)
#                 + (self.width / 2)
#             )

#             rect = arcade.Rect(
#                 left=pos_x - self.width / 2,
#                 right=pos_x + self.width / 2,
#                 bottom=self.y - self.height / 2,
#                 top=self.y + self.height / 2,
#                 width=self.width,
#                 height=self.height,
#                 x=pos_x,
#                 y=self.y
#             )

#             arcade.draw_texture_rect(
#                 texture=self.texture,
#                 rect=rect
#             )


# class Game(arcade.Window):

#     def __init__(self):

#         super().__init__(
#             SCREEN_WIDTH,
#             SCREEN_HEIGHT,
#             SCREEN_TITLE
#         )

#         self.player = None
#         self.player_list = arcade.SpriteList()

#         self.camera = arcade.Camera2D()
#         self.camera_x = SCREEN_WIDTH / 2

#         self.background_layers = []

#     def setup(self):

#         self.player = arcade.SpriteSolidColor(
#             width=50,
#             height=50,
#             color=arcade.color.BLUE
#         )

#         self.player.center_x = 100
#         self.player.center_y = 120

#         self.player_list.append(self.player)

#         # Caminhos montados com os.path.join
#         sky_path = os.path.join(
#             BACKGROUND_DIR,
#             "sky.png"
#         )

#         mountains_path = os.path.join(
#             BACKGROUND_DIR,
#             "mountains.png"
#         )

#         trees_path = os.path.join(
#             BACKGROUND_DIR,
#             "trees.png"
#         )

#         self.background_layers = [
#             ParallaxLayer(
#                 sky_path,
#                 0.1,
#                 450,
#                 1920,
#                 600
#             ),

#             ParallaxLayer(
#                 mountains_path,
#                 0.3,
#                 300,
#                 1920,
#                 400
#             ),

#             ParallaxLayer(
#                 trees_path,
#                 0.6,
#                 220,
#                 1920,
#                 300
#             )
#         ]

#     def on_draw(self):

#         self.clear()

#         for layer in self.background_layers:
#             layer.draw(self.camera_x)

#         self.camera.use()

#         self.player_list.draw()

#     def on_update(self, delta_time):

#         self.player.center_x += (
#             self.player.change_x * delta_time
#         )

#         if self.player.center_x < 25:
#             self.player.center_x = 25

#         if self.player.center_x > WORLD_WIDTH - 25:
#             self.player.center_x = WORLD_WIDTH - 25

#         self.camera_x = self.player.center_x

#         self.camera.position = (
#             self.camera_x,
#             SCREEN_HEIGHT / 2
#         )

#     def on_key_press(self, key, modifiers):

#         if key == arcade.key.RIGHT:
#             self.player.change_x = MOVE_SPEED

#         elif key == arcade.key.LEFT:
#             self.player.change_x = -MOVE_SPEED

#     def on_key_release(self, key, modifiers):

#         if key in (
#             arcade.key.RIGHT,
#             arcade.key.LEFT
#         ):
#             self.player.change_x = 0


# game = Game()
# game.setup()
# arcade.run()

####################################
#   CÓDIGO 020 - Áudio
#####################################
# import arcade


# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600
# SCREEN_TITLE = "Som"


# class Game(arcade.Window):

#     def __init__(self):

#         super().__init__(
#             SCREEN_WIDTH,
#             SCREEN_HEIGHT,
#             SCREEN_TITLE
#         )

#         # Carrega som de moeda
#         self.coin_sound = arcade.load_sound(
#             ":resources:sounds/coin1.wav"
#         )

#         # Carrega som de pulo
#         self.jump_sound = arcade.load_sound(
#             ":resources:sounds/jump1.wav"
#         )

#     def collect_coin(self):

#         arcade.play_sound(
#             self.coin_sound
#         )

#     def jump(self):

#         arcade.play_sound(
#             self.jump_sound
#         )

#     def on_key_press(self, key, modifiers):

#         # Espaço toca som da moeda
#         if key == arcade.key.SPACE:

#             self.collect_coin()

#         # Seta para cima toca som de pulo
#         elif key == arcade.key.UP:

#             self.jump()


# game = Game()
# arcade.run()





####################################
#   CÓDIGO 021 - Partículas
#####################################

# import arcade
# import random


# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600
# SCREEN_TITLE = "Partículas"

# PARTICLE_SPEED = 400
# PARTICLE_GRAVITY = 300
# PARTICLE_LIFETIME = 1.0


# class Particle(arcade.Sprite):

#     def __init__(self, x, y):

#         super().__init__()

#         self.texture = arcade.make_soft_circle_texture(
#             10,
#             arcade.color.ORANGE,
#             255,
#             0
#         )

#         self.center_x = x
#         self.center_y = y

#         self.change_x = random.uniform(
#             -PARTICLE_SPEED,
#             PARTICLE_SPEED
#         )

#         self.change_y = random.uniform(
#             -PARTICLE_SPEED,
#             PARTICLE_SPEED
#         )

#         self.life = PARTICLE_LIFETIME

#     def update(self, delta_time=1 / 60):

#         self.center_x += (
#             self.change_x * delta_time
#         )

#         self.center_y += (
#             self.change_y * delta_time
#         )

#         self.change_y -= (
#             PARTICLE_GRAVITY * delta_time
#         )

#         self.life -= delta_time

#         self.alpha = max(
#             0,
#             int(
#                 255 *
#                 (self.life / PARTICLE_LIFETIME)
#             )
#         )

#         if self.life <= 0:

#             self.remove_from_sprite_lists()


# class Game(arcade.Window):

#     def __init__(self):

#         super().__init__(
#             SCREEN_WIDTH,
#             SCREEN_HEIGHT,
#             SCREEN_TITLE
#         )

#         self.particle_list = arcade.SpriteList()

#     def create_particles(self, x, y):

#         for i in range(70):

#             particle = Particle(x, y)

#             self.particle_list.append(particle)

#     def on_mouse_press(
#         self,
#         x,
#         y,
#         button,
#         modifiers
#     ):

#         self.create_particles(x, y)

#     def on_update(self, delta_time):

#         self.particle_list.update(delta_time)

#     def on_draw(self):

#         self.clear()

#         self.particle_list.draw()


# game = Game()
# arcade.run()



####################################
#   CÓDIGO 022 - Load/Save
#####################################

# import arcade
# import json


# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600


# class Game(arcade.Window):

#     def __init__(self):

#         super().__init__(
#             SCREEN_WIDTH,
#             SCREEN_HEIGHT,
#             "Save e Load"
#         )

#         self.score = 0

#     def save_game(self):

#         dados = {
#             "score": self.score
#         }

#         with open("save.json", "w") as arquivo:

#             json.dump(dados, arquivo)

#         print("Jogo salvo.")

#     def load_game(self):

#         try:

#             with open("save.json", "r") as arquivo:

#                 dados = json.load(arquivo)

#                 self.score = dados["score"]

#             print("Jogo carregado.")

#         except FileNotFoundError:

#             print("Save não encontrado.")

#     def on_key_press(self, key, modifiers):

#         if key == arcade.key.S:

#             self.save_game()

#         elif key == arcade.key.L:

#             self.load_game()

#         elif key == arcade.key.SPACE:

#             self.score += 100

#     def on_draw(self):

#         self.clear()

#         arcade.draw_text(
#             f"Score: {self.score}",
#             300,
#             300,
#             arcade.color.WHITE,
#             30
#         )

#         arcade.draw_text(
#             "SPACE = +100 pontos",
#             250,
#             200,
#             arcade.color.YELLOW,
#             18
#         )

#         arcade.draw_text(
#             "S = salvar | L = carregar",
#             230,
#             160,
#             arcade.color.GREEN,
#             18
#         )


# game = Game()
# arcade.run()




####################################
#   CÓDIGO 023 - Views
#####################################
# import arcade


# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600
# SCREEN_TITLE = "Views"


# class MenuView(arcade.View):

#     def on_show_view(self):

#         self.window.background_color = arcade.color.BLACK

#     def on_draw(self):

#         self.clear()

#         arcade.draw_text(
#             "MEU JOGO",
#             280,
#             400,
#             arcade.color.YELLOW,
#             40
#         )

#         arcade.draw_text(
#             "Pressione ENTER",
#             260,
#             300,
#             arcade.color.WHITE,
#             24
#         )

#     def on_key_press(self, key, modifiers):

#         if key == arcade.key.ENTER:

#             game_view = GameView()

#             game_view.setup()

#             self.window.show_view(game_view)


# class GameView(arcade.View):

#     def __init__(self):

#         super().__init__()

#         self.player = None
#         self.player_list = arcade.SpriteList()

#     def setup(self):

#         self.player = arcade.SpriteSolidColor(
#             width=50,
#             height=50,
#             color=arcade.color.BLUE
#         )

#         self.player.center_x = 400
#         self.player.center_y = 300

#         self.player_list.append(self.player)

#     def on_draw(self):

#         self.clear()

#         self.player_list.draw()

#         arcade.draw_text(
#             "Gameplay",
#             20,
#             20,
#             arcade.color.WHITE,
#             20
#         )

#     def on_key_press(self, key, modifiers):

#         if key == arcade.key.ESCAPE:

#             menu_view = MenuView()

#             self.window.show_view(menu_view)


# def main():

#     window = arcade.Window(
#         SCREEN_WIDTH,
#         SCREEN_HEIGHT,
#         SCREEN_TITLE
#     )

#     menu_view = MenuView()

#     window.show_view(menu_view)

#     arcade.run()


# main()





####################################
#   CÓDIGO 024
#####################################

# import arcade

# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600
# SCREEN_TITLE = "Exemplo com Views"

# class MenuView(arcade.View):

#     def on_draw(self):

#         self.clear()

#         arcade.draw_text(
#             "MENU INICIAL",
#             250,
#             360,
#             arcade.color.WHITE,
#             32
#         )

#         arcade.draw_text(
#             "Pressione ENTER para jogar",
#             230,
#             300,
#             arcade.color.YELLOW,
#             20
#         )

#     def on_key_press(self, key, modifiers):

#         if key == arcade.key.ENTER:

#             # Troca do menu para o jogo
#             game_view = GameView()
#             self.window.show_view(game_view)


# class GameView(arcade.View):

#     def __init__(self):

#         super().__init__()

#         self.score = 0

#     def on_draw(self):

#         self.clear()

#         arcade.draw_text(
#             "JOGO EM EXECUÇÃO",
#             230,
#             360,
#             arcade.color.WHITE,
#             32
#         )

#         arcade.draw_text(
#             "Pressione G para simular Game Over",
#             190,
#             300,
#             arcade.color.YELLOW,
#             20
#         )

#     def on_key_press(self, key, modifiers):

#         if key == arcade.key.G:

#             # Troca do jogo para a tela de fim
#             game_over_view = GameOverView(self.score)
#             self.window.show_view(game_over_view)


# class GameOverView(arcade.View):

#     def __init__(self, score):

#         super().__init__()

#         self.score = score

#     def on_draw(self):

#         self.clear()

#         arcade.draw_text(
#             "GAME OVER",
#             280,
#             360,
#             arcade.color.RED,
#             32
#         )

#         arcade.draw_text(
#             f"Pontuação final: {self.score}",
#             260,
#             300,
#             arcade.color.WHITE,
#             20
#         )

#         arcade.draw_text(
#             "Pressione ENTER para voltar ao menu",
#             190,
#             240,
#             arcade.color.YELLOW,
#             20
#         )

#     def on_key_press(self, key, modifiers):

#         if key == arcade.key.ENTER:

#             # Troca da tela de fim para o menu
#             menu_view = MenuView()
#             self.window.show_view(menu_view)


# window = arcade.Window(
#     SCREEN_WIDTH,
#     SCREEN_HEIGHT,
#     SCREEN_TITLE
# )

# menu_view = MenuView()

# window.show_view(menu_view)

# arcade.run()

####################################
#   CÓDIGO 025
#####################################

# import arcade

# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600

# arcade.enable_timings()


# class Game(arcade.Window):

#     def __init__(self):

#         super().__init__(
#             SCREEN_WIDTH,
#             SCREEN_HEIGHT,
#             "Debug Visual"
#         )

#         self.player = arcade.SpriteSolidColor(
#             50,
#             50,
#             arcade.color.BLUE
#         )

#         self.player.center_x = 400
#         self.player.center_y = 300

#         self.player_list = arcade.SpriteList()
#         self.player_list.append(self.player)

#     def on_draw(self):

#         self.clear()

#         self.player_list.draw()

#         arcade.draw_text(
#             f"X: {self.player.center_x}",
#             10,
#             50,
#             arcade.color.WHITE,
#             18
#         )

#         arcade.draw_text(
#             f"Y: {self.player.center_y}",
#             10,
#             25,
#             arcade.color.WHITE,
#             18
#         )

#         arcade.draw_text(
#             f"FPS: {round(arcade.get_fps())}",
#             10,
#             75,
#             arcade.color.YELLOW,
#             18
#         )


# game = Game()
# arcade.run()


####################################
#   CÓDIGO 026 - A*
#####################################
# def heuristica(a, b):
#     """
#     Calcula a distância de Manhattan entre dois pontos.

#     Parâmetros:
#         a: tupla (linha, coluna)
#         b: tupla (linha, coluna)

#     Retorno:
#         distância estimada entre a e b
#     """

#     return abs(a[0] - b[0]) + abs(a[1] - b[1])


# def criar_no(posicao, g, objetivo, pai):
#     """
#     Cria um nó para ser usado nas listas aberta e fechada.

#     Estrutura do nó:
#         [linha, coluna, g, h, f, pai_linha, pai_coluna]
#     """

#     h = heuristica(posicao, objetivo)
#     f = g + h

#     if pai is None:
#         pai_linha = None
#         pai_coluna = None
#     else:
#         pai_linha = pai[0]
#         pai_coluna = pai[1]

#     return [posicao[0], posicao[1], g, h, f, pai_linha, pai_coluna]


# def obter_posicao(no):
#     """
#     Retorna a posição de um nó no formato (linha, coluna).
#     """

#     return (no[0], no[1])


# def obter_posicao_pai(no):
#     """
#     Retorna a posição do pai de um nó no formato (linha, coluna).
#     """

#     return (no[5], no[6])


# def buscar_no_por_posicao(lista, posicao):
#     """
#     Procura um nó em uma lista a partir de sua posição.

#     Retorno:
#         o nó encontrado ou None
#     """

#     for no in lista:
#         if no[0] == posicao[0] and no[1] == posicao[1]:
#             return no

#     return None


# def remover_no_por_posicao(lista, posicao):
#     """
#     Remove de uma lista o nó que possui a posição informada.
#     """

#     for i in range(len(lista)):
#         if lista[i][0] == posicao[0] and lista[i][1] == posicao[1]:
#             lista.pop(i)
#             return


# def escolher_menor_f(lista_aberta):
#     """
#     Escolhe da lista aberta o nó com menor valor de f.

#     Em caso de empate, escolhe o nó com menor h.
#     Isso ajuda o algoritmo a preferir nós mais próximos do objetivo.
#     """

#     melhor_no = lista_aberta[0]

#     for no in lista_aberta:
#         f_no = no[4]
#         h_no = no[3]

#         f_melhor = melhor_no[4]
#         h_melhor = melhor_no[3]

#         if f_no < f_melhor:
#             melhor_no = no
#         elif f_no == f_melhor and h_no < h_melhor:
#             melhor_no = no

#     return melhor_no


# def reconstruir_caminho(lista_fechada, objetivo):
#     """
#     Reconstrói o caminho usando os dados de pai armazenados nos nós
#     da lista fechada.
#     """

#     caminho = []

#     no_atual = buscar_no_por_posicao(lista_fechada, objetivo)

#     while no_atual is not None:
#         posicao_atual = obter_posicao(no_atual)
#         caminho.append(posicao_atual)

#         pai_linha = no_atual[5]
#         pai_coluna = no_atual[6]

#         if pai_linha is None or pai_coluna is None:
#             break

#         posicao_pai = (pai_linha, pai_coluna)
#         no_atual = buscar_no_por_posicao(lista_fechada, posicao_pai)

#     caminho.reverse()

#     return caminho


# def obter_vizinhos(posicao, mapa):
#     """
#     Retorna os vizinhos válidos de uma posição no mapa.

#     Parâmetros:
#         posicao: tupla (linha, coluna)
#         mapa: matriz representando o ambiente

#     Retorno:
#         lista de posições vizinhas válidas
#     """

#     linha, coluna = posicao

#     movimentos = [
#         (-1, 0),  # cima
#         (1, 0),   # baixo
#         (0, -1),  # esquerda
#         (0, 1)    # direita
#     ]

#     vizinhos = []

#     total_linhas = len(mapa)
#     total_colunas = len(mapa[0])

#     for movimento_linha, movimento_coluna in movimentos:
#         nova_linha = linha + movimento_linha
#         nova_coluna = coluna + movimento_coluna

#         dentro_do_mapa = (
#             0 <= nova_linha < total_linhas and
#             0 <= nova_coluna < total_colunas
#         )

#         if dentro_do_mapa:
#             nao_e_obstaculo = mapa[nova_linha][nova_coluna] == 0

#             if nao_e_obstaculo:
#                 vizinhos.append((nova_linha, nova_coluna))

#     return vizinhos


# def a_estrela(mapa, inicio, objetivo):
#     """
#     Executa o algoritmo A* usando somente listas.

#     Lista aberta:
#         nós descobertos, mas ainda não processados.

#     Lista fechada:
#         nós já processados.

#     Cada nó possui o formato:
#         [linha, coluna, g, h, f, pai_linha, pai_coluna]
#     """

#     lista_aberta = []
#     lista_fechada = []

#     no_inicial = criar_no(inicio, 0, objetivo, None)
#     lista_aberta.append(no_inicial)
    
#     while len(lista_aberta) > 0:
#         no_atual = escolher_menor_f(lista_aberta)
#         posicao_atual = obter_posicao(no_atual)

#         remover_no_por_posicao(lista_aberta, posicao_atual)
#         lista_fechada.append(no_atual)
        

#         if posicao_atual == objetivo:
#             return reconstruir_caminho(lista_fechada, objetivo)

#         vizinhos = obter_vizinhos(posicao_atual, mapa)

#         for posicao_vizinho in vizinhos:
#             no_na_fechada = buscar_no_por_posicao(lista_fechada, posicao_vizinho)

#             if no_na_fechada is not None:
#                 continue

#             novo_g = no_atual[2] + 1

#             no_na_aberta = buscar_no_por_posicao(lista_aberta, posicao_vizinho)

#             if no_na_aberta is None:
#                 novo_no = criar_no(
#                     posicao=posicao_vizinho,
#                     g=novo_g,
#                     objetivo=objetivo,
#                     pai=posicao_atual
#                 )

#                 lista_aberta.append(novo_no)

#             else:
#                 g_antigo = no_na_aberta[2]

#                 if novo_g < g_antigo:
#                     novo_h = heuristica(posicao_vizinho, objetivo)
#                     novo_f = novo_g + novo_h

#                     no_na_aberta[2] = novo_g
#                     no_na_aberta[3] = novo_h
#                     no_na_aberta[4] = novo_f
#                     no_na_aberta[5] = posicao_atual[0]
#                     no_na_aberta[6] = posicao_atual[1]
#             print("LA: ", lista_aberta)
#             print("LF: ", lista_fechada)
#             print()            

#     return None


# def imprimir_mapa(mapa, caminho, inicio, objetivo):
#     """
#     Imprime o mapa no terminal mostrando o caminho encontrado.

#     Símbolos:
#         S = início
#         G = objetivo
#         # = obstáculo
#         * = caminho
#         . = espaço livre
#     """

#     for linha in range(len(mapa)):
#         for coluna in range(len(mapa[0])):
#             posicao = (linha, coluna)

#             if posicao == inicio:
#                 print("S", end=" ")
#             elif posicao == objetivo:
#                 print("G", end=" ")
#             elif caminho is not None and posicao in caminho:
#                 print("*", end=" ")
#             elif mapa[linha][coluna] == 1:
#                 print("#", end=" ")
#             else:
#                 print(".", end=" ")

#         print()


# def main():
#     mapa = [
#         [0, 0, 0, 0, 0],
#         [1, 1, 0, 1, 0],
#         [0, 1, 0, 1, 0],
#         [0, 1, 1, 1, 0],
#         [0, 0, 0, 0, 0]
#     ]

#     inicio = (0, 0)
#     objetivo = (4, 4)

#     caminho = a_estrela(mapa, inicio, objetivo)

#     if caminho is None:
#         print("Nenhum caminho encontrado.")
#     else:
#         print("Caminho encontrado:")
#         print(caminho)
#         print()

#         imprimir_mapa(mapa, caminho, inicio, objetivo)


# if __name__ == "__main__":
#    main()



# ####################################
# #   CÓDIGO 027 - A* no Arcade 3.3.3
# #####################################

# import arcade


# TAMANHO_TILE = 80
# ALTURA_HUD = 60

# MAPA_TEXTO = [
#     "#############",
#     "#S_____#____#",
#     "#_####_#_##_#",
#     "#____#______#",
#     "#__#_###__#_#",
#     "##_#______#_#",
#     "#G___#_#____#",
#     "#############"
# ]

# LINHAS = len(MAPA_TEXTO)
# COLUNAS = len(MAPA_TEXTO[0])

# LARGURA_TELA = COLUNAS * TAMANHO_TILE
# ALTURA_TELA = LINHAS * TAMANHO_TILE + ALTURA_HUD

# VELOCIDADE_JOGADOR = 4
# VELOCIDADE_INIMIGO = 4


# def heuristica(a, b):
#     return abs(a[0] - b[0]) + abs(a[1] - b[1])


# def criar_no(posicao, g, objetivo, pai):
#     h = heuristica(posicao, objetivo)
#     f = g + h

#     if pai is None:
#         pai_linha = None
#         pai_coluna = None
#     else:
#         pai_linha = pai[0]
#         pai_coluna = pai[1]

#     return [posicao[0], posicao[1], g, h, f, pai_linha, pai_coluna]


# def obter_posicao(no):
#     return (no[0], no[1])


# def buscar_no_por_posicao(lista, posicao):
#     for no in lista:
#         if no[0] == posicao[0] and no[1] == posicao[1]:
#             return no

#     return None


# def remover_no_por_posicao(lista, posicao):
#     for i in range(len(lista)):
#         if lista[i][0] == posicao[0] and lista[i][1] == posicao[1]:
#             lista.pop(i)
#             return


# def escolher_menor_f(lista_aberta):
#     melhor_no = lista_aberta[0]

#     for no in lista_aberta:
#         if no[4] < melhor_no[4]:
#             melhor_no = no
#         elif no[4] == melhor_no[4] and no[3] < melhor_no[3]:
#             melhor_no = no

#     return melhor_no


# def reconstruir_caminho(lista_fechada, objetivo):
#     caminho = []
#     no_atual = buscar_no_por_posicao(lista_fechada, objetivo)

#     while no_atual is not None:
#         caminho.append(obter_posicao(no_atual))

#         pai_linha = no_atual[5]
#         pai_coluna = no_atual[6]

#         if pai_linha is None or pai_coluna is None:
#             break

#         no_atual = buscar_no_por_posicao(lista_fechada, (pai_linha, pai_coluna))

#     caminho.reverse()
#     return caminho


# def posicao_valida(mapa, posicao):
#     linha, coluna = posicao

#     if linha < 0 or linha >= len(mapa):
#         return False

#     if coluna < 0 or coluna >= len(mapa[0]):
#         return False

#     return mapa[linha][coluna] != "#"


# def obter_vizinhos(posicao, mapa):
#     linha, coluna = posicao

#     movimentos = [
#         (-1, 0),
#         (1, 0),
#         (0, -1),
#         (0, 1)
#     ]

#     vizinhos = []

#     for mov_linha, mov_coluna in movimentos:
#         nova_posicao = (linha + mov_linha, coluna + mov_coluna)

#         if posicao_valida(mapa, nova_posicao):
#             vizinhos.append(nova_posicao)

#     return vizinhos


# def a_estrela(mapa, inicio, objetivo):
#     lista_aberta = []
#     lista_fechada = []

#     no_inicial = criar_no(inicio, 0, objetivo, None)
#     lista_aberta.append(no_inicial)

#     while len(lista_aberta) > 0:
#         no_atual = escolher_menor_f(lista_aberta)
#         posicao_atual = obter_posicao(no_atual)

#         remover_no_por_posicao(lista_aberta, posicao_atual)
#         lista_fechada.append(no_atual)

#         if posicao_atual == objetivo:
#             return reconstruir_caminho(lista_fechada, objetivo)

#         vizinhos = obter_vizinhos(posicao_atual, mapa)

#         for posicao_vizinho in vizinhos:
#             if buscar_no_por_posicao(lista_fechada, posicao_vizinho) is not None:
#                 continue

#             novo_g = no_atual[2] + 1
#             no_na_aberta = buscar_no_por_posicao(lista_aberta, posicao_vizinho)

#             if no_na_aberta is None:
#                 novo_no = criar_no(posicao_vizinho, novo_g, objetivo, posicao_atual)
#                 lista_aberta.append(novo_no)
#             else:
#                 if novo_g < no_na_aberta[2]:
#                     novo_h = heuristica(posicao_vizinho, objetivo)
#                     novo_f = novo_g + novo_h

#                     no_na_aberta[2] = novo_g
#                     no_na_aberta[3] = novo_h
#                     no_na_aberta[4] = novo_f
#                     no_na_aberta[5] = posicao_atual[0]
#                     no_na_aberta[6] = posicao_atual[1]

#     return None


# def grid_para_tela(posicao_grid):
#     linha, coluna = posicao_grid

#     x = coluna * TAMANHO_TILE + TAMANHO_TILE // 2
#     y = ALTURA_HUD + (LINHAS - 1 - linha) * TAMANHO_TILE + TAMANHO_TILE // 2

#     return x, y


# def tela_para_grid(x, y):
#     coluna = int(x // TAMANHO_TILE)
#     linha = LINHAS - 1 - int((y - ALTURA_HUD) // TAMANHO_TILE)

#     return linha, coluna


# def limites_tile(linha, coluna):
#     x, y = grid_para_tela((linha, coluna))

#     esquerda = x - TAMANHO_TILE // 2
#     direita = x + TAMANHO_TILE // 2
#     baixo = y - TAMANHO_TILE // 2
#     cima = y + TAMANHO_TILE // 2

#     return esquerda, direita, baixo, cima


# class JogoAStar(arcade.Window):

#     def __init__(self):
#         super().__init__(LARGURA_TELA, ALTURA_TELA, "A* com Arcade 3.3.3")

#         self.mapa = MAPA_TEXTO

#         self.player_x = 0
#         self.player_y = 0

#         self.inimigo_x = 0
#         self.inimigo_y = 0

#         self.caminho = None
#         self.tempo_recalculo = 0

#         self.teclas = {
#             arcade.key.UP: False,
#             arcade.key.DOWN: False,
#             arcade.key.LEFT: False,
#             arcade.key.RIGHT: False
#         }

#         self.texto_info = arcade.Text(
#             "Setas: mover jogador | Inimigo usa A*",
#             20,
#             20,
#             arcade.color.WHITE,
#             16
#         )

#         self.setup()

#     def setup(self):
#         for linha in range(LINHAS):
#             for coluna in range(COLUNAS):
#                 simbolo = self.mapa[linha][coluna]
#                 x, y = grid_para_tela((linha, coluna))

#                 if simbolo == "S":
#                     self.player_x = x
#                     self.player_y = y

#                 elif simbolo == "G":
#                     self.inimigo_x = x
#                     self.inimigo_y = y

#     def on_draw(self):
#         self.clear(arcade.color.BLACK)

#         self.desenhar_mapa()
#         self.desenhar_caminho()
#         self.desenhar_personagens()

#         self.texto_info.draw()

#     def desenhar_mapa(self):
#         for linha in range(LINHAS):
#             for coluna in range(COLUNAS):
#                 simbolo = self.mapa[linha][coluna]

#                 esquerda, direita, baixo, cima = limites_tile(linha, coluna)

#                 if simbolo == "#":
#                     cor = (35, 35, 45)
#                 else:
#                     cor = (90, 90, 105)

#                 arcade.draw_lrbt_rectangle_filled(
#                     left=esquerda,
#                     right=direita,
#                     bottom=baixo,
#                     top=cima,
#                     color=cor
#                 )

#                 arcade.draw_lrbt_rectangle_outline(
#                     left=esquerda,
#                     right=direita,
#                     bottom=baixo,
#                     top=cima,
#                     color=(20, 20, 25),
#                     border_width=2
#                 )

#     def desenhar_caminho(self):
#         if self.caminho is None:
#             return

#         for posicao in self.caminho:
#             x, y = grid_para_tela(posicao)

#             arcade.draw_circle_filled(
#                 x,
#                 y,
#                 8,
#                 arcade.color.YELLOW
#             )

#     def desenhar_personagens(self):
#         arcade.draw_circle_filled(
#             self.player_x,
#             self.player_y,
#             24,
#             arcade.color.BLUE
#         )

#         arcade.draw_circle_filled(
#             self.inimigo_x,
#             self.inimigo_y,
#             24,
#             arcade.color.RED
#         )

#     def on_key_press(self, key, modifiers):
#         if key in self.teclas:
#             self.teclas[key] = True

#     def on_key_release(self, key, modifiers):
#         if key in self.teclas:
#             self.teclas[key] = False

#     def pode_mover_para(self, novo_x, novo_y):
#         linha, coluna = tela_para_grid(novo_x, novo_y)
#         return posicao_valida(self.mapa, (linha, coluna))

#     def mover_jogador(self):
#         dx = 0
#         dy = 0

#         if self.teclas[arcade.key.UP]:
#             dy += VELOCIDADE_JOGADOR
#         if self.teclas[arcade.key.DOWN]:
#             dy -= VELOCIDADE_JOGADOR
#         if self.teclas[arcade.key.LEFT]:
#             dx -= VELOCIDADE_JOGADOR
#         if self.teclas[arcade.key.RIGHT]:
#             dx += VELOCIDADE_JOGADOR

#         novo_x = self.player_x + dx
#         novo_y = self.player_y

#         if self.pode_mover_para(novo_x, novo_y):
#             self.player_x = novo_x

#         novo_x = self.player_x
#         novo_y = self.player_y + dy

#         if self.pode_mover_para(novo_x, novo_y):
#             self.player_y = novo_y

#     def mover_inimigo_com_astar(self, delta_time):
#         self.tempo_recalculo += delta_time

#         if self.tempo_recalculo >= 0.25:
#             self.tempo_recalculo = 0

#             inicio = tela_para_grid(self.inimigo_x, self.inimigo_y)
#             objetivo = tela_para_grid(self.player_x, self.player_y)

#             self.caminho = a_estrela(self.mapa, inicio, objetivo)

#         if self.caminho is None:
#             return

#         if len(self.caminho) < 2:
#             return

#         proxima_posicao = self.caminho[1]
#         destino_x, destino_y = grid_para_tela(proxima_posicao)

#         diferenca_x = destino_x - self.inimigo_x
#         diferenca_y = destino_y - self.inimigo_y

#         distancia = (diferenca_x ** 2 + diferenca_y ** 2) ** 0.5

#         if distancia <= VELOCIDADE_INIMIGO:
#             self.inimigo_x = destino_x
#             self.inimigo_y = destino_y
#         else:
#             direcao_x = diferenca_x / distancia
#             direcao_y = diferenca_y / distancia

#             self.inimigo_x += direcao_x * VELOCIDADE_INIMIGO
#             self.inimigo_y += direcao_y * VELOCIDADE_INIMIGO

#     def on_update(self, delta_time):
#         self.mover_jogador()
#         self.mover_inimigo_com_astar(delta_time)


# def main():
#     jogo = JogoAStar()
#     arcade.run()


# if __name__ == "__main__":
#     main()


#############################################################
#   CÓDIGO 028 - A* no Arcade 3.3.3 com lanterna(L)
#############################################################

# import arcade


# TAMANHO_TILE = 80
# ALTURA_HUD = 60

# RAIO_LUZ = 100
# TAMANHO_BLOCO_SOMBRA = 20
# ALPHA_MAXIMO_SOMBRA = 245

# MAPA_TEXTO = [
#     "#############",
#     "#S_____#____#",
#     "#_####_#_##_#",
#     "#____#______#",
#     "#__#_###__#_#",
#     "##_#______#_#",
#     "#G___#_#____#",
#     "#############"
# ]

# LINHAS = len(MAPA_TEXTO)
# COLUNAS = len(MAPA_TEXTO[0])

# LARGURA_TELA = COLUNAS * TAMANHO_TILE
# ALTURA_TELA = LINHAS * TAMANHO_TILE + ALTURA_HUD

# VELOCIDADE_JOGADOR = 4
# VELOCIDADE_INIMIGO = 5


# def heuristica(a, b):
#     return abs(a[0] - b[0]) + abs(a[1] - b[1])


# def criar_no(posicao, g, objetivo, pai):
#     h = heuristica(posicao, objetivo)
#     f = g + h

#     if pai is None:
#         pai_linha = None
#         pai_coluna = None
#     else:
#         pai_linha = pai[0]
#         pai_coluna = pai[1]

#     return [posicao[0], posicao[1], g, h, f, pai_linha, pai_coluna]


# def obter_posicao(no):
#     return (no[0], no[1])


# def buscar_no_por_posicao(lista, posicao):
#     for no in lista:
#         if no[0] == posicao[0] and no[1] == posicao[1]:
#             return no
#     return None


# def remover_no_por_posicao(lista, posicao):
#     for i in range(len(lista)):
#         if lista[i][0] == posicao[0] and lista[i][1] == posicao[1]:
#             lista.pop(i)
#             return


# def escolher_menor_f(lista_aberta):
#     melhor_no = lista_aberta[0]

#     for no in lista_aberta:
#         if no[4] < melhor_no[4]:
#             melhor_no = no
#         elif no[4] == melhor_no[4] and no[3] < melhor_no[3]:
#             melhor_no = no

#     return melhor_no


# def reconstruir_caminho(lista_fechada, objetivo):
#     caminho = []
#     no_atual = buscar_no_por_posicao(lista_fechada, objetivo)

#     while no_atual is not None:
#         caminho.append(obter_posicao(no_atual))

#         pai_linha = no_atual[5]
#         pai_coluna = no_atual[6]

#         if pai_linha is None or pai_coluna is None:
#             break

#         no_atual = buscar_no_por_posicao(lista_fechada, (pai_linha, pai_coluna))

#     caminho.reverse()
#     return caminho


# def posicao_valida(mapa, posicao):
#     linha, coluna = posicao

#     if linha < 0 or linha >= len(mapa):
#         return False

#     if coluna < 0 or coluna >= len(mapa[0]):
#         return False

#     return mapa[linha][coluna] != "#"


# def obter_vizinhos(posicao, mapa):
#     linha, coluna = posicao

#     movimentos = [
#         (-1, 0),
#         (1, 0),
#         (0, -1),
#         (0, 1)
#     ]

#     vizinhos = []

#     for mov_linha, mov_coluna in movimentos:
#         nova_posicao = (linha + mov_linha, coluna + mov_coluna)

#         if posicao_valida(mapa, nova_posicao):
#             vizinhos.append(nova_posicao)

#     return vizinhos


# def a_estrela(mapa, inicio, objetivo):
#     lista_aberta = []
#     lista_fechada = []

#     no_inicial = criar_no(inicio, 0, objetivo, None)
#     lista_aberta.append(no_inicial)

#     while len(lista_aberta) > 0:
#         no_atual = escolher_menor_f(lista_aberta)
#         posicao_atual = obter_posicao(no_atual)

#         remover_no_por_posicao(lista_aberta, posicao_atual)
#         lista_fechada.append(no_atual)

#         if posicao_atual == objetivo:
#             return reconstruir_caminho(lista_fechada, objetivo)

#         vizinhos = obter_vizinhos(posicao_atual, mapa)

#         for posicao_vizinho in vizinhos:
#             if buscar_no_por_posicao(lista_fechada, posicao_vizinho) is not None:
#                 continue

#             novo_g = no_atual[2] + 1
#             no_na_aberta = buscar_no_por_posicao(lista_aberta, posicao_vizinho)

#             if no_na_aberta is None:
#                 novo_no = criar_no(posicao_vizinho, novo_g, objetivo, posicao_atual)
#                 lista_aberta.append(novo_no)
#             else:
#                 if novo_g < no_na_aberta[2]:
#                     novo_h = heuristica(posicao_vizinho, objetivo)
#                     novo_f = novo_g + novo_h

#                     no_na_aberta[2] = novo_g
#                     no_na_aberta[3] = novo_h
#                     no_na_aberta[4] = novo_f
#                     no_na_aberta[5] = posicao_atual[0]
#                     no_na_aberta[6] = posicao_atual[1]

#     return None


# def grid_para_tela(posicao_grid):
#     linha, coluna = posicao_grid

#     x = coluna * TAMANHO_TILE + TAMANHO_TILE // 2
#     y = ALTURA_HUD + (LINHAS - 1 - linha) * TAMANHO_TILE + TAMANHO_TILE // 2

#     return x, y


# def tela_para_grid(x, y):
#     coluna = int(x // TAMANHO_TILE)
#     linha = LINHAS - 1 - int((y - ALTURA_HUD) // TAMANHO_TILE)

#     return linha, coluna


# def limites_tile(linha, coluna):
#     x, y = grid_para_tela((linha, coluna))

#     esquerda = x - TAMANHO_TILE // 2
#     direita = x + TAMANHO_TILE // 2
#     baixo = y - TAMANHO_TILE // 2
#     cima = y + TAMANHO_TILE // 2

#     return esquerda, direita, baixo, cima


# class JogoAStar(arcade.Window):

#     def __init__(self):
#         super().__init__(LARGURA_TELA, ALTURA_TELA, "A* com Arcade 3.3.3")

#         self.mapa = MAPA_TEXTO

#         self.player_x = 0
#         self.player_y = 0

#         self.inimigo_x = 0
#         self.inimigo_y = 0

#         self.caminho = None
#         self.tempo_recalculo = 0

#         self.luz_ativa = False
#         self.sombra_list = arcade.SpriteList()
#         self.blocos_sombra = []
#         self.ultima_posicao_luz = None

#         self.teclas = {
#             arcade.key.UP: False,
#             arcade.key.DOWN: False,
#             arcade.key.LEFT: False,
#             arcade.key.RIGHT: False
#         }

#         self.texto_info = arcade.Text(
#             "Setas: mover jogador | L: liga/desliga luz | Inimigo usa A*",
#             20,
#             20,
#             arcade.color.WHITE,
#             16
#         )

#         self.setup()
#         self.criar_sombra_otimizada()

#     def setup(self):
#         for linha in range(LINHAS):
#             for coluna in range(COLUNAS):
#                 simbolo = self.mapa[linha][coluna]
#                 x, y = grid_para_tela((linha, coluna))

#                 if simbolo == "S":
#                     self.player_x = x
#                     self.player_y = y

#                 elif simbolo == "G":
#                     self.inimigo_x = x
#                     self.inimigo_y = y

#     def on_draw(self):
#         self.clear(arcade.color.BLACK)

#         self.desenhar_mapa()
#         self.desenhar_caminho()
#         self.desenhar_personagens()

#         self.desenhar_escuridao_com_halo()

#         self.texto_info.draw()

#     def desenhar_mapa(self):
#         for linha in range(LINHAS):
#             for coluna in range(COLUNAS):
#                 simbolo = self.mapa[linha][coluna]

#                 esquerda, direita, baixo, cima = limites_tile(linha, coluna)

#                 if simbolo == "#":
#                     cor = (35, 35, 45)
#                 else:
#                     cor = (90, 90, 105)

#                 arcade.draw_lrbt_rectangle_filled(
#                     left=esquerda,
#                     right=direita,
#                     bottom=baixo,
#                     top=cima,
#                     color=cor
#                 )

#                 arcade.draw_lrbt_rectangle_outline(
#                     left=esquerda,
#                     right=direita,
#                     bottom=baixo,
#                     top=cima,
#                     color=(20, 20, 25),
#                     border_width=2
#                 )

#     def desenhar_caminho(self):
#         if self.caminho is None:
#             return

#         for posicao in self.caminho:
#             x, y = grid_para_tela(posicao)

#             arcade.draw_circle_filled(
#                 x,
#                 y,
#                 8,
#                 arcade.color.YELLOW
#             )

#     def desenhar_personagens(self):
#         arcade.draw_circle_filled(
#             self.player_x,
#             self.player_y,
#             24,
#             arcade.color.BLUE
#         )

#         arcade.draw_circle_filled(
#             self.inimigo_x,
#             self.inimigo_y,
#             24,
#             arcade.color.RED
#         )

#     def criar_sombra_otimizada(self):
#         textura_sombra = arcade.make_soft_square_texture(
#             size=TAMANHO_BLOCO_SOMBRA,
#             color=(0, 0, 0),
#             outer_alpha=255
#         )

#         for x in range(0, LARGURA_TELA, TAMANHO_BLOCO_SOMBRA):
#             for y in range(ALTURA_HUD, ALTURA_TELA, TAMANHO_BLOCO_SOMBRA):

#                 bloco = arcade.Sprite()
#                 bloco.texture = textura_sombra
#                 bloco.center_x = x + TAMANHO_BLOCO_SOMBRA / 2
#                 bloco.center_y = y + TAMANHO_BLOCO_SOMBRA / 2
#                 bloco.alpha = ALPHA_MAXIMO_SOMBRA

#                 self.sombra_list.append(bloco)
#                 self.blocos_sombra.append(bloco)


#     def atualizar_sombra_otimizada(self):
#         posicao_atual = (int(self.player_x), int(self.player_y))

#         if self.ultima_posicao_luz == posicao_atual:
#             return

#         self.ultima_posicao_luz = posicao_atual

#         for bloco in self.blocos_sombra:
#             dx = bloco.center_x - self.player_x
#             dy = bloco.center_y - self.player_y

#             distancia = (dx ** 2 + dy ** 2) ** 0.5

#             if distancia >= RAIO_LUZ:
#                 bloco.alpha = ALPHA_MAXIMO_SOMBRA
#             else:
#                 proporcao = distancia / RAIO_LUZ
#                 bloco.alpha = int((proporcao ** 2) * ALPHA_MAXIMO_SOMBRA)


#     def desenhar_escuridao_com_halo(self):
#         if not self.luz_ativa:
#             return

#         self.atualizar_sombra_otimizada()
#         self.sombra_list.draw()

#     def on_key_press(self, key, modifiers):
#         if key == arcade.key.L:
#             self.luz_ativa = not self.luz_ativa
#             self.ultima_posicao_luz = None
#             return

#         if key in self.teclas:
#             self.teclas[key] = True

#     def on_key_release(self, key, modifiers):
#         if key in self.teclas:
#             self.teclas[key] = False

#     def pode_mover_para(self, novo_x, novo_y):
#         linha, coluna = tela_para_grid(novo_x, novo_y)
#         return posicao_valida(self.mapa, (linha, coluna))

#     def mover_jogador(self):
#         dx = 0
#         dy = 0

#         if self.teclas[arcade.key.UP]:
#             dy += VELOCIDADE_JOGADOR
#         if self.teclas[arcade.key.DOWN]:
#             dy -= VELOCIDADE_JOGADOR
#         if self.teclas[arcade.key.LEFT]:
#             dx -= VELOCIDADE_JOGADOR
#         if self.teclas[arcade.key.RIGHT]:
#             dx += VELOCIDADE_JOGADOR

#         novo_x = self.player_x + dx
#         novo_y = self.player_y

#         if self.pode_mover_para(novo_x, novo_y):
#             self.player_x = novo_x

#         novo_x = self.player_x
#         novo_y = self.player_y + dy

#         if self.pode_mover_para(novo_x, novo_y):
#             self.player_y = novo_y

#     def mover_inimigo_com_astar(self, delta_time):
#         self.tempo_recalculo += delta_time

#         if self.tempo_recalculo >= 0.25:
#             self.tempo_recalculo = 0

#             inicio = tela_para_grid(self.inimigo_x, self.inimigo_y)
#             objetivo = tela_para_grid(self.player_x, self.player_y)

#             self.caminho = a_estrela(self.mapa, inicio, objetivo)

#         if self.caminho is None:
#             return

#         if len(self.caminho) < 2:
#             return

#         proxima_posicao = self.caminho[1]
#         destino_x, destino_y = grid_para_tela(proxima_posicao)

#         diferenca_x = destino_x - self.inimigo_x
#         diferenca_y = destino_y - self.inimigo_y

#         distancia = (diferenca_x ** 2 + diferenca_y ** 2) ** 0.5

#         if distancia <= VELOCIDADE_INIMIGO:
#             self.inimigo_x = destino_x
#             self.inimigo_y = destino_y
#         else:
#             direcao_x = diferenca_x / distancia
#             direcao_y = diferenca_y / distancia

#             self.inimigo_x += direcao_x * VELOCIDADE_INIMIGO
#             self.inimigo_y += direcao_y * VELOCIDADE_INIMIGO

#     def on_update(self, delta_time):
#         self.mover_jogador()
#         self.mover_inimigo_com_astar(delta_time)


# def main():
#     jogo = JogoAStar()
#     arcade.run()


# if __name__ == "__main__":
#     main()


####################################
# A* no Arcade 3.3.3
# Com iluminação ativada/desativada pela tecla L
####################################

# import arcade


# TAMANHO_TILE = 80
# ALTURA_HUD = 60

# RAIO_LUZ = 120
# TAMANHO_BLOCO_SOMBRA = 24
# ALPHA_MAXIMO_SOMBRA = 245
# LUZ_ATIVA_INICIAL = False

# MAPA_TEXTO = [
#     "#############",
#     "#S_____#____#",
#     "#_####_#_##_#",
#     "#____#______#",
#     "#__#_###__#_#",
#     "##_#______#_#",
#     "#G___#_#____#",
#     "#############"
# ]

# LINHAS = len(MAPA_TEXTO)
# COLUNAS = len(MAPA_TEXTO[0])

# LARGURA_TELA = COLUNAS * TAMANHO_TILE
# ALTURA_TELA = LINHAS * TAMANHO_TILE + ALTURA_HUD

# VELOCIDADE_JOGADOR = 4
# VELOCIDADE_INIMIGO = 4


# def heuristica(a, b):
#     return abs(a[0] - b[0]) + abs(a[1] - b[1])


# def criar_no(posicao, g, objetivo, pai):
#     h = heuristica(posicao, objetivo)
#     f = g + h

#     if pai is None:
#         pai_linha = None
#         pai_coluna = None
#     else:
#         pai_linha = pai[0]
#         pai_coluna = pai[1]

#     return [posicao[0], posicao[1], g, h, f, pai_linha, pai_coluna]


# def obter_posicao(no):
#     return (no[0], no[1])


# def buscar_no_por_posicao(lista, posicao):
#     for no in lista:
#         if no[0] == posicao[0] and no[1] == posicao[1]:
#             return no
#     return None


# def remover_no_por_posicao(lista, posicao):
#     for i in range(len(lista)):
#         if lista[i][0] == posicao[0] and lista[i][1] == posicao[1]:
#             lista.pop(i)
#             return


# def escolher_menor_f(lista_aberta):
#     melhor_no = lista_aberta[0]

#     for no in lista_aberta:
#         if no[4] < melhor_no[4]:
#             melhor_no = no
#         elif no[4] == melhor_no[4] and no[3] < melhor_no[3]:
#             melhor_no = no

#     return melhor_no


# def reconstruir_caminho(lista_fechada, objetivo):
#     caminho = []
#     no_atual = buscar_no_por_posicao(lista_fechada, objetivo)

#     while no_atual is not None:
#         caminho.append(obter_posicao(no_atual))

#         pai_linha = no_atual[5]
#         pai_coluna = no_atual[6]

#         if pai_linha is None or pai_coluna is None:
#             break

#         no_atual = buscar_no_por_posicao(lista_fechada, (pai_linha, pai_coluna))

#     caminho.reverse()
#     return caminho


# def posicao_valida(mapa, posicao):
#     linha, coluna = posicao

#     if linha < 0 or linha >= len(mapa):
#         return False

#     if coluna < 0 or coluna >= len(mapa[0]):
#         return False

#     return mapa[linha][coluna] != "#"


# def obter_vizinhos(posicao, mapa):
#     linha, coluna = posicao

#     movimentos = [
#         (-1, 0),
#         (1, 0),
#         (0, -1),
#         (0, 1)
#     ]

#     vizinhos = []

#     for mov_linha, mov_coluna in movimentos:
#         nova_posicao = (linha + mov_linha, coluna + mov_coluna)

#         if posicao_valida(mapa, nova_posicao):
#             vizinhos.append(nova_posicao)

#     return vizinhos


# def a_estrela(mapa, inicio, objetivo):
#     lista_aberta = []
#     lista_fechada = []

#     lista_aberta.append(criar_no(inicio, 0, objetivo, None))

#     while len(lista_aberta) > 0:
#         no_atual = escolher_menor_f(lista_aberta)
#         posicao_atual = obter_posicao(no_atual)

#         remover_no_por_posicao(lista_aberta, posicao_atual)
#         lista_fechada.append(no_atual)

#         if posicao_atual == objetivo:
#             return reconstruir_caminho(lista_fechada, objetivo)

#         for posicao_vizinho in obter_vizinhos(posicao_atual, mapa):
#             if buscar_no_por_posicao(lista_fechada, posicao_vizinho) is not None:
#                 continue

#             novo_g = no_atual[2] + 1
#             no_na_aberta = buscar_no_por_posicao(lista_aberta, posicao_vizinho)

#             if no_na_aberta is None:
#                 lista_aberta.append(
#                     criar_no(posicao_vizinho, novo_g, objetivo, posicao_atual)
#                 )
#             elif novo_g < no_na_aberta[2]:
#                 novo_h = heuristica(posicao_vizinho, objetivo)
#                 novo_f = novo_g + novo_h

#                 no_na_aberta[2] = novo_g
#                 no_na_aberta[3] = novo_h
#                 no_na_aberta[4] = novo_f
#                 no_na_aberta[5] = posicao_atual[0]
#                 no_na_aberta[6] = posicao_atual[1]

#     return None


# def grid_para_tela(posicao_grid):
#     linha, coluna = posicao_grid

#     x = coluna * TAMANHO_TILE + TAMANHO_TILE // 2
#     y = ALTURA_HUD + (LINHAS - 1 - linha) * TAMANHO_TILE + TAMANHO_TILE // 2

#     return x, y


# def tela_para_grid(x, y):
#     coluna = int(x // TAMANHO_TILE)
#     linha = LINHAS - 1 - int((y - ALTURA_HUD) // TAMANHO_TILE)

#     return linha, coluna


# def limites_tile(linha, coluna):
#     x, y = grid_para_tela((linha, coluna))

#     esquerda = x - TAMANHO_TILE // 2
#     direita = x + TAMANHO_TILE // 2
#     baixo = y - TAMANHO_TILE // 2
#     cima = y + TAMANHO_TILE // 2

#     return esquerda, direita, baixo, cima


# class JogoAStar(arcade.Window):

#     def __init__(self):
#         super().__init__(LARGURA_TELA, ALTURA_TELA, "A* com Iluminação - Arcade 3.3.3")

#         self.mapa = MAPA_TEXTO

#         self.player_x = 0
#         self.player_y = 0

#         self.inimigo_x = 0
#         self.inimigo_y = 0

#         self.caminho = None
#         self.tempo_recalculo = 0

#         self.luz_ativa = LUZ_ATIVA_INICIAL
#         self.sombra_list = arcade.SpriteList()
#         self.blocos_sombra = []
#         self.ultima_posicao_luz = None

#         self.teclas = {
#             arcade.key.UP: False,
#             arcade.key.DOWN: False,
#             arcade.key.LEFT: False,
#             arcade.key.RIGHT: False
#         }

#         self.texto_info = arcade.Text(
#             "Setas: mover jogador | L: liga/desliga iluminacao | Inimigo usa A*",
#             20,
#             20,
#             arcade.color.WHITE,
#             16
#         )

#         self.setup()
#         self.criar_sombra()

#     def setup(self):
#         for linha in range(LINHAS):
#             for coluna in range(COLUNAS):
#                 simbolo = self.mapa[linha][coluna]
#                 x, y = grid_para_tela((linha, coluna))

#                 if simbolo == "S":
#                     self.player_x = x
#                     self.player_y = y
#                 elif simbolo == "G":
#                     self.inimigo_x = x
#                     self.inimigo_y = y

#     def criar_sombra(self):
#         textura_sombra = arcade.make_soft_square_texture(
#             size=TAMANHO_BLOCO_SOMBRA + 2,
#             color=(0, 0, 0),
#             outer_alpha=255
#         )

#         for x in range(0, LARGURA_TELA, TAMANHO_BLOCO_SOMBRA):
#             for y in range(ALTURA_HUD, ALTURA_TELA, TAMANHO_BLOCO_SOMBRA):
#                 bloco = arcade.Sprite()
#                 bloco.texture = textura_sombra
#                 bloco.center_x = x + TAMANHO_BLOCO_SOMBRA / 2
#                 bloco.center_y = y + TAMANHO_BLOCO_SOMBRA / 2
#                 bloco.alpha = ALPHA_MAXIMO_SOMBRA

#                 self.sombra_list.append(bloco)
#                 self.blocos_sombra.append(bloco)

#     def atualizar_sombra(self):
#         posicao_atual = (int(self.player_x), int(self.player_y))

#         if self.ultima_posicao_luz == posicao_atual:
#             return

#         self.ultima_posicao_luz = posicao_atual

#         for bloco in self.blocos_sombra:
#             dx = bloco.center_x - self.player_x
#             dy = bloco.center_y - self.player_y
#             distancia = (dx ** 2 + dy ** 2) ** 0.5

#             if distancia >= RAIO_LUZ:
#                 bloco.alpha = ALPHA_MAXIMO_SOMBRA
#             else:
#                 proporcao = distancia / RAIO_LUZ
#                 bloco.alpha = int((proporcao ** 2) * ALPHA_MAXIMO_SOMBRA)

#     def on_draw(self):
#         self.clear(arcade.color.BLACK)

#         self.desenhar_mapa()
#         self.desenhar_caminho()
#         self.desenhar_personagens()

#         if self.luz_ativa:
#             self.atualizar_sombra()
#             self.sombra_list.draw()

#         self.texto_info.draw()

#     def desenhar_mapa(self):
#         for linha in range(LINHAS):
#             for coluna in range(COLUNAS):
#                 simbolo = self.mapa[linha][coluna]
#                 esquerda, direita, baixo, cima = limites_tile(linha, coluna)

#                 if simbolo == "#":
#                     cor = (35, 35, 45)
#                 else:
#                     cor = (90, 90, 105)

#                 arcade.draw_lrbt_rectangle_filled(
#                     left=esquerda,
#                     right=direita,
#                     bottom=baixo,
#                     top=cima,
#                     color=cor
#                 )

#                 arcade.draw_lrbt_rectangle_outline(
#                     left=esquerda,
#                     right=direita,
#                     bottom=baixo,
#                     top=cima,
#                     color=(20, 20, 25),
#                     border_width=2
#                 )

#     def desenhar_caminho(self):
#         if self.caminho is None:
#             return

#         for posicao in self.caminho:
#             x, y = grid_para_tela(posicao)

#             arcade.draw_circle_filled(
#                 x,
#                 y,
#                 8,
#                 arcade.color.YELLOW
#             )

#     def desenhar_personagens(self):
#         arcade.draw_circle_filled(
#             self.player_x,
#             self.player_y,
#             24,
#             arcade.color.BLUE
#         )

#         arcade.draw_circle_filled(
#             self.inimigo_x,
#             self.inimigo_y,
#             24,
#             arcade.color.RED
#         )

#     def on_key_press(self, key, modifiers):
#         if key == arcade.key.L:
#             self.luz_ativa = not self.luz_ativa
#             self.ultima_posicao_luz = None
#             return

#         if key in self.teclas:
#             self.teclas[key] = True

#     def on_key_release(self, key, modifiers):
#         if key in self.teclas:
#             self.teclas[key] = False

#     def pode_mover_para(self, novo_x, novo_y):
#         linha, coluna = tela_para_grid(novo_x, novo_y)
#         return posicao_valida(self.mapa, (linha, coluna))

#     def mover_jogador(self):
#         dx = 0
#         dy = 0

#         if self.teclas[arcade.key.UP]:
#             dy += VELOCIDADE_JOGADOR
#         if self.teclas[arcade.key.DOWN]:
#             dy -= VELOCIDADE_JOGADOR
#         if self.teclas[arcade.key.LEFT]:
#             dx -= VELOCIDADE_JOGADOR
#         if self.teclas[arcade.key.RIGHT]:
#             dx += VELOCIDADE_JOGADOR

#         novo_x = self.player_x + dx
#         novo_y = self.player_y

#         if self.pode_mover_para(novo_x, novo_y):
#             self.player_x = novo_x

#         novo_x = self.player_x
#         novo_y = self.player_y + dy

#         if self.pode_mover_para(novo_x, novo_y):
#             self.player_y = novo_y

#     def mover_inimigo_com_astar(self, delta_time):
#         self.tempo_recalculo += delta_time

#         if self.tempo_recalculo >= 0.25:
#             self.tempo_recalculo = 0

#             inicio = tela_para_grid(self.inimigo_x, self.inimigo_y)
#             objetivo = tela_para_grid(self.player_x, self.player_y)

#             self.caminho = a_estrela(self.mapa, inicio, objetivo)

#         if self.caminho is None or len(self.caminho) < 2:
#             return

#         proxima_posicao = self.caminho[1]
#         destino_x, destino_y = grid_para_tela(proxima_posicao)

#         diferenca_x = destino_x - self.inimigo_x
#         diferenca_y = destino_y - self.inimigo_y

#         distancia = (diferenca_x ** 2 + diferenca_y ** 2) ** 0.5

#         if distancia <= VELOCIDADE_INIMIGO:
#             self.inimigo_x = destino_x
#             self.inimigo_y = destino_y
#         else:
#             direcao_x = diferenca_x / distancia
#             direcao_y = diferenca_y / distancia

#             self.inimigo_x += direcao_x * VELOCIDADE_INIMIGO
#             self.inimigo_y += direcao_y * VELOCIDADE_INIMIGO

#     def on_update(self, delta_time):
#         self.mover_jogador()
#         self.mover_inimigo_com_astar(delta_time)


# def main():
#     jogo = JogoAStar()
#     arcade.run()


# if __name__ == "__main__":
#     main()


####################################
# A* no Arcade 3.3.3
# Iluminação com máscara escura e halo amarelado
####################################

# import arcade
# from PIL import Image


# TAMANHO_TILE = 80
# ALTURA_HUD = 60

# RAIO_LUZ = 110
# ALPHA_ESCURO = 235
# LUZ_ATIVA_INICIAL = False

# COR_LUZ_VELA = (255, 190, 70)
# ALPHA_LUZ_VELA = 65

# MAPA_TEXTO = [
#     "#############",
#     "#S_____#____#",
#     "#_####_#_##_#",
#     "#____#______#",
#     "#__#_###__#_#",
#     "##_#______#_#",
#     "#G___#_#____#",
#     "#############"
# ]

# LINHAS = len(MAPA_TEXTO)
# COLUNAS = len(MAPA_TEXTO[0])

# LARGURA_TELA = COLUNAS * TAMANHO_TILE
# ALTURA_TELA = LINHAS * TAMANHO_TILE + ALTURA_HUD

# VELOCIDADE_JOGADOR = 4
# VELOCIDADE_INIMIGO = 4


# def heuristica(a, b):
#     return abs(a[0] - b[0]) + abs(a[1] - b[1])


# def criar_no(posicao, g, objetivo, pai):
#     h = heuristica(posicao, objetivo)
#     f = g + h

#     if pai is None:
#         pai_linha = None
#         pai_coluna = None
#     else:
#         pai_linha = pai[0]
#         pai_coluna = pai[1]

#     return [posicao[0], posicao[1], g, h, f, pai_linha, pai_coluna]


# def obter_posicao(no):
#     return (no[0], no[1])


# def buscar_no_por_posicao(lista, posicao):
#     for no in lista:
#         if no[0] == posicao[0] and no[1] == posicao[1]:
#             return no
#     return None


# def remover_no_por_posicao(lista, posicao):
#     for i in range(len(lista)):
#         if lista[i][0] == posicao[0] and lista[i][1] == posicao[1]:
#             lista.pop(i)
#             return


# def escolher_menor_f(lista_aberta):
#     melhor_no = lista_aberta[0]

#     for no in lista_aberta:
#         if no[4] < melhor_no[4]:
#             melhor_no = no
#         elif no[4] == melhor_no[4] and no[3] < melhor_no[3]:
#             melhor_no = no

#     return melhor_no


# def reconstruir_caminho(lista_fechada, objetivo):
#     caminho = []
#     no_atual = buscar_no_por_posicao(lista_fechada, objetivo)

#     while no_atual is not None:
#         caminho.append(obter_posicao(no_atual))

#         pai_linha = no_atual[5]
#         pai_coluna = no_atual[6]

#         if pai_linha is None or pai_coluna is None:
#             break

#         no_atual = buscar_no_por_posicao(lista_fechada, (pai_linha, pai_coluna))

#     caminho.reverse()
#     return caminho


# def posicao_valida(mapa, posicao):
#     linha, coluna = posicao

#     if linha < 0 or linha >= len(mapa):
#         return False

#     if coluna < 0 or coluna >= len(mapa[0]):
#         return False

#     return mapa[linha][coluna] != "#"


# def obter_vizinhos(posicao, mapa):
#     linha, coluna = posicao

#     movimentos = [
#         (-1, 0),
#         (1, 0),
#         (0, -1),
#         (0, 1)
#     ]

#     vizinhos = []

#     for mov_linha, mov_coluna in movimentos:
#         nova_posicao = (linha + mov_linha, coluna + mov_coluna)

#         if posicao_valida(mapa, nova_posicao):
#             vizinhos.append(nova_posicao)

#     return vizinhos


# def a_estrela(mapa, inicio, objetivo):
#     lista_aberta = []
#     lista_fechada = []

#     lista_aberta.append(criar_no(inicio, 0, objetivo, None))

#     while len(lista_aberta) > 0:
#         no_atual = escolher_menor_f(lista_aberta)
#         posicao_atual = obter_posicao(no_atual)

#         remover_no_por_posicao(lista_aberta, posicao_atual)
#         lista_fechada.append(no_atual)

#         if posicao_atual == objetivo:
#             return reconstruir_caminho(lista_fechada, objetivo)

#         for posicao_vizinho in obter_vizinhos(posicao_atual, mapa):
#             if buscar_no_por_posicao(lista_fechada, posicao_vizinho) is not None:
#                 continue

#             novo_g = no_atual[2] + 1
#             no_na_aberta = buscar_no_por_posicao(lista_aberta, posicao_vizinho)

#             if no_na_aberta is None:
#                 lista_aberta.append(
#                     criar_no(posicao_vizinho, novo_g, objetivo, posicao_atual)
#                 )
#             else:
#                 if novo_g < no_na_aberta[2]:
#                     novo_h = heuristica(posicao_vizinho, objetivo)
#                     novo_f = novo_g + novo_h

#                     no_na_aberta[2] = novo_g
#                     no_na_aberta[3] = novo_h
#                     no_na_aberta[4] = novo_f
#                     no_na_aberta[5] = posicao_atual[0]
#                     no_na_aberta[6] = posicao_atual[1]

#     return None


# def grid_para_tela(posicao_grid):
#     linha, coluna = posicao_grid

#     x = coluna * TAMANHO_TILE + TAMANHO_TILE // 2
#     y = ALTURA_HUD + (LINHAS - 1 - linha) * TAMANHO_TILE + TAMANHO_TILE // 2

#     return x, y


# def tela_para_grid(x, y):
#     coluna = int(x // TAMANHO_TILE)
#     linha = LINHAS - 1 - int((y - ALTURA_HUD) // TAMANHO_TILE)

#     return linha, coluna


# def limites_tile(linha, coluna):
#     x, y = grid_para_tela((linha, coluna))

#     esquerda = x - TAMANHO_TILE // 2
#     direita = x + TAMANHO_TILE // 2
#     baixo = y - TAMANHO_TILE // 2
#     cima = y + TAMANHO_TILE // 2

#     return esquerda, direita, baixo, cima


# class JogoAStar(arcade.Window):

#     def __init__(self):
#         super().__init__(
#             LARGURA_TELA,
#             ALTURA_TELA,
#             "A* com Iluminacao - Arcade 3.3.3"
#         )

#         self.mapa = MAPA_TEXTO

#         self.player_x = 0
#         self.player_y = 0

#         self.inimigo_x = 0
#         self.inimigo_y = 0

#         self.caminho = None
#         self.tempo_recalculo = 0

#         self.luz_ativa = LUZ_ATIVA_INICIAL

#         self.tamanho_mascara_luz = max(LARGURA_TELA, ALTURA_TELA) * 2
#         self.textura_mascara_luz = self.criar_textura_mascara_luz()

#         self.textura_luz_vela = arcade.make_soft_circle_texture(
#             RAIO_LUZ * 2,
#             COR_LUZ_VELA,
#             ALPHA_LUZ_VELA,
#             0
#         )

#         self.teclas = {
#             arcade.key.UP: False,
#             arcade.key.DOWN: False,
#             arcade.key.LEFT: False,
#             arcade.key.RIGHT: False
#         }

#         self.texto_info = arcade.Text(
#             "Setas: mover jogador | L: liga/desliga luz | Inimigo usa A*",
#             20,
#             20,
#             arcade.color.WHITE,
#             16
#         )

#         self.setup()

#     def criar_textura_mascara_luz(self):
#         tamanho = self.tamanho_mascara_luz
#         centro = tamanho // 2

#         imagem = Image.new(
#             "RGBA",
#             (tamanho, tamanho),
#             (0, 0, 0, ALPHA_ESCURO)
#         )

#         pixels = imagem.load()

#         for y in range(tamanho):
#             for x in range(tamanho):
#                 dx = x - centro
#                 dy = y - centro

#                 distancia = (dx ** 2 + dy ** 2) ** 0.5

#                 if distancia <= RAIO_LUZ:
#                     proporcao = distancia / RAIO_LUZ

#                     alpha = int((proporcao ** 2.2) * ALPHA_ESCURO)

#                     pixels[x, y] = (0, 0, 0, alpha)

#         try:
#             return arcade.Texture(imagem)
#         except TypeError:
#             return arcade.Texture("mascara_luz", imagem)

#     def setup(self):
#         for linha in range(LINHAS):
#             for coluna in range(COLUNAS):
#                 simbolo = self.mapa[linha][coluna]
#                 x, y = grid_para_tela((linha, coluna))

#                 if simbolo == "S":
#                     self.player_x = x
#                     self.player_y = y

#                 elif simbolo == "G":
#                     self.inimigo_x = x
#                     self.inimigo_y = y

#     def on_draw(self):
#         self.clear(arcade.color.BLACK)

#         self.desenhar_mapa()
#         self.desenhar_caminho()
#         self.desenhar_personagens()

#         if self.luz_ativa:
#             self.desenhar_mascara_luz()

#         self.texto_info.draw()

#     def desenhar_mapa(self):
#         for linha in range(LINHAS):
#             for coluna in range(COLUNAS):
#                 simbolo = self.mapa[linha][coluna]
#                 esquerda, direita, baixo, cima = limites_tile(linha, coluna)

#                 if simbolo == "#":
#                     cor = (35, 35, 45)
#                 else:
#                     cor = (90, 90, 105)

#                 arcade.draw_lrbt_rectangle_filled(
#                     left=esquerda,
#                     right=direita,
#                     bottom=baixo,
#                     top=cima,
#                     color=cor
#                 )

#                 arcade.draw_lrbt_rectangle_outline(
#                     left=esquerda,
#                     right=direita,
#                     bottom=baixo,
#                     top=cima,
#                     color=(20, 20, 25),
#                     border_width=2
#                 )

#     def desenhar_caminho(self):
#         if self.caminho is None:
#             return

#         if not self.luz_ativa:
#             for posicao in self.caminho:
#                 x, y = grid_para_tela(posicao)

#                 arcade.draw_circle_filled(
#                     x,
#                     y,
#                     8,
#                     arcade.color.YELLOW
#                 )

#     def desenhar_personagens(self):
#         arcade.draw_circle_filled(
#             self.player_x,
#             self.player_y,
#             24,
#             arcade.color.BLUE
#         )

#         arcade.draw_circle_filled(
#             self.inimigo_x,
#             self.inimigo_y,
#             24,
#             arcade.color.RED
#         )

#     def desenhar_mascara_luz(self):
#         tamanho = self.tamanho_mascara_luz

#         arcade.draw_texture_rect(
#             texture=self.textura_mascara_luz,
#             rect=arcade.Rect(
#                 left=self.player_x - tamanho // 2,
#                 right=self.player_x + tamanho // 2,
#                 bottom=self.player_y - tamanho // 2,
#                 top=self.player_y + tamanho // 2,
#                 width=tamanho,
#                 height=tamanho,
#                 x=self.player_x,
#                 y=self.player_y
#             )
#         )

#         arcade.draw_texture_rect(
#             texture=self.textura_luz_vela,
#             rect=arcade.Rect(
#                 left=self.player_x - RAIO_LUZ,
#                 right=self.player_x + RAIO_LUZ,
#                 bottom=self.player_y - RAIO_LUZ,
#                 top=self.player_y + RAIO_LUZ,
#                 width=RAIO_LUZ * 2,
#                 height=RAIO_LUZ * 2,
#                 x=self.player_x,
#                 y=self.player_y
#             )
#         )

#         arcade.draw_circle_filled(
#             self.player_x,
#             self.player_y,
#             24,
#             arcade.color.BLUE
#         )

#     def on_key_press(self, key, modifiers):
#         if key == arcade.key.L:
#             self.luz_ativa = not self.luz_ativa
#             return

#         if key in self.teclas:
#             self.teclas[key] = True

#     def on_key_release(self, key, modifiers):
#         if key in self.teclas:
#             self.teclas[key] = False

#     def pode_mover_para(self, novo_x, novo_y):
#         linha, coluna = tela_para_grid(novo_x, novo_y)
#         return posicao_valida(self.mapa, (linha, coluna))

#     def mover_jogador(self):
#         dx = 0
#         dy = 0

#         if self.teclas[arcade.key.UP]:
#             dy += VELOCIDADE_JOGADOR
#         if self.teclas[arcade.key.DOWN]:
#             dy -= VELOCIDADE_JOGADOR
#         if self.teclas[arcade.key.LEFT]:
#             dx -= VELOCIDADE_JOGADOR
#         if self.teclas[arcade.key.RIGHT]:
#             dx += VELOCIDADE_JOGADOR

#         novo_x = self.player_x + dx
#         novo_y = self.player_y

#         if self.pode_mover_para(novo_x, novo_y):
#             self.player_x = novo_x

#         novo_x = self.player_x
#         novo_y = self.player_y + dy

#         if self.pode_mover_para(novo_x, novo_y):
#             self.player_y = novo_y

#     def mover_inimigo_com_astar(self, delta_time):
#         self.tempo_recalculo += delta_time

#         if self.tempo_recalculo >= 0.25:
#             self.tempo_recalculo = 0

#             inicio = tela_para_grid(self.inimigo_x, self.inimigo_y)
#             objetivo = tela_para_grid(self.player_x, self.player_y)

#             self.caminho = a_estrela(self.mapa, inicio, objetivo)

#         if self.caminho is None:
#             return

#         if len(self.caminho) < 2:
#             return

#         proxima_posicao = self.caminho[1]
#         destino_x, destino_y = grid_para_tela(proxima_posicao)

#         diferenca_x = destino_x - self.inimigo_x
#         diferenca_y = destino_y - self.inimigo_y

#         distancia = (diferenca_x ** 2 + diferenca_y ** 2) ** 0.5

#         if distancia <= VELOCIDADE_INIMIGO:
#             self.inimigo_x = destino_x
#             self.inimigo_y = destino_y
#         else:
#             direcao_x = diferenca_x / distancia
#             direcao_y = diferenca_y / distancia

#             self.inimigo_x += direcao_x * VELOCIDADE_INIMIGO
#             self.inimigo_y += direcao_y * VELOCIDADE_INIMIGO

#     def on_update(self, delta_time):
#         self.mover_jogador()
#         self.mover_inimigo_com_astar(delta_time)


# def main():
#     jogo = JogoAStar()
#     arcade.run()


# if __name__ == "__main__":
#     main()



####################################
# Exemplo de Flocking / Boids
# Arcade 3.3.3
# Boids seguindo o mouse
####################################

# import arcade
# import random
# import math


# LARGURA_TELA = 1000
# ALTURA_TELA = 700
# TITULO = "Flocking / Boids - Seguindo o Mouse"

# QUANTIDADE_BOIDS = 35

# RAIO_VISAO = 90
# DISTANCIA_SEPARACAO = 35

# VELOCIDADE_MAXIMA = 3.2
# FORCA_MAXIMA = 0.08

# PESO_SEPARACAO = 1.8
# PESO_ALINHAMENTO = 1.0
# PESO_COESAO = 0.9
# PESO_MOUSE = 0.7


# def limitar_vetor(x, y, limite):
#     modulo = math.sqrt(x ** 2 + y ** 2)

#     if modulo > limite and modulo != 0:
#         x = (x / modulo) * limite
#         y = (y / modulo) * limite

#     return x, y


# def distancia(x1, y1, x2, y2):
#     dx = x2 - x1
#     dy = y2 - y1

#     return math.sqrt(dx ** 2 + dy ** 2)


# class Boid:

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#         angulo = random.uniform(0, math.tau)

#         self.vx = math.cos(angulo) * VELOCIDADE_MAXIMA
#         self.vy = math.sin(angulo) * VELOCIDADE_MAXIMA

#         self.ax = 0
#         self.ay = 0

#     def aplicar_forca(self, fx, fy):
#         self.ax += fx
#         self.ay += fy

#     def calcular_separacao(self, boids):
#         direcao_x = 0
#         direcao_y = 0
#         total = 0

#         for outro in boids:
#             if outro is self:
#                 continue

#             d = distancia(self.x, self.y, outro.x, outro.y)

#             if 0 < d < DISTANCIA_SEPARACAO:
#                 diferenca_x = self.x - outro.x
#                 diferenca_y = self.y - outro.y

#                 diferenca_x /= d
#                 diferenca_y /= d

#                 direcao_x += diferenca_x
#                 direcao_y += diferenca_y

#                 total += 1

#         if total > 0:
#             direcao_x /= total
#             direcao_y /= total

#             direcao_x, direcao_y = limitar_vetor(
#                 direcao_x,
#                 direcao_y,
#                 VELOCIDADE_MAXIMA
#             )

#             direcao_x -= self.vx
#             direcao_y -= self.vy

#             direcao_x, direcao_y = limitar_vetor(
#                 direcao_x,
#                 direcao_y,
#                 FORCA_MAXIMA
#             )

#         return direcao_x, direcao_y

#     def calcular_alinhamento(self, boids):
#         media_vx = 0
#         media_vy = 0
#         total = 0

#         for outro in boids:
#             if outro is self:
#                 continue

#             d = distancia(self.x, self.y, outro.x, outro.y)

#             if d < RAIO_VISAO:
#                 media_vx += outro.vx
#                 media_vy += outro.vy
#                 total += 1

#         if total > 0:
#             media_vx /= total
#             media_vy /= total

#             media_vx, media_vy = limitar_vetor(
#                 media_vx,
#                 media_vy,
#                 VELOCIDADE_MAXIMA
#             )

#             media_vx -= self.vx
#             media_vy -= self.vy

#             media_vx, media_vy = limitar_vetor(
#                 media_vx,
#                 media_vy,
#                 FORCA_MAXIMA
#             )

#         return media_vx, media_vy

#     def calcular_coesao(self, boids):
#         centro_x = 0
#         centro_y = 0
#         total = 0

#         for outro in boids:
#             if outro is self:
#                 continue

#             d = distancia(self.x, self.y, outro.x, outro.y)

#             if d < RAIO_VISAO:
#                 centro_x += outro.x
#                 centro_y += outro.y
#                 total += 1

#         if total > 0:
#             centro_x /= total
#             centro_y /= total

#             desejado_x = centro_x - self.x
#             desejado_y = centro_y - self.y

#             desejado_x, desejado_y = limitar_vetor(
#                 desejado_x,
#                 desejado_y,
#                 VELOCIDADE_MAXIMA
#             )

#             desejado_x -= self.vx
#             desejado_y -= self.vy

#             desejado_x, desejado_y = limitar_vetor(
#                 desejado_x,
#                 desejado_y,
#                 FORCA_MAXIMA
#             )

#             return desejado_x, desejado_y

#         return 0, 0

#     def calcular_busca_mouse(self, mouse_x, mouse_y):
#         desejado_x = mouse_x - self.x
#         desejado_y = mouse_y - self.y

#         desejado_x, desejado_y = limitar_vetor(
#             desejado_x,
#             desejado_y,
#             VELOCIDADE_MAXIMA
#         )

#         steer_x = desejado_x - self.vx
#         steer_y = desejado_y - self.vy

#         steer_x, steer_y = limitar_vetor(
#             steer_x,
#             steer_y,
#             FORCA_MAXIMA
#         )

#         return steer_x, steer_y

#     def flocking(self, boids, mouse_x, mouse_y):
#         sep_x, sep_y = self.calcular_separacao(boids)
#         ali_x, ali_y = self.calcular_alinhamento(boids)
#         coe_x, coe_y = self.calcular_coesao(boids)
#         mouse_x_forca, mouse_y_forca = self.calcular_busca_mouse(mouse_x, mouse_y)

#         sep_x *= PESO_SEPARACAO
#         sep_y *= PESO_SEPARACAO

#         ali_x *= PESO_ALINHAMENTO
#         ali_y *= PESO_ALINHAMENTO

#         coe_x *= PESO_COESAO
#         coe_y *= PESO_COESAO

#         mouse_x_forca *= PESO_MOUSE
#         mouse_y_forca *= PESO_MOUSE

#         self.aplicar_forca(sep_x, sep_y)
#         self.aplicar_forca(ali_x, ali_y)
#         self.aplicar_forca(coe_x, coe_y)
#         self.aplicar_forca(mouse_x_forca, mouse_y_forca)

#     def atualizar(self):
#         self.vx += self.ax
#         self.vy += self.ay

#         self.vx, self.vy = limitar_vetor(
#             self.vx,
#             self.vy,
#             VELOCIDADE_MAXIMA
#         )

#         self.x += self.vx
#         self.y += self.vy

#         self.ax = 0
#         self.ay = 0

#         self.verificar_bordas()

#     def verificar_bordas(self):
#         if self.x < 0:
#             self.x = LARGURA_TELA

#         elif self.x > LARGURA_TELA:
#             self.x = 0

#         if self.y < 0:
#             self.y = ALTURA_TELA

#         elif self.y > ALTURA_TELA:
#             self.y = 0

#     def desenhar(self):
#         angulo = math.atan2(self.vy, self.vx)

#         ponta_x = self.x + math.cos(angulo) * 14
#         ponta_y = self.y + math.sin(angulo) * 14

#         esquerda_x = self.x + math.cos(angulo + 2.5) * 10
#         esquerda_y = self.y + math.sin(angulo + 2.5) * 10

#         direita_x = self.x + math.cos(angulo - 2.5) * 10
#         direita_y = self.y + math.sin(angulo - 2.5) * 10

#         arcade.draw_triangle_filled(
#             ponta_x,
#             ponta_y,
#             esquerda_x,
#             esquerda_y,
#             direita_x,
#             direita_y,
#             arcade.color.SKY_BLUE
#         )


# class JanelaBoids(arcade.Window):

#     def __init__(self):
#         super().__init__(LARGURA_TELA, ALTURA_TELA, TITULO)

#         self.boids = []

#         self.mouse_x = LARGURA_TELA // 2
#         self.mouse_y = ALTURA_TELA // 2

#         self.texto_titulo = arcade.Text(
#             "Flocking / Boids",
#             20,
#             ALTURA_TELA - 30,
#             arcade.color.WHITE,
#             20
#         )

#         self.texto_regras = arcade.Text(
#             "Regras: Separacao + Alinhamento + Coesao + Atracao pelo mouse",
#             20,
#             ALTURA_TELA - 60,
#             arcade.color.WHITE,
#             14
#         )

#         self.texto_pesos = arcade.Text(
#             f"Pesos: Sep={PESO_SEPARACAO} | Ali={PESO_ALINHAMENTO} | Coe={PESO_COESAO} | Mouse={PESO_MOUSE}",
#             20,
#             ALTURA_TELA - 85,
#             arcade.color.WHITE,
#             14
#         )

#         self.texto_mouse = arcade.Text(
#             "",
#             20,
#             20,
#             arcade.color.WHITE,
#             14
#         )

#         self.setup()

#     def setup(self):
#         for _ in range(QUANTIDADE_BOIDS):
#             x = random.randint(50, LARGURA_TELA - 50)
#             y = random.randint(50, ALTURA_TELA - 50)

#             boid = Boid(x, y)
#             self.boids.append(boid)

#     def on_draw(self):
#         self.clear(arcade.color.BLACK)

#         self.desenhar_alvo_mouse()

#         for boid in self.boids:
#             boid.desenhar()

#         self.texto_titulo.draw()
#         self.texto_regras.draw()
#         self.texto_pesos.draw()

#         self.texto_mouse.text = f"Alvo atual: mouse em ({int(self.mouse_x)}, {int(self.mouse_y)})"
#         self.texto_mouse.draw()

#     def desenhar_alvo_mouse(self):
#         arcade.draw_circle_outline(
#             self.mouse_x,
#             self.mouse_y,
#             20,
#             arcade.color.YELLOW,
#             2
#         )

#         arcade.draw_line(
#             self.mouse_x - 30,
#             self.mouse_y,
#             self.mouse_x + 30,
#             self.mouse_y,
#             arcade.color.YELLOW,
#             2
#         )

#         arcade.draw_line(
#             self.mouse_x,
#             self.mouse_y - 30,
#             self.mouse_x,
#             self.mouse_y + 30,
#             arcade.color.YELLOW,
#             2
#         )

#         arcade.draw_text(
#             "ALVO",
#             self.mouse_x + 25,
#             self.mouse_y + 20,
#             arcade.color.YELLOW,
#             12
#         )

#     def on_mouse_motion(self, x, y, dx, dy):
#         self.mouse_x = x
#         self.mouse_y = y

#     def on_update(self, delta_time):
#         for boid in self.boids:
#             boid.flocking(self.boids, self.mouse_x, self.mouse_y)

#         for boid in self.boids:
#             boid.atualizar()


# def main():
#     janela = JanelaBoids()
#     arcade.run()


# if __name__ == "__main__":
#     main()
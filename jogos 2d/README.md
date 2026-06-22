# Utility AI Simplificada

Projeto para o seminario de Tecnicas de Inteligencia Artificial para Jogos 2D.

Grupo: Mateus H e Marlon

## Tema

Utility AI Simplificada.

O NPC calcula valores de utilidade para quatro acoes:

- Atacar
- Fugir
- Buscar vida
- Patrulhar

A acao com maior pontuacao e escolhida a cada atualizacao do jogo. Os valores aparecem no painel lateral durante a execucao.

O exemplo foi montado como uma arena top-down com assets da propria Arcade: tanques, estrada em tiles formando uma malha, props de cenario, itens de vida usados pelo jogador e pelo NPC, tiros, particulas e indicadores visuais da decisao atual.

## Como executar

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python main.py
```

## Controles

- Setas ou WASD: mover o jogador
- Espaco: atirar no NPC
- R: reiniciar a demonstracao

## Como demonstrar em sala

1. Comece longe do NPC para mostrar a patrulha pela estrada, usando apenas parte da malha de ruas.
2. Aproxime-se do NPC para aumentar a utilidade de ataque.
3. Observe que, ao escolher atacar, o NPC passa a atirar no jogador.
4. Use espaco para atirar no NPC, reduzir a vida dele e gerar particulas de impacto.
5. Observe a IA trocar para fugir ou buscar vida conforme os valores mudam.
6. Mostre o painel lateral e explique que a maior barra define a acao escolhida.

## Organizacao do codigo

- `Jogador`: controla movimento, tiro e vida do jogador.
- `NpcUtilidade`: calcula utilidades, escolhe a maior acao e executa o comportamento.
- `Tiro`: representa os tiros do jogador e do NPC.
- `KitVida`: representa itens de vida que recuperam o jogador ou o NPC.
- `ParticulaFlutuante`: cria feedback visual para dano e troca de comportamento.
- `Jogo`: janela principal da Arcade, atualizacao, desenho, eventos de teclado e HUD.

O projeto segue o modelo top-down visto em aula: `arcade.Window`, `setup`, `on_draw`, `on_update`, eventos de teclado, `SpriteList`, classes e separacao de responsabilidades.

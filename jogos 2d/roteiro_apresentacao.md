# Roteiro de apresentacao

Tempo sugerido: ate 10 minutos.

## 1. Ideia geral

Nosso tema e Utility AI Simplificada. Em vez de o NPC seguir uma regra fixa, ele calcula uma pontuacao para cada acao possivel e escolhe a que parece mais util no momento.

No exemplo, o NPC pode:

- atacar o jogador;
- fugir;
- buscar vida;
- patrulhar.

## 2. O que aparece na tela

O jogador e o tanque azul. O NPC e o tanque vermelho. Os cristais verdes com simbolo de cura funcionam como pontos de vida. A estrada forma uma malha, mas o NPC usa apenas um trecho dela como trajeto de patrulha. A linha colorida mostra o alvo atual da IA e os circulos roxos marcam os pontos do percurso. No painel lateral aparecem as barras de utilidade e os simbolos de vida do jogador e do NPC.

## 3. Como a decisao funciona

A cada `on_update`, o NPC mede informacoes do jogo:

- distancia ate o jogador;
- vida atual do NPC;
- vida atual do jogador;
- distancia ate o kit de vida mais proximo.

Essas informacoes viram valores entre 0 e 1. Depois cada acao recebe uma formula de utilidade.

Exemplo:

- atacar fica mais util quando o jogador esta perto e o NPC tem bastante vida. Nesse estado, o NPC mira e atira;
- fugir fica mais util quando o NPC esta com pouca vida e o jogador esta perto;
- buscar vida fica mais util quando a vida do NPC esta baixa e existe kit disponivel;
- patrulhar fica mais util quando o jogador esta longe e nao existe perigo imediato.

## 4. Funcoes principais do codigo

- `calcular_utilidades`: calcula as pontuacoes de cada acao.
- `escolher_acao`: escolhe a acao com maior utilidade.
- `executar_acao`: executa atacar, fugir, buscar vida ou patrulhar.
- `Tiro`: representa tiros com velocidade, dano e colisao.
- `desenhar_painel`: desenha na tela os valores para a apresentacao.
- `criar_particulas`: cria feedback visual quando existe dano ou troca de comportamento.

## 5. Demonstracao pratica

Primeiro deixamos o jogador longe para mostrar o NPC patrulhando por um trecho da estrada. Depois aproximamos o jogador para mostrar a utilidade de ataque subindo e o NPC atirando. Em seguida usamos espaco para atirar no NPC; com pouca vida, a utilidade de fugir ou buscar vida cresce e o comportamento muda automaticamente. O painel lateral deve ser mostrado junto com a mudanca visual da linha de alvo.

## 6. Conclusao

A vantagem da Utility AI e permitir decisoes mais flexiveis. O NPC nao fica preso em uma sequencia fixa; ele compara opcoes e muda de comportamento conforme o estado do jogo.

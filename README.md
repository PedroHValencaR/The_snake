# The_snake
🐍 The Snake - Classic Snake Game in Python
Esta é uma implementação completa e polida do clássico jogo Snake, desenvolvido do zero com Python e a biblioteca Pygame. O projeto demonstra conceitos fundamentais de desenvolvimento de jogos, práticas de código limpo e atenção à experiência do usuário.

(Dica: Grave um GIF do seu jogo e substitua o link acima para uma apresentação visual incrível!)

📜 Descrição
Este não é apenas um clone básico do Snake. É uma versão rica em funcionalidades, projetada para ser uma experiência de jogo divertida, desafiadora e completa. O jogador controla uma cobra que cresce ao comer maçãs, enquanto a velocidade do jogo aumenta gradualmente. O objetivo é alcançar a maior pontuação possível sem colidir com as paredes ou com o próprio corpo da cobra.

✨ Funcionalidades
Este projeto inclui uma vasta gama de funcionalidades que vão além de uma implementação simples:

Gráficos Customizados: A cobra e a maçã são representadas por imagens .png personalizadas, não simples quadrados.

Cabeça da Cobra Animada: O sprite da cabeça da cobra rotaciona dinamicamente para apontar na direção do movimento (Cima, Baixo, Esquerda, Direita).

Corpo com Imagens: O corpo da cobra também é renderizado com sprites de imagem, criando um visual consistente e polido.

Dificuldade Progressiva: O jogo começa em uma velocidade gerenciável e acelera gradualmente cada vez que uma maçã é comida, proporcionando uma curva de dificuldade suave.

Sistema de High Score: A pontuação mais alta é salva automaticamente em um arquivo highscore.txt e exibida na tela inicial e na de game over, incentivando os jogadores a baterem seu recorde.

Efeitos Sonoros: Feedback de áudio para eventos chave, como comer uma maçã e a condição de game over, aprimorando a experiência do jogador.

Telas de UI Polidas: O jogo inclui uma tela de início estilizada com instruções e uma tela de game over clara e centralizada, com opções para jogar novamente ou sair.

Fundo Temático: Uma grade sutil é desenhada no fundo, reforçando a sensação clássica e retrô do jogo.

🛠️ Tecnologias Utilizadas
Linguagem: Python 3

Biblioteca: Pygame

⚙️ Configuração e Instalação
Para rodar este projeto em sua máquina local, siga estes passos:

Clone o repositório ou baixe o código-fonte.

Instale a biblioteca necessária. Certifique-se de que você tem o Python 3 instalado e então rode o seguinte comando no seu terminal:

Bash

pip install pygame
Crie a estrutura de pastas. O código espera uma estrutura de pastas específica para as imagens e sons. Na pasta principal do projeto, crie duas subpastas: imagens e sons.

Coloque os arquivos (assets) nas pastas corretas.

Dentro da pasta imagens, você deve ter:

apple.png

snake_head.png

snake_body.png

Dentro da pasta sons, você deve ter:

comer.mp3

game_over.mp3

A estrutura final do projeto deve se parecer com esta:

pasta-do-projeto/
├── snake_game.py
├── highscore.txt
├── README.md
├── imagens/
│   ├── apple.png
│   ├── snake_head.png
│   └── snake_body.png
└── sons/
    ├── comer.mp3
    └── game_over.mp3
Execute o jogo!

Bash

python snake_game.py
🎮 Como Jogar
Objetivo: Marque o máximo de pontos possível comendo as maçãs sem bater nas paredes ou em si mesmo.

Controles:

Teclas de Seta (Cima, Baixo, Esquerda, Direita): Controlam a direção da cobra.

Game Over:

Pressione 'C' para jogar novamente.

Pressione 'S' para sair do jogo.

🚀 Melhorias Futuras
Este projeto tem uma base sólida, mas sempre há maneiras de expandi-lo. Possíveis funcionalidades futuras incluem:

Função de Pause: Uma tecla para pausar e resumir o jogo.

Múltiplos Níveis: Arenas diferentes com obstáculos.

Power-ups: Maçãs especiais que concedem habilidades temporárias (ex: diminuir a velocidade, ficar invencível).

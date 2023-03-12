# Pygame (Desenvolvimento de Jogos com Python)
 Meus estudos da biblioteca Pygames.
 ***
 
 De início, posso adiantar que venho estudando pela playlist [Pygame (Python Game Development)](https://youtube.com/playlist?list=PL6gx4Cwl9DGAjkwJocj7vlc_mFU-4wXJq) do canal [thenewboston](https://www.youtube.com/@thenewboston).
 Por ser um conteúdo em inglês, talvez seja bacana deixar minhas anotações em português, podendo talvez ser de ajuda a alguém.
 Espero que assim o seja.
 
 _Que a força esteja com vocês..._
*** 

### Tutorial 01

###### Aqui há apenas uma introdução de como instalar o pygame:
Provavelmente, para começar a estudar uma biblioteca, já se possui os conhecimentos suficientes para instalá-la, mas para não deixar vazio...
Creio que a opção mais simples e menos sucetível a erros é, pela _IDLE_ do python, rodar o comando `install pygame.`
***

### Tutorial 02

###### Aqui aprendemos a montar o esqueleto básico de qualquer programa com o pygame:
```
import pygame # Importar Biblioteca

pygame.init() # Iniciar operação do pygame

gameDisplay = pygame.display.set_mode((800, 600)) # Criação do display

pygame.display.update() # Atualiza a tela, mas se torna possivel alteração apenas da parte modificada
pygame.display.flip() # Igual flipbooks, atualiza a tela inteira
# O comando pygame.display.update() sem especificações exerce a mesma função de pygame.display.flip()

pygame.quit() # Encerra o pygame
quit() # Encerra o Python
```

Resultado esperado... O seu primeiro programa com pygame :)
É um incrível display que fecha instantaneamente... Não é muito, mas é o primeiro passo

**Notas:**
 * Os valores 800 e 600 de `pygame.display.set_mode((800, 600))` se referem ao tamanho do display - escolha o que achar melhor.(Variável que recebe o display também)
 * Lembre-se que os comandos `pygame.display.update()` e `pygame.display.flip()` possuem a mesma função, então escolha o que julgar melhor para o seu jogo.
 Caso queira um padrão, geralmente se utiliza o primeiro.
***

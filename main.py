import os
import copy


# FUNÇÂO PARA LIMPAR A TELA
def clear():
  os.system('clear')

# ABRINDO TXT E SALVANDO EM VARIAVEL
#  5 5 - TAMANHO DA MATRIZ
#  8   - NUMERO DE BOMBAS
#  0 1 - POSIÇÂO DAS BOMBAS
#  1 0
#  1 2...
with open("posicao.txt", 'r') as pos: # Quando with é utilizado, o arquivo é fechado automaticamente
  posicao = pos.readlines()

# SEPARANDO OS DADOS DA LISTA
Posicao = []
for linha in posicao:
  linha = linha.rstrip('\n') # Remove \n do final da string
  pData = linha.split(' ') # Encontra os espaços e divide a string
  Posicao.append(pData)

# SEPARANDO O TAMANHO DA MATRIZ PARA OUTRA LISTA
TAM = []
TAM.append(Posicao[int(0)]) # Define a posição 0 de TAM como [['11', '11']]
Posicao.remove(TAM[0])

# SEPARANDO A QUANTIDADE DE BOMBAS PARA UMA VARIAVEL
minas = list(map(int,Posicao[0])) ##!!!
Posicao.pop(0)
nMinas = minas[0]

# FACILITANDO O CODIGO
L = int(TAM[0][0]) # Linha
C = int(TAM[0][1]) # Coluna

# CRIANDO UMA MATRIZ CHEIA DE '#'
MatrizO = [['#']*C for i in range(L + 1)]

# COPIANDO MATRIZ OCULTA
MatrizG = copy.deepcopy(MatrizO) # !!!

# FACILITANDO MAIS O CODIGO
# L -= 1
# C -= 1

# INSERINDO MINAS
y = 0
while y < nMinas:
  MatrizG[int(Posicao[y][0])][int(Posicao[y][1])] = '*'
  y += 1

# CONTAR BOMBAS EM VOLTA
for I in range(L):
  for J in range(C):
    contBomba = 0
    # CONTA AS BOMBAS
    for i in range(-1, 2):  # -1 a 1
      for j in range(-1, 2):  # -1 a 1
        # EXTRAPOLOU LIMITES
        Valido = 1
        if I + i < 0 or I + i >= L or J + j < 0 or J + j >= C:
          Valido = 0
        # CONTAR BOMBAS EM VOLTA
        if Valido != 0 and MatrizG[I + i][J + j] == '*':
          contBomba += 1
          
    # INSERE   
    if MatrizG[I][J] != '*':
      MatrizG[I][J] = str(contBomba)
    # INSERE '-' CASO NENHUMA BOMBA SEJA ENCONTRADA
    if contBomba == 0:
      MatrizG[I][J] = '-'
    
GANHOU = copy.deepcopy(MatrizG) #!!!

for i in range(L):
  for j in range(C):
    if GANHOU[i][j] == '*':
      GANHOU[i][j] = '#'

# START JOGO
Jogar = 1
while Jogar == 1:
  clear()
  # IMPRIME MATRIZ
  for i in range(L):
    for j in range(C):
      print(MatrizO[i][j],' ', end='')
    print('')

  # INPUTS
  print('Insira a posição da linha e da coluna que deseja revelar.')
  while True:
    l = int(input(f"Insira a linha (1 - {L}): "))
    if l > 0 and l <= L:
      break
  while True:
    c = int(input(f"Insira a Coluna (1 - {C}): "))
    if c > 0 and c <= C:
      break
  l -= 1
  c -= 1
  
  # PERDEU
  if MatrizG[l][c] == '*':
    Jogar = 0
  # ESPAÇO VAZIO
  elif MatrizG[l][c] == '-':
    for i in range(-1, 2):  # -1 a 1
      for j in range(-1, 2):  # -1 a 1
        Valido = 0
        if l + i < 0 or l + i >= L or c + j < 0 or c + j >= C:
          Valido = 1
        if Valido == 0:
          MatrizO[l + i][c + j] = MatrizG[l + i][c + j]
  # REVELAR NUMERO
  else:
    print("entru else")
    MatrizO[l][c] = MatrizG[l][c]

  #VERIFICA SE AS MATRIZES SÃO IGUAIS
  contCerto = 0
  for i in range(L):
    for j in range(C):
      if MatrizO[i][j] == GANHOU[i][j]:
        contCerto += 1
      if contCerto == L*C:
        Jogar = 2

# PERDEU
if Jogar == 0:
  clear()
  
  for i in range(L):
    for j in range(C):
      print(MatrizG[i][j], " ", end="")
    print("")
  print("Não foi desta vez, a bomba estourou!!!")
  
else:
  clear()
  for i in range(L):
    for j in range(C):
      print(MatrizG[i][j], " ", end="")
    print("")
  print("Parabens você ganhou ^^")

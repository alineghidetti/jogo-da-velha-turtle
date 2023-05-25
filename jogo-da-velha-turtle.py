#Modelo de jogo da velha desenvolvido por Aline Ghidetti
import turtle
import random

#DESENHANDO TABULEIRO (MATRIZ)
def desenhe_campo (luna):
    luna.pd()
    luna.fd(lado)
    luna.pu()
    luna.left(-90)
    luna.fd(-lado/3)
    luna.right(90)
    luna.pd()
    luna.fd(lado)
    luna.pu()
    luna.right(90)
    luna.fd(lado/3)
    luna.right(90)
    luna.fd(lado/3)
    luna.left(90)
    luna.pd()
    luna.fd(-lado)
    luna.right(90)
    luna.pu()
    luna.fd(lado/3)
    luna.right(-90)
    luna.pd()
    luna.fd(lado)
    luna.pu()
    luna.home()

#Atribui os valores de "1" e "-1" a cada jogador, de maneira que para vencer, a linha, coluna ou diagonal deve ter valor de "3" ou "-3"

def valor_linha(linha):     
    return sum(m[linha])
        
def valor_coluna(coluna):
    scol=0 #soma da coluna
    for l in range (0,3):
        scol += m[l][coluna]
    return scol

def valor_diagonal1():
    sdiag=0# soma diagonal
    for d in range (0, 3):
        sdiag+= m[d][d]
    return sdiag

def valor_diagonal2():
    sdiag=0#soma contra diagonal
    for d in range (0,3):
        sdiag+= m[d][2-d]
    return sdiag

def vitoria():
    for l in range (3): #abs é o valor absoluto, em módulo 
    #(me referi aos valores de 3 e -3).
        if abs(valor_linha(l)) == 3: #vitoria retorna 3 resultados, 
        #1o: quem venceu, 2o: a forma como ganhou e 
        #3o a posição da linha ou coluna (ou None)
            return True,"linha",l
        if abs(valor_coluna(l)) == 3:
            return True,"coluna",l
    if abs (valor_diagonal1())== 3:
        return True, 'diagonal',None
    if abs (valor_diagonal2())== 3:
        return True, 'contradiagonal',None
    return False, None, None #caso o if não se concretize, a 
    #função cai direto no return False
 
def tracar_reta(t, g, tiporeta, valorreta,lado):
    t.home()
    t.pencolor(g)
    lado3=lado/3
    lado6=lado3/2
    t.pu()

    if tiporeta == 'linha':       
        if linha == 0:
            t.right(90)
            t.fd(lado6)
            t.left(90)
            t.pd()
            t.fd(lado)
        elif linha >= 1:
            t.left (90)
            t.fd(lado6+lado3*(valorreta-1))
            t.right(90)
            t.pd()
            t.fd(lado)           
    elif tiporeta == 'coluna':
        t.right(90)
        t.fd(lado3)
        t.left(90)
        t.fd(lado6+lado3*valorreta)
        t.left(90)
        t.pd()
        t.fd(lado)
    elif tiporeta == 'diagonal':
        t.right (90)
        t.fd(lado3)
        t.left(135)
        t.pd()
        t.fd(lado*(2)**.5)      
    elif tiporeta == 'contradiagonal':
        t.left(90)
        t.fd(2*lado3)
        t.right(125)
        t.pd()
        t.fd(lado*(2)**.5)
    else:
        print('Erro: Tipo de reta', tiporeta,'inválido')
    t.pu()
    t.pencolor('black')
    t.home()
    
#Programa Principal
lado = 300
lado3 = lado/3
jogadas=0

#m é a matriz
m = [ 
[0, 0, 0], 
[0, 0, 0], 
[0, 0, 0]
    ]
jogadores = ["Vermelho","Azul"] #jogador 1 e jogador 2
cor=['blue','red']
luna = turtle.Turtle()
luna.shape('turtle')

desenhe_campo(luna)

while not vitoria()[0] and jogadas < 9:
    jogadas+=1
    linha= random.randint (0, 2)
    coluna= random.randint(0, 2)
    
    while m[linha][coluna] != 0: #while repetirá até haver uma posição válida
        linha = random.randint (0, 2)
        coluna = random.randint(0, 2)
        
    if jogadas%2 == 0: #jogador 1 joga com +1 (JOGADA ÍMPAR)
        m[linha][coluna] = 1
    else:
        m[linha][coluna] = -1 #jogador 2 joga com -1 (PAR) 
        
    pos= coluna*lado3+lado3/2, linha*lado3-lado3/2
    luna.fillcolor(cor[jogadas%2]) #resto de 2 é sempre 0 ou 1, assim variando 
    #na lista entre 0 e 1
    luna.setpos(pos)
    luna.stamp()

luna.hideturtle()

#Definir o jogador baseado no número de jogadas ser impar ou par
if vitoria()[0]:
    if jogadas %2 == 0:
        vencedor= jogadores[1]
    else:
        vencedor= jogadores[0]
    msg ='O vencedor foi:' +  str(vencedor)
    tracar_reta(luna, cor[jogadas%2], vitoria()[1], vitoria()[2], lado)
else:
    msg = 'Deu velha'
    
luna.goto(lado/2, lado*2.2/3)
font = ("Comic Sans", 12, "bold")

luna.write (msg, align='center', font=font)  
    
    
    

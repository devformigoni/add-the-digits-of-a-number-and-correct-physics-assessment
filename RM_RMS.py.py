""" Este programa foi desenvolvido por Prof. Me. Paulo O. Formigoni, PhD
para obter a soma dos digitos do número de matrícula dos alunos (RM) dos cursos técnicos e de graduação,
com o intuito de ser usado em avaliações individuais e sem consulta, para inibir a cópia.
    Também corrige as questões da avaliação de recuperação do 3º trimestre de 2022 sobre eletricidade.

##### Usando o comando while e apenas números #####
RM = int(input('Digite o seu RM =   ')) 
RMS = 0
while(RM > 0):
    RMS += RM % 10
    # Soma o valor anterior de RMS com o resto da divisão
    RM = int(RM /10)
    # O novo RM sem a casa decimal após ser dividido por 10
print('O RMS é =  ',RMS)"""

##### Usando o comando for e convertendo números em strings e vice-versa #####
RMS = 0
RM = str(input('Digite o seu RM =   ')) #Transformo em str para poder usar posição. Ex: "b[1] = 2"

for i in range(len(RM)):
        RMS += int(RM[i]) # Converte string em número inteiro
print('O RMS é =  ',RMS)

Q2 = (RMS*4)
print("""Q2- Determine o valor da resistência equivalente (Req) entre os polos A e B (série), sabendo que
R1 = R2 = R3 = R4 = RMS Ω.. Resposta: """, Q2)
print("""

""")
Q3 = (RMS*0.01)/2
print("""Q3- Uma família comprou para enfeitar a árvore de Natal um pisca-pisca com 100 lâmpadas montadas num
circuito em série. Partindo da premissa que todas as lâmpadas possuem a mesma resistência e sabendo que as
lâmpadas foram colocadas numa tomada com RMS volts onde flui uma corrente elétrica de 2 ampères, determine
o valor da resistência de cada lâmpada. Resposta: """, Q3)
print("""

""")
Q4 = (RMS/6)
print("""Q4- Sendo a tensão elétrica na bateria é U = RMS V e sabendo que as resistências elétricas valem
R1 = 1 Ω, R2 = 2 Ω e R3 = 3 Ω (Série). Determine a corrente elétrica i. Resposta: """, Q4)
print("""

""")
Q5 = ((RMS*RMS)/(RMS+RMS))
print("""Q5- Determine a alternativa correta que apresenta o valor da resistência elétrica equivalente (Req)
entre os polos A e B (Paralelo) no circuito abaixo se R1= R2 = RMS Ω.. Resposta: """, Q5)
print("""

""")
Q6 = ((RMS*(RMS/2))/(RMS+(RMS/2)))+(3*RMS)+(4*RMS)
print("""Q6- Calcule a resistência equivalente (Req) de uma associação mista, apresentada no esquema abaixo,
em que dois resistores, R1 = RMS Ω e R2 = RMS/2 Ω, encontram-se associados em paralelos a outros dois
resistores, de R3 = 3.RMS Ω e R4 = 4.RMS Ω, associados em série. Resposta: """, Q6)
print("""

""")
Q7 = 'Curto-circuito' 
print("""Q7- Calcule a resistência equivalente (Req) de uma associação mista, apresentada no esquema abaixo,
em que os resistores valem, R1 = R2 = R3 = R4 = RMS Ω. Resposta: """, Q7)
print("""

""")
Q8 = RMS/8 
print("""Q8- Calcule a resistência equivalente (Req) de uma associação em paralelo, apresentada no esquema abaixo,
em que todos os oito resistores possuem o mesmo valor, R = RMS Ω: Resposta: """, Q8)
print("""

""")
Q9 = 10*RMS 
print("""Q9- Determine a tensão elétrica (U) do gerador se a resistência é R = 10 Ω e a corrente elétrica i = RMS A.
Resposta: """, Q9)
print("""

""")
Q10_i2 = 10*RMS/2
Q10_i3 = 10*RMS/5
Q10_i1 = Q10_i2 + Q10_i3
print("""Q10- Determine a alternativa correta que apresenta o valor da correntes elétricas i1, i2 e i3 produzida no
circuito abaixo, sabendo que a tensão U = 10.RMS V;  RA = 2 Ω e RB = 5 Ω.
Resposta: """, Q10_i1, Q10_i2, Q10_i3)
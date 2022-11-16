""" Este programa (função) foi desenvolvido por Prof. Me. Paulo O. Formigoni, PhD
para obter a soma dos digitos do número de matrícula dos alunos (RM) dos cursos técnicos e de graduação,
com o intuito de ser usado em avaliações individuais e sem consulta, para inibir a cópia

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
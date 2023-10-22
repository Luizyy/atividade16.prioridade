# Exercício Python 16: # Exercício Python 16: Para ter acesso a fila de prioridade, você deve ser idoso, gestante ou cadeirante. 
# Escreva um programa que pergunta a situação do usuário 
# (se é idoso, se é gestante, se é cadeirante ou nenhum destes) 
# e diga se ele pode ter acesso a fila prioridade ou não


print("fila de prioridade:")
print('1. Idoso')
print('2. Gestante')
print('3. Cadeirante')
print('4. Nenhum destes')
priorit=int( input('Digite o número que voçê se aplica: ') )

if (priorit==1) or (priorit==2) or (priorit==3) :
    print('Você tem direito a fila prioritária :)')
else:
    print('Você não tem direito a flia, aguarde na fila.')



    
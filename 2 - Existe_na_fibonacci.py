#declaração das variaveis
t1 = 0
t2 = 1
seq = []

print(f'{" Existe na Fibonacci? " :=^52}')#---------------------------topo a ser mostrado na tela

#recebendo valor do usuário
while True:#----------------------------------------------------------laço infinito
    try:#-------------------------------------------------------------bloco de teste de erros
        num = int(input('Digite um número inteiro maior que zero: '))#mensagem a ser mostrada na tela para receber valor que será convetido para inteiro
        print('-'*52)#------------------------------------------------linha
        if num <= 0:#-------------------------------------------------verificação se valor é menor que zero
            raise ValueError('Número inválido')#----------------------retorno de mensagem e retorno para o bloco de testes
    except ValueError as e:#------------------------------------------trata o erro encontrado bloco de testes caso digite valor que não pode ser convertido para inteiro
        print('Número inválido')#-------------------------------------retorno de mensagem de erro  na conversão para inteiro
        print('-'*45)#------------------------------------------------linha
    else:#------------------------------------------------------------condição que aceita o valor digitado
        break#--------------------------------------------------------encerra o laço infinito

#laço que gera a seqência até um termo depois do valor digitado
while num >= t1:
    seq.append(t1)#---------------------------------------------------adiciona o valor de t1 a lista seq
    t1, t2 = t2, t1 + t2#---------------------------------------------atribuição multipla de valores para as variaveis
seq.append(t1)#-------------------------------------------------------após o laço atribui o ultimo valor de t1 para obter valor acima do digitado na sequencia

#resultado
print(f'3 últimos termos: {seq[-3:]}')#-------------------------------3 ultimos termos mostrado na tela
if num in seq:#-------------------------------------------------------verifica se existe o valor digitado na sequencia
    print(f'O número {num} pertence à sequência de Fibonacci.')#------mostra mensagem se existe
else:#----------------------------------------------------------------condição que não encontra o valor na sequencia gerada
    print(f'O número {num} não pertence à sequência de Fibonacci.')#--mostra mensagem se não existe



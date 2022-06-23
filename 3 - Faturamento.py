#importando função json
import json

#abertura do arquivo
with open('dados.json', encoding='utf-8') as dados:
    faturamento_mensal = json.load(dados)
    
#declaração de variaveis
total = 0
menor = []
dias_uteis = 0
dias_maiores_media = []

#leitura diaria do faturamento para dias uteis, menor e maior valor
for diario in faturamento_mensal:
    if menor == []:#-------------------------------------------------atribuição de valores maiores e menores na primeira vez do laço
        menor = [diario['dia'], diario['valor']]#--------------------atribui dia com menor valor
        maior = [diario['dia'], diario['valor']]#--------------------atribui dia com maior valor
    if diario['valor'] > 0:#-----------------------------------------verificação de dias uteis
        total += diario['valor']#------------------------------------soma do valor total de faturamento
        if diario['valor'] < menor[1]:#------------------------------verificação de dia com menor valor
            menor = [diario['dia'], diario['valor']]#----------------atribui dia com menor valor
        if diario['valor'] > maior[1]:#------------------------------verificação de dia com maior valor
            maior = [diario['dia'], diario['valor']]#----------------atribui dia com maior valor
        dias_uteis += 1#---------------------------------------------conta dias uteis

media_mensal = total / dias_uteis#-----------------------------------atribui calculo media mensal

#leitura diaria do faturamento para dias com faturamento maior que media mensal
for diario in faturamento_mensal:
    if diario['valor'] > media_mensal:#------------------------------verificação de dia com valor maior que media
        dias_maiores_media.append([diario['dia'], diario['valor']])#-alimenta a lista dias_maiores_media
        
#Relatório(mostrado na tela)
print(f'{" Relatório de Faturamento Mensal " :=^55}')#---------------topo a ser mostrado na tela
print(f'Faturamento: R$ {total:.2f}')#-------------------------------valor total do mês
print(f'Dias úteis: {dias_uteis}')#----------------------------------qtd dias úteis
print(f'Média mensal: R$ {media_mensal :.2f}')#----------------------média mensal
print(f'Dias com faturamento diário maior que média mensal:\n'#
      f'{len(dias_maiores_media)} dias\n'                     #------quantidade de dias com faturamento maior que a média mensal
      f'{"-"*55}')                                            #
for maiores in dias_maiores_media:#----------------------------------leitura da lista dias_maiores_media
    print(f'Dia {maiores[0]:2} - R$ {maiores[1]:.2f}')#--------------print de cada item da lista
print('-' *55)#------------------------------------------------------separador
print(f'Menor faturamento: Dia {menor[0]:2} - R$ {menor[1]:.2f}')#---dia com menor faturamento
print(f'Maior faturamento: Dia {maior[0]:2} - R$ {maior[1]:.2f}')#---dia com maior faturamento
print('=' *55)#------------------------------------------------------separador


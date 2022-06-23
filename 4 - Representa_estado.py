#ao final é gerada uma tabela com as representações.

#dados
sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

#ciração da lista
estados = [('São Paulo', sp), ('Rio de Janeiro', rj), ('Minas Gerais', mg), ('Espírito Santo', es), ('Outros', outros)]

#criação da função linha
def linha():
    return print(f'|{"-"*56}|')#------------------------retorna uma linha pontilhada

#calculo do total
total = sp + rj + mg + es + outros


#estruturando a tabela
linha()#------------------------------------------------linha a ser mostrada na tela
print(f'|{" Relatório de Faturamento " :^56}|')#--------topo a ser mostrado na tela
linha()
print(f'|{f"Faturamento total R${total}":^56}|')#-------total do faturamento
linha()
print(f'|{"Estado":^27}|{"Representa (%)":^28}|')#------nome das colunas
linha()
#leitura da lista com os dados
for c in estados:
    print(f'|{c[0]:^27}|{f"{c[1]/total*100:.2f}%":^28}|')#print do nome do estado e a porcentagem que representa
linha()
  

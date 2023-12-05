# aula 6 de Python Turma 21 - 04/12/2023
# programa para calcular se um ano é bissexto ou não

# Apresentação
print ('O ano bissexto acontece a cada quatro anos e têm duração de 366 dias. A inclusão de um dia foi feita para aproximar '
      'o calendário ao movimento de translação da Terra \n(365 dias, 5 horas, 48 minutos e 46 segundos. '
      '\nEssas horas que ultrapassam os 365 dias são compensadas a cada quatro anos, no dia 29 de fevereiro')
def bissexto(ano):
    # SE o ano for divisível por 4 *E* também *Não* for divisível por 100.
    # Porque anos divisíveis por 100 só são bissextos quando também são divisíveis por 400.
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

# Entrada
ano = int(input("\nDigite um ano: "))

# Saída
if bissexto(ano):
    print(f'\n{ano} é um ano bissexto.')
else:
    print(f'\n{ano} não é um ano bissexto.')

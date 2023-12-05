# "O ano bissexto acontece a cada quatro anos e tem duração de 366 dias, diferentemente dos demais que têm 365 dias.
# A inclusão de um dia foi feita para aproximar o calendário ao movimento de translação da Terra, tempo que o planeta leva para dar a volta no Sol,
# que é de 365 dias, 5 horas, 48 minutos e 46 segundos. Essas horas que ultrapassam os 365 dias são compensadas a cada quatro anos, no dia 29 de fevereiro."

def bissexto(ano):
    # SE o ano quando for divisível por 4 E também não deixa resto quando divisível por 100.
    # Anos divisíveis por 100 só são bissextos quando também sejam divisíveis por 400.
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):

        return True
    else:
        return False

# Entrada
ano = int(input("Digite um ano: "))

# Saída
if bissexto(ano):
    print(f"{ano} é um ano bissexto.")
else:
    print(f"{ano} não é um ano bissexto.")

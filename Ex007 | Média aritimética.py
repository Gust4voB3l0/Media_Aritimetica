# Desenvolva um programa que leia as duas notas de um aluno e mostre a sua média entre elas

pv1 = int(input('Digite a nota da primeira prova: '))
pv2 = int(input('Digite a nota da segunda prova: '))

# nota média da prova

media = 5.0
if pv1 + pv2 > media:

    # Mensagem exibida para acima da média
    print('O aluno está acima da média, PARABÉNS!')
else:
    # Mensagem exibida para abaixo da média
    print('O aluno está abaixo da média, ESTUDE MAIS!')

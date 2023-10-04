nome = 'Luiz Otávio'
altura = 1.80
peso = 95
imc = peso / (altura * altura)

#print(nome, 'tem', altura, 'de altura',) Essa é uma maneira para exibir a mensagem desejada.
#print('peso', peso, 'quilos e seu IMC é',)
#print(imc)


"f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura' # Essa é uma forma de formatação de strings / só de colocar esse f no começo dessa string ja habilito a possibilidade de usar variaveis nesse texto apenas colocando essa chave{..}

# Para formatar as casas decimais de um numero você pode seguir o exemplo {altura:.2f}, nesse caso você coloca : e o . esse ponto que vai separar os numeros e a quantidade de decimais que você deseja, no caso do meu foram 2 e finalizando com o f.
print(linha_1)


linha_2 = f'peso {peso} quilos e seu IMC é'
print(linha_2)

linha_3 = f'{imc}'
print(linha_3)
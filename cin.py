#Apresentação do juros simples

c =float(input('informe o capital:'))
i =float(input('informe a taxa:'))
p =int(input('me informe o prazo:'))

#Processamento

total =  c * i * p / 100

#Saida

print(f' Juros:R${total}')

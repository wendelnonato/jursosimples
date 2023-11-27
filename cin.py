#Apresentação do juros simples

c =int(input('informe o capital:'))
i =int(input('informe a taxa:'))
p =int(input('me informe o prazo:'))

#Processamento

total =  c * i * p

#Saida

print(f' Juro:{total/100}')

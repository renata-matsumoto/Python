# Propriedades da String

l = "Lista de letras"
data = "02/03/2022"

# tamanho da string

tamanho = len(l)
print(tamanho)

# split da string - divisão

lista = l.split(" ")
lista2 = data.split("/")
print(lista)
print(lista2)


# Substituição de determinados caracteres por outros

print(l.replace("de", " "))


# Fatiamento e divisão de strings
# indices começando em 0

nome = "Python"

nova_string = nome[1]
nova_string = nome[-1] # ultimo caractere - de tras para frente
nova_string = nome[0:4] # intervalo
nova_string = nome[0:4:2]  #intervalo com salto de 2
print(nova_string)
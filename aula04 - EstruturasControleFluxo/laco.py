#While

i = 0

while(i<=10):
    print(i)
    print("O loop está rodando")
    #i = i + 1
    i+=1

#For

for i in "Python":
    print(i)

# in percorre o conteudo de uma lista


num = [1, 2, 3, 4]

for j in num:
    print(j)


# Laço For Range
# i váriavel de controle
# range(vai gerar 10 elementos)
# range(ponto de partida, chegada e o salto)

for i in range(10):
    print(i+1)

print("-----------------")

for j in range(-10, 0 , 2):
    print(j)
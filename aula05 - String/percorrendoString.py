# Percorrendo Strings

nome = "Python"

# percorrer com for

for i in nome:
    print(i)


print("-----------")
# percorrer com While

i = 0 
while i < len(nome):
    print(nome[i])
    i += 1


print("-----------")

# Percorrer com for /enumerate

for k, v in enumerate(nome):
    print(k, v)
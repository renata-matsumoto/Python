# 1-Crie uma string contendo o alfabeto com letras maiúsculas separado por espaços.
# 2- Percorra e imprima essa string com enumerate.
# 3-Substitua os espaços por traço. “-” e imprima para o usuário.

alfabeto = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"

for k, v in enumerate(alfabeto):
    print(k,v)

print(alfabeto.replace(" ", "-"))
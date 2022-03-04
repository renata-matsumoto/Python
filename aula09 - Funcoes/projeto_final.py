#1-Deve se criar 5 funções diferentes,sendo elas somar, subtrair, dividir,multiplicar e listar.
# 2-Deve se criar um MENU com if else sendo que o usuário escolha qual função deve acessar.
# 3-Ao ser escolhido a função, o usuário é direcionado a ela e insere os parâmetros que desejam realizar as operações.
# 4-As funções matemáticas devem receberos números para realizar a operação, realizar o cálculo e imprimir o resultado para o usuário.
# 5-Na função listar, deve-se criar uma lista de vantagens do python e imprimir para o usuário.



 
def soma(num1,num2):
    return num1 + num2

def subtracao(num1,num2):
    return num1 - num2

def multiplicacao(num1,num2):
    return num1 * num2

def divisao(num1,num2):
    return num1 / num2

def listar(a,b,c):
    lista = [a,b,c]
    return lista


menu = input("Digite uma função entre: soma, sub, mult, div ou listar:")

if menu == "soma":
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    print(f"O Resultado da soma dos números é {soma(num1, num2)}")

elif menu == "sub":
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    print(f"O Resultado da subtração dos números é: {subtracao(num1, num2)}")

elif menu == "mult":
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    print(f"O Resultado da multiplicacao dos número é {multiplicacao(num1, num2)}")

elif menu == "div":
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    print(f"O Resultado da divisão dos números é {divisao(num1, num2)}")

elif menu == "listar":
    a = input("Digite a primeira vantagem do Python: ")
    b = input("Digite a segunda vantagem do Python : ")
    c = input("Digite a terceira vantagem do Python: ")
    print(f"As vantagens do Python são: {listar(a,b,c)}")





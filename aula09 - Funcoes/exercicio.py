#1-Crie uma função que receba dois parâmetros e realize sua soma, subtração, adição e multiplicação.
# 2-Informe esses resultados através de um print ao usuário dentro da função.




def soma(num1,num2):
    return num1 + num2
print(soma(277, 365))

def sub(num1,num2):
    return num1 - num2
print(sub(1587,25))

def mult(num1,num2):
    return num1 * num2
print(mult(78,91))

def operacoes(a, b):
    soma = a + b
    sub = a - b
    mult = a * b
    div = a / b
    return soma, sub, mult, div
print(operacoes(10,5))
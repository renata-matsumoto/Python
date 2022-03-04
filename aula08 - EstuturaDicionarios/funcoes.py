#dicionário são mutáveis

agenda = {458978598:"Jose", 45896587:"Maria", 567897898:"Joao", 5897885694:"Marcelo"}
print(agenda)
del(agenda[45896587]) #deleta o elemento
print(agenda)

print(agenda.keys()) #mostra as chaves
print(agenda.values()) #mostra os valores
print(len(agenda)) #mostra o tamanho do dicionario
print(agenda.popitem()) #remove o ultimo elemento
print(agenda)

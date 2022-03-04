# 1-Crie um dicionário contendo dias da semana sendo dia1, dia2, dia3 ...as chaves e o dia seu valor. 
# Ex: “dia1”: “domingo”.
# 2-Remova dois dos últimos dias da semana.
# 3-Remova segunda-feira pela sua chave.
# 4-Imprima chaves e valores do dicionário.
# 5-Imprima o dicionário final.

dias_semana = {"dia1" : "domingo", "dia2": "segunda", "dia3": "terça", "dia4": "quarta", "dia5": "quinta", "dia6": "sexta", "dia7": "sabado"}
print(dias_semana)

print(dias_semana.popitem())
print(dias_semana.popitem())
print(dias_semana)

del(dias_semana["dia2"])
print(dias_semana)

print(dias_semana.keys())
print(dias_semana.values())
print(len(dias_semana))
print(dias_semana)




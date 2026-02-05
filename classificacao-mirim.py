from datetime import datetime

nasc= int(input("digite o seu ano de nascimento: "))
data = datetime.now()

AnoActual = data.year

idade = AnoActual - nasc
print("")
print("IDADE ACTUAL: ",idade,"ANOS")

if(idade < 10):
    print("Classificação: MIRIM")
if (idade > 9 and idade < 15):
    print("Classificação: INFANTIL")
if(idade > 14 and idade < 20):
    print("classificação: JÚNIOR")
if(idade > 19 and idade < 25):
    print("Classificação: SÊNIOR")
if(idade > 24):
    print("classificação: MASTER")
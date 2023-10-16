#Exercício Python 09: faça um software que verifique entre 2 numeros qual o maior

import time
print("veremos agora qual dos dois nuemros que você escolher é o maior")
time.sleep(2)
num1 = int(input("digite o primeiro numero:"))
time.sleep(1)
num2 = int(input("digite o segundo numero: "))
time.sleep(1)
if num1 > num2:
     print(f"{num1} é maior que {num2}" ) 
else num1 = num2:
    print(f"{num1} é igual a {num2}")

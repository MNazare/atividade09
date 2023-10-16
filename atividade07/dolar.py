# Digite um valor e veja quantos dolares voce poderá comprar: R$
real = float(input("digite o valor em real: "))
dolar = float(input("dolar hoje: "))
conv = real / dolar
print("com ", real, "reais, e o dolar tendo o valor de: ", dolar, "dolares, dá pra comprar ", conv, "dolares")
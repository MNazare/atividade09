# Informe um valor e veja quanto de desconto você terá em R$, receba a % do desconto que quer receber;

valor = float(input("preço do produto: "))
desc = float(input("valor do desconto: "))

desconto = (valor * desc) / 100
pagar = valor - desconto

print(f"""
      o desconto é igual a: {desconto}%
      sendo assim o valor a ser pago é igual a: {pagar} reais
      """)
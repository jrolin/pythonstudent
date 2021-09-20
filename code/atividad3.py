# 1

valor = 45.00

pesagem = float(input("Quanto de comida? "))

peso = pesagem / 1000

calcula = peso * valor

print("o valor total deu R${:.2f}".format(calcula))

# 2

salario = float(input("digite o salário: "))

calcula1 = salario * (15/100)
aumento = salario + calcula1

calcula2 = aumento * (8/100)
fgts = aumento - calcula2

print("salário base: R${:.2f}".format(salario))
print("salario com aumento R${:.2f}".format(aumento))
print("salario com desconto R${:.2f}".format(calcula2))
print("salario liquido R${:.2f}".format(fgts))

# 3

pequeno = 330.0
medio = 750.0
grande = 1300.0

print("quantos sucos comprou?")
valor_p = float(input("pequeno: "))
valor_m = float(input("medio: "))
valor_g = float(input("grande: "))

produto_p = valor_p * pequeno
produto_m = valor_m * medio
produto_g = valor_g * grande

soma = (produto_p + produto_m + produto_g)/1000

print("total de suco que comprou foi de {:.2f}L".format(soma))

# 4

cofre = [0.01, 0.05, 0.10, 0.25, 0.50, 1.00]

produto0 = float(input("quantas de 1 centavo?"))
produto1 = float(input("quantas de 5 centavos?"))
produto2 = float(input("quantas de 10 centavos?"))
produto3 = float(input("quantas de 25 centavos?"))
produto4 = float(input("quantas de 50 centavos?"))
produto5 = float(input("quantas de 1 real?"))

soma = ((produto0 * cofre[0])+(produto1 * cofre[1])+(produto2 * cofre[2]) +
        (produto3 * cofre[3])+(produto4 * cofre[4])+(produto5 * cofre[5]))

print("o total no cofre é: R${:.2f}".format(soma))

# 5
salario_min = 1100

salario_func = float(input("qual o salario do funcionário?"))

calcula = float(salario_func / salario_min)

print("esse funcionario tem {:.2f}".format(calcula))

# 6

despesas = float(input("total de despesas?"))
salario1 = float(input("qual o salário do morador 1? "))
salario2 = float(input("qual o salário do morador 2? "))

salario_maior = max(salario1, salario2)
salario_menor = min(salario1, salario2)
somar = salario1 + salario2

maior = salario_maior / somar
menor = salario_menor / somar

mais = despesas * maior
menos = despesas * menor

print("o salario maior(R$", salario_maior,
      ") vai pagar {:.2f}%".format(maior*100))
print("logo será de R${:.2f}".format(mais))

print("o salario menor(R$", salario_menor,
      ") vai pagar {:.2f}%".format(menor*100))
print("logo será de R${:.2f}".format(menos))

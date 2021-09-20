#1
x = input('Informe uma letra: ')

if x >= 'A' and x <= 'Z':
      print('Letra maiúscula')
elif x >= 'a' and x <= 'a':
      print('Letra minúscula')
elif x >= '0' and x <= '9':
      print('Número')
elif x >= '!'and x <= '/':
      print('Símbolo')
elif x >= ':'and x <= '@':
      print('Símbolo')
elif x >= '['and x <= '`':
      print('Símbolo')
elif x >= '{'and x <= '˜':
      print('Símbolo')

#2
num = int(input('digite um numero inteiro: '))

calc = num%2

if calc == 0:
      print('é par')
else:
      print('é ímpar')

#3
num1 = int(input('digite o primeiro número: '))
num2 = int(input('digite o segundo número: '))

calc = num1 % num2

if calc == 0:
      print('nao gera resto...')
else:
      print('gera resto...')

#4
num1 = int(input('digite o primeiro número: '))
num2 = int(input('digite o segundo número: '))

calc = num1 - num2

if calc >= 0:
      print('número é positivo (+)')
else:
      print('número é negativo (-)')

#5
num1 = int(input('digite o primeiro número: '))
num2 = int(input('digite o segundo número: '))
c = int(input('digite o terceiro número (esse é o que eu vou comparar): '))

if c >= num1 and c <= num2:
      print('esse número está dentro da sequencia asc')
elif c <=num1 and c >= num2:
      print('esse número está dentro da sequencia desc')
else:
      print('esse número está fora da sequencia...')

#6
num1 = input('quantos graus está a água? ')

if num1 < '0':
      print('brace yourself tá sólido')
elif num1 == '0':
      print('pode tomar porque tá líquida')
elif num1 > '100':
      print('quer queimar a língua? tá gasoso')

#7
letra1 = input('primeira letra, per favore...')
letra2 = input('segunda letra, por obiséquium...')

if letra1 == letra2:
      print('tá mas, é a mesma letra pessoa...')
elif letra1 > letra2:
      print('essa letra {} é sucessora de {}!'.format(letra1, letra2))
elif letra1 < letra2:
      print('esse {} vem antes de {}'.format(letra1, letra2))

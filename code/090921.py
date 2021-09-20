#1
print('print uma sequencia')

num = int(input('digite um numero: '))
i = num

while i < 10:
      print(i)
      i+=1

#2
print('print apenas impares')

num = int(input('digite um numero: '))

for x in range(num, 11):
      if x % 2 == 0:
            continue
      print(x)

#3
print('print apenas pares')

num = int(input('digite um numero: '))

for x in range(num, 11):
      if x % 2 != 0:
            continue
      print(x)

#4
print('fatorial!')

num = int(input('digite um numero: '))
fat = 1
aux = 2

while aux <= num:
      fat = fat*aux
      aux +=1

print(fat)

#5
print('print uma sequencia')

num = float(input('digite um numero: '))
i = 1.5

while i < num:
      print(i)
      i+=0.5

#6
print('print uma sequencia')

n = int(input('digite o n: '))
p = float(input('digite o p: '))
i = int(input('digite o i: '))

for x in range(i):
      y = x * p + n
      print(y)

#7
#ver como se faz sem array

#8
star = '*'

for x in range (0, 5):
      print(star * 5)

#9
star = '*'
n = 0

for x in range (0,5):
      n +=1
      print(star * n)

#10
star = '*'
n = 6

for x in range (0,5):
      n -=1
      print(star * n)

import os

# Menu com as opções de escolha
def menu():
  os.system('cls' if os.name == 'nt' else 'clear') # Limpa a tela - Win/Linux
  print('\n..:: Desenvolvendo programas com menus ::..\n')
  print('1 - Item 1')
  print('2 - Item 2')
  print('3 - Item 3')
  print('9 - Sair\n')
  item = input('Escolha uma opção: ')
  return item

# Uma função para cada item do menu
def opcao_1():
  print('\nOpção escolhida: 1\n')

def opcao_2():
  print('\nOpção escolhida: 2\n')

def opcao_3():
  print('\nOpção escolhida: 3\n')

# Processamento do menu e chamada das funções
if __name__ == '__main__':
  escolha = '0'
  while(escolha != '9'):
    escolha = menu()

    if escolha == '1':
      opcao_1()
    elif escolha == '2':
      opcao_2()
    elif escolha == '3':
      opcao_3()
    elif escolha == '9':
      print('\nSaindo...\n')
    else:
      print('\nOpção desconhecida!\n')
      
    input('Pressione ENTER para continuar')

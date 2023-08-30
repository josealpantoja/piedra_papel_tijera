import random #Importar una función

print(" █████                █████     █████    ████           █████                               █████")
print("░░███                ░░███     ░░███    ░░███          ░░███                               ░░███ ")
print(" ░███████   ██████   ███████   ███████   ░███   ██████  ░███████    ██████   ████████    ███████ ")
print(" ░███░░███ ░░░░░███ ░░░███░   ░░░███░    ░███  ███░░███ ░███░░███  ░░░░░███ ░░███░░███  ███░░███ ")
print(" ░███ ░███  ███████   ░███      ░███     ░███ ░███████  ░███ ░███   ███████  ░███ ░███ ░███ ░███ ")
print(" ░███ ░███ ███░░███   ░███ ███  ░███ ███ ░███ ░███░░░   ░███ ░███  ███░░███  ░███ ░███ ░███ ░███ ")
print(" ████████ ░░████████  ░░█████   ░░█████  █████░░██████  ████ █████░░████████ ████ █████░░████████")
print("░░░░░░░░   ░░░░░░░░    ░░░░░     ░░░░░  ░░░░░  ░░░░░░  ░░░░ ░░░░░  ░░░░░░░░ ░░░░ ░░░░░  ░░░░░░░░ ")
print('')
user_name = input("¿Cuál es tu nombre 👉 ")
print('')


def choose_option():
  options = ('piedra', 'papel', 'tijera') #lo pasamos a global a local, porque solo le interesa a la función saber cuales son las opciones
  user_option = input(str(user_name) + ' escoje piedra, papel o tijera 👉 ')
  user_option = user_option.lower()
  

  if not user_option in options:
    print('esa opción no es válida')
    return None, None
  

  computer_option = random.choice(options) #uso función Random
  
  print('User option ', user_option)
  print('computer_option', computer_option)
  return user_option, computer_option

def check_rules(user_option, computer_option, user_win, computer_win):
  if user_option == computer_option:
    print('¡Empate!')
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('piedra gana a tijera')
      print('¡user ganó!')
      user_win += 1
    else:
      print('papel gana a piedra')
      print('¡computer ganó!')
      computer_win += 1
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('papel gana a piedra')
      print('¡user ganó!')
      user_win += 1
      
    else:
      print('tijera gana a papel')
      print('¡computer ganó!')
      computer_win += 1
  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('tijera gana a papel')
      print('¡user ganó!')
      user_win += 1
    else:
      print('piedra gana a tijera')
      print('¡computer ganó!')
      computer_win += 1
  return user_win, computer_win

def check_winner(user_win, computer_win):
  
  if computer_win == 2:
      print('*' * 10)
      print('')
      print('el ganador es la computadora')
      print('')
      print('____██████████████')
      print('___██▓▓▓▓▓▓▓▓▓ M ▓███')
      print('_██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██')
      print('_██████░░░░██░░█████')
      print('█░░░████░░██░░░░░░░██')
      print('█░░░████░░░░██░░░░░██')
      print('_████░░░░░░█████████')
      print('_██░░░░░░░░░░░░░██')
      print('___██░░░░░░░░░██')
      print('_____██░░░░░░██')
      print('___██▓▓████▓▓▓█')
      print('██▓▓▓▓▓▓████▓▓█')
      print('▓▓▓▓▓▓███░░███░')
      print('_██░░░░░░███████')
      print('___██░░░░███████')
      print('_____██████████')
      print('____██▓▓▓▓▓▓▓▓▓██')
      print('')
      exit()
      
  if user_win == 2:
      print('*' * 10)
      print('')
      print('¡', user_name, 'haz ganado!')
      print('')
      print("░░░░░░░░░░░░░░░░░░░░░░░░░")
      print("░░░░▄▄▄░░░█▄▄▄█░░░▄▄▄░░░░")
      print("░░▄███░░░░█████░░░░███▄░░")
      print("▄█████▄░░▄█████▄░░▄█████▄")
      print("█████████████████████████")
      print("█████████████████████████")
      print("█████████████████████████")
      print("░▀███████▀█████▀███████▀░")
      print("░░░▀███▀░░░███░░░▀███▀░░░")
      print("░░░░░░▀░░░░░▀░░░░░▀░░░░░░")  
      print('')
      print('')
      exit()
      

def run_game():
  computer_win = 0
  user_win = 0
  rounds = 1
  emoji = ('🤓', '😎', '😭', '🦁', '🎸', '✂️', '👻', '🩰', '🏀')

  while True:

    print('')
    print('*' * 20)
    print('ROUND', rounds, random.choice(emoji))
    print('*' * 20)
    print('')
    print('Ganadas Usuario:', user_win)
    print('Ganadas computadora:', computer_win)
    print('')
    

    user_option, computer_option = choose_option()
    user_win, computer_win = check_rules(user_option, computer_option, user_win, computer_win)
    rounds += 1

    check_winner(user_win, computer_win)
    
    
    
    

run_game()
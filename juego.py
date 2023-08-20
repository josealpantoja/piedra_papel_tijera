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

options = ('piedra', 'papel', 'tijera')
emoji = ('🤓', '😎', '😭', '🦁', '🎸', '✂️', '👻', '🩰', '🏀')

computer_win = 0
user_win = 0

rounds = 1

while True:

  print('')
  print('*' * 20)
  print('ROUND', rounds, random.choice(emoji))
  print('*' * 20)
  print('')
  print('Ganadas Usuario:', user_win)
  print('Ganadas computadora:', computer_win)
  print('')

  user_option = input(str(user_name) + ' escoje piedra, papel o tijera 👉 ')
  user_option = user_option.lower()
  
  if not user_option in options:
    print('esa opción no es válida')
  
  computer_option = random.choice(options) #uso función Random
  
  print('User option ', user_option)
  print('computer_option', computer_option)
  
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
    print('____█████████████')
    print('')
    print('')
    break
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
    break
  rounds += 1
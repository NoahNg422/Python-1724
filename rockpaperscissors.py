import random


def main():
  wins = 0
  while wins == 0:
    options = ['rock', 'paper', 'scissors']
    player1 = input('Rock, paper, or scissors: ')
    cpu = options[random.randint(0, 2)]
    if player1 == 'rock':
      if cpu == 'rock':
        print(f'\nyour choice: {player1}; CPU\'s choice: {cpu}\n')
        print('Tied, going again\n')
      elif cpu == 'paper':
        wins = 1
        print(f'\nyour choice: {player1}; CPU\'s choice: {cpu}\n')
        print('CPU won! (you lost)')
      elif cpu == 'scissors':
        wins = 1
        print(f'\nyour choice: {player1}; CPU\'s choice: {cpu}\n')
        print('You won! You beat CPU!')
    elif player1 == 'paper':
      if cpu == 'paper':
        print(f'\nyour choice: {player1}; CPU\'s choice: {cpu}\n')
        print('Tied, going again\n')
      elif cpu == 'scissors':
        wins = 1
        print(f'\nyour choice: {player1}; CPU\'s choice: {cpu}\n')
        print('CPU won! (you lost)')
      elif cpu == 'rock':
        wins = 1
        print(f'\nyour choice: {player1}; CPU\'s choice: {cpu}\n')
        print('You won! You beat CPU!')
    elif player1 == 'scissors':
      if cpu == 'scissors':
        print(f'\nyour choice: {player1}; CPU\'s choice: {cpu}\n')
        print('Tied, going again\n')
      elif cpu == 'rock':
        wins = 1
        print(f'\nyour choice: {player1}; CPU\'s choice: {cpu}\n')
        print('CPU won! (you lost)')
      elif cpu == 'paper':
        wins = 1
        print(f'\nyour choice: {player1}; CPU\'s choice: {cpu}\n')
        print('You won! You beat CPU!')
    else:
      print('Invalid option!')


main()

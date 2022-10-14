from pyclasses import Hero
from somemoreclasses import Avengers


def logo():                                                          
  print(' _____     _           _            _____ _         ___ ___ ')
  print('|   __|___| |___ ___ _| |___ ___   | __  |_|___ ___|  _|  _|')
  print('|__   | . | | -_|   | . | . |  _|  |    -| | . | . |  _|  _|')
  print('|_____|  _|_|___|_|_|___|___|_|    |__|__|_|  _|___|_| |_|  ')
  print('      |_|                                  |_|              ')


def play(avengers):
  round = 1
  MAX_TIES = 3
  ties = 0
  while avengers.size() >= 2 and ties < MAX_TIES:
    round += 1
    player1 = avengers.peek_left()
    avengers = avengers.pop_left()
    player2 = avengers.peek_left()
    avengers = avengers.pop_left()
    print(f'\nRound #{round}:')
    print(f'\t{player1.get_name()}    battles    {player2.get_name()}')
    round_winner = player1.battle_winner(player2)
    print(f'\twinner is {round_winner}')
    if round_winner[0] == 0:
      ties += 1
    else:
      ties = 0
    if round_winner[0] == 1:
      if avengers:
        avengers = avengers.push_right(player1)
      else:
        avengers = Avengers(player1)
    elif round_winner[0] == 2:
      if avengers:
        avengers = avengers.push_right(player2)
      else:
        avengers = Avengers(player2)
    elif round_winner[0] == 0:
      if avengers:
        avengers = avengers.push_right(player1)
        avengers = avengers.push_right(player2)
      else:
        avengers = Avengers(player1)
        avengers = avengers.push_right(player2)
      print(f'\nAvengers at end of Round #{round}:\n\t{avengers}')
  if ties < MAX_TIES:
    print(f'\n\nAPPLAUSE, The winner is {avengers.hero}!')
  else:
    print(f'\n\nNo one won because {MAX_TIES} ties!')


def main():
  logo()
  
  FlyDragon = Hero('FlyDragon', 2_345)
  print(f'\nFlyDragon is {FlyDragon}')

  tom = Hero('Tom')
  sue = Hero('Sue', 333)
  avengers = [FlyDragon, tom, sue]
  print(f'\nThe list of avengers is {avengers}')

  print(f"\nFlyDragon's getters: {FlyDragon.get_name()}, {FlyDragon.get_gold()}, {FlyDragon.get_gems()}")
  FlyDragon.set_name('Fly Dragon')
  FlyDragon.set_gold(-999)
  FlyDragon.set_gems({})
  print(f'\nFlyDragon after the setters: {FlyDragon}')

  avengers = Avengers(FlyDragon)
  avengers = avengers.prepend(tom)
  avengers = avengers.prepend(sue)
  avengers = avengers.prepend(Hero('Jamitha'))
  print(f'\nThe linked list of avengers:\n{avengers}')

  temp = avengers
  print(f'\nids without cloning: \t {id(avengers)} \t {id(temp)}')
  temp = avengers.clone()
  print(f'ids with cloning: \t {id(avengers)} \t {id(temp)}')

  print(f'\nBefore Avengers.peek_left():\n\t {avengers}')
  player1 = avengers.peek_left()
  print(f'After Avengers.peek_left():\n\t {avengers}')

  avengers = avengers.pop_left()
  print(f'After Avengers.pop_left():\n\t {avengers}')

  player2 = avengers.peek_left()
  avengers = avengers.pop_left()
  print(f'\nPlayers:\n\t{player1}\n\n\t{player2}')
  print(f'\nAvengers left in the linked list:\n\t{avengers}')

  verret = Hero('Verret')
  avengers = avengers.push_right(verret)
  print(f'\nAvengers after pushing verret:\n\t{avengers}')

  mccall = Hero('McCall')
  avengers = avengers.push_right(mccall)
  print(f'\nAvengers after pushing mccall:\n\t{avengers}')

  print(f"\n------------------------------------------------------------")
  print(f"----------  Let\'s play our Avenger Splendor Game  ----------")
  print(f"------------------------------------------------------------\n")
  print(f'\nAvengers at beginning of game:\n\t{avengers}')

  play(avengers)


main()
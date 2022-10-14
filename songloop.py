# Version 0.2!


def main():
  drink = input('Input a beverage: ')
  reaction = input('Play song? y/n ')
  n = 100
  while n > 0 and reaction != 'n':
    n -= 1
    if n > 1:
      print(f'{n} bottles of {drink} on the wall, {n} bottles of {drink}.\n'\
      f'Take one down, pass it around, {n - 1} bottle(s) of {drink} on the'\
      ' wall.')
      print()
      reaction = input('Continue? <n> for no, otherwise <ENTER> \n')
    if n == 1:
      print(f'1 bottle of {drink} on the wall, 1 bottle of {drink}.\nTake '\
      f'one down, pass it around, 0 bottles of {drink} on the wall.')
      print()
    if reaction == 'n':
      print('Song stopped.\n')
  print(f'No more bottles of {drink} on the wall, no more bottles of '\
  f'{drink}.\nWe took them down, passed them around, no more bottles of '\
  f'{drink} on the wall.')


main()
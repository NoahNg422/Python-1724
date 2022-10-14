# I miss the NCF so much!


def main():
  line = 'Hello, Whatever Your Name May Be; Welcome To PYTHON.'
  print(line)
  print(line.upper())
  print(line.lower())
  print(line.capitalize())
  print('9' * 8)
  print()
  print(9 / 3)
  print(10 / 4)
  print((15 // 5) + (7 * 2))
  print(7 % 3)
  print(int(str(96//6)) == 16)
  print(type(80))
  print(type(9.5))
  print(type('Hello'))
  print(type(list))
  print(type(print))
  # Number must not equal 0!
  num = input('how much: ')
  if num != '0' and num.isnumeric():
    print(1 / int(num))
  print()
  print(f'{9 + 9} people')
  print()
  print(4 == 4)
  print('7' == 7)
  print('in' == 'In')
  print('in' == 'In'.lower())
  print()
  print(f'My number is: {42} or {42.0}')
  print('hom' in 'homework')
  print(1 == 1 or 5 == '5')
  print(1 != 2 and 3.0 != 3)
  print('humid' in 'hot weather')


main()
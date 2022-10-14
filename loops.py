def fibonacci(max, num=0, num2=1):
  sum = num + num2
  for i in range(max):
    num += sum
    sum += num
    print(num)
    print(sum)


def main():
  n = 0
  print('counting: 0')
  while n < 22:
    n += 1
    print(f'still counting: {n} seconds')
  else:
    print(f'Counting finished at {n} seconds.')
  print()
  
  fibonacci(6)
  print()
  
  menu = ''
  count = 0
  while menu != 'done' and menu != 'none' and count < 5 and menu.strip() == '':
    count += 1
    menu = input('Your order: ')
  
  if menu == 'done' or count == 5:
    print('Thanks for ordering.')
  else:
    print('OK, see you next time.')
  print()
  
  for num in range(31):
    if num % 3 == 0 and num % 5 == 0:
      print('Fizzbuzz')
    elif num % 3 == 0:
      print('Fizz')
    elif num % 5 == 0:
      print('Buzz')
    else:
      print(num)


main()
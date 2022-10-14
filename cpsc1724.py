import random
import datetime


def add_evens(numbers):
  sums = 0
  for value in numbers:
    if value % 2 == 0:
      sums += value
  return sums


def random_list_of_ints(length, minimum, maximum):
  ints = []
  for i in range(length):
    item = random.randint(minimum, maximum)
    ints.append(item)
  return ints


def fizzlist():
  fizz_list = []
  for i in range(31):
    if i % 3 == 0 and i % 5 == 0:
      fizz_list.append('Fizzbuzz')
    elif i % 3 == 0:
      fizz_list.append('Fizz')
    elif i % 5 == 0:
      fizz_list.append('Buzz')
    else:
      fizz_list.append(i)
  return fizz_list


def Subtotal(menu, order):
  subtotal = 0
  for key in menu:
    subtotal += menu[key] * order[key]
  return round(subtotal, 2)


def total(menu, order, taxes):
  subtotal = Subtotal(menu, order)
  new_total = subtotal + (subtotal * taxes)
  return round(new_total, 2)


def inexpensive(menu):
  cheap_items = []
  for item, price in menu.items():
    if price < 4:
      cheap_items.append(item)
  return cheap_items


def main():
  intlist = random_list_of_ints(20, 0, 99)
  print(intlist)
  print(f'{add_evens(intlist)}\n')

  today = datetime.date.today().year
  tup = ('Nguyễn', 'Noah', 'male', today - 2003, 67.0)
  print(tup)
  print(len(tup))
  print(f'{tup[-3]}\n')

  city = {'San Francisco': 'CA', 'Houston': 'TX', 'Atlanta': 'GA', 'NOLA': 'LA'}
  print(city['NOLA'])
  print(city.keys())
  print(city.values())
  print(f'{city.items()}\n')

  print(fizzlist())

  print('\nThese animals are part of the Chinese / Vietnamese Zodiac.')

  zodiac = {2020: '\U0001f400', 2021: '\U0001f402', 2022: '\U0001f405',
            2023: '\U0001f407', 2024: '\U0001f409', 2025: '\U0001f40D',
            2026: '\U0001f40E', 2027: '\U0001f410', 2028: '\U0001f412',
            2029: '\U0001f413', 2030: '\U0001f415', 2031: '\U0001f417'}
  print(zodiac)
  print(zodiac.keys())
  print(zodiac.values())
  print(f'This year is {today} or year of: {zodiac[today]}\n')

  menu = {'pizza': 7.99, 'chicken': 4.99, 'apple juice': 2.99, 'fries': 1.99, 'cobb salad': 3.99}

  print(f'{Subtotal({"pizza": 7.99, "apple juice": 2.99}, {"pizza": 1, "apple juice": 3})}\n')

  print(total({'pizza': 8, 'apple juice': 3}, {'pizza': 1, 'apple juice': 3}, 0.09))

  print(f'\n{inexpensive(menu)}')


main()

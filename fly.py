def cube(number):
	print(number ** 3)


# We should probably not raise them!
def tax(I):
	THP = I - I/5
	return THP


def average_score(a1, a2, a3, a4, a5):
	average = a1*.25 + a2*.1 + a3*.4 + a4*.15 + a5*.1
	return average


def interest(base, rate, years):
	value = base + base * (rate * years)
	return value


def good_grade(x):
	return x >= 80


def tolerance(radius, your_radius):
  print(f'Lower bound: Upper bound:')
  print(f'Your value: {your_radius}')
  difference = abs(radius - your_radius)
  return difference <= 0.001


def ordinals(name):
  ord_list = []
  for i in range(len(name)):
    ord_list.append(ord(name[i]))
  return ord_list


def reverse(name):
	reverse_name = name[::-1]
	return reverse_name


def palindrome(word):
  reverse = word[::-1]
  remove_spaces = word.replace(' ', '')
  rremove_spaces = reverse.replace(' ', '')
  return remove_spaces.lower() == rremove_spaces.lower()


def anagrams(string1, string2):
  argument1 = sorted(string1.lower())
  argument2 = sorted(string2.lower())
  return argument1 == argument2


def less_than_3(i=0):
  while i <3:
    i += 1
    print('I love you! \U0001f496')


def main():
  cube(4)
  cube(7)

  print(f'\nTake Home Pay: ${tax(60000)}\n')

  print(f'Grade average: {average_score(95, 80, 90, 90, 85)}')

  print(f'\nFed rates are up! How much: {interest(100, 0.0325, 10)}')
	
  print(f'\nGood grades? {good_grade(89)}\n')

  print(f'\nIs this radius close to the other circle radius? {tolerance(5, 4.9992)}\n')
  
  name = input('Who are you? ')
  print(f'\nHi, {name.capitalize()}. [*hugs*]')
  
  if name.lower() == 'none' or name.strip() == '':
    print("But nobody is there.\n")
  else:
    print(ordinals(name))
    print(f'\n{reverse(name)}\n')
  print(f"Is this word a palindrome: {palindrome(name)}")

  print(f"\nAre these words anagrams: {anagrams('information', 'miniantroof')}\n")

  less_than_3()


main()

from pyclasses import AreYou as types
from pyclasses import LinkedList
import random


def transfer(file, output, ids=[], names=[], hour_list=[], hours=0):
  with open(file) as file:
    for line in range(5):
      data = file.readline()
      ids.append(data[:4])
      names.append(data[4:11].strip())
      hour_list.append(data[12:])
  with open(output, 'w') as document:
    for n in range(5):
      worktime = 0
      hours_per_day = hour_list[n].split(' ')
      for count in hours_per_day:
        worktime += float(count)
        hours += float(count)
      document.write(f'Name: {names[n]}. ID#: {ids[n]}. Hours: {worktime}. '\
      f'Hours/day: {worktime / 5}. Pay: ${round(worktime * 20.5, 2)}\n')
  return round(hours, 2)


def ris_palindrome(word):
	if len(word) <= 1:
		return True
	elif word[0] != word[-1]:
		return False
	return ris_palindrome(word[1:-1].replace(' ', ''))


def generate_number():
  ls = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  num1 = ls[random.randrange(len(ls))]
  num2 = ls[random.randrange(len(ls))]
  num3 = ls[random.randrange(len(ls))]
  return str(num1) + str(num2) + str(num3)


def generate_numbers(max):
  ls = LinkedList(generate_number())
  for value in range(max):
    num = generate_number()
    ls = ls.prepend(num)
  return ls


def main():
  print('CPSC-2735\n')

  print(transfer('c:\\Users\\InnOu\\OneDrive\\Documents\\PythonPrograms\\work-hours.txt', \
    'c:\\Users\\InnOu\\OneDrive\\Documents\\PythonPrograms\\work-outdoc.txt'))
  
  print(f'\n{ris_palindrome("123 43 21")}')

  print(types(1, 2, 'muscular'))
  print(repr(types(0, 2, 'long and thin')))
  print(repr(types(1, 2, 'muscular')))
  print(repr(types(1, 1, 'muscular')))
  print(repr(types(1, 2, 'long and thin')))

  all_nodes = generate_numbers(10)
  print(f'\n{all_nodes}\n')

  print(all_nodes.pop_left())


main()
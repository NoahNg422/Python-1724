import datetime
import random


def age_message(name, birth_year, from_now):
	if name.strip() == '':
		return 'Everyone deserves to have a name!'
	elif birth_year <= 0:
		return f'{name} was alive BC!'
	else:
		age = year_now - birth_year
		if from_now == 0 and age >= 0:
			return f'{name} is now {age} years old.'
		elif from_now > 0 and age >= 0:
			return f'{name} is {age} and in {from_now} years (s)he\'ll be {age + from_now}.'
		else:
			if birth_year > year_now:
				return f"{name} isn't born yet!"
			elif age == -from_now:
				return f"{name} wasn't born yet."
			elif age > -from_now:
				return f'{-from_now} years ago, {name} was {age + from_now} years old.'
			else:
				return f'{-from_now} years ago was {-(age + from_now)} years before {name} was born.'


def generate_birth_years(start_year, end_year, number_birth_years):
	if start_year > end_year:
		start_year, end_year = end_year, start_year
	if number_birth_years <= 0:
		return []
	ls = []
	for _ in range(number_birth_years):
		ls.append(random.randrange(start_year, end_year))
	return ls


def find_even_from_back(ls):
  index = len(ls) - 1
  while index >= 0 and (ls[index] % 2 != 0):
    index -= 1
  return index


def find_odd_from_front(ls):
	index = 0
	while index < len(ls) and (ls[index] % 2 == 0):
		index += 1
	return index


def move_then_star(ls):
	for i in range(len(ls)):
		if ls[i] % 2 != 0:
			j = find_even_from_back(ls)
			if j >= 0 and i <= j:
				ls[i], ls[j] = ls[j], ls[i]
	star = find_odd_from_front(ls)
	if star >= 0 and star < len(ls):
		ls[star] = str(ls[star]) + '*'
	return ls


def main():
  today = datetime.date.today().day
  month = datetime.date.today().month
  year = datetime.date.today().year
  print(f'Today is {month}-{today}-{year} (UTC)\n')
  print(age_message('Noah', 2003, 0))
  print()
  print(move_then_star(generate_birth_years(1990, 2020, 20)))
  print()
year_now = datetime.date.today().year


main()
import random

def add_odds(numbers):
	sums = 0
	for value in numbers:
		if value % 2 == 1:
			sums += value
	return sums


def ints_list(ints=[]):
	length = len(ints)
	length = random.randint(1, 100)
	while len(ints) < length:
		item = random.randint(1, length)
		ints.append(item)
	return ints


def fizzlist():
	num = 0
	end = 30
	fizz_list = []
	while num < end:
		num += 1
		if num % 3 == 0 and num % 5 == 0:
			fizz_list.append('Fizzbuzz')
		elif num % 3 == 0:
			fizz_list.append('Fizz')
		elif num % 5 == 0:
			fizz_list.append('Buzz')
		else:
			fizz_list.append(num)
	return fizz_list


def Subtotal(menu, order):
	Subtotal = 0
	for key in menu:
		Subtotal += menu[key] * order[key]
	return Subtotal


def total(menu, order, taxes):
	subtotal = Subtotal(menu, order)
	new_total = subtotal + (subtotal * taxes)
	return new_total


def inexpensive(menu):
	cheap_items = []
	for item, price in menu.items():
		if price < 4:
			cheap_items.append(item)
	return cheap_items


def main():
	print(f'All odd numbers added: {add_odds([1, 3, 6, 8, 12, 14, 17, 19, 20])}')

	print(f'\nA random number list: {ints_list()}\n')

	tup = ('a', 'b', 1, 2, 3)
	print(tup)
	print(len(tup))
	print(f'{tup[-3]}\n')

	city = {'Sacramento': 'CA', 'Austin': 'TX', 'Atlanta': 'GA', 'Baton Rouge': 'LA'}
	print(city['Baton Rouge'])
	print(city.keys())
	print(city.values())
	print(city.items())

	print('\nThese animals are part of the Chinese Zodiac.')
	zodiac = {2017: '\U0001f413', 2018: '\U0001f415', 2019: '\U0001f417',\
		2020: '\U0001f400', 2021: '\U0001f402', 2022: '\U0001f405',\
		2023: '\U0001f407', 2024: '\U0001f409', 2025: '\U0001f40D',\
		2026: '\U0001f40E', 2027: '\U0001f410', 2028: '\U0001f412'}
	print(zodiac)
	print(f'This year is 2022 or year of {zodiac[2022]}\n')

	print(f'{fizzlist()}\n')

	menu = {'pizza': 7.99, 'chicken': 4.99, 'apple juice': 2.99, 'fries': 1.99, 'cobb salad': 3.99}
	print(Subtotal({'pizza': 7.99, 'apple juice': 2.99}, {'pizza': 1, 'apple juice': 3}))
	print(total({'pizza': 8, 'apple juice': 3}, {'pizza': 1, 'apple juice': 3}, 0.09))
	print(f'\n{inexpensive(menu)}\n')

	matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
	print(matrix)


main()

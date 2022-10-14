import random


def count_workouts(workouts, index, target):
  if index < 0 or index >= len(workouts):
    return 0
  if workouts[index] == target:
    return 1 + count_workouts(workouts, index + 1, target)
  else:
    return count_workouts(workouts, index + 1, target)


def generate_workout_lengths(outfile, num_workouts, low_time, high_time):
  with open(outfile, 'w') as f:
    for _ in range(num_workouts):
      f.write(f'{random.randint(low_time, high_time)}\n')


def indexes(workouts, target, answer=[], index=0):
  if index < 0 or index >= len(workouts):
    return answer
  if workouts[index] == target:
    answer.append(index)
  return indexes(workouts, target, answer, index + 1)


def indexes_of_workouts(low, high, workouts, answer=[], index=0):
  if index < 0 or index >= len(workouts):
    return answer
  workout = workouts[index]
  if workout >= low and workout <= high:
    answer.append(index)
  return indexes_of_workouts(low, high, workouts, answer, index + 1)


def indexes_of_workouts_in(low, high, workouts):
  answer = []
  for i, workout in enumerate(workouts):
    if workout >= low and workout <= high:
      answer.append(i)
  return answer


def number_workouts(low, high, workouts, index=0):
  if index < 0 or index >= len(workouts):
    return 0
  workout = workouts[index]
  if workout >= low and workout <= high:
    return 1 + number_workouts(low, high, workouts, index + 1)
  return number_workouts(low, high, workouts, index + 1)


def number_workouts_in(low, high, workouts):
  count = 0
  for workout in workouts:
    if workout >= low and workout <= high:
      count = count + 1
  return count


def output_indexes(workouts, target, index=0):
  if index >= 0 and index < len(workouts):
    if workouts[index] == target:
      print(index)
    output_indexes(workouts, target, index + 1)


def output_workouts(low, high, workouts, index=0):
  if index >= 0 and index < len(workouts):
    workout = workouts[index]
    if workout >= low and workout <= high:
      print(workout)
    output_workouts(low, high, workouts, index + 1)


def output_workouts_in(low, high, workouts):
  for workout in workouts:
    if workout >= low and workout <= high:
      print(workout)


def read_workouts_from(file):
  result = []
  with open(file, 'r') as f:
    for row in f:
      workout = int(f.readline().strip())
      result.append(workout)
  return result


def contains(fragment, string):
	return fragment in string


def rcontains(fragment, string, index=0):
	if string[index:index + len(fragment)] == fragment:
		return True
	if index <= len(string):
		return rcontains(fragment, string, index + 1)
	else:
		return False


def count_z(string):
	count = 0
	for char in string:
		if char.lower() == 'z':
			count += 1
	return count


def rcount_z(string, num_z=0, index=0):
	if index > len(string):
		return 0
	if index == len(string):
		return num_z
	elif index < len(string):
		if string[index].lower() == 'z':
			return rcount_z(string, num_z + 1, index + 1)
		else:
			return rcount_z(string, num_z, index + 1)


def is_and_xu(string):
	return 'x' in string.lower() and 'u' in string.lower()


def ris_and_xu(string, pos=0, l1_in='x', l2_in='u'):
	lowercase = string.lower()
	if pos > len(string) or len(string) == 0:
		return False
	if pos < len(string):
		if lowercase[pos] == l1_in:
			ris_and_xu(string, pos + 1, l1_in, l2_in)
		if lowercase[pos] == l2_in:
			ris_and_xu(string, pos + 1, l1_in, l2_in)
			return True
	return ris_and_xu(string, pos + 1, l1_in, l2_in)


def is_or_xu(string):
	return 'x' in string.lower() or 'u' in string.lower()


def ris_or_xu(string, pos=0, l1_in='x', l2_in='u'):
	lowercase = string.lower()
	if pos >= len(string) or len(string) == 0:
		return False
	if pos < len(string):
		if lowercase[pos] == l1_in or lowercase[pos] == l2_in:
			return True
	return ris_or_xu(string, pos + 1, l1_in, l2_in)


def maximum(limit, low, high):
	if low >= high or limit < 1:
		return high
	highest = random.randint(low, high)
	for i in range(limit):
		num = random.randint(low, high)
		if num > highest:
			highest = num
	return highest


def rmax(limit, low, high, largest=0, index=0):
	if index > limit or low >= high:
		return largest
	elif index < limit:
		num = random.randint(low, high)
		if num > largest:
			largest = num
		return rmax(limit, low, high, largest, index + 1)
	return largest


def negate_odds(numbers, start=0, new_list=[]):
	for n in numbers:
		if n % 2 == 1:
			new_list.append(-n)
		else:
			new_list.append(n)
	return new_list


def rnegate_odds(num_list, new_list=[], index=0):
	if index < len(num_list):
		num = num_list[index]
		if num % 2 == 1:
			new_list.append(-num)
			rnegate_odds(num_list, new_list, index + 1)
		else:
			new_list.append(num)
			rnegate_odds(num_list, new_list, index + 1)
	return new_list


def output_low_high(low, high):
	if low > high:
		print()
	else:
		for i in range(low, high + 1):
			print(i)


def routput_low_high(low, high, num=0):
	if num >= high or num < low or low >= high:
		print(num)
	else:
		print(num)
		routput_low_high(low, high, num + 1)


def remove_evens(num_list, index=0, new_list=[]):
	for i in num_list:
		if i % 2 == 1:
			new_list.append(i)
	return new_list


def rremove_evens(num_list, new_list=[], index=0):
	if index <= len(num_list) - 1:
		num = num_list[index]
		if num % 2 == 1:
			new_list.append(num)
			rremove_evens(num_list, new_list, index + 1)
		else:
			rremove_evens(num_list, new_list, index + 1)
		return new_list


def str_index(fragment, string):
	return string.find(fragment)


def rstr_index(fragment, string, index=0):
	if string[index:index + len(fragment)] == fragment:
		return index
	if index <= len(string):
		return rstr_index(fragment, string, index + 1)
	else:
		return -1


def sum_low_high(low, high):
	if low >= high:
		return 0
	num = 0
	for value in range(low, high + 1):
		num += value
	return num


def rsum_low_high(low, high, num=0, total=0):
  if num >= high:
    return total
  elif low >= high:
    return 0
  return rsum_low_high(low, high, num + 1, total+num-low)


def main():
  generate_workout_lengths('workout_lengths.txt', 100, 0, 60)

  workouts = read_workouts_from('workout_lengths.txt')
  print(f'\nThe workouts are:\n{workouts}')

  print('\nThe workouts of exactly 60 minutes are at indexes:')
  output_indexes(workouts, 60, 0)

  count = count_workouts(workouts, 0, 60)
  if count == 1:
    print(f'\nThere is {count} workout of 60 minutes.')
  else:
    print(f'\nThere are {count} workouts of 60 minutes.')
  print(f'\nThe workouts of 60 minutes are at indexes:\t{indexes(workouts, 60)}')

  print('\nThe workouts in the 20s are:')
  output_workouts_in(20, 29, workouts)
  print('\nAgain, the workouts in the 20s are:')
  output_workouts(20, 29, workouts)

  print(f'\nThe indexes of workouts in the 20s are:\n\t{indexes_of_workouts_in(20, 29, workouts)}')
  print(f'\nAgain, the indexes of workouts are:\n\t{indexes_of_workouts(20, 29, workouts)}')

  print(f'\nThe number of workouts in the 20s is:\t{number_workouts_in(20, 29, workouts)}')
  print(f'\nAgain, the number of workouts is:\t{number_workouts(20, 29, workouts)}\n')

  output_low_high(0, 9)
  # output_low_high(0, 7)
  
  print("\nRec low_high")
  routput_low_high(0, 9)
  # routput_low_high(0, 7)

  print(f'\n{sum_low_high(-1, 4)}')
  print(f'{rsum_low_high(-1, 4)}')

  print(f'\n{maximum(10, 1, 25)}')
  print(f'{rmax(10, 1, 25)}\n')

  print(is_or_xu('Xavier'))
  print(f'{ris_or_xu("Xavier")}\n')

  print(is_and_xu('Xavier'))
  print(f'{ris_and_xu("Xavier")}\n')

  print(count_z('hezllo, worldzZz.'))
  print(str(rcount_z('hezllo, worldzZz')) + '\n')
  
  # print(f"{str(rcount_z('FizzBuzz is a ZzZzZany interview question.'))}\n")
  
  print(contains('abc', 'acbcababc'))
  print(f"{rcontains('abc', 'acbcababc')}\n")

  # print(str_index('abc', 'abdabdcac'))
  print(str_index('abc', 'abdabcdac'))
  print(f"{rstr_index('abc', 'abdabcdac')}\n")

  numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  print(f'\n{negate_odds(numbers)}')
  print(rnegate_odds(numbers))

  print(f'\n{remove_evens(numbers)}')
  print(f'{rremove_evens(numbers)}')


main()
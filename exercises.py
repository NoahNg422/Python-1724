from pyclasses import Exercise


def consecutives(exercises, types):
  map_type_to_days = which_days_each_type_exercise(exercises)
  days = []
  for type in types:
    if type in map_type_to_days:
      days.extend(map_type_to_days[type])
  print(f'\t{days}')
  for i in range(1, len(Exercise._days) - 1):
    if i in days and i + 1 in days:
      return f'*BAD* consecutive days with {types}'
  return f'*GOOD* Good job spacing out {types}'


def count_type(exercises, type, index):
  if index < 0 or index >= len(exercises):
    return 0
  if exercises[index]._type == type:
    return 1 + count_type(exercises, type, index + 1)
  return count_type(exercises, type, index + 1)


def days_no_exercises(exercises):
  days_of_exercises = how_many_exercises_each_day(exercises)
  answer = []
  for day in range(1, len(Exercise._days) + 1):
    if day not in days_of_exercises:
      answer.append(day)
  return answer


def how_many_exercises_each_day(exercises):
  answer = {}
  for exercise in exercises:
    if exercise._day not in answer:
      answer[exercise._day] = 0
    answer[exercise._day] = answer[exercise._day] + 1
  return answer


def increase_durations(exercises, index, increase, answer):
  if index < 0 or index >= len(exercises):
    return answer
  answer.append(exercises[index])
  duration = answer[index]._duration
  answer[index]._duration = duration + increase
  return increase_durations(exercises, index + 1, increase, answer)    


def increase_durations_in_place(exercises, index, increase):
  if index >= 0 and index < len(exercises):
    exercises[index]._duration = exercises[index]._duration + increase
    increase_durations_in_place(exercises, index + 1, increase)


def output_pretty(message, exercises, index):
  if index == 0:
    print(message)
  if index >= 0 and index < len(exercises):
    print(f'{index:2}:\t {exercises[index]}')
    output_pretty(message, exercises, index + 1)


def sum_durations(exercises, index):
  if index < 0 or index >= len(exercises):
    return 0
  return exercises[index]._duration + sum_durations(exercises, index + 1)


def types_on_day(exercises, index, day, types):
  if index < 0 or index >= len(exercises):
    return types
  if exercises[index]._day == day:
    type = exercises[index]._type
    if type not in types:
      types.append(type)
  return types_on_day(exercises,index + 1, day, types)


def which_days_each_type_exercise(exercises):
  answer = {}
  for exercise in exercises:
    if exercise._type not in answer:
      answer[exercise._type] = []
    if exercise._day not in answer[exercise._type]:
      answer[exercise._type].append(exercise._day)
  return answer


def which_exercises_each_day(exercises):
  answer = {}
  for exercise in exercises:
    if exercise._day not in answer:
      answer[exercise._day] = []
    if exercise._type not in answer[exercise._day]:
      answer[exercise._day].append(exercise._type)
  return answer


def main():
  e1 = Exercise('walk', 5, 33)
  print(f'e1:  {e1}')

  e2 = Exercise.random_exercise()
  e3 = Exercise.random_exercise()

  exercises = [e1, e2, e3]
  print(f'\nThe first 3 exercises: {exercises}')
  
  for _ in range(7):
    exercises.append(Exercise.random_exercise())
  print(f'\nThe 10 exercises are:\n{exercises}')

  output_pretty('\nThe exercises are:', exercises, 0)

  type = 'pilates'
  print(f'\n{type} was done {count_type(exercises, type, 0)} times')

  print(f'\nTotal time exercised is {sum_durations(exercises, 0)} minutes')

  day = 7
  types = types_on_day(exercises, 0, day, [])
  if len(types) <= 1:
    print(f'\nOn Day {day} ({e1.wordy_day(day)}), {types} was done')
  else:
    print(f'\nOn Day {day} ({e1.wordy_day(day)}), {types} were done')

  output_pretty('\nThe exercises:', exercises, 0)
  increase_durations_in_place(exercises, 0, 10)
  output_pretty('\nThe exercises after adding 10:', exercises, 0)

  revised = increase_durations(exercises, 0, 30, [])
  output_pretty('\nAdded 30 more:', revised, 0)

  print(f'\nExercises each day: {how_many_exercises_each_day(exercises)}')

  print(f'\nDays with no exercises: {days_no_exercises(exercises)}')
  
  print(f'\nWhich exercises on each day: {which_exercises_each_day(exercises)}')

  print(f'\nWhich days ach exercise: {which_days_each_type_exercise(exercises)}')

  print(f"\n{consecutives(exercises, ['strength training', 'core training'])}")


main()
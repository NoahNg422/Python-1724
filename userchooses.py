# The first game ever programmed by me!
# TO Jen: I will remember this program FOREVER!
# 0.1 Finished on October 8, 2021


def exam():
  print('Will you pass the exam?')
  print('Published by: Nnguyen422')
  print('=' * 64)
  print('The finals are taking place tomorrow. What will you do:')
  choice_1 = input('Play games or Study? ')
  while 'play' not in choice_1 and choice_1 != 'study':
    choice_1 = input('That wasn\'t a valid option! Play or study: ')
  
  if choice_1.lower() == 'study':
    print('You chose to study. You remember everything you learned since the first day of class.')
  else:
    print('You decided to play games, but forgot about the exam. You won\'t know anything in it.')
    return False
  print('=' * 64)
  
  print('The time is now 10:00 PM. You realize it\'s getting late.')
  choice_2 = input('Will you sleep or cram? ')
  while choice_2 != 'cram' and choice_2 != 'sleep':
    choice_2 = input('That wasn\'t a valid option! Sleep or cram: ')

  if choice_2.lower() == 'sleep':
    print('You chose to sleep at 10:30 PM. You were well rested.')
  else:
    print('You wanted to study as much for the exam as possible, but by the time you finished, \nthe time was already 2:00 AM. You woke up tired and couldn\'t get out of bed. \nYou missed the exam.')
    return False
  print('=' * 64)
  
  print('You woke up at 7:30 AM, just in time for breakfast.')
  choice_3 = input('Do you want to eat or skip breakfast? ')
  while 'eat' not in choice_3 and 'skip' not in choice_3:
    choice_3 = input('That wasn\'t a valid option! Eat or skip: ')

  if 'eat' in choice_3.lower():
    print('You ate a good breakfast. You have enough energy for the exam.')
  else:
    print('You chose to skip breakfast to save time. You end up having less than enough energy. \nThe exam won\'t be easy.')
  print('=' * 64)
  
  if 'eat' in choice_3.lower():
    print('After finishing breakfast, you realize your exam starts in less than 30 minutes. \nIt\'s now 8:32 AM. You need to get to school fast.')
  else:
    print('You leave the house at 8:25 AM. You need to get to school on time.')
  choice_4 = input('Will you take the bus or drive? ')
  while 'bus' not in choice_4 and 'drive' not in choice_4:
    choice_4 = input('That wasn\'t a valid option! Bus or drive: ')
  if choice_4.lower() == 'drive':
    print('You tried to drive quickly to class, but you encounter traffic.')
    choice_5 = input('Do you want to sit in traffic or take alt? ')
    while 'traffic' not in choice_5 and 'alt' not in choice_5:
      choice_5 = input('That wasn\'t a valid option! Traffic or alternate: ')
		
    if 'alt' in choice_5.lower():
      print('You chose to avoid traffic by taking an alternate route. You made it on time [8:57 AM].')
    else:
      print('You sat in traffic. It was very slow. The exam starts before you could arrive; \nYou missed the exam.')
      return False
  else:
    print('You chose the bus to avoid traffic, but the bus stops many times along the way. \nDespite this, you arrive just as class starts [9:00 AM].')
  print('=' * 64)

  print('You arrive at school. The exam starts. It looks hard.')
  choice_6 = input('Will you rush the test or go easy? ')
  if 'easy' in choice_6.lower():
    print('You took the exam in a calm and careful manner. You complete it just in time [59 Mins]. \nYou passed the exam.')
    import random
    grade = random.randint(80, 100)
    print(f'Score: {grade}')
  elif 'rush' in choice_6.lower():
    if 'eat' in choice_3.lower():
      print('With the energy from eating breakfast and the knowledge from studying, \nyou took the exam in a fast and confident manner. You completed it in 25 mins. \nYou passed the exam.')
      import random
      score = random.randint(75, 100)
      print(f'Score: {score}')
    else:
      print('You took the exam in a rushed and nervous manner. You complete the exam in 28 mins, \nbut many questions were wrong. You failed the exam.')
      import random
      result = random.randint(1, 70)
      print(f'Score: {result}')
      return False
  else:
    print('That wasn\'t a valid option!')
    print('Score: N/A')
    return None
  return True


def main():
  you_pass = exam()
  if you_pass:
    print('YOU WON: You passed the exam! Your GPA rises.\n:)')
  else:
    print('YOU LOSE: You failed the exam. Your GPA suffers.\n:(\nTry again? Press the <UP> key in shell or RUN.')


main()
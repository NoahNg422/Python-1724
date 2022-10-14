def main():
  print('Welcome to Python Geography Trivia!')
  topic = input('Ready? ')
  if topic == 'y':
    print('Begin.')
    print('NOTE: the answers will be case sensitive!')
    print('=' * 64)
    score = 0

    q1 = input('Question 1: What is the capital of Florida? ')
    q1_attempts = 0
    while q1 != 'Tallahassee' and q1_attempts < 3:
      q1_attempts += 1
      q1 = input('Try again. Capital of FL: ')
    if q1 == 'Tallahassee':
      score += 1
      print('Correct')
    else:
      print('Incorrect. The correct answer is: Tallahassee')
    print('=' * 64)

    q2 = input('Question 2: Which country is bigger, Mexico or Brazil? ')
    q2_attempts = 0
    while q2 != 'Brazil' and q2_attempts < 3:
      q2_attempts += 1
      q2 = input('Try again. Bigger country: ')
    if q2 == 'Brazil':
      score += 1
      print('Correct')
    else:
      print('Incorrect. The correct answer is: Brazil')
    print('=' * 64)

    q3 = input('Question 3: Which country\'s capital is Berlin? ')
    q3_attempts = 0
    while q3 != 'Germany' and q3_attempts < 3:
      q3_attempts += 1
      q3 = input('Try again. Berlin is in...: ')
    if q3 == 'Germany':
      score += 1
      print('Correct')
    else:
      print('Incorrect. The correct answer is: Germany')
    print('=' * 64)

    q4 = input('Question 4: Which country has more people: Russia or Phillipines? ')
    q4_attempts = 0
    while q4 != 'Russia' and q4_attempts < 3:
      q4_attempts += 1
      q4 = input('Try again. More populated country: ')
    if q4 == 'Russia':
      score += 1
      print('Correct')
    else:
      print('Incorrect. The correct answer is: Russia')
    print('=' * 64)

    q5 = input('Question 5: Which state borders Mexico: Illinois or Texas? ')
    q5_attempts = 0
    while q5 != 'Texas' and q5_attempts < 3:
      q5_attempts += 1
      q5 = input('Try again. State bordering Mexico: ')
    if q5 == 'Texas':
      score += 1
      print('Correct')
    else:
      print('Incorrect. The correct answer is: Texas')
    print('=' * 64)

    q6 = input('Question 6: What is the biggest island in the world? ')
    q6_attempts = 0
    while q6 != 'Greenland' and q6_attempts < 3:
      q6_attempts += 1
      q6 = input('Try again. Biggest island: ')
    if q6 == 'Greenland':
      score += 1
      print('Correct')
    else:
      print('Incorrect. The correct answer is: Greenland')
    print('=' * 64)

    q7 = input('Question 7: French Polynesia is in which ocean: ')
    q7_attempts = 0
    while q7 != 'Pacific'  and q7_attempts < 3:
      q7_attempts += 1
      q7 = input('Try again. French Polynesia in which ocean: ')
    if q7 == 'Pacific':
      score += 1
      print('Correct')
    else:
      print('Incorrect. The correct answer is: Pacific')
    print('=' * 64)

    q8 = input('Question 8: Which country does South Africa surround? ')
    q8_attempts = 0
    while q8 != 'Lesotho' and q8_attempts < 3:
      q8_attempts += 1
      q8 = input('Try again. country surrounded by SA: ')
    if q8 == 'Lesotho':
      score += 1
      print('Correct')
    else:
      print('Incorrect. The correct answer is: Lesotho')
    print('=' * 64)

    q9 = input('Question 9: Italy borders France. ')
    q9_attempts = 0
    while q9 != 'True' and q9_attempts < 2:
      q9_attempts += 1
      q9 = input('Try again. Italy borders France: ')
    if q9 == 'True':
      score += 1
      print('Correct')
    else:
      print('Incorrect. The correct answer is: True')
    print('=' * 64)

    q10 = input('Question 10: Which country has the most people? ')
    q10_attempts = 0
    while q10 != 'China' and q10_attempts < 3:
      q10_attempts += 1
      q10 = input('Try again. Country with most people: ')
    if q10 == 'China':
      score += 1
      print('Correct')
    else:
      print('Incorrect. The correct answer is: China')

    print('=' * 64)
    print(f'your score: {score}/10')
    if score <= 3:
      print('Ooh, you should look at a map. Try better next time, and I hope you can learn something new!')
    elif score > 3 and score <= 6:
      print('Don\'t give up! You can do better than this.')
    elif score == 7 or score == 8:
      print('Hey, not bad; you know your maps.')
    else:
      print('Awesome! you are a geography expert.')
    print('Go again?')

  else:
    print('Need to study your geography skills? No problem. Here\'s a map:')
    print('\nwww.google.com/maps')


main()
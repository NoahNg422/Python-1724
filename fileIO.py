import random
import datetime


def duplicate_usernames(filename, max_duplicates):
  dups = []
  with open(filename, 'r') as f:
    for username in f:
      username = username.strip()
      if username_dups(username) < max_duplicates:
        dups.append(username)
  return dups


def get_usernames_beginning_with(letter, usernames_filename):
  usernames = []
  with open(usernames_filename, 'r') as f:
    for username in f:
      username = username.strip()
      if username[0] == letter:
        usernames.append(username)
  return usernames


def get_names_beginning_with(letter, names_filename):
  names = []
  with open(names_filename, 'r') as f:
    for name in f:
      name = name.strip()
      if name[0].lower() == letter.lower():
        names.append(name)
  return names


def in_order(ls):
  for i in range(len(ls) - 1):
    if ls[i] > ls[i + 1]:
      return False
  return True


def is_valid(username, usernames_filename):
  with open(usernames_filename, 'r') as infile_usernames:
    for line in infile_usernames:
      line = line.strip()
      if line == username:
        return True
  return False


def personalized_reminder(letter, usernames_filename, names_filename):
  usernames = get_usernames_beginning_with(letter, usernames_filename)
  if not usernames:
    return f'No usernames begin with the letter {letter}.'
  emails = '@xula.edu, '.join(usernames) + '@xula.edu'
  names = ', '.join(get_names_beginning_with(letter, names_filename))
  border = f'--------------------------------------------------------------'
  print(border)
  print(f'\nFrom: aedwards@xula.edu')
  print(f'To:   {emails}')
  print(f'Subj: CPSC 2735 Reminder\n')
  print(f'Dear {names}:\n')
  print(f'Remember, we have lab at {datetime.datetime.now()}.\n')
  return border


def username_dups(username):
  for i in range(len(username)):
    if username[i] >= '0' and username[i] <= '9':
      return int(username[i:])
  return 0


def file_word_anagrams(file):
  wordlist = []
  score = 0
  with open(file) as file:
    words = file.readlines()
  for word in words:
    wordlist.append(word)
  word1 = words[random.randint(0, len(words))].strip('\n')
  print(word1)
  while True:
    word2 = input("\nYour word here: ")
    argument1 = sorted(word1.lower())
    argument2 = sorted(word2.lower())
    print(argument1)
    print(argument2)
    if argument1 != argument2:
      break
    score += 1
    print(score)
  print("Final score: ")
  return score


def main():
  with open('c:\\Users\\InnOu\\OneDrive\\Documents\\PythonPrograms\\valid_names.txt', 'r') as file_names:
    names = file_names.readlines()
  print(f'"names.txt" has {len(names)} names in it.')
  print(f'\nThe first line: {names[0]}')
  print(f'The last line:  {names[-1]}')
  print(f'\nThe 5th-10th lines:\n{names[5:11]}')

  print(f'\nAre the names in alphabetical order? {in_order(names)}')

  random.shuffle(names)

  names.sort()

  print(f"\nusernames with fewer than 2 duplicates:\n")
  duplicate_usernames('c:\\Users\\InnOu\\OneDrive\\Documents\\PythonPrograms\\xemail_addresses.txt', 1)

  with open('c:\\Users\\InnOu\\OneDrive\\Documents\\PythonPrograms\\xemail_addresses.txt', 'r') as infile_usernames, \
  open('c:\\Users\\InnOu\\OneDrive\\Documents\\PythonPrograms\\xemail_addresses.txt', 'w') as outfile_email_addresses:
    for line in infile_usernames:
      line = line.strip()
      outfile_email_addresses.write(line + '@xula.edu\n')
  
  print(f"\nMy personalized reminder for these usernames:\n")
  print(personalized_reminder('n', 'c:\\Users\\InnOu\\OneDrive\\Documents\\PythonPrograms\\xemail_addresses.txt', \
    'c:\\Users\\InnOu\\OneDrive\\Documents\\PythonPrograms\\valid_names.txt'))
  
  print(file_word_anagrams("c:\\Users\\InnOu\\OneDrive\\Documents\\PythonPrograms\\word_anagrams.txt"))


main()
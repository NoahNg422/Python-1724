import random
import collections
from pyclasses import Refugees


def create_refugees_file(file_name, num_refugees, surnames, countries, family_size):
  with open(file_name, 'w') as outfile:
    for _ in range(num_refugees):
      surname = surnames[random.randrange(len(surnames))]
      country = countries[random.randrange(len(countries))]
      family_size = random.randint(1, family_size)
      outfile.write(f'{surname},{country},{family_size}\n')


def add_to_odd_indexes(numq, increase):
  for i in range(len(numq)):
    value = numq.popleft()
    if value % 2 == 0:
      value += increase
    numq.append(value)


def generate_password(plaintext):
  deq = collections.deque()
  for ch in plaintext:
    deq.append(ch)
  answer = ''
  for _ in range(len(plaintext)):
    ch = deq.pop()
    if ch == 'a' or ch == 'A':
      answer += '@'
    elif ch == 'e' or ch == 'E':
      answer += '3'
    elif ch == 'l' or ch == 'L':
      answer += '1'
    elif ch == 'i' or ch == 'I':
      answer += '!'
    elif ch == 'o' or ch == 'O':
      answer += '0'
    else:
      answer += ch
  return answer


def is_palindrome(ls):
  if len(ls) < 2:
    return True
  deq = collections.deque()
  for i in range(len(ls) // 2):
    deq.append(ls[i])
  if len(ls) % 2 == 0:
    half_index = len(ls) // 2
  else:
    half_index = len(ls) // 2 + 1
  for i in range(half_index, len(ls)):
    if ls[i] != deq.pop():
      return False
  return True


def match_parenths(message):
  deq = collections.deque()
  for ch in message:
    if ch == '(':
      deq.append(ch)
    elif ch == ')':
      if len(deq) >= 1:
        top = deq.pop()
      else:
        return False
  if len(deq) != 0:
    return False
  return True


def output_queue(message, que):
  answer = message + '\t front'
  for value in que:
    answer += f'   {value}'
  print(f'{answer} \t back')


def reverse(ls):
  deq = collections.deque()
  for value in ls:
    deq.append(value)
  answer = []
  for i in range(len(ls)):
    answer.append(deq.pop())
  return answer


def main():
  surnames = ['Hussein', 'Ibrahim', 'Mahmoud', 'Melnyk', 'Sayyid', 'Zelensky']
  countries = ['Syria', 'Afghanistan', 'South Sudan', 'Somalia', 'Ukraine']
  create_refugees_file('warrefugees.csv', 300, surnames, countries, 7)
  
  refugees = Refugees('warrefugees.csv')
  refugees.add_user_input(3)
  refugees.output('\nOriginal Refugees:', 100)
  print(f'\nThe aid per country is {refugees.aid_per_country()}')

  '''
  Stacks: 
  | 30 |   Top of the stack, it's the only access point
  | 20 |
  | 10 |   Bottom of the stack, remove everything else to get here
  ------
  '''
  
  '''
  Deque:
            ------     ------     ------ 
  vals  --> | 10 | --> | 20 | --> | 30 | -->  None    
  None  <-- | 10 | <-- | 20 | <-- | 30 | <--  tail pointer sometimes
            ------     ------     ------
  '''

  nums = [n for n in range(10, 60, 10)]
  reversed_nums = reverse(nums)
  print(f'\n{nums} reversed is {reversed_nums}')

  print(f'\nis this a palindrome? {is_palindrome([1, 2, 3, 4, 3, 2, 1])}')

  print(f"\nA string becoming password: {generate_password('[Hello, World-tii]')}\n")

  refugees.reverse()
  refugees.output('The reversed refugees:', 100)

  print(f"Are parentheses properly closed? {match_parenths('(1 + 2) * 3')}")

  '''
  Queues:
            ---------------- 
  front     | 10 | 20 | 30 |     back    
            ---------------- 
  dequeue here                   enqueue here
  '''

  numq = collections.deque([11, 22, 33, 44, 55])
  output_queue('\nprior numq:', numq)
  add_to_odd_indexes(numq, 100)
  output_queue('after numq:', numq)
  numq = reverse(numq)
  output_queue('reversed numq:', numq)


main()
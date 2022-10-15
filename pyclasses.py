from collections import deque
import random


class Exercise:
  _days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
  _types = ['walk', 'run', 'cycle', 'core training', 'strength training', 'pilates']
  _max_length = 60

  def __init__(self, type, day, duration):
    self._type = type
    self._day = day
    self._duration = duration

  @classmethod
  def random_exercise(self):
    type = self._types[random.randrange(0, len(self._types))]
    day = random.randint(1, len(self._days))
    duration = random.randint(0, self._max_length)
    return Exercise(type, day, duration)

  def __repr__(self):
    return f'Exercise({self._type}, {self._duration}, {self._day})'
  
  def __str__(self):
    return f'{self._type} for {self._duration} minutes on a ' \
    f'{self.wordy_day(self._day)}'

  def wordy_day(self, day):
    if day >= 1 and day <= len(self._days):
      return self._days[day - 1]
    else:
      return None


class Hero:
  __JEWELS = ['emerald', 'ruby', 'diamond', 'wild']

  def __init__(self, name, gold=100, gems={}, max_num_jewel=3):
    self.name = name
    self._gold = gold
    if gems != {}:
      self.__gems = gems
    else:
      self.__gems = {}
      for gem in self.__JEWELS:
        self.__gems[gem] = random.randrange(max_num_jewel + 1)
    self.__gems['wild'] = 1

  def battle_winner(self, other_player) -> tuple:
    winner = -1
    gem1 = self.select_random_gem()
    gem2 = other_player.select_random_gem()
    # print(f'\n{self.get_name()} selected {gem1}\n{other_player.get_name()} selected {gem2}')
    if gem1 is None and gem2 is None:
      winner = -1
    elif gem1 is None:
      winner = 2
    elif gem2 is None:
      winner = 1
    else:
      index1 = self.__JEWELS.index(gem1)
      index2 = self.__JEWELS.index(gem2)
      if index1 > index2:
        winner = 1
      elif index1 < index2:
        winner = 2
      else:
        winner = 0
    return (winner, [gem1, gem2])

  def clone(self):
    if self is None:
      return None
    return Hero(self.get_name(), self.get_gold(), self.get_gems())

  def get_gems(self) -> dict:
    return self.__gems
  
  def get_gold(self) -> int:
    return self._gold
  
  def get_name(self) -> str:
    return self.name

  def select_random_gem(self):
    choices = []
    for gem, count in self.__gems.items():
      if count > 0:
        choices.append(gem)
    if len(choices) == 0:
      return None
    choice = choices[random.randrange(len(choices))]
    self.__gems[choice] = self.__gems[choice] - 1
    return choice

  def set_gems(self, gems):
    valid = True
    if type(gems) is not dict:
      valid = False
    for gem in self.__JEWELS:
      if gem not in gems.keys():
        valid = False
      else:
        if gems[gem] < 0:
          valid = False
    if valid:
      self.__gems = gems

  def set_gold(self, gold):
    if gold >= 0:
      self._gold = gold
  
  def set_name(self, name):
    if len(name.split()) == 1:
      self.name = name

  def __str__(self) -> str:
    return f'{self.name}, {self._gold}, {self.__gems}'

  def __repr__(self) -> str:
    return f'Hero({self.name}, {self._gold}, {self.__gems})'


class LinkedList:
  def __init__(self, value, next=None):
    self.item = value
    self.next = next

  def prepend(self, item):
    head = LinkedList(item)
    if self is None:
      return head
    head.next = self
    return head
  
  def __str__(self):
    return f'[{self.item}] <-> {self.next}'

  def len(self):
    pointer = self
    count = 0
    while pointer is not None:
      count += 1
      pointer = pointer.next
    return count

  def pop_left(self):
    if self.next is None:
      return None
    return self.next
  
  def get_item(self):
    return self.item


class Refugee:
  def __init__(self, surname, country, family_size):
    self.surname = surname
    self.country = country
    self.family_size = family_size

  def __str__(self) -> str:
    return f'{self.surname:20s} {self.country:20s} {self.family_size}'


class Refugees:
  __MAX_AID = 58_500_000_000

  def __init__(self, filename):
    line_number = 1
    self.refugees = []
    with open(filename, 'r') as infile:
      line = infile.readline()
      while line:
        if len(line.split(',')) == 3:
          surname, country, family_size = line.split(',')
          self.refugees.append(Refugee(surname.strip(), country.strip(), int(family_size)))
        else:
          print(f'Skipping {line_number}: {line}')
        line = infile.readline()
        line_number += 1

  def add_user_input(self, num_new_families):
    country = input('Enter a country: ')
    for i in range(num_new_families):
      surname = input(f'\nSurname for {i+1}/{num_new_families} families: ')
      family_size = int(input(f'Enter {surname}\'s family size: '))
      self.refugees.append(Refugee(surname, country, family_size))

  def aid_per_country(self):
    answer = {}
    counts = self.count_refugees_per_country()
    for country in counts:
      answer[country] = round(Refugees.__MAX_AID / counts[country], 2)
    return answer

  def count_refugees_per_country(self):
    answer = {}
    for family in self.refugees:
      country = family.country
      if country not in answer:
        answer[country] = 0
      answer[country] += family.family_size
    return answer

  def countries_with_surnames(self, surnames):
    answer = []
    ptr = surnames
    while ptr is not None:
      for family in self.refugees:
        if ptr.value == family.surname:
          if family.country not in answer:
            answer.append(family.country)
      ptr = ptr.next
    return answer

  def get(self, index):
    if index < 0 or index >= len(self.refugees):
      return None
    return self.refugees[index]

  def __len__(self):
    return len(self.refugees)

  def no_aid(self):
    answer = []
    aid_amounts = self.aid_per_country()
    for family in self.refugees:
      country = family.country
      if country not in aid_amounts:
        answer.append(country)
    return answer

  def output(self, message, factor):
    print(message)
    print(self.output_header())
    for i in range(len(self.refugees)):
      if i % factor == 0:
        print(f'{i:5d} {self.refugees[i]}')

  def output_header(self):
    return f"{'INDEX':5s} {'SURNAME':20s} {'COUNTRY':20s} {'FAMILY SIZE'}"

  def __repr__(self):
    return f'{self.refugees}'

  def reverse(self):
    deq = deque(self.refugees)
    answer = []
    for _ in range(len(self.refugees)):
      answer.append(deq.pop())
    self.refugees = answer

  def __str__(self):
    answer = self.output_header() + '\n'
    for i in range(len(self.refugees)):
      answer += f'{i:5d} {self.refugees[i]}\n'
      return answer

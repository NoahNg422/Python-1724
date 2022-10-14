from pyclasses import Hero
import datetime
import random


class Avengers:
  def __init__(self, hero, next=None):
    self.hero : Hero = hero
    self.next : Avengers = next

  def clone(self):
    if self is None:
      return None
    temp = self
    hero = Hero(temp.hero.get_name(), temp.hero.get_gold(), temp.hero.get_gems())
    answer = Avengers(hero, None)
    answer_temp = answer
    while temp.next is not None:
      temp = temp.next
      hero = Hero(temp.hero.get_name(), temp.hero.get_gold(), temp.hero.get_gems())
      answer_temp.next = Avengers(hero)
      answer_temp = answer_temp.next
    return answer

  def peek_left(self) -> Hero:
    if self is None:
      return None
    temp = self.hero.clone()
    return temp

  def pop_left(self) -> Hero:
    if self is None:
      return None
    return self.next

  def prepend(self, hero: Hero):
    return Avengers(hero, self)

  def push_right(self, hero: Hero):
    if hero is None:
      return self
    if self is None:
      return Avengers(hero)
    answer = self.clone()
    temp = answer
    while temp.next is not None:
      temp = temp.next
    temp.next = Avengers(hero)
    return answer

  def size(self):
    count = 0
    temp = self
    while temp is not None:
      count += 1
      temp = temp.next
    return count

  def __str__(self):
    return f'{self.hero} \n\t --> {self.next}'


class Orders:
  def __init__(self, item, count, cost, next=None):
    self.item = item
    self.price = cost
    self.qty = count
    self.next = next

  def prepend(self, item, count, cost):
    head = Orders(item, count, cost)
    if self is None:
      return head
    head.next = self
    return head
  
  def __str__(self):
    return f'[{self.item}: {self.qty} @ {self.price}] >> {self.next}'

  def get_order(self):
    return self.item

  def get_cost(self):
    return self.price

  def get_count(self):
    return self.qty

  def add(self, amount_to_add):
    self.qty += amount_to_add

  def is_already_ordered(self, menu_item):
    item = self
    while item is not None:
      if item.get_order() == menu_item.get_order():
        return True
      item = item.next
    return False
  
  def __len__(self):
    count = 0
    item = self
    while item is not None:
      count += 1
      item = item.next
    return count
  
  def generate_code(self):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'      
    char1 = letters[random.randrange(len(letters))]
    char2 = letters[random.randrange(len(letters))]
    num = random.randint(10, 99)
    num2 = random.randint(10, 99)
    return f'{char1}{char2}-{num}{num2}'

  def border(self):
    border = '-' * 55
    return border
  
  def output_receipt(self):
    today = str(datetime.datetime.now())[:-7]
    print(self.border())
    print(f'YOUR RECEIPT {today}')
    print(self.border())
    order = f'  {self.item:24s} {self.qty} @ ${self.price:.2f}'
    print(order)
    total = self.price * self.qty
    while len(self) != 1:
      self = self.next
      total += self.price * self.qty
      print(f'  {self.item:24s} {self.qty} @ ${self.price:.2f}')
    print()
    print(f'                 Subtotal:                    ${total:5.2f}')
    print(f'                 Tax 9.20% (Jefferson, LA):   ${(total * 0.092):5.2f}')
    print(f'                 Grand Total:                 ${(total * 1.092):5.2f}')
    print()
    print(f'  When you drive up, your order is {datetime.date.today().year}-{self.generate_code()}')
    message = self.border()
    return message


class SuperHero:
  POWERS = ['No superpowers', 'Born with powers', 'Enhanced', 'Accidental or mutant powers', \
  'Psychic powers', 'Magic user', 'Power Cosmic']
  
  def __init__(self, name='Boss Lady', human_name='Jamitha', gender='Female', \
  alignment=['Hero'], species=['Human', 'Symbiote'], powers=['Power Cosmic', \
  'Enhanced'], year=2001):
    self.name = name
    self.human_name = human_name
    self.gender = gender
    self.alignments = alignment
    self.species = species
    self.powers = powers
    self.year = year

  def human_without_human_name(self):
    return 'Human' in self.species and self.human_name.strip() == ''
      
  def __repr__(self):
    return f'Hero: {self.name}, {self.human_name}, {self.gender}, ' \
    f'{self.alignments}, {self.species}, {self.powers}, {self.year}'


class Tree:
  def __init__(self, name, num_siblings, left=None, right=None):
    self.name = name
    self.left = left
    self.right = right
    self.num_siblings = num_siblings

  def preorder(self):
    answer  = ''
    if self:
      answer += self.name + ', '
      if self.left is not None:
        answer += self.left.preorder()
      if self.right is not None:
        answer += self.right.preorder()
    return answer
  
  def inorder(self):
    answer  = ''
    if self:
      if self.left is not None:
        answer += self.left.preorder()
      answer += self.name + ', '
      if self.right is not None:
        answer += self.right.preorder()
    return answer

  def postorder(self):
    answer  = ''
    if self:
      if self.left is not None:
        answer += self.left.preorder()
      if self.right is not None:
        answer += self.right.preorder()
      answer += self.name + ', '
    return answer

  def is_leaf(self):
    return self.left is None and self.right is None
  
  def output_with_indents(self, indents):
    answer = '\t' * indents + self.name
    if self.left is not None:
      answer += '\n' + '\t' * (indents+1) + self.left.output_with_indents(indents+1)
    if self.right is not None:
      answer += '\n' + '\t' * (indents+1) + self.right.output_with_indents(indents+1)
    return answer

  def postorder_print(self):
    if self.left is not None:
      self.left.postorder_print()
    if self.right is not None:
      self.right.postorder_print()
    print(self.name, end=', ')

  def size(self, count=1):
    if self.is_leaf():
      return 1
    if self.left is not None and self.right is not None:
      return 1 + self.left.size() + self.right.size()
    if self.right is not None:
      return 1 + self.right.size()
    if self.left is not None:
      return 1 + self.left.size()

  def each_name(self, names=[]):
    if self.is_leaf():
      names.append(self.name)
      return names
    names.append(self.name)
    if self.right is not None:
      self.right.each_name(names)
    if self.left is not None:
      self.left.each_name(names)
    return names

  def siblings_per_family(self, families={}):
    families[self.name] = self.num_siblings
    if self.is_leaf():
      families[self.name] = self.num_siblings
      return families
    if self.left is not None:
      families[self.name] = self.num_siblings
      self.left.siblings_per_family()
    if self.right is not None:
      families[self.name] = self.num_siblings
      self.right.siblings_per_family()
    return families

  def __count_siblings(self, families={}):
    families[self.name] = self.num_siblings
    if self.is_leaf():
      families[self.name] = self.num_siblings
      return families[self.name]
    if self.left is not None:
      self.left.__count_siblings()
    if self.right is not None:
      self.right.__count_siblings()
    return families[self.name]

  def aunts_and_uncles(self):
    if self.left is not None and self.right is not None:
      return self.right.__count_siblings() + self.left.__count_siblings()
    if self.left is not None:
      return self.left.__count_siblings()
    if self.right is not None:
      return self.right.__count_siblings()
    return 0

  def had_more_siblings(self, node2):
    return self.__count_siblings() > node2.__count_siblings()

  def family_grand_total(self, count=1, families={}):
    families[self.name] = self.num_siblings
    if self.is_leaf():
      families[self.name] = self.num_siblings
      count += families[self.name]
      return count
    if self.left is not None and self.right is not None:
      return 1 + families[self.name] + self.left.family_grand_total() + \
      self.right.family_grand_total()
    if self.left is not None:
      return families[self.name] + self.left.family_grand_total()
    if self.right is not None:
      return families[self.name] + self.right.family_grand_total()

  def num_members(self, count=1):
    if self.left.is_leaf() and self.right.is_leaf():
      return self.family_grand_total()
    if self.right is not None:
      return self.right.num_members()
    if self.left is not None:
      return self.left.num_members()

  def only_child(self):
    num = 0
    if self.num_siblings == 0:
      num += 1
    if self.left is not None:
      num += self.left.only_child()
    if self.right is not None:
      num += self.right.only_child()
    return num
  
  def __str__(self):
    return self.output_with_indents(0)
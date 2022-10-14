from pyclasses import LinkedList
import random


def how_many_in_family(family_name, all_names):
  count = 0
  for name in all_names:
    parts = name.split()
    if family_name.lower() == parts[1].lower():
      count += 1
  return count


def includes_me(my_name, all_names):
  answer = []
  my_name_parts = my_name.split()
  for part_of_my_name in my_name_parts:
    for name in all_names:
      if part_of_my_name.lower() in name and name not in answer:
        answer.append(name)
  return answer


def output_3_nodes(message, n1, n2, n3):
  print(message)
  print(f'head: {n1}')    
  print(f'n2:   {n2}')    
  print(f'n3:   {n3}')    


def random_name():
  FIRST_NAMES = ['aarion', 'ahmed', 'andrea', 'austin', 'cortland', 'darryl', 'davis', 'elana',
    'jade', 'jordan', 'joshua', 'kaleb', 'khalil', 'noah', 'rodney', 'ryan',
    'shawn', 'tariq', 'terrance', 'tia', 'william', 'zoë']
  LAST_NAMES = ['alexander', 'cooke', 'edwards', 'el-desoky', 'felder', 'foster',
    'harrington', 'hunter', 'johnson', 'livingston', 'mitchell', 'monroe', 'myles',
    'nelson', 'nguyen', 'orgah', 'perriott', 'porter', 'riley', 'robertson', 'terrell', 'winbush']
  first_name = FIRST_NAMES[random.randrange(len(FIRST_NAMES))]
  last_name = LAST_NAMES[random.randrange(len(LAST_NAMES))] 
  return first_name + ' ' + last_name


def random_names(num_names):
  return [random_name() for _ in range(num_names)]


def main():
  head = LinkedList(10)
  n20 = LinkedList(20)
  n30 = LinkedList(30)
  output_3_nodes('The original nodes', head, n20, n30)

  # head --> 10 --> None
  head = LinkedList(10)
  # head --> 10 --> 20 --> None
  head.next = LinkedList(20)
  # head --> 10 --> 20 --> 30 --> None
  head.next.next = LinkedList(30)
  output_3_nodes('\nBuild head --> 10 --> 20 --> 30 --> None:', head, n20, n30)

  # n30 --> 30 --> None
  n30 = LinkedList(30)
  # n20 --> 20 --> 30 --> None
  n20 = LinkedList(20, n30)
  # head --> 10 --> 20 --> 30 --> None
  head = LinkedList(10, n20)
  output_3_nodes('\nBuild it again:', head, n20, n30)

  head = LinkedList(10, LinkedList(20, LinkedList(30)))
  print(f'\nBuild it a third time:\n{head}')
  print(f'{head} has {head.len()} nodes')

  winners = LinkedList('Ukraine 🇺🇦')
  winners = winners.prepend('Germany 🇩🇪')
  winners = winners.prepend('United States 🇺🇸')
  winners = winners.prepend('Sweden 🇸🇪')
  print(f'\nThe {winners.len()} winners are {winners}')

  losers = LinkedList('Russia 🇷🇺')
  losers = losers.prepend('China 🇨🇳')
  losers = losers.prepend('United Arab Emirates 🇦🇪')
  losers = losers.prepend('Iran')
  print(f'The {losers.len()} losers are {losers}')

  print(f"\n'{random_name()}' is a random name")

  all_names = random_names(111)
  my_name = 'Noah Nguyen'
  print(f"\nThese random names include me:\n{includes_me(my_name, all_names)}")

  family = 'Nguyen'
  how_many = how_many_in_family(family, all_names)
  if how_many == 1:
    print(f"There is {how_many} person in the {family.upper()} family.")
  elif how_many == 0:
    print(f'Nobody is from the {family.upper()} family!.')
  else:
    print(f"There are {how_many} people in the {family.upper()} family.")

  # 10 --> 20 --> 30 --> None (3 nodes)


main()
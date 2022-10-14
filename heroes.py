import random
from somemoreclasses import SuperHero


def have_human_names(heroes):
  for hero in heroes:
    if hero.human_without_human_name():
      print(f'\t {hero}')
      return False
  return True


def debut_year_range(heroes, start_year, end_year):
  names = []
  for hero in heroes:
    if hero.year >= start_year and hero.year <= end_year:
      names.append(hero.name)
  return names


def num_with_power(heroes, power):
  count = 0
  for h in heroes:
    if power in h.powers:
      count += 1
  return count
           

def unique_species(heroes):
  species = []
  for hero in heroes:
    for s in hero.species:
      if s not in species:
        species.append(s)
  return species


def main():
  generic = SuperHero()
  print(f'My generic {generic.name} hero was created in {generic.year}.')
  print(f'  {generic}')

  another_hero = SuperHero('Captain Endure', '', 'male', \
  ['Anti-hero'], ['Fairy', 'Titan', 'Artificial Body'], ['Magic user', \
  'Psychic powers'], 2022)
  print(f'\nAnother_hero:\n  {another_hero}')

  me = SuperHero('Flydragon', 'Noah', 'Male', ['Hero'], ['Human'], \
  ['Engaged Student', 'Determined', 'Expert Computer Programmer'], 2021)
  print(f'\n{me}')

  hero4 = SuperHero('Spiderman', 'Peter Parker', 'Male', \
  ['Hero'], ['Human'], ['Accidental or mutant powers'], 1962)
  hero5 = SuperHero('Black Panther', 'T\'challa', 'Male', \
  ['Hero'], ['Human'], ['No Superpowers'], 1966)
  hero6 = SuperHero('Captain America', 'Steve Rogers', 'Male', \
  ['Hero'], ['Human'], ['Enhanced'], 1941)

  heroes = [generic, another_hero, me, hero4, hero5, hero6]
  random.shuffle(heroes)
  print(f'\n{heroes}\n')

  print(f'{debut_year_range(heroes, 1960, 2020)}\n')

  print(have_human_names(heroes))

  print(f'\n{unique_species(heroes)}\n')
  
  print(num_with_power(heroes, 'Expert Computer Programmer'))


main()
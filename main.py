def file_opener(file):
	with open(file) as f:
		data = f.read()
	return data


def main():
  file = input('Which file do you want to open? ')
  
  if file == 'atm':
    import atm
    input('\nPress <ENTER> to see code.')
    print('=' * 80)
    print(file_opener('c:\\Users\\InnOu\\OneDrive\\Documents\\PythonPrograms\\atm.py'))
  
  elif file == 'blackjack':
    import blackjack
    input('\nPress <ENTER> to see code.')
    print('=' * 80)
    print(file_opener('c:\\Users\\InnOu\\OneDrive\\Documents\\PythonPrograms\\blackjack.py'))
  
  elif file == 'christmas-songs':
    import christmas_songs
    input('\nPress <ENTER> to see code.')
    print('=' * 80)
    print(file_opener('c:\\Users\\InnOu\\OneDrive\\Documents\\PythonPrograms\\christmas_songs.py'))
  
  elif file == 'dstructures':
    import datastructures
    input('\nPress <ENTER> to see code.')
    print('=' * 80)
    print(file_opener('c:\\Users\\InnOu\\OneDrive\\Documents\\PythonPrograms\\datastructures.py'))
  
  elif file == 'fly':
    import fly
    input('\nPress <ENTER> to see code.')
    print('=' * 80)
    print(file_opener('c:\\Users\\InnOu\\OneDrive\\Documents\\PythonPrograms\\fly.py'))
  
  elif file == 'loops':
    import loops
    input('\nPress <ENTER> to see code.')
    print('=' * 80)
    print(file_opener('c:\\Users\\InnOu\\OneDrive\\Documents\\PythonPrograms\\loops.py'))
  
  elif file == 'basics':
    import py3basics
    input('\nPress <ENTER> to see code.')
    print('=' * 80)
    print(file_opener('c:\\Users\\InnOu\\OneDrive\\Documents\\PythonPrograms\\py3basics.py'))
  
  elif file == 'rps':
    import rockpaperscissors
    input('\nPress <ENTER> to see code.')
    print('=' * 80)
    print(file_opener('c:\\Users\\InnOu\\OneDrive\\Documents\\PythonPrograms\\rockpaperscissors.py'))

  elif file == 'songloop':
    import songloop
    input('\nPress <ENTER> to see code.')
    print('=' * 80)
    print(file_opener('c:\\Users\\InnOu\\OneDrive\\Documents\\PythonPrograms\\songloop.py'))
  
  elif file == 'trivia':
    import trivia
    input('\nPress <ENTER> to see code.')
    print('=' * 80)
    print(file_opener('c:\\Users\\InnOu\\OneDrive\\Documents\\PythonPrograms\\trivia.py'))
  
  elif file == 'webapp':
    try:
      import jswebapp
      input('\nPress <ENTER> to see code.')
      print('=' * 80)
    except:
      print(file_opener('c:\\Users\\InnOu\\OneDrive\\Documents\\PythonPrograms\\jswebapp.py'))
  
  elif file == 'youchoose':
    import userchooses
    input('\nPress <ENTER> to see code.')
    print('=' * 80)
    print(file_opener('c:\\Users\\InnOu\\OneDrive\\Documents\\PythonPrograms\\userchooses.py'))

  elif file == 'avengers':
    import avengersbattle
    input('\nPress <ENTER> to see code.')
    print('=' * 80)
    print(file_opener('c:\\Users\\InnOu\\OneDrive\\Documents\\PythonPrograms\\avengersbattle.py'))
  
  elif file == 'cpsc1724':
    import cpsc1724
    input('\nPress <ENTER> to see code.')
    print('=' * 80)
    print(file_opener('c:\\Users\\InnOu\\OneDrive\\Documents\\PythonPrograms\\cpsc1724.py'))
  
  elif file == 'datasp22':
    import dataSP22
    input('\nPress <ENTER> to see code.')
    print('=' * 80)
    print(file_opener('c:\\Users\\InnOu\\OneDrive\\Documents\\PythonPrograms\\dataSP22.py'))
  
  elif file == 'fileio':
    import fileIO
    input('\nPress <ENTER> to see code.')
    print('=' * 80)
    print(file_opener('c:\\Users\\InnOu\\OneDrive\\Documents\\PythonPrograms\\fileIO.py'))

  elif file == 'graph':
    import graphandtree
    input('\nPress <ENTER> to see code.')
    print('=' * 80)
    print(file_opener('c:\\Users\\InnOu\\OneDrive\\Documents\\PythonPrograms\\graphandtree.py'))
  
  elif file == 'hero':
    import heroes
    input('\nPress <ENTER> to see code.')
    print('=' * 80)
    print(file_opener('c:\\Users\\InnOu\\OneDrive\\Documents\\PythonPrograms\\heroes.py'))
  
  elif file == 'intro':
    import introToDS
    input('\nPress <ENTER> to see code.')
    print('=' * 80)
    print(file_opener('c:\\Users\\InnOu\\OneDrive\\Documents\\PythonPrograms\\introToDS.py'))

  elif file == 'linklist':
    import linklist
    input('\nPress <ENTER> to see code.')
    print('=' * 80)
    print(file_opener('c:\\Users\\InnOu\\OneDrive\\Documents\\PythonPrograms\\linklist.py'))
  
  elif file == 'orders':
    import orders
    input('\nPress <ENTER> to see code.')
    print('=' * 80)
    print(file_opener('c:\\Users\\InnOu\\OneDrive\\Documents\\PythonPrograms\\orders.py'))

  elif file == 'queuestack':
    import qandstack
    input('\nPress <ENTER> to see code.')
    print('=' * 80)
    print(file_opener('c:\\Users\\InnOu\\OneDrive\\Documents\\PythonPrograms\\qandstack.py'))
  
  elif file == 'recursion':
    import recursion
    input('\nPress <ENTER> to see code.')
    print('=' * 80)
    print(file_opener('c:\\Users\\InnOu\\OneDrive\\Documents\\PythonPrograms\\recursion.py'))
  
  elif file == 'solutions':
    import exercises
    input('\nPress <ENTER> to see code.')
    print('=' * 80)
    print(file_opener('c:\\Users\\InnOu\\OneDrive\\Documents\\PythonPrograms\\exercises.py'))

  elif file == 'classes':
    print('Nothing really interesting here, just some classes.')
    input("Here's the source code instead. Press <ENTER> to see code.")
    print(file_opener('c:\\Users\\InnOu\\OneDrive\\Documents\\PythonPrograms\\pyclasses.py'))

  elif file == 'moreclasses':
    print('Nothing really interesting here, just some more classes.')
    input("Here's the source code instead. Press <ENTER> to see code.")
    print(file_opener('c:\\Users\\InnOu\\OneDrive\\Documents\\PythonPrograms\\somemoreclasses.py'))

  elif file == 'main':
    print('I cannot execute main.py, as it will enter an infinite recursion!')
    input("Here's the source code instead. Press <ENTER> to see code.")
    print(file_opener('c:\\Users\\InnOu\\OneDrive\\Documents\\PythonPrograms\\main.py'))
  
  elif file.strip() == '' or file.strip().lower() == 'none':
    print(file_opener('c:\\Users\\InnOu\\OneDrive\\Documents\\PythonPrograms\\main.py'))
  
  else:
    with open('c:\\Users\\InnOu\\OneDrive\\Documents\\PythonPrograms\\welcome.txt') as file:
      data = file.read()
    print(data)
    print('\nIt appears the file name you entered does not match any existing file.')
    print('Did you try to access a nonexistant file, made a typo, anything?')
    print('Oh well, here is every character on the English keyboard:')
    print('\n`~1!2@3#4$5%6^7&8*9(0)-_=+qQwWeErRtTyYuUiIoOpPa', end='')
    print('AsSdDfFgGhHjJkKlLzZxXcCvVbBnNmM,<.>/?;:""[{]}\\|\n')
    print('Oh, and one last thing... ')
    i = 0 
    while i <3:
      i += 1
      print('"I love you! \U0001f48b" \n-Fly Dragon \U0001f409')


if __name__ == "__main__":
  main()
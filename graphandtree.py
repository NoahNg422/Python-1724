import random
from somemoreclasses import Tree


def Graph_of_america():
  return {
    'Austin': ['Dallas', 'Houston'],
    'Houston': ['Austin', 'Dallas', 'New Orleans', 'Shreveport'],
    'New Orleans': ['Birmingham', 'Houston', 'Jackson', 'Mobile', 'Shreveport'],
    'Dallas/FW': ['Austin', 'Houston', 'Little Rock', 'OK City', 'Shreveport'],
    'Shreveport': ['Dallas', 'Houston', 'Jackson', 'New Orleans'],
    'Jackson': ['Birmingham', 'Memphis', 'New Orleans', 'Shreveport'],
    'Oklahoma City': ['Dallas', 'Little Rock'],
    'Little Rock': ['Dallas', 'OK City', 'Memphis'],
    'Memphis': ['Jackson', 'Little Rock', 'Nashville'],
    'Nashville': ['Atlanta', 'Birmingham', 'Knoxville', 'Memphis'],
    'Birmingham': ['Atlanta', 'Jackson', 'Mobile', 'Nashville', 'New Orleans'],
    'Mobile/Pensacola': ['Atlanta', 'Birmingham', 'New Orleans', 'Tampa'],
    'Orlando/Tampa': ['Atlanta', 'Pensacola'],
    'Atlanta': ['Birmingham', 'Charlotte', 'Knoxville', 'Mobile', 'Nashville', 'Orlando'],
    'Knoxville': ['Atlanta', 'Charlotte', 'Nashville'],
    'Charlotte': ['Atlanta', 'Knoxville']
  }


def main():
  print('I know very well that I will graduate and look for a job out-of-state in 3 years.')
  print("As a result, I won't have much time to travel from [TX or GA] to LA to meet family.")
  print('So, I made this project as a tribute to my family and my Vietnamese ancestry. \U0001f409\n')
  
  siblings = random.randint(0, 11)
  siblings2 = random.randint(0, 11)
  siblings3 = random.randint(0, 11)
  siblings4 = random.randint(0, 11)
  siblings5 = random.randint(0, 11)
  siblings6 = random.randint(0, 11)
  siblings7 = random.randint(0, 11)
  siblings8 = random.randint(0, 11)
  siblings9 = random.randint(0, 11)
  siblingsA = random.randint(0, 11)
  siblingsB = random.randint(0, 11)
  siblingsC = random.randint(0, 11)

  me = Tree('Noah Nguyễn (2003)', 2) # My 2 sisters
  print(f'The initial <Nguyễn> tree:\n{me}')

  me.left = Tree('Mom: mẹ (1967)', 7) # 2 Aunts and 5 uncles
  me.right = Tree('Dad: ba (1961)', 6) # 3 aunts and 3 uncles
  print(f'\nThe tree with parents:\n{me}')

  me.left.left = Tree('Grandma: bà ngoại (1945)', siblings)
  me.left.right = Tree('Grandpa: ông ngoại (1941)', siblings2)
  print(f'\nThe tree with maternal grandparents:\n{me}')

  me.right.left = Tree('Grandma: bà nội (1931 to 2017)', siblings3)
  me.right.right = Tree('Grandpa: ông nội (1927 to 1981)', siblings4)
  print(f'\nThe tree with paternal grandparents:\n{me}')

  me.left.left.left = Tree("Great grandma: bà cố (19?? to 20??)", siblings5)
  me.left.left.right = Tree("Great grandpa: ông cố (19?? to 20??)", siblings6)
  me.left.right.left = Tree("Great grandma: bà cố (19?? to 2003)", siblings7)
  me.left.right.right = Tree("Great grandpa: ông cố (19?? to 19??)", siblings8)
  me.right.left.left = Tree("Great grandma: bà cố (1??? to ????)", siblings9)
  me.right.left.right = Tree("Great grandpa: ông cố (1??? to ????)", siblingsA)
  me.right.right.left = Tree("Great grandma: bà cố (No data)", siblingsB)
  me.right.right.right = Tree("Great grandpa: ông cố (No data)", siblingsC)
  print(f'\nA tree including my great grandparents (EN >> VN translations included):\n{me}')
  
  vertex = me.left.is_leaf()
  vertex2 = me.right.right.right.is_leaf()
  print(f'\nIs vertex a leaf: {vertex}')
  print(f'Is vertex2 a leaf: {vertex2}\n')

  print(f'The size of my tree: {me.size()}')

  print(f'\nPreorder: {me.preorder()}')
  
  print(f'\nInorder: {me.inorder()}')
  
  print(f'\nPostorder: {me.postorder()}\n')
  
  print(f'All names: {me.each_name()}\n')

  print(f'Siblings per person: {me.siblings_per_family()}\n')

  print(f'Number of uncles and aunts: {me.aunts_and_uncles()}\n')
  
  node1 = me.left.left
  node2 = me.right.left.right
  print(f'Node1 has more siblings: {node1.had_more_siblings(node2)}\n')

  "Used recursive transversal instead of tree.right.right"
  
  print(f'My family size (GRAND TOTAL): {me.family_grand_total()}\n')

  grandpa_family_size = me.num_members()
  print(f'Size of grandpa\'s (ông nội) family: {grandpa_family_size}\n')

  print(f'People who were the only child: {me.only_child()}')

  print('\nGRAPHS\n')

  graph = Graph_of_america()
  print('     O----L----M----N----K----C')
  print('     |   /     |    |\   |   / ')
  print('     |  /      |    | \  |  /  ')
  print('     | /       |    |  \ | /   ')
  print('     |/        |    |   \|/    ')
  print('     D----S----J----B----A     ')
  print('    /|   / \   |   /|   / \    ')
  print('   / |  /   \  |  / |  /   \   ')
  print('  /  | /     \ | /  | /     \  ')
  print(' /   |/       \|/   |/       \ ')
  print('A----H---------N----M---------O')
  
  print('\nThe function below represents this graph.\n')
  print(graph)


main()
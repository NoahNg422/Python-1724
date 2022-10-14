import random
from somemoreclasses import Orders


def logo():
  print('|\       |        |--\                         |      |          \n'\
        '| \     /|        |   |                        |      |          \n'\
        '|  \   / |   /--  |   |   /--\   |/-\    /--|  |   /--|  J  /--- \n'\
        '|   \ /  |  |     |   |  |    |  |   |  |   |  |  |   |     \__  \n'\
        '|    V   |   \__  |__/    \__/   |   |   \_/|  |   \__|     ___/ \n')


def output_welcome_message():
  print("Welcome to the McDonald's app. What would you like to order?")


def possible_orders():
  item0 = Orders('Hamburger Meal', 1, 5.49)
  item1 = Orders('Cheeseburger Meal', 1, 5.99)
  item2 = Orders('Big-Mac Meal', 1, 7.49)
  item3 = Orders('Chicken Sandwich', 1, 5.49)
  item4 = Orders('Filet-O-Fish Meal', 1, 8.09)
  item5 = Orders('10 pc Chicken Nuggets', 1, 2.99)
  item6 = Orders('20 pc Chicken Nuggets', 1, 4.69)
  item7 = Orders('6 pc Chicken Tenders', 1, 2.89)
  item8 = Orders('12 pc Chicken Tenders', 1, 5.29)
  item9 = Orders('Hash Browns', 1, 1.59)
  itemA = Orders('Pancakes', 1, 2.59)
  itemB = Orders('Any McGriddle', 1, 3.59)
  itemC = Orders('Croissant', 1, 2.99)
  itemD = Orders('Any 24 Oz Drink', 1, 1.99)
  itemE = Orders('Any Flavor Ice Cream', 1, 1.39)
  itemF = Orders('Apple Pie', 1, 1.99)
  menu = [item0, item1, item2, item3, item4, item5, item6, item7,
    item8, item9, itemA, itemB, itemC, itemD, itemE, itemF]
  new_order = menu[random.randrange(len(menu))]
  return new_order


def place_order(count):
  order = possible_orders()
  for i in range(count - 1):
    food = possible_orders()
    if order.is_already_ordered(food):
      order.add(1)
    else:
      order = order.prepend(food.get_order(), food.get_count(), food.get_cost())
  return order


def main():
  logo()
  output_welcome_message()

  order = place_order(5)
  print(f'\nYour link-list order:  {order}\n')
  
  code = Orders.output_receipt(order)
  print(code)

  print("Thank you for ordering at McDonald's. Enjoy your meal!")


main()
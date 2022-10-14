def main():
  account_pins = ['0012', '0042', '1234', '1337', '8023']
  account_balances = [12, 100000, 100, 2000, 1024]
  
  pin = ''
  
  print('Welcome to Simulated Bank.')
  
  if pin == '':
    while pin.upper() != 'EXIT':
      pin = input('Please enter your pin: ')
      if pin == account_pins[0]:
        c = input('\nAccess granted! \nWould you like to d or w: ')
        if c == 'w':
          w = input('\nWithdraw how much: ')
          account_balances[0] -= int(w)
          if account_balances[0] < 0:
            print('\nInsufficient balance; cannot withdraw.')
          else:
            print(f'\nYour new balance is ${account_balances[0]}. \nTransaction complete!')
        elif c == 'd':
          d = input('\nDeposit how much: ')
          account_balances[0] += int(d)
          print(f'\nYour new balance is ${account_balances[0]}. \nTransaction complete!')
        else:
          print('\nError!')
      elif pin == account_pins[1]:
        c = input('\nAccess granted! \nWould you like to d or w: ')
        if c == 'w':
          w = input('\nWithdraw how much: ')
          account_balances[1] -= int(w)
          if account_balances[1] < 0:
            print('\nInsufficient balance; cannot withdraw.')
          else:
            print(f'\nYour new balance is ${account_balances[1]}. \nTransaction complete!')
        elif c == 'd':
          d = input('\nDeposit how much: ')
          account_balances[1] += int(d)
          print(f'\nYour new balance is ${account_balances[1]}. \nTransaction complete!')
        else:
          print('\nError!')
      elif pin == account_pins[2]:
        c = input('\nAccess granted! \nWould you like to d or w: ')
        if c == 'w':
          w = input('\nWithdraw how much: ')
          account_balances[2] -= int(w)
          if account_balances[2] < 0:
            print('\nInsufficient balance; cannot withdraw.')
          else:
            print(f'\nYour new balance is ${account_balances[2]}. \nTransaction complete!')
        elif c == 'd':
          d = input('\nDeposit how much: ')
          account_balances[2] += int(d)
          print(f'\nYour new balance is ${account_balances[2]}. \nTransaction complete!')
        else:
          print('\nError!')
      elif pin == account_pins[3]:
        c = input('\nAccess granted! \nWould you like to d or w: ')
        if c == 'w':
          w = input('\nWithdraw how much: ')
          account_balances[3] -= int(w)
          if account_balances[3] < 0:
            print('\nInsufficient balance; cannot withdraw.')
          else:
            print(f'\nYour new balance is ${account_balances[3]}. \nTransaction complete!')
        elif c == 'd':
          d = input('\nDeposit how much: ')
          account_balances[3] += int(d)
          print(f'\nYour new balance is ${account_balances[3]}. \nTransaction complete!')
        else:
          print('\nError!')
      elif pin == account_pins[4]:
        c = input('\nAccess granted! \nWould you like to d or w: ')
        if c == 'w':
          w = input('withdraw how much: ')
          account_balances[4] -= int(w)
          if account_balances[4] < 0:
            print('Insufficient balance; cannot withdraw.')
          else:
            print(f'Your new balance is ${account_balances[4]}. \nTransaction complete!')
        elif c == 'd':
          d = input('Deposit how much: ')
          account_balances[4] += int(d)
          print(f'Your new balance is ${account_balances[4]}. \nTransaction complete!')
        else:
          print('Error!')
      elif pin.upper() == 'EXIT':
          print('\nGoodbye!')
      else:
          print('\nAccess denied: Pin not recognized!')


main()
def main():
	print('Welcome to Python Blackjack!')
	start = input('Do you want to play? ')

	if start == 'yes':
		def ask_hit_or_stand():
			choice = ''
			while choice != 'hit' and choice != 'stand':
				choice = input('Hit or stand? ')

			return choice == 'hit'
			

		def is_a_bust(score):
			return score > 21


		import random
		def draw_card():
			card_int = random.randint(1, 13)

			card = ''
			if card_int == 1:
				card = 'A'
			elif card_int == 11:
				card = 'J'
			elif card_int == 12:
				card = 'Q'
			elif card_int == 13:
				card = 'K'
			else:
				card = str(card_int)

			return card


		def score_card_low(card):
			card_score = 0

			if card == 'J' or card == 'Q' or card == 'K':
				card_score = 10
			elif card == 'A':
				card_score = 1
			else:
				card_score = int(card)
			
			return card_score


		def score_card_high(card):
			card_score = 0

			if card == 'J' or card == 'Q' or card == 'K':
				card_score = 10
			elif card == 'A':
				card_score = 11
			else:
				card_score = int(card)
			
			return card_score


		def score_hand(cards):
			score = 0 
			num_aces = cards.count('A')
			possible_scores = []
			for num_high in range(0, num_aces + 1):
				high_aces_left = num_high
				possible_score = 0
				for card in cards:
					if card == 'A' and high_aces_left > 0:
						possible_score += score_card_high(card)
						high_aces_left -= 1
					else:
						possible_score += score_card_low(card)
				possible_scores.append(possible_score)
			best_so_far = possible_scores[0]
			for score in possible_scores:
				if score > best_so_far and not is_a_bust(score):
					best_so_far = score
			return best_so_far


		def play_blackjack():
			player_name = input('Enter a name: ')
			dealer_name = 'Fly Dragon'
			player_hand = []

			player_hand.append(draw_card())
			player_hand.append(draw_card())

			print(f'{player_name}\'s hand: {player_hand}')
		
			while len(player_hand) < 5 and ask_hit_or_stand():
				player_hand.append(draw_card())
				print(f'{player_name}\'s hand: {player_hand}')

			player_score = score_hand(player_hand)

			if is_a_bust(player_score):
				print(f'Score: {player_score} Busted \nYou lose :(')
				return False

			print(f'You scored: {player_score}')

			dealer_hand = []
			dealer_hand.append(draw_card())
			dealer_hand.append(draw_card())
			print(f'{dealer_name}\'s hand: {dealer_hand}')

			dealer_score = score_hand(dealer_hand)

			print(f'{dealer_name}\'s score: {dealer_score}')

			while dealer_score < 17 and len(dealer_hand) < 5:
				print(f'{dealer_name} is taking a hit')
				dealer_hand.append(draw_card())
				dealer_score = score_hand(dealer_hand)

			print(f'{dealer_name}\'s ending hand {dealer_hand}')
			print(f'{dealer_name}\'s final score: {dealer_score}')

			if is_a_bust(dealer_score):
				print(f'{dealer_name}\'s busted: You WIN!')
				return True
			elif dealer_score >= player_score:
				print('You lose :(')
				return False
			else:
				print('You WIN!!')
				return True

		play_blackjack()


	else:
		print('Goodbye')


main()
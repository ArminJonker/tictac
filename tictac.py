from os import system
from random import randint

print('Welcome to TicTacTow')

rand = input('Do you want to randomize who begins (y/n): ').lower()
rsym = True

while rsym:
	if rand == 'y':
		symbol = randint(1,10)
		rsym = False
	elif rand =='n':
		symbol = 2
		rsym = False
	else:
		if not(rand in ('y','n')):
			print('Plz only enter y(yes) or n(no)')
			rand = input('Do you want to randomize who begins (y/n): ').lower()
			rsym = True
            


test = True
test1 = True
win = True


    

def testifwork(test,player1 = 'A',player2 = 'b'):
	while test:
		if player1 == 'X' or player1== 'O':
			if player2 == 'X':
				player1 = 'O'
			else:
				player1 = 'X'
			test = False
			break
		else:
			player1 = (input('Player1: What symbol would you like to use(X/O): ')).upper()
			if player1 == 'X' or player1== 'O':
				test = False
				break
			else:
				test = True
                



def testifwork2(test1,player2 = 'A',player1 = 'b'):
	while test1:
			if player2 == 'X' or player2== 'O':
				if player2 == 'X':
					player1 = 'O'
				else:
					player1 = 'X'
				test1 = False
				break
			else:
				player2 = (input('Player2: What symbol would you like to use(X/O): ')).upper()
				if player2 == 'X' or player2== 'O':
					test1 = False
					break
				else:
					test1 = True




board_display = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']


#how does this github work


if symbol == 2 or symbol%2 == 0:
	player1 = (input('Player1: What symbol would you like to use(X/O): ')).upper()
	print()
	testifwork(test,player1)
else:
	player2 = (input('Player2: What symbol would you like to use(X/O): ')).upper()
	print()
	testifwork2(test1,player2)


value = True

count = 0
while win:
	if symbol == 2 or symbol%2 == 0:
		print()
		position = int(input('Where would you like to play player1: '))
		print()
		
		if board_display[position] == 'O' or board_display[position] == 'X':
			print()
			print('Someone already played on that spot. Plz pick another spot.')
			print()
		else:
			board_display[position] = 'X'
			print(board_display[7]+'|'+board_display[8]+'|'+board_display[9])
			print('-----')
			print(board_display[4]+'|'+board_display[5]+'|'+board_display[6])
			print('-----')
			print(board_display[1]+'|'+board_display[2]+'|'+board_display[3])
			count += 1
			symbol += 1
			if board_display[1] == 'X' and board_display[4] == 'X' and board_display[7] == 'X':
				value = True
				while value:
					print()
					print('Well Done Player 1 is the winner !!!!!')
					replay = input('Would you like to play again (y/n) ?').lower()
					if replay == 'y':
						board_display = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
						win = True
						value = False
					elif replay == 'n':
						win = False
						value = False
						break
					else:
						print('Plz only enter y(yes) or n(no)')
						replay = input('Would you like to play again (y/n) ?').lower()
						value = True
			elif board_display[1] == 'X' and board_display[2] == 'X' and board_display[3] == 'X':
				value = True
				while value:
					print()
					print('Well Done Player 1 is the winner !!!!!')
					replay = input('Would you like to play again (y/n) ?').lower()
					if replay == 'y':
						board_display = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
						win = True
						value = False
					elif replay == 'n':
						win = False
						value = False
						break
					else:
						print('Plz only enter y(yes) or n(no)')
						replay = input('Would you like to play again (y/n) ?').lower()
						value = True
			elif board_display[1] == 'X' and board_display[5] == 'X' and board_display[9] == 'X':
				value = True
				while value:
					print()
					print('Well Done Player 1 is the winner !!!!!')
					replay = input('Would you like to play again (y/n) ?').lower()
					if replay == 'y':
						board_display = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
						win = True
						value = False
					elif replay == 'n':
						win = False
						value = False
						break
					else:
						print('Plz only enter y(yes) or n(no)')
						replay = input('Would you like to play again (y/n) ?').lower()
						value = True
			elif board_display[2] == 'X' and board_display[5] == 'X' and board_display[8] == 'X':
				value = True
				while value:
					print()
					print('Well Done Player 1 is the winner !!!!!')
					replay = input('Would you like to play again (y/n) ?').lower()
					if replay == 'y':
						board_display = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
						win = True
						value = False
					elif replay == 'n':
						win = False
						value = False
						break
					else:
						print('Plz only enter y(yes) or n(no)')
						replay = input('Would you like to play again (y/n) ?').lower()
						value = True
			elif board_display[3] == 'X' and board_display[6] == 'X' and board_display[9] == 'X':
				value = True
				while value:
					print()
					print('Well Done Player 1 is the winner !!!!!')
					replay = input('Would you like to play again (y/n) ?').lower()
					if replay == 'y':
						board_display = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
						win = True
						value = False
					elif replay == 'n':
						win = False
						value = False
						break
					else:
						print('Plz only enter y(yes) or n(no)')
						replay = input('Would you like to play again (y/n) ?').lower()
						value = True
			elif board_display[3] == 'X' and board_display[5] == 'X' and board_display[7] == 'X':
				value = True
				while value:
					print()
					print('Well Done Player 1 is the winner !!!!!')
					replay = input('Would you like to play again (y/n) ?').lower()
					if replay == 'y':
						board_display = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
						win = True
						value = False
					elif replay == 'n':
						win = False
						value = False
						break
					else:
						print('Plz only enter y(yes) or n(no)')
						replay = input('Would you like to play again (y/n) ?').lower()
						value = True
						board_display = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
			elif board_display[6] == 'X' and board_display[5] == 'X' and board_display[4] == 'X':
				value = True
				while value:
					print()
					print('Well Done Player 1 is the winner !!!!!')
					replay = input('Would you like to play again (y/n) ?').lower()
					if replay == 'y':
						board_display = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
						win = True
						value = False
					elif replay == 'n':
						win = False
						value = False
						break
					else:
						print('Plz only enter y(yes) or n(no)')
						replay = input('Would you like to play again (y/n) ?').lower()
						value = True
			elif board_display[9] == 'X' and board_display[8] == 'X' and board_display[7] == 'X':
				value = True
				while value:
					print()
					print('Well Done Player 1 is the winner !!!!!')
					replay = input('Would you like to play again (y/n) ?').lower()
					if replay == 'y':
						board_display = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
						win = True
						value = False
					elif replay == 'n':
						win = False
						value = False
						break
					else:
						print('Plz only enter y(yes) or n(no)')
						replay = input('Would you like to play again (y/n) ?').lower()
						value = True
	else:
		print()
		position = int(input('Where would you like to play player2: '))
		print()
		if board_display[position] == 'O' or board_display[position] == 'X':
			print()
			print('Someone already played on that spot. Plz pick another spot.')
			print()
		else:
			board_display[position] = 'O'
			print(board_display[7]+'|'+board_display[8]+'|'+board_display[9])
			print('-----')
			print(board_display[4]+'|'+board_display[5]+'|'+board_display[6])
			print('-----')
			print(board_display[1]+'|'+board_display[2]+'|'+board_display[3])
			count += 1
			symbol += 1
			if board_display[1] == 'O' and board_display[4] == 'O' and board_display[7] == 'O':
				value = True
				while value:
					print()
					print('Well Done Player 2 is the winner !!!!!')
					replay = input('Would you like to play again (y/n) ?').lower()
					if replay == 'y':
						board_display = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
						win = True
						value = False
					elif replay == 'n':
						win = False
						value = False
						break
					else:
						print('Plz only enter y(yes) or n(no)')
						replay = input('Would you like to play again (y/n) ?').lower()
						value = True
			elif board_display[1] == 'O' and board_display[2] == 'O' and board_display[3] == 'O':
				value = True
				while value:
					print()
					print('Well Done Player 2 is the winner !!!!!')
					replay = input('Would you like to play again (y/n) ?').lower()
					if replay == 'y':
						board_display = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
						win = True
						value = False
					elif replay == 'n':
						win = False
						value = False
						break
					else:
						print('Plz only enter y(yes) or n(no)')
						replay = input('Would you like to play again (y/n) ?').lower()
						value = True
			elif board_display[1] == 'O' and board_display[5] == 'O' and board_display[9] == 'O':
				value = True
				while value:
					print()
					print('Well Done Player 2 is the winner !!!!!')
					replay = input('Would you like to play again (y/n) ?').lower()
					if replay == 'y':
						board_display = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
						win = True
						value = False
					elif replay == 'n':
						win = False
						value = False
						break
					else:
						print('Plz only enter y(yes) or n(no)')
						replay = input('Would you like to play again (y/n) ?').lower()
						value = True
			elif board_display[2] == 'O' and board_display[5] == 'O' and board_display[8] == 'O':
				value = True
				while value:
					print()
					print('Well Done Player 2 is the winner !!!!!')
					replay = input('Would you like to play again (y/n) ?').lower()
					if replay == 'y':
						board_display = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
						win = True
						value = False
					elif replay == 'n':
						win = False
						value = False
						break
					else:
						print('Plz only enter y(yes) or n(no)')
						replay = input('Would you like to play again (y/n) ?').lower()
						value = True
			elif board_display[3] == 'O' and board_display[6] == 'O' and board_display[9] == 'O':
				value = True
				while value:
					print()
					print('Well Done Player 2 is the winner !!!!!')
					replay = input('Would you like to play again (y/n) ?').lower()
					if replay == 'y':
						board_display = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
						win = True
						value = False
					elif replay == 'n':
						win = False
						value = False
						break
					else:
						print('Plz only enter y(yes) or n(no)')
						replay = input('Would you like to play again (y/n) ?').lower()
						value = True
			elif board_display[3] == 'O' and board_display[5] == 'O' and board_display[7] == 'O':
				value = True
				while value:
					print()
					print('Well Done Player 2 is the winner !!!!!')
					replay = input('Would you like to play again (y/n) ?').lower()
					if replay == 'y':
						board_display = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
						win = True
						value = False
					elif replay == 'n':
						win = False
						value = False
						break
					else:
						print('Plz only enter y(yes) or n(no)')
						replay = input('Would you like to play again (y/n) ?').lower()
						value = True
			elif board_display[6] == 'O' and board_display[5] == 'O' and board_display[4] == 'O':
				value = True
				while value:
					print()
					print('Well Done Player 2 is the winner !!!!!')
					replay = input('Would you like to play again (y/n) ?').lower()
					if replay == 'y':
						board_display = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
						win = True
						value = False
					elif replay == 'n':
						win = False
						value = False
						break
					else:
						print('Plz only enter y(yes) or n(no)')
						replay = input('Would you like to play again (y/n) ?').lower()
						value = True
			elif board_display[9] == 'O' and board_display[8] == 'O' and board_display[7] == 'O':
				value = True
				while value:
					print()
					print('Well Done Player 2 is the winner !!!!!')
					replay = input('Would you like to play again (y/n) ?').lower()
					if replay == 'y':
						board_display = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
						win = True
						value = False
					elif replay == 'n':
						win = False
						value = False
						break
					else:
						print('Plz only enter y(yes) or n(no)')
						replay = input('Would you like to play again (y/n) ?').lower()
						value = True









	








	
	



	

	





from utils import Token, read_file

letters = 'abcdefghijklmnopqrstuvwxyz'
digits = '1234567890'

variables = letters + letters.upper() + digits


def analyze():
	lines = read_file()

	for line in lines:
		prev_token = None
		for char in line:
			if char in variables:
				if char in digits:
					if not prev_token:
						prev_token = Token('NUM', char, 2)
					else:
						prev_token.lexema += str(char)
				else:
					if not prev_token:
						prev_token = Token('VAR', char, 1)
					else:
						prev_token.lexema += str(char)
			else:
				if char == ':':
					if prev_token:
						print(prev_token)
						prev_token = None
					prev_token = Token('ASSIGNOP', char, 12)
				elif char == '=':
					if prev_token:
						prev_token.lexema += str(char)
						print(prev_token)
						prev_token = None
					else:
						prev_token = Token('EQOP', char, 11)
				else:
					if prev_token:
						print(prev_token)
						prev_token = None
					if char == '(':
						print(Token('LPAR', char, 3))

					if char == ')':
						print(Token('RPAR', char, 4))
					
					if char == '+':
						print(Token('ADDOP', char, 5))
					
					if char == '-':
						print(Token('SUBOP', char, 6))
					
					if char == '*':
						print(Token('MULOP', char, 7))

					if char == '/':
						print(Token('DIVOP', char, 8))

					if char == '>':
						print(Token('LTOP', char, 9))

					if char == '<':
						print(Token('STOP', char, 10))
		if prev_token:
			print(prev_token)
			prev_token = None

analyze()

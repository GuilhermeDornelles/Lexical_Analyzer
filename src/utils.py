
def read_file():
	with open('input.txt') as file:
		lines = file.readlines()
	return lines

class Token:

	def __init__(self, token, lexema, id):
		self.token = token
		self.lexema = lexema
		self.id = id

	def __repr__(self):
		return f"('{self.token}', {self.lexema}, {self.id})"

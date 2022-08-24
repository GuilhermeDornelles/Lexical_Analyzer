class Token:
    def __init__(self, token, lexema, id):
        self.token = token
        self.lexema = lexema
        self.id = id
    
    def print(self):
        print("<{0}, {1}, {2}>".format(self.token, self.lexema, self.id))

class Lexycal_analyzer:
    def __init__(self, count_id=1):
        self.count_id = count_id

    def analyze(self):
        with open('input.txt') as file:
            lines = file.readlines()
        for line in lines:
            #Está considerando word como cada caractere, deve considerar word como cada palavra
            for word in line:
                tok = Token(str(word), word, self.count_id)
                tok.print()
                self.count_id = self.count_id + 1

analyzer = Lexycal_analyzer()

analyzer.analyze()
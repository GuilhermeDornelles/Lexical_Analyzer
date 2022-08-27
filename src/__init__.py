from ast import match_case


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
        words = []
        for line in lines:
            currWord = ""
            for char in line:
                if char not in " ":
                    match char:
                        case "(":
                            words.append(char)
                        case ")":
                            words.append(char)
                        case "+":
                            words.append(char)
                        case "-":
                            words.append(char)
                        case "*":
                            words.append(char)
                        case "/":
                            words.append(char)
                        case _:
                            currWord += char
                elif currWord not in "":
                    words.append(currWord)
                    currWord = ""
            words.append(currWord.replace("\n", ""))
        return words


            #Está considerando word como cada caractere, deve considerar word como cada palavra
                # tok = Token(str(word), word, self.count_id)
                # tok.print()
                # self.count_id = self.count_id + 1



def main():
    analyzer = Lexycal_analyzer()
    
    print(analyzer.analyze())



if __name__ == "__main__":
    main()
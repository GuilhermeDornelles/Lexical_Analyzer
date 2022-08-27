from utils import Token


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
    def makeTokens(self, words):
        tokens = []
        for i, word in enumerate(words):
            if str(word).isdigit():
                token = Token(str(word), "NUM", 1)
                tokens.append(token)
            else:
                match word:
                    case "(":
                        token = Token(str(word), "LPAR", 3)
                        tokens.append(token)
                    case ")":
                        token = Token(str(word), "RPAR", 4)
                        tokens.append(token)
                    case "+":
                        token = Token(str(word), "ADDOP", 5)
                        tokens.append(token)
                    case "-":
                        token = Token(str(word), "SUBOP", 6)
                        tokens.append(token)
                    case "*":
                        token = Token(str(word), "MULOP", 7)
                        tokens.append(token)
                    case "/":
                        token = Token(str(word), "DIVOP", 8)
                        tokens.append(token)
                    case "==":
                        token = Token(str(word), "EQOP", 9)
                        tokens.append(token)
                    case ":=":
                        token = Token(str(word), "ASSIGNOP", 10)
                        tokens.append(token)                        
                    case _:
                        token = Token(str(word), "VAR", 2)
                        tokens.append(token)

        return tokens

    def print_tokens(self, tokens):
        result = "["
        for token in tokens:
            result+= token.__str__() + "\n"
        result+="]"
        return result

def main():
    analyzer = Lexycal_analyzer()
    words = analyzer.analyze()
    tokens = analyzer.makeTokens(words)
    print(analyzer.print_tokens(tokens))

if __name__ == "__main__":
    main()


from s_token import SToken as Token
from s_types import *

from errors import IllegalError

class Lexer:
    def __init__(self, text: str) -> None:
        self.text = text;
        self.pos: int = -1;
        self.current_char = None;
        self.advance(); 
        
    def advance(self):
        self.pos += 1;
        self.current_char = self.text[self.pos] if len(self.text) > self.pos else None;
    
    def create_numeric_token(self):
        num_str = ''
        dots_count = 0
        
        while self.current_char != None and self.current_char in NUMBERS + '.':
            if self.current_char == '.':
                if dots_count == 1:
                    break;
                
                dots_count += 1;
                num_str += '.'
            else:
                num_str += self.current_char
                
            self.advance()
        
        if dots_count == 0:
            return Token(TOKEN_INT, int(num_str))
        else:
            return Token(TOKEN_FLOAT, float(num_str))
        
    def tokenize(self):
        tokens = []
        
        while self.current_char != None:
            if self.current_char == '\t':
                self.advance()
                continue
            elif self.current_char == " ":
                self.advance()
                continue
            elif self.current_char == '+':
                tokens.append(Token(TOKEN_PLUS))
                self.advance()
                
                continue

            if self.current_char == '-':
                tokens.append(Token(TOKEN_MINUS))
                self.advance()
                
                continue

            if self.current_char == '/':
                tokens.append(Token(TOKEN_DIVIDE))
                self.advance()
                
                continue

            if self.current_char == "*":
                tokens.append(Token(TOKEN_MULTIPLY))
                self.advance()
                
                continue

            elif self.current_char == "(":
                tokens.append(Token(TOKEN_LEFTPAREN))
                self.advance()
                
                continue

            elif self.current_char == ")":
                tokens.append(Token(TOKEN_RIGHTPAREN))
                self.advance()
                
                continue

            elif self.current_char in NUMBERS:
                tokens.append(self.create_numeric_token())
                self.advance()
                
                continue

            else:
                ch = self.current_char
                self.advance()
                return [], IllegalError(f"\'{ch}\' at position {self.pos}")
        
        return tokens, None
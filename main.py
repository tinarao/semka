import sys
from lexer import Lexer
    
def main():
    if len(sys.argv) != 2:
        print("Вы не указали путь к .sm файлу!")
        return
    
    filepath = sys.argv[1]
    
    try:
        data = ""
        with open(filepath, "r") as file:
            data = file.read()
            
        lexer = Lexer(data)
        result, error = lexer.tokenize()
        if error:
            print(f"Error! {error}")
            return
        
        print(result) 
        return
        
    except FileNotFoundError:
        print("File does not exist!")
        return
    
if __name__ == "__main__":
    main();
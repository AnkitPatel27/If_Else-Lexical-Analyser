import re
from enum import Enum

class Keywords(Enum):
    IF = "if"
    ELSE = "else"
    THEN = "then"


def tokenize(statement):
    # Define regular expressions for the tokens
    patterns = [
        (r"[a-zA-Z]([a-zA-Z0-9]*)", 'IDENTIFIER'),  # Identifier (starts with a letter or underscore, followed by letters, digits, or underscores)
        (r"<=|>=|<>|<|>|=", 'RELOP'),  
        (r"([0-9]+)(\.[0-9]+)?(E[+-]?[0-9]+)?", 'NUMBER'),  # Identifier (starts with a letter or underscore, followed by letters, digits, or underscores)
    ]
    
    tokens = []
    
    while statement:
        for pattern, token_type in patterns:
            match = re.match(pattern, statement)
            if match:
                token = match.group(0)
                if token_type == 'IDENTIFIER':
                    # Check if the token is a keyword
                    if token in [keyword.value for keyword in Keywords]:
                        token_type = 'KEYWORD'
                    else:
                        token_type = 'IDENTIFIER'

                tokens.append((token, token_type))
                statement = statement[match.end():].lstrip()
                break
        else:
            # If no token matches, raise an error for invalid input
            raise ValueError(f"Invalid token in the statement: {statement}")
    
    return tokens

if __name__ == "__main__":
    # Test the lexical analyzer
    statement = input("Enter a statement: ")
    tokens = tokenize(statement)
    print("Tokens:")
    for token, token_type in tokens:
        print(f"{token_type}: {token}")

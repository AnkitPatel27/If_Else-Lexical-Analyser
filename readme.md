# Lexical Analyzer for IF ELSE THEN

This project implements a simple lexical analyzer in Python to tokenize and categorize keywords in a given input statement. Specifically, the analyzer identifies and categorizes the keywords "IF," "ELSE," and "THEN" in the input statement.

## What is a Lexical Analyzer?

The lexical analyzer serves as the first step in the process of transforming the source code into a form that can be processed by the compiler or interpreter. A lexical analyzer, also known as a lexer or scanner, is an essential component of a compiler or interpreter. Its main task is to break down the input source code into smaller units called tokens.
 
## Types of TOKENS
 1. Identifiers
 2. Keyword 
 3. Relop
 4. Digit

## How to Use the Lexical Analyzer

python3 20cs01009_A2.py

## Code Explanation

### Libraries

1. `re` (regular expression) for pattern matching 
2. `Enum` for creating an enumeration class.


### Regular Expressions
1. `"[a-zA-Z]([a-zA-Z0-9]*)"` , IDENTIFIER / KEYWORD
2. `"<=|>=|<>|<|>|="` , RELOP     
3. `"([0-9]+)(\.[0-9]+)?(E[+-]?[0-9]+)?"` , DIGIT

### How Code Works
1. After taking the input string which needs to be analysed it is passed to function `tokenize`
2. `tokenize` define the above three regular expression in an array and uses a `re.match()` function to match the start of the string with each regex one by one if it matches anyone one of the regex it pushes the part of the string to `token[]` which containes tuple of `(token,token_type)` 
3. regex of `IDENTIFIER & KEYWORD` are same so how do we know if the token is Identifier or Keyword for this we have created a ENUM which contains all the possible Keyword if the token matches any ENUM value then it is `KEYWORD` , `IDENTIFIER` if other  


## Main Functions of `re` Library

The `re` library in Python provides support for working with regular expressions. In this code, we use the `re.match` function to attempt matching patterns at the beginning of a string. If a match is found, we retrieve the matched portion using the `match.group(0)` function.

## Example
```
python3 20cs01009_Ankit.py
Enter a statement: if input<10 then output1=100 else output2>=100
Tokens:
KEYWORD: if
IDENTIFIER: input
RELOP: <
NUMBER: 10
KEYWORD: then
IDENTIFIER: output1
RELOP: =
NUMBER: 100
KEYWORD: else
IDENTIFIER: output2
RELOP: >=
NUMBER: 100```
#!/usr/bin/env python3
'''
- Design of a lexical analyzer
- Author: https://github.com/otaviocesar
- Author: https://github.com/otaviobelfort

'''
import JackTokenizer

def main():
    # Chamando o arquivo main.jack e imprimindo os tokens enumerados.  
    with open('main.jack', 'r') as f:
        TEST_LINES = f.readlines()
    TOKENIZER = JackTokenizer.JackTockenizer(TEST_LINES)
    for i, token in enumerate(TOKENIZER.tokens):
        print(i, token)
        print(JackTokenizer.JackTockenizer.token_type(token))
        
    print('-----------------')


if __name__ == '__main__':
    main()
        
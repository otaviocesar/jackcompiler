# Implementação de um Compilador

## Como rodar esse Projeto?
Parte I - Analisador Léxico:

	1. cd /lexical-analyzer
	2. No terminal rodar o comando: Python JackCompiler.py

Parte II - Analisador Sintático:

	1. cd /parser
	2. No terminal rodar o comando: Python JackCompiler.py

Parte III - Gerador de Código Intermediário:

	1. cd /code-generator
	2. No terminal rodar o comando: Python JackCompiler.py

Parte IV - Gerador de Código Intermediário:

	1. cd /translator
	2. No terminal rodar o comando: python main.py BasicTest.vm

## Etapas

	1. Desenvolvimento do analisador léxico
	2. Projeto do analisador léxico e sintático
	3. Desenvolvimento do analisador sintático 
    4. Projeto do gerador de código intermediário 
	5. Desenvolvimento do gerador de código intermediário
    6. Projeto do tradutor - Parte1 
    7. Projeto do tradutor - Parte2
	

## Analisador Léxico
### Especificação da microsintaxe
-------------------
* Palavras reservadas: 

	* 'class' | 'constructor' | 'function' | 'method' | 'field' | 'static' | 'var' | 'int' | 'char' | 'boolean' | 'void' | 'true' | 'false' | 'null' | 'this' | 'let' |  do' | 'if' | 'else' | 'while' | 'return’

- Símbolos: 
	* '{' | '}' | '(' | ')' | '[' | ']' | '. ' | ', ' | '; ' | '+' | '-' | '*' | '/' | '&' | '|' | '<' | '>' | '=' | '~'

- Inteiros: um número decimal inteiro
- Strings: "uma sequência de caracteres Unicode entre aspas dupla"
- Identificadores: uma sequência de letras, digitos e *undescore* ( '_' ) não iniciando com um dígito.

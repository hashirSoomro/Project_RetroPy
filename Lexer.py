import re

# Define token types
TOK_TYP = {
    'DATATYPE':['int','float','bool','str','char','byte','list','tuple','dict'],# int a= | public int a= 
    'GLOBAL':['global','nonlocal','del'], # global i, del i,nonlocal i |global(i),del(i),nonlocal(i)
    'DEFINE':['def','class'], # def sum():,class sum(): | def sum(a,b): , class sum(a,b):
    'VALUE':['True','False','None'], # = True
    'LAMBDA':['lambda'], # lambda a, b, c : a + b + c
    'ACCESSMODIFIER':['public','private','protected','internal'],# public string a='hey'
    'FOR':['for'], #for x in fruits:|for x in range(0,2):
    'IF':['if','elif','while'], # if(x>6): , while(a>6): | if x>6: , while a>6:
    'EXCEPTIONHANDLING':['try','else','finally'],# try: ,else: ,finally:
    'EXCEPT':['except'], # except: | except Exception:
    'RAISE':['raise'], # raise TypeError("Only integers are allowed")
    'ASSERT':['assert'],# assert x == "goodbye", "x should be 'hello'"
    'SKIP':['break','continue','pass'], # break|continue|pass
    'AS':['as'],# import calendar as c | with open('geek.txt') as geek:
    'WITH':['with'], #with open('geek.txt') as geek:
    'RETURN':['return','yield'], # return even_nums, yield i | return [num for num in numbers if not num % 2]
    'ASYNC':['async'],# async def main():
    'AWAIT':['await'],# await asyncio.gather(count(), count(), count())
    'IMPORT':['import','from'],# import datetime | from datetime import time
    'IDENTIFIER': r'[a-zA-Z_][a-zA-Z0-9_]*', 
    'INTEGER_LITERAL': r'\d+',
    'FLOAT_LITERAL': r'\d+\.\d+',
    'STRING_LITERAL': r'\".*?\"|\'.*?\'',
    'EXPONENT': ['^'],
    'ADD_SUB': ['+','-'],
    'MUL_DIV':['*','/','//','%'],
    'ASSIGN_OPERATOR':['=','+=','-=','*=','/=','%=','^='],
    'REL_OPERATOR':['==','!=','<','>','<=','>='],
    'AND':['and'],
    'OR':['or'],
    'NOT':['not'],
    'IN':['in'],
    'IS':['is'],    
    '(':['('],
    ')':[')'],
    '[':['['],
    ']':[']'],
    '{':['{'],
    '}':['}'],
    ',':[','],
    '.':['.'],
    ':':[':'],
    ';':[';'],
    '"':['"'],
    "'":["'"],
    '$':['$'],
    '!':['!'],
    'COMMENT':['#'],
    'WHITE_SPACE': [' ','  ','   '],
    'ESC_SEQ':['\n','\t']
}

def tokenizer(words):
    tokens=[]
    line_no = 1
    print("Class Part Value Part Line Number")
    for i in range(len(words)):
        if words[i] in TOK_TYP['DATATYPE']:
            tok=['DATATYPE',words[i],line_no]
            tokens.append(tok)
            #print(tokens,i)
            i=i+1
            
        elif words[i] in TOK_TYP['GLOBAL']:
            tok=['GLOBAL',words[i],line_no]
            tokens.append(tok)
            #print(tokens,i)
            i=i+1

        elif words[i] in TOK_TYP['DEFINE']:
            tok=['DEFINE',words[i],line_no]
            tokens.append(tok)
            #print(tokens,i)
            i=i+1

        elif words[i] in TOK_TYP['VALUE']:
            tok=['VALUE',words[i],line_no]
            tokens.append(tok)
            #print(tokens,i)
            i=i+1

        elif words[i] in TOK_TYP['LAMBDA']:
            tok=['LAMBDA',words[i],line_no]
            tokens.append(tok)
            #print(tokens,i)
            i=i+1
            
        elif words[i] in TOK_TYP['ACCESSMODIFIER']:
            tok=['ACCESSMODIFIER',words[i],line_no]
            tokens.append(tok)
            #print(tokens,i)
            i=i+1

        elif words[i] in TOK_TYP['FOR']:
            tok=['FOR',words[i],line_no]
            tokens.append(tok)
            #print(tokens,i)
            i=i+1

        elif words[i] in TOK_TYP['IF']:
            tok=['IF',words[i],line_no]
            tokens.append(tok)
            #print(tokens,i)
            i=i+1

        elif words[i] in TOK_TYP['EXCEPTIONHANDLING']:
            tok=['EXCEPTIONHANDLING',words[i],line_no]
            tokens.append(tok)
            #print(tokens,i)
            i=i+1

        elif words[i] in TOK_TYP['EXCEPT']:
            tok=['EXCEPT',words[i],line_no]
            tokens.append(tok)
            #print(tokens,i)
            i=i+1

        elif words[i] in TOK_TYP['RAISE']:
            tok=['RAISE',words[i],line_no]
            tokens.append(tok)
            #print(tokens,i)
            i=i+1

        elif words[i] in TOK_TYP['ASSERT']:
            tok=['ASSERT',words[i],line_no]
            tokens.append(tok)
            #print(tokens,i)
            i=i+1

        elif words[i] in TOK_TYP['SKIP']:
            tok=['SKIP',words[i],line_no]
            tokens.append(tok)
            #print(tokens,i)
            i=i+1

        elif words[i] in TOK_TYP['AS']:
            tok=['AS',words[i],line_no]
            tokens.append(tok)
            #print(tokens,i)
            i=i+1

        elif words[i] in TOK_TYP['WITH']:
            tok=['WITH',words[i],line_no]
            tokens.append(tok)
            #print(tokens,i)
            i=i+1

        elif words[i] in TOK_TYP['RETURN']:
            tok=['RETURN',words[i],line_no]
            tokens.append(tok)
            #print(tokens,i)
            i=i+1

        elif words[i] in TOK_TYP['ASYNC']:
            tok=['ASYNC',words[i],line_no]
            tokens.append(tok)
            #print(tokens,i)
            i=i+1

        elif words[i] in TOK_TYP['AWAIT']:
            tok=['AWAIT',words[i],line_no]
            tokens.append(tok)
            #print(tokens,i)
            i=i+1

        elif words[i] in TOK_TYP['IMPORT']:
            tok=['IMPORT',words[i],line_no]
            tokens.append(tok)
            #print(tokens,i)
            i=i+1

        elif words[i] in TOK_TYP['EXPONENT']:
            tok=['EXPONENT',words[i],line_no]
            tokens.append(tok)
            #print(tokens,i)
            i=i+1

        elif words[i] in TOK_TYP['ADD_SUB']:
            tok=['ADD_SUB',words[i],line_no]
            tokens.append(tok)
            #print(tokens,i)
            i=i+1

        elif words[i] in TOK_TYP['MUL_DIV']:
            tok=['MUL_DIV',words[i],line_no]
            tokens.append(tok)
            #print(tokens,i)
            i=i+1

        elif words[i] in TOK_TYP['ASSIGN_OPERATOR']:
            tok=['ASSIGN_OPERATOR',words[i],line_no]
            tokens.append(tok)
            #print(tokens,i)
            i=i+1

        elif words[i] in TOK_TYP['REL_OPERATOR']:
            tok=['REL_OPERATOR',words[i],line_no]
            tokens.append(tok)
            #print(tokens,i)
            i=i+1

        elif words[i] in TOK_TYP['AND']:
            tok=['AND',words[i],line_no]
            tokens.append(tok)
            #print(tokens,i)
            i=i+1

        elif words[i] in TOK_TYP['OR']:
            tok=['OR',words[i],line_no]
            tokens.append(tok)
            #print(tokens,i)
            i=i+1

        elif words[i] in TOK_TYP['NOT']:
            tok=['IN',words[i],line_no]
            tokens.append(tok)
            #print(tokens,i)
            i=i+1

        elif words[i] in TOK_TYP['IS']:
            tok=['IS',words[i],line_no]
            tokens.append(tok)
            #print(tokens,i)
            i=i+1

        elif words[i] in TOK_TYP['(']:
            tok=['(',words[i],line_no]
            tokens.append(tok)
            #print(tokens,i)
            i=i+1

        elif words[i] in TOK_TYP[')']:
            tok=[')',words[i],line_no]
            tokens.append(tok)
            #print(tokens,i)
            i=i+1

        elif words[i] in TOK_TYP['[']:
            tok=['[',words[i],line_no]
            tokens.append(tok)
            #print(tokens,i)
            i=i+1

        elif words[i] in TOK_TYP[']']:
            tok=[']',words[i],line_no]
            tokens.append(tok)
            #print(tokens,i)
            i=i+1

        elif words[i] in TOK_TYP['{']:
            tok=['{',words[i],line_no]
            tokens.append(tok)
            #print(tokens,i)
            i=i+1

        elif words[i] in TOK_TYP['}']:
            tok=['}',words[i],line_no]
            tokens.append(tok)
            #print(tokens,i)
            i=i+1

        elif words[i] in TOK_TYP[',']:
            tok=[',',words[i],line_no]
            tokens.append(tok)
            #print(tokens,i)
            i=i+1

        elif words[i] in TOK_TYP['.']:
            tok=['.',words[i],line_no]
            tokens.append(tok)
            #print(tokens,i)
            i=i+1

        elif words[i] in TOK_TYP[':']:
            tok=[':',words[i],line_no]
            tokens.append(tok)
            #print(tokens,i)
            i=i+1
            
        elif words[i] in TOK_TYP[';']:
            tok=[';',words[i],line_no]
            tokens.append(tok)
            #print(tokens,i)
            i=i+1

        elif words[i][0]=='"':
            tok=['"',words[i],line_no]
            tokens.append(tok)
            #print(tokens,i)
            i=i+1

        elif words[i][0]=="'":
            tok=["'",words[i],line_no]
            tokens.append(tok)
            #print(tokens,i)
            i=i+1

        elif words[i] in TOK_TYP['$']:
            tok=['$',words[i],line_no]
            tokens.append(tok)
            #print(tokens,i)
            i=i+1

        elif words[i] in TOK_TYP['!']:
            tok=['!',words[i],line_no]
            tokens.append(tok)
            #print(tokens,i)
            i=i+1

        elif words[i] in TOK_TYP['COMMENT']:
            tok=['COMMENT',words[i],line_no]
            tokens.append(tok)
            #print(tokens,i)
            i=i+1
            
        elif words[i] in TOK_TYP['WHITE_SPACE']:
            tok=['WHITE_SPACE',words[i],line_no]
            tokens.append(tok)
            #print(tokens,i)
            i=i+1
            
        elif words[i] in TOK_TYP['ESC_SEQ']:
            if words[i]=='\n':
                tok=['ESC_SEQ',words[i],line_no]
                tokens.append(tok)
                #print(tokens,i)
                line_no=line_no+1
                i=i+1
            else:
                tok=['ESC_SEQ',words[i],line_no]
                tokens.append(tok)
                #print(tokens,i)
                i=i+1
        else:
            tok=['NORM',words[i],line_no]
            tokens.append(tok)
            #print(tokens,i)
            i=i+1

    return tokens

def word_splitter(source_code):
    words=[]
    
    punctuator=['...','_',',',';',':','!','$','?','(',')','[',']','.','{','}','"',"'"]
    double_op=['==','!=','<=','>=','+=','-=','*=','/=','%=','//']
    operator=['<','>','=','+','-','^','+','-','*','/','%']
    escape_seq=['\n','\t']
    comment=['#']
    white_space=['    ','   ','  ',' ']
    
    global i
    i=0
    lexem=""
    
    while(i<len(source_code)):
        if(source_code[i] in white_space):
            if(lexem==""):
                i=i+1
            else:
                words.append(lexem)
                lexem=""
                i=i+1
                #print(i,words,"white")
        
        elif (source_code[i] in operator):
            chk_str=source_code[i]+source_code[i+1]
            if(chk_str in double_op):
                if lexem=="":
                    words.append(chk_str)
                    i=i+2
                    #print(i,words,"doub_op")
                else:
                    words.append(lexem)
                    words.append(chk_str)
                    lexem=""
                    i=i+2
                    #print(i,words,"doub_op")
            else:
                if lexem=="":
                    words.append(source_code[i])
                    i=i+1
                    #print(i,words,"single_op")
                else:
                    words.append(lexem)
                    words.append(source_code[i])
                    lexem=""
                    i=i+1
                    #print(i,words,"single_op")
                
        elif (source_code[i] in punctuator) or (source_code[i] in escape_seq):
            if source_code[i]=='"': #0-9 while source_code[j]=='"': chk_str=source_code[j]+source_code[j+1] j=j+1

                j=i+1
                chk_str1=source_code[i]

                while (source_code[j]!='"'):
                    if (source_code[j] == '\n'):
                        break
                    #print('j=',j,'chk_str=',chk_str1)
                    chk_str1=chk_str1+source_code[j]
                    j=j+1
                if (source_code[j] == '\n'):
                    chk_str1=chk_str1+source_code[j]
                    i=j
                    chk_str1=chk_str1[:-1]
                    words.append(chk_str1)
                
                else:
                    chk_str1=chk_str1+source_code[j]
                    i=j+1
                    words.append(chk_str1)

            elif source_code[i]=="'": #0-9 while source_code[j]=='"': chk_str=source_code[j]+source_code[j+1] j=j+1

                j=i+1
                chk_str1=source_code[i]
                
                while (source_code[j]!="'"):
                    if (source_code[j] == '\n'):
                        break
                    #print('j=',j,'chk_str=',chk_str1)
                    chk_str1=chk_str1+source_code[j]
                    j=j+1
                    
                if (source_code[j] == '\n'):
                    chk_str1=chk_str1+source_code[j]
                    i=j
                    chk_str1=chk_str1[:-1]
                    words.append(chk_str1)
                
                else:
                    chk_str1=chk_str1+source_code[j]
                    i=j+1
                    words.append(chk_str1)
            
            elif lexem=="":
                words.append(source_code[i])
                i=i+1
            else:
                words.append(lexem)
                words.append(source_code[i])
                lexem=""
                i+=1
                #print(i,words,"pun_esc")
            
        elif(source_code[i] in comment):
            
            if lexem=="":
                j=i+1
                chk_str2=source_code[i]
                
                while(source_code[j] !='\n' ):
                    chk_str2=chk_str2+source_code[j]
                    j=j+1
                chk_str2=chk_str2+source_code[j]
                i=j
                chk_str2=chk_str2[:-1]
                words.append(chk_str2)
        
            else:
                words.append(lexem)
                lexem=""
                
                j=i+1
                chk_str2=source_code[i]
                
                while(source_code[j] !='\n' ):
                    chk_str2=chk_str2+source_code[j]
                    j=j+1
                chk_str2=chk_str2+source_code[j]
                i=j
                chk_str2=chk_str2[:-1]
                words.append(chk_str2)
                
        else:
            lexem+=source_code[i]
            i+=1
            #print(i,words,"norm")
    return words

    
source_code = """
int run = 50
if(run >= 50):
    print("King karlega, 'Bobsie the king' karlega!")
else:
    print('"Naaaaa!"
    ')
while(a>6):
    print("ye kia baat hui boss?")
for i in range(67):
    print("hey")
#bobsie the king
"""
print(source_code)
words=word_splitter(source_code)
tokenizer=tokenizer(words)
for token in tokenizer:
    print(token)
#print(words)
##for word in words:
##    print(word)

exit()



##import re
##
### Defining token types dictionary
##TOKEN_PATTERNS = {
##    1: r'(?P<DATATYPE>int|float|bool|double|str|char|byte|list|tuple|dict)',
##    2: r'(?P<GLOBAL>global|nonlocal|del)',
##    3: r'(?P<DEFINE>def|class)',
##    4: r'(?P<VALUE>True|False|None)',
##    5: r'(?P<LAMBDA>lambda)',
##    6: r'(?P<ACCESSMODIFIER>public|private|protected|internal)',
##    7: r'(?P<FOR>for)',
##    8: r'(?P<IF>if|elif|while)',
##    9: r'(?P<EXCEPTIONHANDLING>try|else|finally)',
##    10: r'(?P<EXCEPT>except)',
##    11: r'(?P<RAISE>raise)',
##    12: r'(?P<ASSERT>assert)',
##    13: r'(?P<SKIP>break|continue|pass)',
##    14: r'(?P<AS>as)',
##    15: r'(?P<WITH>with)',
##    16: r'(?P<RETURN>return|yield)',
##    17: r'(?P<ASYNC>async)',
##    18: r'(?P<AWAIT>await)',
##    19: r'(?P<IMPORT>import|from)',
##    20: r'(?P<IDENTIFIER>[a-zA-Z_][a-zA-Z0-9_]*)',
##    21: r'(?P<INTEGER_LITERAL>\d+)',
##    22: r'(?P<FLOAT_LITERAL>\d+\.\d+)',
##    23: r'(?P<STRING_LITERAL>\".*?\"|\'.*?\')',
##    24: r'(?P<EXPONENT>\^)',
##    25: r'(?P<ADD_SUB>\+|-)',
##    26: r'(?P<MUL_DIV>\*|/|\\|%)',
##    27: r'(?P<ASSIGN_OPERATOR>[+\-*/\\%]?=|\^=)',
##    28: r'(?P<REL_OPERATOR>==|!=|<|>|<=|>=)',
##    29: r'(?P<AND>and)',
##    30: r'(?P<OR>or)',
##    31: r'(?P<NOT>not)',
##    32: r'(?P<IN>in)',
##    33: r'(?P<IS>is)',
##    34: r'(?P<LPAREN>\()',
##    35: r'(?P<RPAREN>\))',
##    36: r'(?P<LSQUARE>\[)',
##    37: r'(?P<RSQUARE>\])',
##    38: r'(?P<LBRACE>\{)',
##    39: r'(?P<RBRACE>\})',
##    40: r'(?P<COMMA>,)',
##    41: r'(?P<DOT>\.)',
##    42: r'(?P<UNDERSCORE>_)',
##    43: r'(?P<ELLIPSIS>\.\.\.)',
##    44: r'(?P<COMMENT>#.*)',
##    45: r'(?P<WHITESPACE>\s+)',
##}
##
### Modify the order of patterns to prioritize longer patterns
##TOKEN_REGEX = '|'.join(sorted(TOKEN_PATTERNS.values(), key=lambda x: len(x), reverse=True))
##
### Tokenizing the source code
##def lexer(source_code):
##    tokens = []
##    line_number = 1
##
##    for match in re.finditer(TOKEN_REGEX, source_code, re.MULTILINE):
##        token_type = next((name for name, value in match.groupdict().items() if value is not None), None)
##        if token_type:
##            tokens.append((line_number, token_type, match.group(token_type)))
##
##        line_number += source_code[match.start():match.end()].count('\n')
##
##    return tokens
##
### Example input source code
##source_code = """
##int king_karlega = 50
##if(king_karlega>=50):
##    print("King karlega, Bobsie the king karlega!")
##else:
##    print("Naaaaa!")
##while(a>6):
##    print("ye kia baat hui boss?")
##for i in range(67):
##    print("hey")
###bobsie the king
##"""
##
##
##
### Tokenize the source code
##tokens = lexer(source_code)
##
### Print the tokens with line numbers
##for line_number, token_type, token_value in tokens:
##    print(f"Line {line_number}: Token: {token_type}, Value: {token_value}")
##
##
##exit()

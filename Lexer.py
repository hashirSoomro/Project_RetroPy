#importing re for creating regular expressions and importing pandas to create a dataframe for output
import re
import pandas as pd

# Defining token types
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
    'STRING_LITERAL': r'["\'].*?(?<!["\'])',
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

# defining tokenizer function by taking input words(an array) from word splitter
def tokenizer(words):
    #initializing tokens list for storing tokens and line_no for keeping the track of line
    tokens=[]
    line_no = 1

    #creating a loop to iterate over words array
    for i in range(len(words)):
        
        #checking every token word by word to fit it in a class
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

        elif words[i] in TOK_TYP['"']:
            tok=['"',words[i],line_no]
            tokens.append(tok)
            #print(tokens,i)
            i=i+1

        elif words[i] in TOK_TYP["'"]:
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

        elif words[i][0] in TOK_TYP['COMMENT']:
            tok=['COMMENT',words[i],line_no]
            tokens.append(tok)
            #print(tokens,i)
            i=i+1
            
        elif words[i] in TOK_TYP['WHITE_SPACE']:
            tok=['WHITE_SPACE',words[i],line_no]
            tokens.append(tok)
            #print(tokens,i)
            i=i+1
        
        # Handle IDENTIFIER
        elif re.match(TOK_TYP['IDENTIFIER'], words[i]):
            tokens.append(['IDENTIFIER', words[i], line_no])

        # Handle FLOAT_LITERAL
        elif re.match(TOK_TYP['FLOAT_LITERAL'], words[i]):
            tokens.append(['FLOAT_LITERAL', words[i], line_no])

        # Handle INTEGER_LITERAL
        elif re.match(TOK_TYP['INTEGER_LITERAL'], words[i]):
            tokens.append(['INTEGER_LITERAL', words[i], line_no])

        # Handle STRING_LITERAL
        elif re.match(TOK_TYP['STRING_LITERAL'], words[i]):
            tokens.append(['STRING_LITERAL', words[i], line_no])

            
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
            tok=['INVALID',words[i],line_no]
            tokens.append(tok)
            #print(tokens,i)
            i=i+1
    
    return tokens

# defining word_splitter function by taking input words(an array) from word splitter
def word_splitter(source_code):

    #initializing words array to split words from source_code 
    words=[]
    
    #defining punctuator,double operator, operator, escape sequence,comment and white space for word splitting
    punctuator=['...',',',';',':','!','$','?','(',')','[',']','.','{','}','"',"'"]
    double_op=['==','!=','<=','>=','+=','-=','*=','/=','%=','//']
    operator=['<','>','=','+','-','^','+','-','*','/','%']
    escape_seq=['\n','\t']
    comment=['#']
    white_space=[' ']

    #defining lexem for storing the character of words,and  global i so it value doesn't change throughout the loop in conditional statements 
    global i
    i=0
    lexem=""

    #creating a loop so we can iterate through source code
    while(i<len(source_code)):
        
        #in source code identifying different separators
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
            if source_code[i]=='.' and re.match(TOK_TYP['INTEGER_LITERAL'], source_code[i-1]) and re.match(TOK_TYP['INTEGER_LITERAL'], source_code[i+1]):
                j=i+1
                k=i-1
                float_str=source_code[i]
                while(re.match(TOK_TYP['INTEGER_LITERAL'], source_code[k])):
                    float_str=source_code[k]+float_str
                    k=k-1
                #print(float_str)
                while(re.match(TOK_TYP['INTEGER_LITERAL'], source_code[j])):
                    float_str=float_str+source_code[j]
                    j=j+1
                #print(float_str)
                i=j
                words.append(float_str)
                lexem=''
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
            A_B_C =6
            #print(i,words,"norm")
    return words

#example source code for our language
source_code = """
interface::A_B_C
while(a.b.c<<<<<==78.65
b+++=56.75ab7.11*/.56bcx.55.55.a5c
char c="abc++=\\"abc\\\*/"abc"a=b=c
string s='\\\'+'++'\n'+=35'\\
return a&&==@bc
"""
##int run = 50.23
##if(run >= 50):
##    print("King karlega, 'Bobsie the king' karlega!")
##else:
##    print('"Naaaaa!"
##    ')
##while(a>6):
##    print("ye kia baat hui boss?")
##for i in range(67):
##    print("hey")
###bobsie the king
#calling word_spliiter and tokenizer functions and creating+printing the dataframe
print(source_code)
words=word_splitter(source_code)
tokenizer=tokenizer(words)
pd.set_option('display.max_rows', None)
df=pd.DataFrame(tokenizer,columns=["Class Part","Value Part","Line No."])

print(df)
##for word in words:
#   print(word)


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

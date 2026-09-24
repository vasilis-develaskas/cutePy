# VASILEIOS DEVELASKAS
import sys

# All letters that CutePy accepts
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
           'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
           'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# All digits that CutePy accepts
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Keywords
keywords = ['#declare', 'if', 'else', 'while', 'return', 'print', 'def', 'and', 'or', 'input', 'int', 'not', '__name__',
            '__main__']

# Open file from terminal
file = sys.stdin
if len(sys.argv) != 2:
    print("Error!:Please provide a cpy file after the program name")

file = open(sys.argv[1], 'r')  # Opens .cpy file
keep_file_name = sys.argv[1].split(".").pop(0)  # Keeps file name same with the file name of the original programme

line = 1  # First line of file

# Transition Matrix Characters

whiteSpaceChar = 0
changeRow = 1
number = 2
letter = 3
plusSign = 4
minusSign = 5
multiplySign = 6
leftParenthesis = 7
rightParenthesis = 8
leftBracket = 9
rightBracket = 10
equalSign = 11
lessThanSign = 12
greaterThanSign = 13
backslash = 14
hashtag = 15
openBlock = 16
closeBlock = 17
dollarSign = 18
EOF = 19
unSupportedChar = 20
comma = 21
semiColon = 22
colon = 23
exclamationMark = 24
quotationMark = 25
underscore = 26

# Transition Matrix States

startState = 0
idkState = 1
digitState = 2
exclamationMarkState = 3
equalState = 4
lessThanState = 5
greaterThanState = 6
backslashState = 7
hashtagState = 8
remState = 9  # State of comments
closeHashtagState = 10

# Tokens

numberToken = 201
keywordToken = 202
plusToken = 203
minusToken = 204
multiplyToken = 205
leftParenthesisToken = 206
rightParenthesisToken = 207
leftBracketToken = 208
rightBracketToken = 209
equalToken = 210
lessThanToken = 211
greaterThanToken = 212
assignmentToken = 213
differToken = 214
lessOrEqualToken = 215
greaterOrEqualToken = 216
commaToken = 217
semiColonToken = 218
colonToken = 219
divideToken = 220
openBlockToken = 221
closeBlockToken = 222
quotesToken = 223
EOFToken = 224
declareToken = 225
ifToken = 226
elseToken = 227
whileToken = 228
returnToken = 229
printToken = 230
defToken = 231
andToken = 232
orToken = 233
inputToken = 234
intToken = 235
notToken = 236
nameToken = 237
mainToken = 238

token_dictionary = {'201': 'number', '202': 'id', '203': 'addOperator', '204': 'addOperator', '205': 'mulOperator',
                    '206': 'groupSymbol', '207': 'groupSymbol', '208': 'groupSymbol', '209': 'groupSymbol',
                    '210': 'relOperator', '211': 'relOperator', '212': 'relOperator', '213': 'assignment',
                    '214': 'relOperator', '215': 'relOperator', '216': 'relOperator', '217': 'delimiter',
                    '218': 'delimiter', '219': 'delimiter', '220': 'mulOperator', '221': 'groupSymbol',
                    '222': 'groupSymbol', '223': 'delimiter', '224': 'EOF', '225': 'keyword', '226': 'keyword',
                    '227': 'keyword', '228': 'keyword', '229': 'keyword', '230': 'keyword', '231': 'keyword',
                    '232': 'keyword', '233': 'keyword', '234': 'keyword', '235': 'keyword', '236': 'keyword',
                    '237': 'keyword', '238': 'keyword'}

# Errors

errorUnsupportedSymbol = 400
errorAfterExclamationMark = 401
errorAfterSlash = 402
errorOver30Chars = 403
errorOpenBlock = 404
errorCloseBlock = 405
errorDollarSign = 406
errorLetterAfterNumber = 407
errorCommentsEOF = 408
errorHashtag = 409
errorUnderscore = 410
errorNumber = 411

# Transition Matrix
# Its element of the transition matrix is referred to a transition matrix state in the same order as they are defined

transitionMatrix = [

    [startState, startState, digitState, idkState, plusToken, minusToken, multiplyToken, leftParenthesisToken,
     rightParenthesisToken, leftBracketToken, rightBracketToken, equalState, lessThanState, greaterThanState,
     backslashState, hashtagState, errorOpenBlock, errorCloseBlock, errorDollarSign, EOFToken, errorUnsupportedSymbol,
     commaToken, semiColonToken, colonToken, exclamationMarkState, quotesToken, idkState],

    [keywordToken, keywordToken, idkState, idkState, keywordToken, keywordToken, keywordToken, keywordToken,
     keywordToken,
     keywordToken, keywordToken, keywordToken, keywordToken, keywordToken, keywordToken, keywordToken, keywordToken,
     keywordToken, keywordToken, keywordToken, errorUnsupportedSymbol, keywordToken, keywordToken, keywordToken,
     keywordToken, keywordToken, idkState],

    [numberToken, numberToken, digitState, errorLetterAfterNumber, numberToken, numberToken, numberToken, numberToken,
     numberToken, numberToken, numberToken, numberToken, numberToken, numberToken, numberToken, numberToken,
     numberToken,
     numberToken, numberToken, numberToken, errorUnsupportedSymbol, numberToken, numberToken, numberToken, numberToken,
     numberToken, numberToken],

    [errorAfterExclamationMark, errorAfterExclamationMark, errorAfterExclamationMark, errorAfterExclamationMark,
     errorAfterExclamationMark, errorAfterExclamationMark, errorAfterExclamationMark,
     errorAfterExclamationMark, errorAfterExclamationMark, errorAfterExclamationMark, errorAfterExclamationMark,
     differToken, errorAfterExclamationMark, errorAfterExclamationMark, errorAfterExclamationMark,
     errorAfterExclamationMark, errorAfterExclamationMark, errorAfterExclamationMark, errorAfterExclamationMark,
     errorAfterExclamationMark, errorUnsupportedSymbol, errorAfterExclamationMark, errorAfterExclamationMark,
     errorAfterExclamationMark, errorAfterExclamationMark, errorAfterExclamationMark, errorAfterExclamationMark],

    [assignmentToken, assignmentToken, assignmentToken, assignmentToken, assignmentToken, assignmentToken,
     assignmentToken,
     assignmentToken, assignmentToken, assignmentToken, assignmentToken, equalToken, assignmentToken, assignmentToken,
     assignmentToken, assignmentToken, assignmentToken, assignmentToken, assignmentToken, assignmentToken,
     errorUnsupportedSymbol, assignmentToken, assignmentToken, assignmentToken, assignmentToken, assignmentToken,
     assignmentToken],

    [lessThanToken, lessThanToken, lessThanToken, lessThanToken, lessThanToken, lessThanToken, lessThanToken,
     lessThanToken, lessThanToken, lessThanToken, lessThanToken, lessOrEqualToken, lessThanToken, lessThanToken,
     lessThanToken, lessThanToken, lessThanToken, lessThanToken, lessThanToken, lessThanToken, errorUnsupportedSymbol,
     lessThanToken, lessThanToken, lessThanToken, lessThanToken, lessThanToken, lessThanToken],

    [greaterThanToken, greaterThanToken, greaterThanToken, greaterThanToken, greaterThanToken, greaterThanToken,
     greaterThanToken, greaterThanToken, greaterThanToken, greaterThanToken, greaterThanToken, greaterOrEqualToken,
     greaterThanToken, greaterThanToken, greaterThanToken, greaterThanToken, greaterThanToken, greaterThanToken,
     greaterThanToken, greaterThanToken, errorUnsupportedSymbol, greaterThanToken, greaterThanToken, greaterThanToken,
     greaterThanToken, greaterThanToken, greaterThanToken],

    [errorAfterSlash, errorAfterSlash, errorAfterSlash, errorAfterSlash, errorAfterSlash, errorAfterSlash,
     errorAfterSlash,
     errorAfterSlash, errorAfterSlash, errorAfterSlash, errorAfterSlash, errorAfterSlash, errorAfterSlash,
     errorAfterSlash,
     divideToken, errorAfterSlash, errorAfterSlash, errorAfterSlash, errorAfterSlash, errorAfterSlash,
     errorUnsupportedSymbol,
     errorAfterSlash, errorAfterSlash, errorAfterSlash, errorAfterSlash, errorAfterSlash, errorAfterSlash],

    [errorHashtag, errorHashtag, errorHashtag, idkState, errorHashtag, errorHashtag, errorHashtag, errorHashtag,
     errorHashtag, errorHashtag, errorHashtag, errorHashtag, errorHashtag, errorHashtag, errorHashtag, errorHashtag,
     openBlockToken, closeBlockToken, remState, errorHashtag, errorUnsupportedSymbol, errorHashtag, errorHashtag,
     errorHashtag, errorHashtag, errorHashtag, errorHashtag],

    [remState, remState, remState, remState, remState, remState, remState, remState, remState, remState, remState,
     remState, remState, remState, remState, closeHashtagState, remState, remState, remState, errorCommentsEOF,
     remState,
     remState, remState, remState, remState, remState, remState],

    [remState, remState, remState, remState, remState, remState, remState, remState, remState, remState, remState,
     remState, remState, remState, remState, closeHashtagState, remState, remState, startState, errorCommentsEOF,
     remState,
     remState, remState, remState, remState, remState, remState]

]

# Variables for intermediate code
quad_dictionary = {}  # Quad lists with labels
next_label = 1  # Counter for labels
temp_value = 1  # Counter for new_temp()
program_name = ''  # Name of main function
name_block = []  # List of function names

# Variables for symbol table
scope_list = []
function_framelength = 0

# Variables for final code
quad_dictionary_block = {}
final_code_counter = 0


###############   LEXICAL ANALYZER   ###############


def lex():
    global line
    word = ''
    currentState = startState
    lexLine = line
    output = []

    while (currentState >= 0 and currentState <= 10):
        char = file.read(1)
        if (char == ' ' or char == '\t'):
            charToken = whiteSpaceChar
        elif (char == '\n'):
            lexLine += 1
            charToken = changeRow
        elif (char in numbers):
            charToken = number
        elif (char in letters):
            charToken = letter
        elif (char == '+'):
            charToken = plusSign
        elif (char == '-'):
            charToken = minusSign
        elif (char == '*'):
            charToken = multiplySign
        elif (char == '('):
            charToken = leftParenthesis
        elif (char == ')'):
            charToken = rightParenthesis
        elif (char == '['):
            charToken = leftBracket
        elif (char == ']'):
            charToken = rightBracket
        elif (char == '='):
            charToken = equalSign
        elif (char == '<'):
            charToken = lessThanSign
        elif (char == '>'):
            charToken = greaterThanSign
        elif (char == '/'):
            charToken = backslash
        elif (char == '#'):
            charToken = hashtag
        elif (char == '{'):
            charToken = openBlock
        elif (char == '}'):
            charToken = closeBlock
        elif (char == '$'):
            charToken = dollarSign
        elif (char == ''):
            charToken = EOF
        elif (char == ','):
            charToken = comma
        elif (char == ';'):
            charToken = semiColon
        elif (char == ':'):
            charToken = colon
        elif (char == '!'):
            charToken = exclamationMark
        elif (char == '"'):
            charToken = quotationMark
        elif (char == '_'):
            charToken = underscore
        else:
            charToken = unSupportedChar

        currentState = transitionMatrix[currentState][charToken]

        if (len(word) < 30):
            if (currentState != startState and currentState != remState and currentState != closeHashtagState):
                word += char
            else:
                word = ''
        else:
            currentState = errorOver30Chars

    if (
            currentState == keywordToken or currentState == numberToken or currentState == lessThanToken or currentState == greaterThanToken or currentState == assignmentToken):
        if (char == '\n'):
            lexLine -= 1
        position = file.tell() - 1  # Moves the file pointer one byte back
        char = file.seek(position, 0)  # Seeks to the position
        word = word[:-1]  # Removes the last Character of the string

    if (currentState == keywordToken):
        if (word in keywords):
            if (word == '#declare'):
                currentState = declareToken
            elif (word == 'if'):
                currentState = ifToken
            elif (word == 'else'):
                currentState = elseToken
            elif (word == 'while'):
                currentState = whileToken
            elif (word == 'return'):
                currentState = returnToken
            elif (word == 'print'):
                currentState = printToken
            elif (word == 'def'):
                currentState = defToken
            elif (word == 'and'):
                currentState = andToken
            elif (word == 'or'):
                currentState = orToken
            elif (word == 'input'):
                currentState = inputToken
            elif (word == 'int'):
                currentState = intToken
            elif (word == 'not'):
                currentState = notToken
            elif (word == '__name__'):
                currentState = nameToken
            elif (word == '__main__'):
                currentState = mainToken
        elif (word[0] == '_'):
            currentState = errorUnderscore

    if (currentState == numberToken):
        if (int(word) >= pow(2, 32)):
            currentState = errorNumber

    if (currentState == errorUnsupportedSymbol):
        print("You used an unsupported symbol! line:", line)
    elif (currentState == errorAfterExclamationMark):
        print("The not-equal operator is (!=) you cannot use Exclamation Mark in any other way! line:", line)
    elif (currentState == errorAfterSlash):
        print("The divide operator is (//) not a single backslash! line:", line)
    elif (currentState == errorOver30Chars):
        print("A word is over 30 characters! line:", line)
    elif (currentState == errorOpenBlock):
        print("You can only use '{' after a hashtag mark! line:", line)
    elif (currentState == errorCloseBlock):
        print("You can only use '}' after a hashtag mark! line:", line)
    elif (currentState == errorDollarSign):
        print("You can only use '$' after a hashtag mark! line:", line)
    elif (currentState == errorLetterAfterNumber):
        print("Letter immediately after a number! line:", line)
    elif (currentState == errorCommentsEOF):
        print("You need to close your comments! line:", line)
    elif (currentState == errorHashtag):
        print("Cannot support Hashtag! line:", line)
    elif (currentState == errorUnderscore):
        print("Word is starting with a single underscore! line:", line)
    elif (currentState == errorNumber):
        print("Number out of value range! line:", line)

    output.append(currentState)
    output.append(word)
    output.append(lexLine)

    if (output[0] <= 238):

        token_family = str(output[0])
        print(" %-20s %s%s %s %d" % (output[1], "family: ", token_dictionary[token_family], ", line: ", output[2]))
    else:
        print("")
        exit(-20)
    return output


###############   SYNTAX ANALYZER   ###############


def syn():
    global line
    global lexOutput
    lexOutput = lex()
    line = lexOutput[2]  # Third column of the transition Matrix is the line number
    startRule()


def startRule():
    addScope(0)
    def_main_part()
    call_main_part()


def def_main_part():
    global lexOutput
    def_main_function()
    while (lexOutput[0] == defToken):
        def_main_function()


def def_main_function():
    global lexOutput
    global line
    global program_name
    if (lexOutput[0] == defToken):
        lexOutput = lex()
        line = lexOutput[2]
        if (lexOutput[0] == keywordToken):
            program_name = lexOutput[1]
            addFunction(program_name, "Function", scope_list[-1].entity_list)
            addScope(scope_list[-1].nestingLevel + 1)
            lexOutput = lex()
            line = lexOutput[2]
            if (lexOutput[0] == leftParenthesisToken):
                lexOutput = lex()
                line = lexOutput[2]
                if (lexOutput[0] == rightParenthesisToken):
                    lexOutput = lex()
                    line = lexOutput[2]
                    if (lexOutput[0] == colonToken):
                        lexOutput = lex()
                        line = lexOutput[2]
                        if (lexOutput[0] == openBlockToken):
                            lexOutput = lex()
                            line = lexOutput[2]
                            declarations()
                            while (lexOutput[0] == defToken):
                                def_function()
                            block(program_name)
                            if (lexOutput[0] == closeBlockToken):
                                lexOutput = lex()
                                line = lexOutput[2]
                            else:
                                print("Error!:You must close the block! line: ", line)
                                exit(-20)
                        else:
                            print("Error!:You must open a block before declarations in main function! line: ", line)
                            exit(-20)
                    else:
                        print("Error!:No colon after main! line: ", line)
                        exit(-20)
                else:
                    print("Error!:No right parenthesis found! line: ", line)
                    exit(-20)
            else:
                print("Error!:No left parenthesis found! line: ", line)
                exit(-20)
        else:
            print("Error!:No main function found! line: ", line)
            exit(-20)
    else:
        print("Error!:Program must begin with def keyword! line: ", line)
        exit(-20)


def def_function():
    global lexOutput
    global line
    global name_block
    if (lexOutput[0] == defToken):
        lexOutput = lex()
        line = lexOutput[2]
        if (lexOutput[0] == keywordToken):
            name_block.append(lexOutput[1])
            function_name = lexOutput[1]
            addFunction(function_name, "Function", scope_list[-1].entity_list)
            addScope(scope_list[-1].nestingLevel + 1)
            lexOutput = lex()
            line = lexOutput[2]
            if (lexOutput[0] == leftParenthesisToken):
                lexOutput = lex()
                line = lexOutput[2]
                id_list()
                if (lexOutput[0] == rightParenthesisToken):
                    lexOutput = lex()
                    line = lexOutput[2]
                    if (lexOutput[0] == colonToken):
                        lexOutput = lex()
                        line = lexOutput[2]
                        if (lexOutput[0] == openBlockToken):
                            lexOutput = lex()
                            line = lexOutput[2]
                            declarations()
                            while (lexOutput[0] == defToken):
                                def_function()
                            block(function_name)
                            if (lexOutput[0] == closeBlockToken):
                                lexOutput = lex()
                                line = lexOutput[2]
                            else:
                                print("Error!:You must close the block! line: ", line)
                                exit(-20)
                        else:
                            print("Error!:You must open a block before declarations in a function! line: ", line)
                            exit(-20)
                    else:
                        print("Error!:You must open a block before declarations in a function! line: ", line)
                        exit(-20)
                else:
                    print("Error!:No right parenthesis found! line: ", line)
                    exit(-20)
            else:
                print("Error!:No left bracket found! line: ", line)
                exit(-20)
        else:
            print("Error!:No function found! line: ", line)
            exit(-20)
    else:
        print("Error!:Program must begin with def keyword! line: ", line)
        exit(-20)


def declarations():
    global lexOutput
    while (lexOutput[0] == declareToken):
        declaration_line()

def statements():
    global lexOutput
    statement()
    while (lexOutput[0] == keywordToken or lexOutput[0] == ifToken or lexOutput[0] == whileToken or lexOutput[
        0] == returnToken or lexOutput[0] == printToken):
        statement()


def id_list():
    global lexOutput
    global line
    if (lexOutput[0] == keywordToken):
        offset = scope_list[-1].framelength
        addParameter(lexOutput[1], "Parameter", offset, scope_list[-1].entity_list)
        scope_list[-1].framelength = scope_list[-1].entity_list[-1].offset + 4
        lexOutput = lex()
        line = lexOutput[2]
        while (lexOutput[0] == commaToken):
            lexOutput = lex()
            line = lexOutput[2]
            if (lexOutput[0] == keywordToken):
                offset = scope_list[-1].framelength
                addParameter(lexOutput[1], "Parameter", offset, scope_list[-1].entity_list)
                scope_list[-1].framelength = scope_list[-1].entity_list[-1].offset + 4
                lexOutput = lex()
                line = lexOutput[2]
            else:
                print("Error!:No id after comma found! line: ", line)
                exit(-20)


def declaration_line():
    global lexOutput
    global line
    if (lexOutput[0] == declareToken):
        lexOutput = lex()
        line = lexOutput[2]
        variable_list()


def statement():
    global lexOutput
    global line
    if (lexOutput[0] == keywordToken or lexOutput[0] == printToken or lexOutput[0] == returnToken):
        simple_statement()
    elif (lexOutput[0] == ifToken or lexOutput[0] == whileToken):
        structured_statement()
    else:
        print("Error!:Wrong statement! line: ", line)
        exit(-20)


def simple_statement():
    global lexOutput
    if (lexOutput[0] == keywordToken):
        assignment_stat()
    elif (lexOutput[0] == printToken):
        print_stat()
    elif (lexOutput[0] == returnToken):
        return_stat()


def call_main_part():
    global lexOutput
    global line
    if (lexOutput[0] == ifToken):
        line = lexOutput[2]
        lexOutput = lex()
        if (lexOutput[0] == nameToken):
            lexOutput = lex()
            line = lexOutput[2]
            if (lexOutput[0] == equalToken):
                lexOutput = lex()
                line = lexOutput[2]
                if (lexOutput[0] == quotesToken):
                    lexOutput = lex()
                    line = lexOutput[2]
                    if (lexOutput[0] == mainToken):
                        line = lexOutput[2]
                        lexOutput = lex()
                        if (lexOutput[0] == quotesToken):
                            lexOutput = lex()
                            line = lexOutput[2]
                            if (lexOutput[0] == colonToken):
                                lexOutput = lex()
                                line = lexOutput[2]
                                gen_quad("begin_block", "main", "_", "_")
                                main_function_call()
                                while (lexOutput[0] == keywordToken):
                                    main_function_call()
                                gen_quad("halt", "_", "_", "_")
                                gen_quad("end_block", "main", "_", "_")

                            else:
                                print("Error!:No colon after main function call! line: ", line)
                                exit(-20)
                        else:
                            print("Error!:No quote found!", line)
                            exit(-20)
                    else:
                        print("Error!:Main function call must start with word __main__! line: ", line)
                        exit(-20)
                else:
                    print("Error!:No quote found! line: ", line)
                    exit(-20)
            else:
                print("Error!:No equal sign found! line: ", line)
                exit(-20)
        else:
            print("Error!:No name found! line: ", line)
            exit(-20)
    else:
        print("Error!:No if found! line: ", line)
        exit(-20)


def structured_statement():
    global lexOutput
    if (lexOutput[0] == ifToken):
        if_stat()
    elif (lexOutput[0] == whileToken):
        while_stat()


def assignment_stat():
    global lexOutput
    global line
    if (lexOutput[0] == keywordToken):
        id_name = lexOutput[1]
        lexOutput = lex()
        line = lexOutput[2]
        if (lexOutput[0] == assignmentToken):
            lexOutput = lex()
            line = lexOutput[2]
            if (lexOutput[0] == intToken):
                lexOutput = lex()
                line = lexOutput[2]
                if (lexOutput[0] == leftParenthesisToken):
                    lexOutput = lex()
                    line = lexOutput[2]
                    if (lexOutput[0] == inputToken):
                        gen_quad("in", "_", "_", id_name)
                        lexOutput = lex()
                        line = lexOutput[2]
                        if (lexOutput[0] == leftParenthesisToken):
                            lexOutput = lex()
                            line = lexOutput[2]
                            if (lexOutput[0] == rightParenthesisToken):
                                lexOutput = lex()
                                line = lexOutput[2]
                                if (lexOutput[0] == rightParenthesisToken):
                                    lexOutput = lex()
                                    line = lexOutput[2]
                                    if (lexOutput[0] == semiColonToken):
                                        lexOutput = lex()
                                        line = lexOutput[2]
                                    else:
                                        print("Error!:No semicolon found! line: ", line)
                                        exit(-20)
                                else:
                                    print("Error!:No right parenthesis found! line: ", line)
                                    exit(-20)
                            else:
                                print("Error!:No left parenthesis found! line: ", line)
                                exit(-20)
                        else:
                            print("Error!:No right parenthesis found! line: ", line)
                            exit(-20)
                    else:
                        print("Error!:No input found! line: ", line)
                        exit(-20)
                else:
                    print("Error!:No left parenthesis found! line: ", line)
                    exit(-20)
            else:
                ex = expression()
                gen_quad("=", ex, "_", id_name)
                if (lexOutput[0] == semiColonToken):
                    lexOutput = lex()
                    line = lexOutput[2]
                else:
                    print("Error!:No semicolon found after expression! line: ", line)
                    exit(-20)
        else:
            print("Error!:No assignment sign found after the id! line: ", line)
            exit(-20)
    else:
        print("Error!:No id! line: ", line)
        exit(-20)


def print_stat():
    global lexOutput
    global line
    if (lexOutput[0] == printToken):
        lexOutput = lex()
        line = lexOutput[2]
        if (lexOutput[0] == leftParenthesisToken):
            lexOutput = lex()
            line = lexOutput[2]
            ex = expression()
            gen_quad("out", ex, "_", "_")
            if (lexOutput[0] == rightParenthesisToken):
                lexOutput = lex()
                line = lexOutput[2]
                if (lexOutput[0] == semiColonToken):
                    lexOutput = lex()
                    line = lexOutput[2]
                else:
                    print("Error!:No semicolon found after expression! line: ", line)
                    exit(-20)
            else:
                print("Error!:No right parenthesis found! line: ", line)
                exit(-20)
        else:
            print("Error!:No left parenthesis found! line: ", line)
            exit(-20)
    else:
        print("Error!:There is no print! line: ", line)
        exit(-20)


def return_stat():
    global lexOutput
    global line
    if (lexOutput[0] == returnToken):
        lexOutput = lex()
        line = lexOutput[2]
        if (lexOutput[0] == leftParenthesisToken):
            lexOutput = lex()
            line = lexOutput[2]
            ex = expression()
            gen_quad("retv", ex, "_", "_")
            if (lexOutput[0] == rightParenthesisToken):
                lexOutput = lex()
                line = lexOutput[2]
                if (lexOutput[0] == semiColonToken):
                    lexOutput = lex()
                    line = lexOutput[2]
                else:
                    print("Error!:No semicolon found after expression! line: ", line)
                    exit(-20)
            else:
                print("Error!:No right parenthesis found! line: ", line)
                exit(-20)
        else:
            print("Error!:No left parenthesis found! line: ", line)
            exit(-20)
    else:
        print("Error!:There is no return! line: ", line)
        exit(-20)


def main_function_call():
    global lexOutput
    global line
    global main_name
    if (lexOutput[0] == keywordToken):
        main_name = lexOutput[1]
        lexOutput = lex()
        line = lexOutput[2]
        if (lexOutput[0] == leftParenthesisToken):
            lexOutput = lex()
            line = lexOutput[2]
            if (lexOutput[0] == rightParenthesisToken):
                lexOutput = lex()
                line = lexOutput[2]
                if (lexOutput[0] == semiColonToken):
                    gen_quad("call", main_name, "_", "_")
                    lexOutput = lex()
                    line = lexOutput[2]
                else:
                    print("Error!:No semicolon found! line: ", line)
                    exit(-20)
            else:
                print("Error!:No right parenthesis found! line: ", line)
                exit(-20)
        else:
            print("Error!:No left parenthesis found! line: ", line)
            exit(-20)
    else:
        print("Error!:No id found! line: ", line)
        exit(-20)


def if_stat():
    global lexOutput
    global line
    global if_list
    if (lexOutput[0] == ifToken):
        lexOutput = lex()
        line = lexOutput[2]
        if (lexOutput[0] == leftParenthesisToken):
            lexOutput = lex()
            line = lexOutput[2]
            [B_true, B_false] = condition()
            if (lexOutput[0] == rightParenthesisToken):
                lexOutput = lex()
                line = lexOutput[2]
                if (lexOutput[0] == colonToken):
                    lexOutput = lex()
                    line = lexOutput[2]
                    backpatch(B_true, next_quad())
                    if (lexOutput[0] == openBlockToken):
                        lexOutput = lex()
                        line = lexOutput[2]
                        statements()
                        if_list = make_list(next_quad())
                        gen_quad("jump", "_", "_", "_")
                        backpatch(B_false, next_quad())
                        if (lexOutput[0] == closeBlockToken):
                            lexOutput = lex()
                            line = lexOutput[2]
                            else_part()
                            backpatch(if_list, next_quad())
                        else:
                            print("Error!:No close block found after if statements! line: ", line)
                            exit(-20)
                    else:
                        statement()
                        if_list = make_list(next_quad())
                        gen_quad("jump", "_", "_", "_")
                        backpatch(B_false, next_quad())
                        else_part()
                        backpatch(if_list, next_quad())
                else:
                    print("Error!:No colon found! line: ", line)
                    exit(-20)
            else:
                print("Error!:No right parenthesis found! line: ", line)
                exit(-20)
        else:
            print("Error!:No left parenthesis found! line: ", line)
            exit(-20)
    else:
        print("Error!:There is no if! line: ", line)
        exit(-20)


def else_part():
    global lexOutput
    global line
    global if_list
    if (lexOutput[0] == elseToken):
        lexOutput = lex()
        line = lexOutput[2]
        if (lexOutput[0] == colonToken):
            lexOutput = lex()
            line = lexOutput[2]
            if (lexOutput[0] == openBlockToken):
                lexOutput = lex()
                line = lexOutput[2]
                if (lexOutput[0] == ifToken):
                    else_if()
                else:
                    statements()
                if (lexOutput[0] == closeBlockToken):
                    lexOutput = lex()
                    line = lexOutput[2]
                else:
                    print("Error!:No close block found after else statements! line: ", line)
                    exit(-20)
            elif (lexOutput[0] == ifToken):
                else_if()
            else:
                statement()
        else:
            print("Error!:No colon found! line: ", line)
            exit(-20)


def else_if():
    global lexOutput
    global line
    global if_list
    if (lexOutput[0] == ifToken):
        lexOutput = lex()
        line = lexOutput[2]
        if (lexOutput[0] == leftParenthesisToken):
            lexOutput = lex()
            line = lexOutput[2]
            [B1_true, B1_false] = condition()
            if (lexOutput[0] == rightParenthesisToken):
                lexOutput = lex()
                line = lexOutput[2]
                if (lexOutput[0] == colonToken):
                    lexOutput = lex()
                    line = lexOutput[2]
                    backpatch(B1_true, next_quad())
                    if (lexOutput[0] == openBlockToken):
                        lexOutput = lex()
                        line = lexOutput[2]
                        statements()
                        t = make_list(next_quad())
                        gen_quad("jump", "_", "_", "_")
                        if_list = merge(if_list, t)
                        backpatch(B1_false, next_quad())
                        if (lexOutput[0] == closeBlockToken):
                            lexOutput = lex()
                            line = lexOutput[2]
                            else_part()
                            backpatch(if_list, next_quad())
                        else:
                            print("Error!:No close block found after if statements! line: ", line)
                            exit(-20)
                    else:
                        statement()
                        t = make_list(next_quad())
                        gen_quad("jump", "_", "_", "_")
                        if_list = merge(if_list, t)
                        backpatch(B1_false, next_quad())
                        else_part()
                        backpatch(if_list, next_quad())


def while_stat():
    global lexOutput
    global line
    if (lexOutput[0] == whileToken):
        lexOutput = lex()
        line = lexOutput[2]
        B_quad = next_quad()
        if (lexOutput[0] == leftParenthesisToken):
            lexOutput = lex()
            line = lexOutput[2]
            [B_true, B_false] = condition()
            if (lexOutput[0] == rightParenthesisToken):
                lexOutput = lex()
                line = lexOutput[2]
                if (lexOutput[0] == colonToken):
                    lexOutput = lex()
                    line = lexOutput[2]
                    if (lexOutput[0] == openBlockToken):
                        lexOutput = lex()
                        line = lexOutput[2]
                        backpatch(B_true, next_quad())
                        statements()
                        gen_quad("jump", "_", "_", B_quad)
                        backpatch(B_false, next_quad())
                        if (lexOutput[0] == closeBlockToken):
                            lexOutput = lex()
                            line = lexOutput[2]
                        else:
                            print("Error!:No close block found after while statements! line: ", line)
                            exit(-20)
                    else:
                        backpatch(B_true, next_quad())
                        statement()
                        gen_quad("jump", "_", "_", B_quad)
                        backpatch(B_false, next_quad())
                else:
                    print("Error!:No colon found! line: ", line)
                    exit(-20)
            else:
                print("Error!:No right parenthesis found! line: ", line)
                exit(-20)
        else:
            print("Error!:No left parenthesis found! line: ", line)
            exit(-20)
    else:
        print("Error!:There is no while!\ line: ", line)
        exit(-20)


def expression():
    global lexOutput
    global line
    optional_sign()
    t1 = term()
    while (lexOutput[0] == plusToken or lexOutput[0] == minusToken):
        op = lexOutput[1]
        ADD_OP()
        t2 = term()
        w = new_temp()
        gen_quad(op, t1, t2, w)
        t1 = w
    return t1


def condition():
    global lexOutput
    global line
    [Q1_true, Q1_false] = bool_term()
    B_true = Q1_true
    B_false = Q1_false
    while (lexOutput[0] == orToken):
        backpatch(B_false, next_quad())
        lexOutput = lex()
        line = lexOutput[2]
        [Q2_true, Q2_false] = bool_term()
        B_true = merge(B_true, Q2_true)
        B_false = Q2_false
    return [B_true, B_false]


def optional_sign():
    global lexOutput
    global line
    op_sign = lexOutput[1]
    if (lexOutput[0] == plusToken or lexOutput[0] == minusToken):
        ADD_OP()
    return op_sign


def term():
    global lexOutput
    global line
    f1 = factor()
    while (lexOutput[0] == multiplyToken or lexOutput[0] == divideToken):
        op = lexOutput[1]
        MUL_OP()
        f2 = factor()
        w = new_temp()
        gen_quad(op, f1, f2, w)
        f1 = w
    return f1


def ADD_OP():
    global lexOutput
    global line
    if (lexOutput[0] == plusToken):
        lexOutput = lex()
        line = lexOutput[2]
    elif (lexOutput[0] == minusToken):
        lexOutput = lex()
        line = lexOutput[2]


def bool_term():
    global lexOutput
    global line
    [R1_true, R1_false] = bool_factor()
    Q_true = R1_true
    Q_false = R1_false
    while (lexOutput[0] == andToken):
        backpatch(Q_true, next_quad())
        lexOutput = lex()
        line = lexOutput[2]
        [R2_true, R2_false] = bool_factor()
        Q_false = merge(Q_false, R2_false)
        Q_true = R2_true
    return [Q_true, Q_false]


def factor():
    global lexOutput
    global line
    global name_block
    factor_value = lexOutput[1]
    if (lexOutput[0] == numberToken):
        lexOutput = lex()
        line = lexOutput[2]
    elif (lexOutput[0] == leftParenthesisToken):
        lexOutput = lex()
        line = lexOutput[2]
        ex = expression()
        factor_value = ex
        if (lexOutput[0] == rightParenthesisToken):
            lexOutput = lex()
            line = lexOutput[2]
        else:
            print("Error!:No right parenthesis found line: ", line)
            exit(-20)
    elif (lexOutput[0] == keywordToken):
        lexOutput = lex()
        line = lexOutput[2]
        idtail()
        if (factor_value in name_block):
            w = new_temp()
            gen_quad("par", w, "RET", "_")
            gen_quad("call", factor_value, "_", "_")
            factor_value = w

    else:
        print("Error!:Wrong syntax of factor! line: ", line)
        exit(-20)
    return factor_value


def MUL_OP():
    global lexOutput
    global line
    if (lexOutput[0] == multiplyToken):
        lexOutput = lex()
        line = lexOutput[2]
    elif (lexOutput[0] == divideToken):
        lexOutput = lex()
        line = lexOutput[2]


def bool_factor():
    global lexOutput
    global line
    if (lexOutput[0] == notToken):
        lexOutput = lex()
        line = lexOutput[2]
        if (lexOutput[0] == leftBracketToken):
            lexOutput = lex()
            line = lexOutput[2]
            [B_true, B_false] = condition()
            R_true = B_false
            R_false = B_true
            if (lexOutput[0] == rightBracketToken):
                lexOutput = lex()
                line = lexOutput[2]
            else:
                print("Error!:No right bracket found! line: ", line)
                exit(-20)
        else:
            print("Error!:No left bracket found! line: ", line)
            exit(-20)
    elif (lexOutput[0] == leftBracketToken):
        lexOutput = lex()
        line = lexOutput[2]
        [B_true, B_false] = condition()
        R_true = B_true
        R_false = B_false
        if (lexOutput[0] == rightBracketToken):
            lexOutput = lex()
            line = lexOutput[2]
        else:
            print("Error!:No right bracket found! line: ", line)
            exit(-20)
    else:
        ex1 = expression()
        relop = REL_OP()
        ex2 = expression()
        R_true = make_list(next_quad())
        gen_quad(relop, ex1, ex2, "_")
        R_false = make_list(next_quad())
        gen_quad("jump", "_", "_", "_")
    return [R_true, R_false]


def idtail():
    global lexOutput
    global line
    if (lexOutput[0] == leftParenthesisToken):
        lexOutput = lex()
        line = lexOutput[2]
        actual_par_list()
        if (lexOutput[0] == rightParenthesisToken):
            lexOutput = lex()
            line = lexOutput[2]
        else:
            print("Error!:No right parenthesis found! line: ", line)
            exit(-20)


def actual_par_list():
    global lexOutput
    global line
    if (lexOutput[0] == keywordToken or lexOutput[0] == numberToken or lexOutput[0] == leftParenthesisToken):
        ex1 = expression()
        if (lexOutput[0] != commaToken):
            gen_quad("par", ex1, "_", "_")
        while (lexOutput[0] == commaToken):
            lexOutput = lex()
            line = lexOutput[2]
            ex2 = expression()
            gen_quad("par", ex1, "_", "_")
            gen_quad("par", ex2, "_", "_")


def REL_OP():
    global lexOutput
    global line
    rel_op = lexOutput[1]
    if (lexOutput[0] == equalToken):
        lexOutput = lex()
        line = lexOutput[2]
    elif (lexOutput[0] == greaterThanToken):
        lexOutput = lex()
        line = lexOutput[2]
    elif (lexOutput[0] == lessThanToken):
        lexOutput = lex()
        line = lexOutput[2]
    elif (lexOutput[0] == greaterOrEqualToken):
        lexOutput = lex()
        line = lexOutput[2]
    elif (lexOutput[0] == lessOrEqualToken):
        lexOutput = lex()
        line = lexOutput[2]
    elif (lexOutput[0] == differToken):
        lexOutput = lex()
        line = lexOutput[2]
    else:
        print("Error!:You are missing a relational operator! line: ", line)
        exit(-20)
    return rel_op


def variable_list():
    global lexOutput
    global line
    if (lexOutput[0] == keywordToken):
        offset = scope_list[-1].framelength 
        addVariable(lexOutput[1], "Variable", offset, scope_list[-1].entity_list) 
        scope_list[-1].framelength = scope_list[-1].entity_list[-1].offset + 4  
        lexOutput = lex()
        line = lexOutput[2]
        while (lexOutput[0] == commaToken):
            lexOutput = lex()
            line = lexOutput[2]
            if (lexOutput[0] == keywordToken):
                offset = scope_list[-1].framelength
                addVariable(lexOutput[1], "Variable", offset, scope_list[-1].entity_list)  
                scope_list[-1].framelength = scope_list[-1].entity_list[-1].offset + 4  
                lexOutput = lex()
                line = lexOutput[2]
            else:
                print("Error!:No id after comma found! line: ", line)
                exit(-20)


###############   INTERMEDIATE CODE   ###############

def gen_quad(op=None, op1='_', op2='_', op3='_'):
    global next_label
    quad_dictionary[next_label] = [op, op1, op2, op3]
    quad_dictionary_block[next_label] = [op, op1, op2, op3]
    next_label += 1


def next_quad():
    return str(next_label)


def new_temp():
    global temp_value
    temp = '%' + str(temp_value)
    offset = scope_list[-1].framelength
    addTemporaryVariable(temp, "TemporaryVariable", offset, scope_list[-1].entity_list)
    scope_list[-1].framelength = scope_list[-1].entity_list[-1].offset + 4
    temp_value += 1
    return temp


def empty_list():
    return []


def make_list(label):
    new_list = [label]
    return new_list


def merge(list_1, list_2):
    return list_1 + list_2


def backpatch(q_list, label):
    global quad_dictionary
    for i in quad_dictionary:
        if str(i) in q_list:
            quad_dictionary[i][3] = label


def block(name):
    global function_framelength
    global quad_dictionary_block

    # Initialize startingQuad for every function
    gen_quad("begin_block", name, "_", "_")
    func, nestLevel = searchEntity(name)
    func.startingQuad = next_quad()
    statements()

    # Update Function_Framelength of nesting level 0 to match Scope_Framelength of nesting level 1
    if nestLevel == 0 and len(scope_list) > 1:
        scope_level_1 = scope_list[1]
        function_framelength = scope_level_1.framelength
        func.framelength = function_framelength  # Update the framelength of the function entity

    gen_quad("end_block", name, "_", "_")

    # Final Code
    for quad_label in quad_dictionary_block:
        final_code(quad_label, func.name)

    # Framelength for functions
    scope = scope_list[-1]
    if not (len(scope.entity_list) == 0):
        vp = None
        for i in range(len(scope.entity_list) - 1, -1, -1):
            if (scope.entity_list[i].datatype == "Variable" or scope.entity_list[i].datatype == "TemporaryVariable" or
                    scope.entity_list[i].datatype == "Parameter"):
                vp = scope.entity_list[i]  # Framelength of the last entity of the function
                break
        if not (vp == None):
            if name == program_name:
                function_framelength = vp.offset + 4  # Last function's entity framelength + 4
                scope.framelength = function_framelength  # Save scope's framelength
            else:
                func.framelength = vp.offset + 4  # Last function's entity framelength + 4
                scope.framelength = func.framelength  # Save scope's framelength
    else:
        func.framelength = 12
        scope.framelength = func.framelength



    # Create .sym file
    sym_table_file = open(keep_file_name + ".sym", "a") # We need to delete the existing file .sym


    for i in scope_list:
        sym_table_file.write(i.printScope() + "\n \n")


    if not (name == program_name):
        scope_list.pop(-1) # Delete scope

        sym_table_file.write("########################")
        sym_table_file.write("     DELETE SCOPE       ")
        sym_table_file.write("########################")
        sym_table_file.write("\n \n")

    else:
        scope_list.pop(-1)  # Delete scope

        sym_table_file.write("########################")
        sym_table_file.write("     DELETE SCOPE       ")
        sym_table_file.write("########################")
        sym_table_file.write("\n \n")

        for i in scope_list:
            sym_table_file.write(i.printScope() + "\n \n")

        sym_table_file.close()

    quad_dictionary_block = {}


# Write all quads in .int file
def int_file():
    for key, value in quad_dictionary.items():
        int_quad_file.write(str(key) + ": " + ", ".join(str(i) for i in value) + "\n")
    int_quad_file.close()

###############   SYMBOL TABLE   ###############

class Entity:
    def __init__(self, name):
        self.name = name

    def printTable(self):
        return self.name


class Variable(Entity):
    def __init__(self, name, datatype, offset):
        super().__init__(name)
        self.datatype = datatype
        self.offset = offset

    def printTable(self):
        return super().printTable() + " / " + str(self.offset) + " / " + self.datatype


class FormalParameters(Entity):
    def __init__(self, name, datatype):
        super().__init__(name)
        self.datatype = datatype

    def printTable(self):
        return super().printTable()


class Function(Entity):
    def __init__(self, name, datatype):
        super().__init__(name)
        self.datatype = datatype
        self.startingQuad = 0
        self.framelength = 12

    def printTable(self):
        flength = super().printTable() + " / Function_Framelength: " + str(self.framelength) + " / " + " StartingQuad: " + str(self.startingQuad)
        return flength


class Parameter(FormalParameters):
    def __init__(self, name, datatype,offset):
        super().__init__(name, datatype)
        self.offset = offset

    def printTable(self):
        return super().printTable() + " / " + str(self.offset) + " / " + self.datatype


class TemporaryVariable(Variable):
    def __init__(self, name, datatype, offset):
        super().__init__(name, datatype, offset)

    def printTable(self):
        return super().printTable()


class Scope:
    def __init__(self, nestingLevel):
        self.nestingLevel = nestingLevel
        self.entity_list = []
        self.framelength = 12

    def printScope(self):
        level = "NestingLevel: " + str(self.nestingLevel) + "\n"
        for i in self.entity_list:
            level = level + str(i.printTable()) + "\n"
        level = level + "Scope_Framelength: " + str(self.framelength)
        return level


def addScope(nestingLevel):
    scope = Scope(nestingLevel)
    if (len(scope_list) == 0):
        scope.nestingLevel = 0
    else:
        scope.nestingLevel = scope_list[-1].nestingLevel + 1
    scope_list.append(scope)


def addVariable(name, datatype, offset, entity_list):
    variable = Variable(name, datatype, offset)
    entity_list.append(variable)


def addParameter(name, datatype, offset, entity_list):
    parameter = Parameter(name, datatype, offset)
    entity_list.append(parameter)


def addFunction(name, datatype, entity_list):
    function = Function(name, datatype)
    entity_list.append(function)


def addFormalParameters(name, datatype, formalParameters):
    fp = FormalParameters(name, datatype)
    formalParameters.append(fp)
    return fp


def addTemporaryVariable(name, datatype, offset, entity_list):
    tv = TemporaryVariable(name, datatype, offset)
    entity_list.append(tv)


def searchEntity(name):
    if (name == program_name):
        for i in range(len(scope_list) - 1, -1, -1):
            for entity in scope_list[i].entity_list:
                if (entity.name == name):
                    return entity, 0

    for i in range(len(scope_list) -1, -1, -1):
        for entity in scope_list[i].entity_list:
            if (entity.name == name):
                return entity, scope_list[i].nestingLevel


###############   FINAL CODE   ###############
def if_main_call():
    begin_block_main = ['begin_block', 'main', '_', '_']
    for key, value in quad_dictionary.items():
        if value == begin_block_main:
            begin = key
            break
    assembly_file.write("L" + str(begin) + ":\n")
    assembly_file.write("Lmain:\n")
    assembly_file.write(" addi sp, sp, 12" + "\n")
    assembly_file.write(" mv gp, sp\n")

    call_main = ["call", program_name, "_", "_"]
    for key, value in quad_dictionary.items():
        if value == call_main:
            call = key
            break
    call_entity, call_nestLevel = searchEntity(quad_dictionary[call][1])
    assembly_file.write("L" + str(call) + ":\n")
    assembly_file.write(" sw sp, -4(fp)\n")
    assembly_file.write(" addi sp, sp, " + str(call_entity.framelength) + "\n")
    assembly_file.write(" jal L" + str(int(call_entity.startingQuad) - 1) + "\n")
    assembly_file.write(" addi sp, sp, -" + str(call_entity.framelength) + "\n")


    halt_main = ['halt', '_', '_', '_']
    for key, value in quad_dictionary.items():
        if value == halt_main:
            halt = key
            break
    assembly_file.write("L" + str(halt) + ":\n")
    assembly_file.write(" li a0, 0\n")
    assembly_file.write(" li a7, 93\n")
    assembly_file.write(" ecall\n")

    end_main = ['end_block', 'main', '_', '_']
    for key, value in quad_dictionary.items():
        if value == end_main:
            end = key
            break
    assembly_file.write("L" + str(end) + ":\n")
    assembly_file.write(" lw ra, (sp)\n")
    assembly_file.write(" jr ra\n")


def gnvlcode(v):
    entity, nestLevel = searchEntity(v)
    assembly_file.write(" lw t0, -4(sp)\n")
    for i in range(scope_list[-1].nestingLevel, nestLevel, -1):
        assembly_file.write(" lw t0, -4(t0)\n")
    assembly_file.write(" addi t0, t0, -" + str(entity.offset) + "\n")


def loadvr(v, reg):
    # v is integer constant
    if (v.isdigit()):
        assembly_file.write(" li t" + str(reg) + ", " + str(v) + "\n")

    else:
        current_level = scope_list[-1].nestingLevel
        entity, nestLevel = searchEntity(v)

        # v is global variable
        if (nestLevel == 0 and entity.datatype == "Variable"):
            assembly_file.write(" lw t" + str(reg) + ", -" + str(entity.offset) + "(gp)\n")

        # v is local variable or parameter or temporary variable
        elif nestLevel == current_level and (entity.datatype == "Variable"
                                             or entity.datatype == "Parameter" or entity.datatype == "TemporaryVariable"):

            assembly_file.write(" lw t" + str(reg) + ", -" + str(entity.offset) + "(sp)\n")

        # v is (local variable or parameter) in ancestor function
        elif (nestLevel < current_level and (entity.datatype == "Variable" or entity.datatype == "Parameter")):
            gnvlcode(v)
            assembly_file.write(" lw t" + str(reg) + ", (t0)\n")



def storerv(reg, v):
    current_level = scope_list[-1].nestingLevel
    entity, nestLevel = searchEntity(v)

    # v is global variable
    if (nestLevel == 0 and entity.datatype == "Variable"):
        assembly_file.write(" sw t" + str(reg) + ", -" + str(entity.offset) + "(gp)\n")

    # v is local variable or parameter or temporary variable
    elif (nestLevel == current_level and (
            entity.datatype == "Variable" or entity.datatype == "Parameter" or entity.datatype == "TemporaryVariable")):
        assembly_file.write(" sw t" + str(reg) + ", -" + str(entity.offset) + "(sp)\n")


    # v is (local variable or parameter) in ancestor function
    elif (nestLevel < current_level and (entity.datatype == "Variable" or entity.datatype == "Parameter")):
        gnvlcode(v)
        assembly_file.write(" sw t" + str(reg) + ", (t0)\n")


def final_code(quad, name):
    global final_code_counter
    global scope
    scope = scope_list[-1]

    if (quad_dictionary[quad][0] == "jump"):
        assembly_file.write("L" + str(quad) + ":\n")
        assembly_file.write(" j L" + quad_dictionary[quad][3] + "\n")

    elif (quad_dictionary[quad][0] == "=="):
        assembly_file.write("L" + str(quad) + ":\n")
        loadvr(quad_dictionary[quad][1], 1)
        loadvr(quad_dictionary[quad][2], 2)
        assembly_file.write(" beq t1, t2, L" + quad_dictionary[quad][3] + "\n")

    elif (quad_dictionary[quad][0] == "!="):
        assembly_file.write("L" + str(quad) + ":\n")
        loadvr(quad_dictionary[quad][1], 1)
        loadvr(quad_dictionary[quad][2], 2)
        assembly_file.write(" bne t1, t2, L" + quad_dictionary[quad][3] + "\n")

    elif (quad_dictionary[quad][0] == ">"):
        assembly_file.write("L" + str(quad) + ":\n")
        loadvr(quad_dictionary[quad][1], 1)
        loadvr(quad_dictionary[quad][2], 2)
        assembly_file.write(" bgt t1, t2, L" + quad_dictionary[quad][3] + "\n")

    elif (quad_dictionary[quad][0] == "<"):
        assembly_file.write("L" + str(quad) + ":\n")
        loadvr(quad_dictionary[quad][1], 1)
        loadvr(quad_dictionary[quad][2], 2)
        assembly_file.write(" blt t1, t2, L" + quad_dictionary[quad][3] + "\n")

    elif (quad_dictionary[quad][0] == ">="):
        assembly_file.write("L" + str(quad) + ":\n")
        loadvr(quad_dictionary[quad][1], 1)
        loadvr(quad_dictionary[quad][2], 2)
        assembly_file.write(" bge t1, t2, L" + quad_dictionary[quad][3] + "\n")

    elif (quad_dictionary[quad][0] == "<="):
        assembly_file.write("L" + str(quad) + ":\n")
        loadvr(quad_dictionary[quad][1], 1)
        loadvr(quad_dictionary[quad][2], 2)
        assembly_file.write(" ble t1, t2, L" + quad_dictionary[quad][3] + "\n")

    elif (quad_dictionary[quad][0] == "="):
        assembly_file.write("L" + str(quad) + ":\n")
        loadvr(quad_dictionary[quad][1], 1)
        storerv(1, quad_dictionary[quad][3])

    elif (quad_dictionary[quad][0] == "+"):
        assembly_file.write("L" + str(quad) + ":\n")
        loadvr(quad_dictionary[quad][1], 1)
        loadvr(quad_dictionary[quad][2], 2)
        assembly_file.write(" add t1, t1, t2\n")
        storerv(1, quad_dictionary[quad][3])

    elif (quad_dictionary[quad][0] == "-"):
        assembly_file.write("L" + str(quad) + ":\n")
        loadvr(quad_dictionary[quad][1], 1)
        loadvr(quad_dictionary[quad][2], 2)
        assembly_file.write(" sub t1, t1, t2\n")
        storerv(1, quad_dictionary[quad][3])

    elif (quad_dictionary[quad][0] == "*"):
        assembly_file.write("L" + str(quad) + ":\n")
        loadvr(quad_dictionary[quad][1], 1)
        loadvr(quad_dictionary[quad][2], 2)
        assembly_file.write(" mul t1, t1, t2\n")
        storerv(1, quad_dictionary[quad][3])

    elif (quad_dictionary[quad][0] == "//"):
        assembly_file.write("L" + str(quad) + ":\n")
        loadvr(quad_dictionary[quad][1], 1)
        loadvr(quad_dictionary[quad][2], 2)
        assembly_file.write(" div t1, t1, t2\n")
        storerv(1, quad_dictionary[quad][3])

    elif (quad_dictionary[quad][0] == "out"):
        assembly_file.write("L" + str(quad) + ":\n")
        loadvr(quad_dictionary[quad][1], 1)  # In case the argument of print is in another block
        assembly_file.write(" mv a0, t1\n")
        assembly_file.write(" li a7, 1\n")
        assembly_file.write(" ecall\n")

    elif (quad_dictionary[quad][0] == "in"):
        assembly_file.write("L" + str(quad) + ":\n")
        assembly_file.write(" li a7, 5\n")
        assembly_file.write(" ecall\n")
        storerv(1, quad_dictionary[quad][1])

    elif (quad_dictionary[quad][0] == "retv"):
        assembly_file.write("L" + str(quad) + ":\n")
        loadvr(quad_dictionary[quad][1], 1)
        assembly_file.write(" lw t0, -8(sp)\n")
        assembly_file.write(" sw t1, (t0)\n")

    elif (quad_dictionary[quad][0] == "par"):
        assembly_file.write("L" + str(quad) + ":\n")
        entity, nestLevel = searchEntity(name)
        assembly_file.write(" addi fp, sp, " + str(entity.framelength))
        if(quad_dictionary[quad][2] == "RET"):
            assembly_file.write(" addi t0, sp, -" + str(entity.offset))
            assembly_file.write("sw t0, -8(fp)")
        else:
            loadvr(quad_dictionary[quad][1], 0)
            assembly_file.write(" sw t0, -" + str(12 + 4 * final_code_counter) + ")(fp)")

    elif (quad_dictionary[quad][0] == "call"):
        assembly_file.write("L" + str(quad) + ":\n")
        callerEntity, callerNestLevel = searchEntity(name)
        calledEntity, calledNestLevel = searchEntity(quad_dictionary[quad][1])

        if (callerNestLevel == calledNestLevel):
            assembly_file.write(" lw t0, -4(sp)\n")
            assembly_file.write(" sw t0, -4(fp)\n")

        elif (callerNestLevel < calledNestLevel):
            assembly_file.write(" sw sp, -4(fp)\n")
        assembly_file.write(" addi sp, sp, " + str(calledEntity.framelength) + "\n")
        assembly_file.write(" jal L" + str(calledEntity.startingQuad) + "\n")
        assembly_file.write(" addi sp, sp, -" + str(calledEntity.framelength) + "\n")
        final_code_counter = 0

    elif (quad_dictionary[quad][0] == "begin_block" and quad_dictionary[quad][1] != "main"):
        assembly_file.write("L" + str(quad) + ":\n")
        assembly_file.write(" sw ra, (sp)\n")

    elif (quad_dictionary[quad][0] == "end_block" and quad_dictionary[quad][1] != "main"):
        assembly_file.write("L" + str(quad) + ":\n")
        assembly_file.write(" lw ra, (sp)\n")
        assembly_file.write(" jr ra\n")


# Create .asm file
assembly_file = open(keep_file_name + ".asm", "w")
assembly_file.write("L0:\n")
assembly_file.write(" j Lmain \n")

syn()
print("Syntax Analysis found no mistakes")


# Create .int file
int_quad_file = open(keep_file_name + ".int", "w")
int_file()

if_main_call()
assembly_file.close()
file.close()

sys.exit(0)  # Terminate programme

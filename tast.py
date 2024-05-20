import sys
from random import randint
import subprocess
import platform as pt
import tkinter as tk

variables = {
    "width": 760,
    "height": 670,
    "text": "Hello, world!",
    "title": "My window",
}
functions = {}
pyfunctions = {}
running_loop = [False]

TOKENS = [
    'NUMBER',
    'PRINT',
    'MAINFUNC',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'COMPARE',
    'CALLFUNC',
    'PUSH',
    'STRING',
    'NEWLINE',
    'DATAFUNC',
    'SET',
    'PRINTVAR',
    'FUNC',
    'ADDCODE',
    'STARTCODE',
    'STRINPUT',
    'INTINPUT',
    'SPACE',
    'RANDNUMBER',
    'LOOP',
    'STOPLOOP',
    'SYSTEM',
    'IMPORT',
    'INCLUDE',
    'COMMENT',
    'ADDPYFUNC',
    'PYFUNCCODE',
    'CALLPYFUNC',
    'ADDNUM',
    'REMOVENUM',
    'CREATEWINDOW',
    'WINDOWLOOP',
    'JOINVAR',
    'NOTCOMPARE',
    'READFILE',
    'WRITEFILE',
    'APPENDFILE',
    'SYSTEMVAR',
]

class Lexer:
    def __init__(self, code):
        self.code = code
        self.linenum = 0
    
    def printtoken(self):
        lines = self.code.split("\n")

        for line in lines:
            self.linenum += 1
            tokens = line.split()

            for token in tokens:
                if token.isdigit():
                    print(F"TYPE: {TOKENS[0]}. LINE: {self.linenum}. TOKEN: {token}")
                elif token == "pr":
                    print(F"TYPE: {TOKENS[1]}. LINE: {self.linenum}. TOKEN: {token}")
                elif token == "main":
                    print(F"TYPE: {TOKENS[2]}. LINE: {self.linenum}. TOKEN: {token}")
                elif token == "+":
                    print(F"TYPE: {TOKENS[3]}. LINE: {self.linenum}. TOKEN: {token}")
                elif token == "-":
                    print(F"TYPE: {TOKENS[4]}. LINE: {self.linenum}. TOKEN: {token}")
                elif token == "*":
                    print(F"TYPE: {TOKENS[5]}. LINE: {self.linenum}. TOKEN: {token}")
                elif token == "/":
                    print(F"TYPE: {TOKENS[6]}. LINE: {self.linenum}. TOKEN: {token}")
                elif token == "compa":
                    print(F"TYPE: {TOKENS[7]}. LINE: {self.linenum}. TOKEN: {token}")
                elif token == "call":
                    print(F"TYPE: {TOKENS[8]}. LINE: {self.linenum}. TOKEN: {token}")
                elif token == "push":
                    print(F"TYPE: {TOKENS[9]}. LINE: {self.linenum}. TOKEN: {token}")
                elif token == "\"":
                    print(F"TYPE: {TOKENS[10]}. LINE: {self.linenum}. TOKEN: {token}")
                elif token == "nl":
                    print(F"TYPE: {TOKENS[11]}. LINE: {self.linenum}. TOKEN: {token}")
                elif token == ".data":
                    print(F"TYPE: {TOKENS[12]}. LINE: {self.linenum}. TOKEN: {token}")
                elif token == "set":
                    print(F"TYPE: {TOKENS[13]}. LINE: {self.linenum}. TOKEN: {token}")
                elif token == "prv":
                    print(F"TYPE: {TOKENS[14]}. LINE: {self.linenum}. TOKEN: {token}")
                elif token == "func":
                    print(F"TYPE: {TOKENS[15]}. LINE: {self.linenum}. TOKEN: {token}")
                elif token == "addfcode":
                    print(F"TYPE: {TOKENS[16]}. LINE: {self.linenum}. TOKEN: {token}")
                elif token == ">":
                    print(F"TYPE: {TOKENS[17]}. LINE: {self.linenum}. TOKEN: {token}")
                elif token == "strinput":
                    print(F"TYPE: {TOKENS[18]}. LINE: {self.linenum}. TOKEN: {token}")
                elif token == "intinput":
                    print(F"TYPE: {TOKENS[19]}. LINE: {self.linenum}. TOKEN: {token}")
                elif token == "spc":
                    print(F"TYPE: {TOKENS[20]}. LINE: {self.linenum}. TOKEN: {token}")
                elif token == "rand":
                    print(F"TYPE: {TOKENS[21]}. LINE: {self.linenum}. TOKEN: {token}")
                elif token == ".loop":
                    print(F"TYPE: {TOKENS[22]}. LINE: {self.linenum}. TOKEN: {token}")
                elif token == "stop":
                    print(F"TYPE: {TOKENS[23]}. LINE: {self.linenum}. TOKEN: {token}")
                elif token == "syst":
                    print(F"TYPE: {TOKENS[24]}. LINE: {self.linenum}. TOKEN: {token}")
                elif token == "import":
                    print(F"TYPE: {TOKENS[25]}. LINE: {self.linenum}. TOKEN: {token}")
                elif token == "include":
                    print(F"TYPE: {TOKENS[26]}. LINE: {self.linenum}. TOKEN: {token}")
                elif token == ";;":
                    print(F"TYPE: {TOKENS[27]}. LINE: {self.linenum}. TOKEN: {token}")
                elif token == "pyfunc":
                    print(F"TYPE: {TOKENS[28]}. LINE: {self.linenum}. TOKEN: {token}")
                elif token == "addpfcode":
                    print(F"TYPE: {TOKENS[29]}. LINE: {self.linenum}. TOKEN: {token}")
                elif token == "callpy":
                    print(F"TYPE: {TOKENS[30]}. LINE: {self.linenum}. TOKEN: {token}")
                elif token == "inc":
                    print(F"TYPE: {TOKENS[31]}. LINE: {self.linenum}. TOKEN: {token}")
                elif token == "dec":
                    print(F"TYPE: {TOKENS[32]}. LINE: {self.linenum}. TOKEN: {token}")
                elif token == "createwindow":
                    print(F"TYPE: {TOKENS[33]}. LINE: {self.linenum}. TOKEN: {token}")
                elif token == "windowloop":
                    print(F"TYPE: {TOKENS[34]}. LINE: {self.linenum}. TOKEN: {token}")
                elif token == "join":
                    print(F"TYPE: {TOKENS[35]}. LINE: {self.linenum}. TOKEN: {token}")
                elif token == "notcompa":
                    print(F"TYPE: {TOKENS[36]}. LINE: {self.linenum}. TOKEN: {token}")
                elif token == "read":
                    print(F"TYPE: {TOKENS[37]}. LINE: {self.linenum}. TOKEN: {token}")
                elif token == "write":
                    print(F"TYPE: {TOKENS[38]}. LINE: {self.linenum}. TOKEN: {token}")
                elif token == "append":
                    print(F"TYPE: {TOKENS[39]}. LINE: {self.linenum}. TOKEN: {token}")
                elif token == "systv":
                    print(F"TYPE: {TOKENS[40]}. LINE: {self.linenum}. TOKEN: {token}")
                elif token == "" or token == "\t":
                    pass
                else:
                    print(f"Lexer error: Illegal token {token} at line {self.linenum}")
        
    def checktoken(self):
        lines = self.code.split("\n")

        for line in lines:
            self.linenum += 1
            tokens = line.split()

            for token in tokens:
                if token.isdigit():
                    return TOKENS[0]
                elif token == "pr":
                    return TOKENS[1]
                elif token == "main":
                    return TOKENS[2]
                elif token == "+":
                    return TOKENS[3]
                elif token == "-":
                    return TOKENS[4]
                elif token == "*":
                    return TOKENS[5]
                elif token == "/":
                    return TOKENS[6]
                elif token == "compa":
                    return TOKENS[7]
                elif token == "call":
                    return TOKENS[8]
                elif token == "push":
                    return TOKENS[9]
                elif token == "\"":
                    return TOKENS[10]
                elif token == "nl":
                    return TOKENS[11]
                elif token == ".data":
                    return TOKENS[12]
                elif token == "set":
                    return TOKENS[13]
                elif token == "prv":
                    return TOKENS[14]
                elif token == "func":
                    return TOKENS[15]
                elif token == "addfcode":
                    return TOKENS[16]
                elif token == ">":
                    return TOKENS[17]
                elif token == "strinput":
                    return TOKENS[18]
                elif token == "intinput":
                    return TOKENS[19]
                elif token == "spc":
                    return TOKENS[20]
                elif token == "rand":
                    return TOKENS[21]
                elif token == ".loop":
                    return TOKENS[22]
                elif token == "stop":
                    return TOKENS[23]
                elif token == "syst":
                    return TOKENS[24]
                elif token == "import":
                    return TOKENS[25]
                elif token == "include":
                    return TOKENS[26]
                elif token == ";;":
                    return TOKENS[27]
                elif token == "pyfunc":
                    return TOKENS[28]
                elif token == "addpfcode":
                    return TOKENS[29]
                elif token == "callpy":
                    return TOKENS[30]
                elif token == "inc":
                    return TOKENS[31]
                elif token == "dec":
                    return TOKENS[32]
                elif token == "createwindow":
                    return TOKENS[33]
                elif token == "windowloop":
                    return TOKENS[34]
                elif token == "join":
                    return TOKENS[35]
                elif token == "notcompa":
                    return TOKENS[36]
                elif token == "read":
                    return TOKENS[37]
                elif token == "write":
                    return TOKENS[38]
                elif token == "append":
                    return TOKENS[39]
                elif token == "systv":
                    return TOKENS[40]
                elif token == "" or token == "\t":
                    pass
                else:
                    print(f"Lexer error: Illegal token: {token}")

class Parser:
    def __init__(self, code):
        self.code = code
        self.linenum = 0
        self.loop_code = []
        self.root = ""
    
    def execute1(self):
        in_main = [False]
        in_data = [False]
        in_loop = [False]
        lines = self.code.split("\n")

        for line in lines:
            self.linenum += 1
            tokens = line.split() or line.split("\t")

            if tokens:
                token = tokens[0]

                tokentype = Lexer(token).checktoken()

                if tokentype == TOKENS[2]:
                    in_main[0] = True
                elif tokentype == TOKENS[12]:
                    in_data[0] = True
                elif tokentype == TOKENS[22]:
                    in_loop[0] = True
                elif tokentype == TOKENS[25]:
                    file = tokens[1]
                    with open(file + ".tasm", "r") as fi:
                        content = fi.read()
                    Parser(content).execute1()
                elif tokentype == TOKENS[26]:
                    if pt.system() == "Window":
                        file = tokens[1]
                        with open(f"C:/tastinclude/{file}.tasm", "r") as fi:
                            content = fi.read()
                        Parser(content).execute1()
                    else:
                        file = tokens[1]
                        with open(f"/usr/local/bin/tastinclude/{file}.tasm", "r") as fi:
                            content = fi.read()
                        Parser(content).execute1()
                elif tokentype == TOKENS[27]:
                    pass

                if in_main[0]:
                    if tokentype == TOKENS[0]:
                        num1 = token
                        operator = Lexer(tokens[1]).checktoken()
                        num2 = Lexer(tokens[2]).checktoken()
                        if operator == TOKENS[3]:
                            if num2 == TOKENS[0]:
                                print(int(num1) + int(tokens[2]))
                        elif operator == TOKENS[4]:
                            if num2 == TOKENS[0]:
                                print(int(num1) - int(tokens[2]))
                        elif operator == TOKENS[5]:
                            if num2 == TOKENS[0]:
                                print(int(num1) * int(tokens[2]))
                        elif operator == TOKENS[6]:
                            if num2 == TOKENS[0]:
                                print(int(num1) / int(tokens[2]))
                    elif tokentype == TOKENS[9]:
                        pushtype = Lexer(tokens[1]).checktoken()
                        if pushtype == TOKENS[1]:
                            msg = tokens[2:]
                            finalmsg = " ".join(msg)
                            print(f"{finalmsg}", end="")
                        elif pushtype == TOKENS[11]:
                            print("")
                        elif pushtype == TOKENS[20]:
                            print(" ", end="")
                        elif pushtype == TOKENS[14]:
                            varname = tokens[2]
                            print(variables.get(varname), end="")
                    elif tokentype == TOKENS[8]:
                        funcname = tokens[1]
                        finalfuncode = "\n".join(functions.get(funcname))
                        Parser(finalfuncode).execute2()
                    elif tokentype == TOKENS[7]:
                        funcname = tokens[1]
                        varname1 = tokens[2]
                        varname2 = tokens[3]
                        if variables.get(varname1) == variables.get(varname2):
                            finalfuncode = "\n".join(functions.get(funcname))
                            Parser(finalfuncode).execute2()
                    elif tokentype == TOKENS[18]:
                        varname = tokens[1]
                        variables[varname] = input()
                    elif tokentype == TOKENS[19]:
                        varname = tokens[1]
                        variables[varname] = int(input())
                    elif tokentype == TOKENS[21]:
                        number1 = int(tokens[1])
                        number2 = int(tokens[2])
                        varname = tokens[3]
                        variables[varname] = randint(number1, number2)
                    elif tokentype == TOKENS[24]:
                        command = tokens[1:]
                        finalcommand = " ".join(command)
                        subprocess.run(finalcommand, shell=True)
                    elif tokentype == TOKENS[30]:
                        funcname = tokens[1]
                        finalfuncode = "\n".join(pyfunctions.get(funcname))
                        exec(finalfuncode)
                    elif tokentype == TOKENS[31]:
                        varname1 = tokens[1]
                        varname2 = tokens[2]
                        variables[varname1] += variables.get(varname2)
                    elif tokentype == TOKENS[32]:
                        varname1 = tokens[1]
                        varname2 = tokens[2]
                        variables[varname1] -= variables.get(varname2)
                    elif tokentype == TOKENS[33]:
                        self.root = tk.Tk()
                        self.root.config(width=variables["width"], height=variables["height"])
                        self.root.title(variables["title"])
                    elif tokentype == TOKENS[34]:
                        self.root.mainloop()
                    elif tokentype == TOKENS[35]:
                        varname1 = tokens[1]
                        varname2 = tokens[2]
                        outputvar = tokens[3]
                        variables[outputvar] = variables.get(varname1) + " " + variables.get(varname2)
                    elif tokentype == TOKENS[36]:
                        funcname = tokens[1]
                        varname1 = tokens[2]
                        varname2 = tokens[3]
                        if variables.get(varname1) != variables.get(varname2):
                            finalfunccode = "\n".join(functions.get(funcname))
                            Parser.execute2(finalfunccode)
                    elif tokentype == TOKENS[37]:
                        varfilename = tokens[1]
                        outputvarname = tokens[2]
                        with open(variables.get(varfilename), "r") as fi:
                            content = fi.read()
                        variables[outputvarname] = content
                    elif tokentype == TOKENS[38]:
                        varfilename = tokens[1]
                        varname = tokens[2]
                        with open(variables.get(varfilename), "w") as fi:
                            fi.write(variables.get(varname) + "\n")
                    elif tokentype == TOKENS[39]:
                        varfilename = tokens[1]
                        varname = tokens[2]
                        with open(variables.get(varfilename), "a") as fi:
                            fi.write(variables.get(varname) + "\n")
                    elif tokentype == TOKENS[40]:
                        varname = tokens[1]
                        subprocess.run(variables.get(varname), shell=True)
                    elif tokentype == TOKENS[2]:
                        pass
                    elif token == "":
                        in_main[0] = False
                    else:
                        print(f"Parser error: Illegal token {token} in line: {self.linenum}")
                elif in_loop[0]:
                    if tokentype == TOKENS[22]:
                        pass
                    elif token == "":
                        in_loop[0] = False
                        finalloopcode = "\n".join(self.loop_code)
                        running_loop[0] = True
                        while running_loop[0]:
                            Parser(finalloopcode).execute2()
                    else:
                        self.loop_code.append(" ".join(tokens))
                elif in_data[0]:
                    if tokentype == TOKENS[13]:
                        varname = tokens[1]
                        valuetype = Lexer(tokens[2]).checktoken()
                        if valuetype == TOKENS[0]:
                            variables[varname] = int(tokens[2])
                        elif valuetype == TOKENS[10]:
                            value = tokens[3:]
                            finalvalue = " ".join(value)
                            variables[varname] = finalvalue
                        else:
                            print(f"Parser error: Illegal token: {tokens[2]} in line: {self.linenum}. use an integer value")
                    elif tokentype == TOKENS[15]:
                        funcname = tokens[1]
                        functions[funcname] = []
                    elif tokentype == TOKENS[16]:
                        funcname = tokens[1]
                        starttype = Lexer(tokens[2]).checktoken()
                        if starttype == TOKENS[17]:
                            codee = tokens[3:]
                            finalcode = " ".join(codee)
                            functions[funcname].append(finalcode)
                    elif tokentype == TOKENS[28]:
                        funcname = tokens[1]
                        pyfunctions[funcname] = []
                    elif tokentype == TOKENS[29]:
                        funcname = tokens[1]
                        starttype = Lexer(tokens[2]).checktoken()
                        if starttype == TOKENS[17]:
                            codee = tokens[3:]
                            finalcode = " ".join(codee)
                            pyfunctions[funcname].append(finalcode)
                    elif token == "":
                        in_data[0] = False
                    elif tokentype == TOKENS[12]:
                        pass
                    else:
                        print(f"Parser error: Illegal token {token} in line: {self.linenum}")

    def execute2(self):
        lines = self.code.split("\n")

        for line in lines:
            self.linenum += 1
            tokens = line.split()

            if tokens:
                token = tokens[0]

                tokentype = Lexer(token).checktoken()

                if tokentype == TOKENS[0]:
                    num1 = token
                    operator = Lexer(tokens[1]).checktoken()
                    num2 = Lexer(tokens[2]).checktoken()
                    if operator == TOKENS[3]:
                        if num2 == TOKENS[0]:
                            print(int(num1) + int(tokens[2]))
                    elif operator == TOKENS[4]:
                        if num2 == TOKENS[0]:
                            print(int(num1) - int(tokens[2]))
                    elif operator == TOKENS[5]:
                        if num2 == TOKENS[0]:
                            print(int(num1) * int(tokens[2]))
                    elif operator == TOKENS[6]:
                        if num2 == TOKENS[0]:
                            print(int(num1) / int(tokens[2]))
                elif tokentype == TOKENS[9]:
                    pushtype = Lexer(tokens[1]).checktoken()
                    if pushtype == TOKENS[1]:
                        msg = tokens[2:]
                        finalmsg = " ".join(msg)
                        print(f"{finalmsg}", end="")
                    elif pushtype == TOKENS[11]:
                        print("")
                    elif pushtype == TOKENS[20]:
                        print(" ", end="")
                    elif pushtype == TOKENS[14]:
                        varname = tokens[2]
                        print(variables.get(varname), end="")
                elif tokentype == TOKENS[8]:
                    funcname = tokens[1]
                    finalfuncode = "\n".join(functions.get(funcname))
                    Parser(finalfuncode).execute2()
                elif tokentype == TOKENS[7]:
                    funcname = tokens[1]
                    varname1 = tokens[2]
                    varname2 = tokens[3]
                    if variables.get(varname1) == variables.get(varname2):
                        finalfuncode = "\n".join(functions.get(funcname))
                        Parser(finalfuncode).execute2()
                elif tokentype == TOKENS[18]:
                    varname = tokens[1]
                    variables[varname] = input()
                elif tokentype == TOKENS[19]:
                    varname = tokens[1]
                    variables[varname] = int(input())
                elif tokentype == TOKENS[21]:
                    number1 = int(tokens[1])
                    number2 = int(tokens[2])
                    varname = tokens[3]
                    variables[varname] = randint(number1, number2)
                elif tokentype == TOKENS[23]:
                    running_loop[0] = False
                elif tokentype == TOKENS[24]:
                    command = tokens[1:]
                    finalcommand = " ".join(command)
                    subprocess.run(finalcommand, shell=True)
                elif tokentype == TOKENS[30]:
                    funcname = tokens[1]
                    finalfuncode = "\n".join(pyfunctions.get(funcname))
                    exec(finalfuncode)
                elif tokentype == TOKENS[31]:
                    varname1 = tokens[1]
                    varname2 = tokens[2]
                    variables[varname1] += variables.get(varname2)
                elif tokentype == TOKENS[32]:
                    varname1 = tokens[1]
                    varname2 = tokens[2]
                    variables[varname1] -= variables.get(varname2)
                elif tokentype == TOKENS[33]:
                    self.root = tk.Tk()
                    self.root.config(width=variables["width"], height=variables["height"])
                    self.root.title(variables["title"])
                    self.root.mainloop()
                elif tokentype == TOKENS[34]:
                    self.root.mainloop()
                elif tokentype == TOKENS[35]:
                    varname1 = tokens[1]
                    varname2 = tokens[2]
                    outputvar = tokens[3]
                    variables[outputvar] = variables.get(varname1) + " " + variables.get(varname2)
                elif tokentype == TOKENS[36]:
                    funcname = tokens[1]
                    varname1 = tokens[2]
                    varname2 = tokens[3]
                    if variables.get(varname1) != variables.get(varname2):
                        finalfunccode = "\n".join(functions.get(funcname))
                        Parser(finalfunccode).execute2()
                elif tokentype == TOKENS[37]:
                    varfilename = tokens[1]
                    outputvarname = tokens[2]
                    with open(variables.get(varfilename), "r") as fi:
                        content = fi.read()
                    variables[outputvarname] = content
                elif tokentype == TOKENS[38]:
                    varfilename = tokens[1]
                    varname = tokens[2]
                    with open(variables.get(varfilename), "w") as fi:
                        fi.write(variables.get(varname) + "\n")
                elif tokentype == TOKENS[39]:
                    varfilename = tokens[1]
                    varname = tokens[2]
                    with open(variables.get(varfilename), "a") as fi:
                        fi.write(variables.get(varname) + "\n")
                elif tokentype == TOKENS[40]:
                    varname = tokens[1]
                    subprocess.run(variables.get(varname), shell=True)
                else:
                    print(f"Parser error: Illegal token {token} in line: {self.linenum}")

if __name__ == "__main__":
    version = "1.0"
    if len(sys.argv) == 1:
        print(f"Usage: {sys.argv[0]} <command>")
        print("commands:")
        print("-v               version")
        print("-d               debug your tokens")
        print("<file>           executes your file")
    else:
        command = sys.argv[1]

        if command == "-v":
            print(f"Version: {version}")
            print("Tast comes from nasm")
        elif command == "-d":
            file = sys.argv[2]
            if file.endswith(".tasm"):
                with open(file, "r") as f:
                    lexer = Lexer(f.read())
                    lexer.printtoken()
            else:
                print("Use a .tasm file extension!")
        else:
            if command.endswith(".tasm"):
                with open(command, "r") as f:
                    parser = Parser(f.read())
                    parser.execute1()
            else:
                print("Use a .tasm file extension!")

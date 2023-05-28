# Synta - 2023_5_28 Copyright (c) gamma-410 

import sys

str_variable = {}
int_variable = {}
float_variable = {}
bool_variable = {}


def main():
    inputSource(sys.argv[1])


def inputSource(fileName):
    f = open(fileName, 'r', encoding='UTF-8')
    for data in f:
        source = data.rstrip('\n')
        splitSource(source)

    f.close()


def sourceSplit(string):
    result = []
    current = ""
    is_quoted = False

    for char in string:
        if char == '"':
            is_quoted = not is_quoted
            current += char

        elif char == ' ' and not is_quoted:
            if current:
                result.append(current)
                current = ""

        else:
            current += char

    if current:
        result.append(current)

    return result


def splitSource(s):
    data = sourceSplit(s)
    executionSource(data)    


def executionSource(cmd):

    if cmd != []:
        if cmd[0] == "let":
            if cmd[2] == "String":
                str_variable[cmd[1]] = str(cmd[4]).replace('"', '')
            elif cmd[2] == "Int":
                int_variable[cmd[1]] = int(cmd[4])
            elif cmd[2] == "Float":
                float_variable[cmd[1]] = float(cmd[4])
            elif cmd[2] == "Bool":
                bool_variable[cmd[1]] = cmd[4]

        elif cmd[0] == "print":
            if cmd[1] == "String":
                print(str(str_variable[cmd[2]]))
            elif cmd[1] == "Int":
                print(int(int_variable[cmd[2]]))
            elif cmd[1] == "Float":
                print(float(float_variable[cmd[2]]))
            elif cmd[1] == "Bool":
                print(bool(bool_variable[cmd[2]]))

        elif cmd[0] == "type":
            if bool(cmd[1] in str_variable):
                print("String")
            elif bool(cmd[1] in int_variable):
                print("Int")
            elif bool(cmd[1] in float_variable):
                print("Float")
            elif bool(cmd[1] in bool_variable):
                print("Bool")
        
        elif cmd[0] == "input":
            if cmd[1] == "String":
                res = input(cmd[2].replace('"', ''))
                str_variable[cmd[4]] = res
            elif cmd[1] == "Int":
                res = input(cmd[2].replace('"', ''))
                int_variable[cmd[4]] = res    
            elif cmd[1] == "Float":
                res = input(cmd[2].replace('"', ''))
                float_variable[cmd[4]] = res
            elif cmd[1] == "Bool":
                res = input(cmd[2].replace('"', ''))
                bool_variable[cmd[4]] = res

        elif cmd[0] == "calc":
            if cmd[1] == "Int":
                A = int_variable[cmd[2]]
                B = int_variable[cmd[4]]
                
                if cmd[3] == "+":
                    C = A + B
                elif cmd[3] == "-":
                    C = A - B
                elif cmd[3] == "*":
                    C = A * B
                elif cmd[3] == "/":
                    C = A / B
                elif cmd[3] == "%":
                    C = A % B
                
                int_variable[cmd[6]] = C

            elif cmd[1] == "Float":
                A = float_variable[cmd[2]]
                B = float_variable[cmd[4]]
                
                if cmd[3] == "+":
                    C = A + B
                elif cmd[3] == "-":
                    C = A - B
                elif cmd[3] == "*":
                    C = A * B
                elif cmd[3] == "/":
                    C = A / B
                elif cmd[3] == "%":
                    C = A % B
                
                float_variable[cmd[6]] = C


if __name__ == "__main__":
    main()
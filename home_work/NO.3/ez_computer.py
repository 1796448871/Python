operand1, operator, operand2 = input().split()

operand1 = int(operand1)
operand2 = int(operand2)


if operator == '+':
    result = operand1 + operand2
    print(result)
elif operator == '-':
    result = operand1 - operand2
    print(result)
elif operator == '*':
    result = operand1 * operand2
    print(result)
elif operator == '/':
    if operand2 != 0:
        result = operand1 / operand2
        print(result)
    else:
        print("ERROR")
elif operator == '%':
    if operand2 != 0:
        result = operand1 % operand2
        print(result)
    else:
        print("ERROR")
else:
    print("ERROR")
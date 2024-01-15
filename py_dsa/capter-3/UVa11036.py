def evaluate_rpn(expression, x, N):
    stack = []
    operators = {'+': lambda a, b: a + b, '*': lambda a, b: a * b, '%': lambda a, b: a % b}

    for token in expression.split():
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            stack.append(int(token))
        elif token == 'x':
            stack.append(x)
        elif token == 'N':
            stack.append(N)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = operators[token](operand1, operand2)
            stack.append(result)

    return stack[0]

def find_period(input_lines):
    for line in input_lines:
        N, n, expression = line.split()[:-1]
        N, n = int(N), int(n)
        result = evaluate_rpn(expression, n, N)
        print(result)

if __name__ == "__main__":
    input_lines = []
    while True:
        line = input().strip()
        if line == '0 0 0 N %':
            break
        input_lines.append(line)

    find_period(input_lines)

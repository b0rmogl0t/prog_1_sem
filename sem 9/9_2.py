def value(expr):
    stack = []

    def basic_ops(op, opd1, opd2):
        if op == '+':
            return opd1 + opd2
        elif op == '-':
            return opd1 - opd2
        elif op == '*':
            return opd1 * opd2
        elif op == '/':
            if opd2 != 0:
                return opd1 / opd2


    # operators = set(['+', '-', '*', '/'])
    op = ['+', '-', '*', '/']

    try:
        for x in expr.split():
            if x.isdigit() or (x[0] == '-' and x[1:].isdigit()):
                stack.append(float(x))
            elif x in op:
                if len(stack) < 2:
                    raise ValueError("invalid expression")
                opd2 = stack.pop()
                opd1 = stack.pop()
                res = basic_ops(x, opd1, opd2)
                stack.append(res)
            else:
                raise ValueError("invalid expression")

        if len(stack) == 1:
            return stack[0]
        else:
            raise ValueError("invalid expression")

    except ValueError as e:
        return str(e)



expr = str(input())
res = value(expr)
print(res)

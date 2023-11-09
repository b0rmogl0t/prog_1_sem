def inf_post(in_expr):
    op_stack = []
    out_expr = []

    ops = {'-': 0,
           '+': 1,
           '/': 2,
           '*': 3}

    for x in in_expr:
        if x in ops.keys():
            while (len(op_stack) != 0
                   and op_stack[-1] != '('
                   and ops[x] <= ops[op_stack[-1]]):
                out_expr.append(op_stack.pop())
            op_stack.append(x)

        elif x == '(':
            op_stack.append(x)
        elif x == ')':
            while op_stack[-1] != '(':
                out_expr.append(op_stack.pop())
            op_stack.pop()

        else:
            out_expr.append(x)

    while len(op_stack) != 0:
        out_expr.append(op_stack.pop())

    return out_expr


in_expr = list(input())
post = inf_post(in_expr)
print("postfix notation:", *post)
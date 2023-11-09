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



def inf_pref(in_expr):
    rev_expr = in_expr[::-1]
    for i in range(len(rev_expr)):
        if rev_expr[i] == '(':
            rev_expr[i] = ')'
        elif rev_expr[i] == ')':
            rev_expr[i] = '('

    post_expr = inf_post(rev_expr)
    out_expr = post_expr[::-1]
    return out_expr


in_expr = list(input())
post = inf_post(in_expr)
pref = inf_pref(in_expr)

print("infix notation:", *in_expr)
print("postfix notation:", *post)
print("prefix notation:", *pref)

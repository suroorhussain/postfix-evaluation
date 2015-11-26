def evaluate(stack, element) :
    if element == '+' :        
        stack.append(stack.pop() + stack.pop())        
    elif element == '-' :        
        stack.append(stack.pop() - stack.pop())        
    elif element == '*' :        
        stack.append(stack.pop() * stack.pop())        
    else :        
        stack.append(stack.pop() / stack.pop())        

def end_of_expr(expr, expr_pointer) :
    if expr_pointer == len(expr) :
        return True
    else :
        return False

def postfix_eval(expr) :
    op_list = ['+', '-', '*', '/']
    stack = []
    expr_pointer = 0
    for element in expr:
        if element in op_list :
             evaluate(stack, element)
        else :
            stack.append(int(element))
        if end_of_expr(expr, expr_pointer) :
            break
    return stack.pop()
    # print stack.pop()

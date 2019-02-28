
def s2i(s):
    return int(s)

def is_operator(item):
    # "/"-> true, 3-> false, "3" -> true :(
    #return type(item) == str
    return item in {'+', '-', '*', '/'}

#print('I am: {}'.format(__name__))

def perform_operation(op1, op2, operator):
    if operator == '+':
        res = op1 + op2
    elif operator == '-':
        res = op1 - op2
    elif operator == '*':
        res = op1 * op2
    elif operator == '/':
        res = op1 / op2
    else:
        raise Exception("Unknonw operand {}".format(operator))
    return res

def convert_rpn_string_to_rpn_list(rpn_str):
    l = rpn_str.split()
    return convert_string_list_to_rpn_list(l)

def convert_string_list_to_rpn_list(str_list):
    l = []
    for item in str_list:        
        if not is_operator(item):
            l.append(s2i(item))
        else: 
            l.append(item)
    return l



def is_valid_rpn_stack(s):
    return len(s) >= 3 and is_operator(s[-1])

#pre: s es una llista(stack) rpn computable vàlida 
def compute_stack(s):
    operator = s.pop()
    op2 = s.pop()
    op1 = s.pop()

    res = perform_operation(op1, op2, operator)
    s.append(res)
    return s




def extract_rpn_block(rpn_list, rpn_stack):

    #return rpn_list.split()
    #rpn block stack to perfrom 1 single operation
    
    rpn_block_array = []

    while not is_operator(rpn_list[0]):
        rpn_stack.append(rpn_list.pop(0))
    rpn_stack.append(rpn_list.pop(0)) #afegim el operator
    rpn_block_array.append(rpn_stack[-3])
    rpn_block_array.append(rpn_stack[-2])
    rpn_block_array.append(rpn_stack[-1])
    return (rpn_block_array, rpn_stack, rpn_list)




def compute_block(op_array):
    op1, op2, operator = op_array
    return perform_operation(op1, op2, operator)


def form_infix_string(op1, op2, operand):
    op1 = str(op1)
    op2 = str(op2)
    return '(' + op1 + operand + op2 + ')'


def perform_rpn(rpn_list):
    rpn_stack = []
    while len(rpn_list) > 1 or len(rpn_stack) > 1 :
        if is_valid_rpn_stack(rpn_stack):
           rpn_stack = compute_stack(rpn_stack)    
        else:
            rpn_block_array, rpn_stack, rpn_list = extract_rpn_block(rpn_list, rpn_stack)        
    result = rpn_stack[0]
    result = '%.2f'%(result)
    return float(result)

def convert_postfix_list_to_string(l): 
    res = ''
    for item in l:
        #res += l.pop(0)
        res += item

    #chapusa per treure el primer parentesis i el ultim
    if res.startswith('(') and res.endswith(')'):
        res = res[1:-1]

    return res


def xtest_main1():
    pass
    #assert main("2 1 12 3 / - +") == '-1'

def prompt(str):
    return input(str)

def convert_string_postfix_to_infix(s):

    postfix_list = convert_rpn_string_to_rpn_list(s)
    postfix_stack = []

    while len(postfix_list) >= 1 : 
        item = postfix_list.pop(0)
        if not is_operator(item): #item is an operand
            postfix_stack.append(item)
        else: #item is an operator or an infix operand block
            op2 = postfix_stack.pop()
            op1 = postfix_stack.pop()
            infix_op = form_infix_string(op1, op2, item)
            postfix_stack.append(infix_op)
    
    result_in_string = convert_postfix_list_to_string(postfix_stack)
    return result_in_string

def main():
    print("quit to quit")
    while True:    
        s = prompt('> ')
        if s == "quit":
            break
        rpn_l = convert_rpn_string_to_rpn_list(s)
        infix_exp = convert_string_postfix_to_infix(s)
        result = perform_rpn(rpn_l)
        print ( str(infix_exp) + ' = ' + str(result) )


def calculate_response(input):
    rpn_l = convert_rpn_string_to_rpn_list(input)
    output = perform_rpn(rpn_l)
    return output


if __name__ == '__main__':
    main()
    

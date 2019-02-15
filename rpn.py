

#definir los tests de py.test con el prefijo "test_"
def test_plus_is_operator():
    assert is_operator('+')

def test_is_not_operator():
    assert not is_operator(42)


def test_convert_string42_to_int():
    assert s2i('42') == 42

def test_convert_string43_to_int():
    assert s2i('43') == 43

def test_process_single_sum():
    assert compute_block([3,4, '+']) == 7

def test_process_single_sum2():
    assert compute_block([3,3, '+']) == 6

def test_process_single_substraction():
    assert compute_block([3,3,'-']) == 0

def test_process_single_mult():
    assert compute_block([3,-3,'*']) == -9
    
def test_process_single_div():
    assert compute_block([8,4,'/']) == 2
    
def test_process_single_div_float():
    assert compute_block([3,2,'/']) == 1.5




def test_is_operator1():
    assert not is_operator('3') # no puc posar  ==false
    
def test_is_operator2():
    assert is_operator('8') == False
    
def test_is_operator3():
    assert not is_operator(8)

def test_is_operator4():
    assert not is_operator(42)

def test_is_operator5():
    assert is_operator('+')
    
def test_is_operator6():
    assert is_operator('/')




def test_string_to_list():
    assert convert_rpn_string_to_rpn_list("4 2 +") == [4, 2,'+']



def test_convert_string_list_to_rpn_list():
    assert convert_string_list_to_rpn_list(['3', '4', '+']) == [3, 4, '+']



def test_valid_stack1():
    assert is_valid_rpn_stack([3,4,5,'*'])

def test_valid_stack2():
    assert not is_valid_rpn_stack([3,4,5,'+',4])

def test_valid_stack3():
    assert not is_valid_rpn_stack([3,'+'])





def test_compute_stack_single_computation():
    assert compute_stack([8, 10, '+']) == [18]  

def test_compute_stack_2():
    assert compute_stack([8,2,8,'+']) == [8,10]  

def test_compute_stack_3():
    assert compute_stack([1,9,8,'-']) == [1 ,1] 

def test_compute_stack_4():
    assert compute_stack([8,2,8,'/']) == [8,0.25] 

def test_compute_stack_5():
    assert compute_stack([8,2,0.5,'*']) == [8,1] 



def test_read_block1():
    assert extract_rpn_block([3,4,'+'], []) == ([3,4,'+'], [3,4,'+'], [])

def test_read_block2():
    assert extract_rpn_block([8,2, 5, 3,'+', '+', '+'], []) == ([5,3,'+'], [8,2,5,3,'+'], ['+','+'])



def test_prform_rpn1():
    assert perform_rpn([3, 4, '+']) == 7

def test_prform_rpn2():
    assert perform_rpn([4, 2, '+', 3, '-']) == 3
    
def test_prform_rpn3():
    assert perform_rpn([8, 2, 5, 3, '+', '+', '+']) == 18

def test_prform_rpn4():
    assert perform_rpn([2,1,12,3,'/','-','+']) == -1
   
def test_prform_rpn5():
    assert perform_rpn([8 ,2, '/', 9, '*', 36, 3, '/', '+', 8, 6, '*', 11, '/', '-']) == 43.64


def s2i(s):
    return int(s)

def is_operator(item):
    # "/"-> true, 3-> false, "3" -> true :(
    #return type(item) == str
    return item == '+' or item == '-' or item == '*' or item == '/'
    

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

# def compute(input_string):
#     op_array = read_rpn_block(input_string)
#     return compute_block(op_array)



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

def xtest_main1():
    pass
    #assert main("2 1 12 3 / - +") == '-1'

def prompt(str):
    return input(str)

def main():
    print("quit to quit")
    while True:    
        s = prompt('> ')
        if s == "quit":
            break
        rpn_l = convert_rpn_string_to_rpn_list(s)
        result = perform_rpn(rpn_l)
        print (result)

if __name__ == '__main__':
    main()
    
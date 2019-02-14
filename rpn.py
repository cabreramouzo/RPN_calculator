

#definir los tests de py.test con el prefijo "test_"
def test_plus_is_operator():
    assert is_operator('+')

def test_is_not_operator():
    assert not is_operator(42)

def test_read_rpn_block_3_4_plus():
    assert read_rpn_block('3 4 +') == [3,4,'+']

def test_read_rpn_block_3_4_plus_8_plus():
    assert read_rpn_block('3 4 + 8 +') == [3,4,'+']

def test_read_rpn_block_2_11_minus_12_plus():
    assert read_rpn_block('2 11 - 12 +') == [2,11,'-']

def test_compute_block_from_string():
    assert compute('3 4 +') == 7

def test_compute_block_from_string_2():
    assert compute('3 3 -') == 0

def test_convert_string42_to_int():
    assert s2i('42') == 42

def test_convert_string43_to_int():
    assert s2i('43') == 43

def s2i(s):
    return int(s)

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


#pre: string es una sequencia d operadors i operands vàlida en rpn.
#post: rpn_stack es una llista amb els operands i operadors ordenats segons notació rpn que tractarem com una pila.  
def read_stack(string):
    rpn_stack = []
    rpn_stack.append(20)
    rpn_stack.append(5)
    rpn_stack.append('/')
    return rpn_stack
    
def test_is_operator1():
    assert not is_operator('3') # no puc posar  ==false
    
def test_is_operator2():
    assert not is_operator('8')
    
def test_is_operator3():
    assert not is_operator(8)

def test_is_operator4():
    assert not is_operator(42)

def test_is_operator5():
    assert is_operator('+')
    
def test_is_operator6():
    assert is_operator('/')


def is_operator(item):
    # "/"-> true, 3-> false, "3" -> true :(
    #return type(item) == str
    return item == '+' or item == '-' or item == '*' or item == '/'
    

#mejor llamar perform_operation
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

""" 
def calc_rpn(rpn_list):
    result = 0
    #casos especiales
    if len(rpn_list) == 1:
        #if rpn_stack[0].type....?
        result = rpn_list[0]
    else:
        while len(rpn_list) > 1: 
            #la primera vegda ha d'entrar per collons perque una ristra de rpn  acaba sempre en operador
            item_act = rpn_list.pop()
            while is_operator(item_act):
                op2 = rpn_list.pop() #el orden cuenta, op2 es el primer pop
                op1 = rpn_list.pop()
                res = perform_operation(op1, op2, item_act) #item_act es un operator
                rpn_list.append(res)
                item_act = rpn_list.pop()
        result = item_act #item_act es el resultat ja que era l'ultim item a la pila
        return result """


def test_string_to_list():
    assert convert_rpn_string_to_rpn_list("4 2 +") == [4, 2,'+']

def convert_rpn_string_to_rpn_list(rpn_str):
    l = rpn_str.split()
    return convert_string_list_to_rpn_list(l)

def test_convert_string_list_to_rpn_list():
    assert convert_string_list_to_rpn_list(['3', '4', '+']) == [3, 4, '+']

def convert_string_list_to_rpn_list(str_list):
    l = []
    for item in str_list:        
        if not is_operator(item):
            l.append(s2i(item))
        else: 
            l.append(item)
    return l


def read_rpn_block(rpn_list):
    return convert_rpn_string_to_rpn_list(rpn_list)[:3]
    #return rpn_list.split()
    #rpn block stack to perfrom 1 single operation
    # rpn_block_array = []
    # while len(rpn_list) >= 3 and not is_operator(rpn_list[0]) :
    #     rpn_block_array.append(rpn_list.pop(0)) #op1
    #     rpn_block_array.append(rpn_list.pop(0)) #op2
    # operator = rpn_list.pop(0)
    # rpn_block_array.append(operator)
    # return rpn_block_array


def compute_block(op_array):
    op1, op2, operator = op_array
    return perform_operation(op1, op2, operator)

def compute(input_string):
    op_array = read_rpn_block(input_string)
    return compute_block(op_array)


def main():
    pass

    #rpn_stack = read_stack("hola")
    #rpn_list = [3,5,8, '*', 7,'+', '*']
    #array_rpn = read_rpn_block(rpn_list)
    #result = calc_rpn(rpn_stack)
    #print (result)


    #for line in sys.stdin:
        #cs = line.split()

if __name__ == '__main__':
    main()
    
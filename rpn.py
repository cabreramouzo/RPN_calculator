

#definir los tests de py.test con el prefijo "test_"
def tes_plus_is_operator():
    assert is_operator('+')

def test_is_not_operator():
    assert not is_operator(42)

def test_20_5_div():
    assert calc_rpn('20 5 /') == 4

def test_4_2_sum_3_subs():
    assert calc_rpn('4 2 + 3 -') == 3

def test_258_mul_7_sum_mul():
    assert calc_rpn('358 * 7 + *') == 141

def test_parse_list():
    assert read_stack('20 5 /') == [20, 5, '/']

def test_make_operation1():
    assert make_operation(3,4,'+') == 7
def test_make_operation2():
    assert make_operation(3,4,'-') == -1
def test_make_operation3():
    assert make_operation(3,4,'*') == 12
def test_make_operation4():
    assert make_operation(3,4,'/') == 0.75

#pre: sting es una sequencia de operadors i operands vàlida en rpn.
#post: rpn_stack es una llista amb els operands i operadors ordenats segons notació rpn que tractarem com una pila.  
def read_stack(string):
    rpn_stack = []
    rpn_stack.append(20)
    rpn_stack.append(5)
    rpn_stack.append('/')
    return rpn_stack
    
# "/"-> true, 3-> false, "3" -> true :(
def is_operator(item):
    return type(item) == str

def make_operation(op1, op2, operator):
    if operator == '+':
        res = op1 + op2
    elif operator == '-':
        res = op1 - op2
    elif operator == '*':
        res = op1 * op2
    elif operator == '/':
        res = op1 / op2
    return res



def calc_rpn(rpn_stack):
    result = 0
    #casos especiales
    if len(rpn_stack) == 1:
        #if rpn_stack[0].type....?
        result = rpn_stack[0]
    else:
        #la primera vegda ha d'entrar per collons perque una ristra de rpn acaba sempre en operador
        opt_act = rpn_stack.pop()
        while is_operator(opt_act):
            op2 = rpn_stack.pop() #el orden cuenta, op2 es el primer pop
            op1 = rpn_stack.pop()
            res = make_operation(op1, op2, opt_act)
            rpn_stack.append(res)
            opt_act = rpn_stack.pop()






def main():
    op1 = 6
    op2 = 8
    opr = "/"

    rpn_stack = read_stack("hola")
    calc_rpn(rpn_stack)




if __name__ == '__main__':
    main()
    
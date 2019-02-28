from calculator.rpn import *


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


def test_form_infix_string():
    assert form_infix_string(3,4,'+') == "(3+4)"

def test_form_infix_string2():
    assert form_infix_string("(3+4)",4,'+') == "((3+4)+4)"

def test_form_infix_string3():
    assert form_infix_string("(3+4)","(8/2)",'*') == "((3+4)*(8/2))"


    
def test_convert_postfix_list_to_string():
    assert convert_postfix_list_to_string( ['(' , '(3+4)' , '*', '(8*2)', ')'] ) == "(3+4)*(8*2)"

def test_convert_postfix_list_to_string2():
    assert convert_postfix_list_to_string( ['(' , '(3+4)' , '*', '8', ')'] ) == "(3+4)*8"

def xtest_convert_postfix_list_to_string3():
    assert convert_postfix_list_to_string( ['(6*2)' , '/', '(2*2)'] ) == "(6*2)/(2*2)"
    


def test_convert_postfix_to_infix():
   assert convert_string_postfix_to_infix("3 4 5 + +") == "3+(4+5)"

def test_convert_postfix_to_infix2():
    assert convert_string_postfix_to_infix("3 5 8 * 7 + *") == "3*((5*8)+7)"



def test_rpn_calc():
    assert calculate_response('2 2 +') == 4

def test_rpn_calc2():
    assert calculate_response('2 3 *') == 6

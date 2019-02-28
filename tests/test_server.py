from calculator.server import *

#pattern1

def test_search_for_invalid_operator_plus():
    assert search_for_invalid_operator("3 4+")
def test_search_for_invalid_operator_minus():
    assert search_for_invalid_operator("3 4-")
def test_search_for_invalid_operator_mult():
    assert search_for_invalid_operator("3 4*")
def test_search_for_invalid_operator_div():
    assert search_for_invalid_operator("3 4/")

def test_search_for_invalid_operator_complex1():
    assert search_for_invalid_operator("3 4 + 4 4+ +")
def test_search_for_invalid_operator_complex2():
    assert search_for_invalid_operator(" 8 8* 7 7 + +")
def test_search_for_invalid_operator_complex3():
    assert search_for_invalid_operator(" 8 8 *7 7 + +")


def test_search_for_invalid_operator_simple_valid():
    assert not search_for_invalid_operator("3 4 + 4 4 + +")



#pattern 2
def test_search_for_invalid_operator_plus_pattern2():
    assert search_for_invalid_operator("3 4 +3 3 + +")
def test_search_for_invalid_operator_minupattern2s():
    assert search_for_invalid_operator("3 4 -3 3 + +")
def test_search_for_invalid_operator_multpattern2():
    assert search_for_invalid_operator("3 4 *3 3 + +")
def test_search_for_invalid_operator_divpattern2():
    assert search_for_invalid_operator("3 4 /3 3 + +")

#TODO: pattern 3 -> ++, /*, -+

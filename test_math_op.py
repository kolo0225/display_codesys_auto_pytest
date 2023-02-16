# test_math_op.py

# Purpose:
#   to test math operation of codesys

# note:
#   the data are taken from the "results.scv" file

# import files/classes
from assign_1_type_to_df_col import AssignType2ListOfDfGrCol

# package
import numpy as np
import pytest

# Arguments:
path_in       = r"C:\Users\AnastasiosKolovos\AK\codesys_me\python_codesys\pytest_codesys\results.csv"
remove_str    = "REAL#"
var_in0       = "PLC_PRG.VAR_A"
var_in1       = "PLC_PRG.VAR_B"
var_out0      = "PLC_PRG.ADD_OUT"
var_out1      = "PLC_PRG.SUB_OUT"
var_out2      = "PLC_PRG.MUL_OUT"
var_list      = np.array ([var_in0, var_in1,var_out0,var_out1,var_out2])
data_type     = "float64"


# call real number input arrays
# input_a
obj_AssignType2ListOfDfGrCol0 = AssignType2ListOfDfGrCol(path_in, remove_str, var_list[0], data_type)
in_a_list = obj_AssignType2ListOfDfGrCol0.assign_dtype_to_list()

# input_b
obj_AssignType2ListOfDfGrCol1 = AssignType2ListOfDfGrCol(path_in, remove_str, var_list[1], data_type)
in_b_list = obj_AssignType2ListOfDfGrCol1.assign_dtype_to_list()

# call real number output arrays
# Add
obj_AssignType2ListOfDfGrCol2 = AssignType2ListOfDfGrCol(path_in, remove_str, var_list[2], data_type)
add_list = obj_AssignType2ListOfDfGrCol2.assign_dtype_to_list()

# Sub
obj_AssignType2ListOfDfGrCol3 = AssignType2ListOfDfGrCol(path_in, remove_str, var_list[3], data_type)
sub_list = obj_AssignType2ListOfDfGrCol3.assign_dtype_to_list()

# Mul
obj_AssignType2ListOfDfGrCol4 = AssignType2ListOfDfGrCol(path_in, remove_str, var_list[4], data_type)
mul_list = obj_AssignType2ListOfDfGrCol4.assign_dtype_to_list()

# array of output array:
list_of_ouput_lists = np.array([add_list, sub_list, mul_list])

#print("\n\n\n==", list_of_ouput_lists)
print("\n\n\n==============================")

# ------------------------------ 
@pytest.mark.parametrize(
    ("input_a", "input_b", "output_add"),
    [
        (in_a_list[0], in_b_list[0], list_of_ouput_lists[0][0]),
        (in_a_list[1], in_b_list[1], list_of_ouput_lists[0][1]),
        (in_a_list[2], in_b_list[2], list_of_ouput_lists[0][2]),
        (in_a_list[3], in_b_list[3], list_of_ouput_lists[0][3]),
        (in_a_list[4], in_b_list[4], list_of_ouput_lists[0][4]),
    ],
)
@pytest.mark.math
def test_addition(input_a, input_b, output_add):

    assert input_a + input_b ==  output_add
    print("\ntest_addition: ", input_a, " + ", input_b, " = ",  output_add)
# ------------------------------ 
# this is one test pass or fail (with many values tested)

@pytest.mark.great
@pytest.fixture
def upper_limit():
    num = 10

    return num

def test_add_less(upper_limit):
    for output_add in list_of_ouput_lists[0]:
         
        assert output_add < upper_limit
        print("\ntest_add_great: ", output_add, " < ",  upper_limit)


# ------------------------------ 
@pytest.mark.parametrize(
    ("input_a", "input_b", "output_sub"),
    [
        (in_a_list[0], in_b_list[0], list_of_ouput_lists[1][0]),
        (in_a_list[1], in_b_list[1], list_of_ouput_lists[1][1]),
        (in_a_list[2], in_b_list[2], list_of_ouput_lists[1][2]),
        (in_a_list[3], in_b_list[3], list_of_ouput_lists[1][3]),
        (in_a_list[4], in_b_list[4], list_of_ouput_lists[1][4]),
    ],
)
@pytest.mark.math
def test_subtraction(input_a, input_b, output_sub):

    assert input_a - input_b ==  output_sub
    print("\ntest_subtraction: ", input_a, " - ", input_b, " = ",  output_sub)



# ------------------------------ 
# this is one test pass or fail (with many values tested)
@pytest.mark.compare
@pytest.fixture
def value_compare():
    num = 1

    return num

def test_sub_compare(value_compare):

    for output_sub in list_of_ouput_lists[1]:
         
        assert output_sub == value_compare
        print("\ntest_sub_compare: ", output_sub, " == ",  value_compare)

# ------------------------------ 

@pytest.mark.parametrize(
    ("input_a", "input_b", "output_mul"),
    [
        (in_a_list[0], in_b_list[0], list_of_ouput_lists[2][0]),
        (in_a_list[1], in_b_list[1], list_of_ouput_lists[2][1]),
        (in_a_list[2], in_b_list[2], list_of_ouput_lists[2][2]),
        (in_a_list[3], in_b_list[3], list_of_ouput_lists[2][3]),
        (in_a_list[4], in_b_list[4], list_of_ouput_lists[2][4]),
    ],
)
@pytest.mark.math
def test_multiplication(input_a, input_b, output_mul):
    assert input_a * input_b ==  output_mul
    print("\ntest_multiplication: ", input_a, " * ", input_b, " = ",  output_mul)

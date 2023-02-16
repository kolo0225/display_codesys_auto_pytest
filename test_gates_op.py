# test_gates_op.py

# Purpose:
#   to test gates operation of codesys

# note:
#   the data are taken from the "results.scv" file

# import files/classes
from assign_1_type_to_df_col import AssignType2ListOfDfGrCol

# package
import numpy as np
import operator
import pytest

# Arguments:
path_in       = r"C:\Users\AnastasiosKolovos\AK\codesys_me\python_codesys\pytest_codesys\results.csv"
remove_str    = ""
var_in0       = "PLC_PRG.BOOL_A"
var_in1       = "PLC_PRG.BOOL_B"
var_out0      = "PLC_PRG.OR_OUT"
var_out1      = "PLC_PRG.AND_OUT"
var_out2      = "PLC_PRG.XOR_OUT"
var_out3      = "PLC_PRG.NAND_OUT"
var_list      = np.array ([var_in0, var_in1,var_out0,var_out1,var_out2, var_out3])
data_type     = "str" 


# call real number input arrays
# input_a
obj_AssignType2ListOfDfGrCol0 = AssignType2ListOfDfGrCol(path_in, remove_str, var_list[0], data_type)
in_a_list = obj_AssignType2ListOfDfGrCol0.assign_bool_to_list()

# input_b
obj_AssignType2ListOfDfGrCol1 = AssignType2ListOfDfGrCol(path_in, remove_str, var_list[1], data_type)
in_b_list = obj_AssignType2ListOfDfGrCol1.assign_bool_to_list()

# call real number output arrays
# or
obj_AssignType2ListOfDfGrCol2 = AssignType2ListOfDfGrCol(path_in, remove_str, var_list[2], data_type)
or_list = obj_AssignType2ListOfDfGrCol2.assign_bool_to_list()

# and
obj_AssignType2ListOfDfGrCol3 = AssignType2ListOfDfGrCol(path_in, remove_str, var_list[3], data_type)
and_list = obj_AssignType2ListOfDfGrCol3.assign_bool_to_list()

# xor
obj_AssignType2ListOfDfGrCol4 = AssignType2ListOfDfGrCol(path_in, remove_str, var_list[4], data_type)
xor_list = obj_AssignType2ListOfDfGrCol4.assign_bool_to_list()

# nand
obj_AssignType2ListOfDfGrCol5 = AssignType2ListOfDfGrCol(path_in, remove_str, var_list[5], data_type)
nand_list = obj_AssignType2ListOfDfGrCol5.assign_bool_to_list()

# array of output array:
list_of_ouput_lists = np.array([or_list, and_list, xor_list, nand_list])

#print("\n\n\n==", list_of_ouput_lists)
print("\n\n\n==============================")


# ------------------------------ 
@pytest.mark.parametrize(
    ("input_a", "input_b", "output_or"),
    [
        (in_a_list[0], in_b_list[0], list_of_ouput_lists[0][0]),
        (in_a_list[1], in_b_list[1], list_of_ouput_lists[0][1]),
        (in_a_list[2], in_b_list[2], list_of_ouput_lists[0][2]),
        (in_a_list[3], in_b_list[3], list_of_ouput_lists[0][3]),
        (in_a_list[4], in_b_list[4], list_of_ouput_lists[0][4]),
    ],
)
@pytest.mark.gates
def test_gate_or(input_a, input_b, output_or):

    assert (input_a or input_b) ==  output_or
    print("\ntest_gate_or: ", input_a, " or ", input_b, " = ",  output_or)

# ------------------------------ 
@pytest.mark.parametrize(
    ("input_a", "input_b", "output_and"),
    [
        (in_a_list[0], in_b_list[0], list_of_ouput_lists[1][0]),
        (in_a_list[1], in_b_list[1], list_of_ouput_lists[1][1]),
        (in_a_list[2], in_b_list[2], list_of_ouput_lists[1][2]),
        (in_a_list[3], in_b_list[3], list_of_ouput_lists[1][3]),
        (in_a_list[4], in_b_list[4], list_of_ouput_lists[1][4]),
    ],
)
@pytest.mark.gates
def test_gate_and(input_a, input_b, output_and):

    assert (input_a and input_b) ==  output_and
    print("\ntest_gate_and: ", input_a, " and ", input_b, " = ",  output_and)

# ------------------------------ 
@pytest.mark.parametrize(
    ("input_a", "input_b", "output_xor"),
    [
        (in_a_list[0], in_b_list[0], list_of_ouput_lists[2][0]),
        (in_a_list[1], in_b_list[1], list_of_ouput_lists[2][1]),
        (in_a_list[2], in_b_list[2], list_of_ouput_lists[2][2]),
        (in_a_list[3], in_b_list[3], list_of_ouput_lists[2][3]),
        (in_a_list[4], in_b_list[4], list_of_ouput_lists[2][4]),
    ],
)
@pytest.mark.gates
def test_gate_xor(input_a, input_b, output_xor):
                                
    assert (input_a ^ input_b)  ==  output_xor
    print("\ntest_gate_xor: ", input_a, " xor ", input_b, " = ",  output_xor)

# ------------------------------ 
# this is one test pass or fail (with many values tested)
@pytest.mark.compare
def test_xor_compare(input_true):

    for output_xor in list_of_ouput_lists[2]:
         
        assert output_xor == input_true
        print("\ntest_xor_compare: ", output_xor, " == ",  input_true)

# ------------------------------ 

@pytest.mark.parametrize(
    ("input_a", "input_b", "output_nand"),
    [
        (in_a_list[0], in_b_list[0], list_of_ouput_lists[3][0]),
        (in_a_list[1], in_b_list[1], list_of_ouput_lists[3][1]),
        (in_a_list[2], in_b_list[2], list_of_ouput_lists[3][2]),
        (in_a_list[3], in_b_list[3], list_of_ouput_lists[3][3]),
        (in_a_list[4], in_b_list[4], list_of_ouput_lists[3][4]),
    ],
)
@pytest.mark.gates
def test_gate_nand(input_a, input_b, output_nand):
    assert not(input_a and input_b) ==  output_nand
    print("\ntest_gate_nand: ", input_a, " NAND ", input_b, " = ",  output_nand)



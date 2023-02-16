# test_bigger_op.py

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
remove_str    = ""
var_out0      = "PLC_PRG.FN_is_A_Bigger"
data_type     = "str"


# call real number output arrays
# bigger
obj_AssignType2ListOfDfGrCol2 = AssignType2ListOfDfGrCol(path_in, remove_str, var_out0, data_type)
bigger_list = obj_AssignType2ListOfDfGrCol2.assign_bool_to_list()

#print("\n\n\n==", bigger_list)
print("\n\n\n==============================")

# ------------------------------ 
@pytest.mark.compare
def test_bigger(input_true):

    for output_bigger in bigger_list:

        assert output_bigger == input_true
        print("\ntest_bigger: ", output_bigger, " == ",  input_true)
                        
# ------------------------------ 

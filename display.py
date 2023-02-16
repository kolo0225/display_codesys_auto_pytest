# display.py 

# Purpose:
#   call explort csv to create clean csv version
#   graphs oupts variables 

# import files/classes
from read_clean_csv import ImportCleanDF
from export_csv import ExportDF
from assign_type_to_df_col import AssignType2ListOfDfGrCol


# packages:
import numpy as np 
import matplotlib.pyplot as plt

# Arguments:
path_in       = r"C:\Users\AnastasiosKolovos\AK\codesys_me\python_codesys\pytest_codesys\results.csv"
remove_str    = "\w*#"
#remove_str    = "REAL#"
var_in0       = "PLC_PRG.VAR_A"
var_in1       = "PLC_PRG.VAR_B"
var_out0      = "PLC_PRG.ADD_OUT"
var_out1      = "PLC_PRG.SUB_OUT"
var_out2      = "PLC_PRG.MUL_OUT"
var_list      = np.array ([var_in0, var_in1,var_out0,var_out1,var_out2])
data_type     = "float64"
path_out      = r"C:\Users\AnastasiosKolovos\AK\codesys_me\python_codesys\pytest_codesys\results_clean.csv"

class Display:
    def __init__(self, path_in, remove_str, var_list, data_type):

        self.path_in       = path_in
        self.remove_str    = remove_str
        self.var_list      = var_list
        self.data_type     = data_type

    def multiple_reals_line_plots(self):


        # call real number input arrays 
        # input_a
        obj_AssignType2ListOfDfGrCol0 = AssignType2ListOfDfGrCol(self.path_in, self.remove_str, self.var_list[0], self.data_type)
        in_a_list = obj_AssignType2ListOfDfGrCol0.assign_dtype_to_list()

        # input_b
        obj_AssignType2ListOfDfGrCol1 = AssignType2ListOfDfGrCol(self.path_in, self.remove_str, self.var_list[1], self.data_type)
        in_b_list = obj_AssignType2ListOfDfGrCol1.assign_dtype_to_list()
        
        # call real number output arrays 
        # Add
        obj_AssignType2ListOfDfGrCol2 = AssignType2ListOfDfGrCol(self.path_in, self.remove_str, self.var_list[2], self.data_type)
        add_list = obj_AssignType2ListOfDfGrCol2.assign_dtype_to_list()

        # Sub
        obj_AssignType2ListOfDfGrCol3 = AssignType2ListOfDfGrCol(self.path_in, self.remove_str, self.var_list[3], self.data_type)
        sub_list = obj_AssignType2ListOfDfGrCol3.assign_dtype_to_list()

        # Mul
        obj_AssignType2ListOfDfGrCol4 = AssignType2ListOfDfGrCol(self.path_in, self.remove_str, self.var_list[4], self.data_type)
        mul_list = obj_AssignType2ListOfDfGrCol4.assign_dtype_to_list()

        # x-value len
        x = np.arange(len(add_list))

        # limit @ x-axis
        x_min_lim = np.amin(x) -1
        x_max_lim = np.amax(x) +1

        plt.xlim((x_min_lim,x_max_lim))   
        print(x) 
        
        # plot line
        plt.plot(x, in_a_list, color="deeppink", label="input_a", linestyle='dashed')
        plt.plot(x, in_b_list, color="crimson", label="input_b", linestyle='dashed')
        plt.plot(x, add_list, color="deepskyblue", label="Add")
        plt.plot(x, sub_list, color="blue", label="Sub")
        plt.plot(x, mul_list, color="navy", label="Mul")
        
        plt.legend()
        plt.show()

# Import & clean df
obj_ImportCleanDF = ImportCleanDF(path_in, remove_str)
df_clean = obj_ImportCleanDF.clean_df()

# Import & clean df
obj_ExportDF = ExportDF(df_clean, path_out)
obj_ExportDF.export_to_csv()

# multigraph 
obj_Display = Display(path_in, remove_str, var_list,  data_type)
obj_Display.multiple_reals_line_plots()

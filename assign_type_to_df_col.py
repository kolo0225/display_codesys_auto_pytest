# assign_type_to_df_col.py

# Purpose:
#   turn col of pandas df to list of a particular dtype

# import files/classes
from read_clean_csv import ImportCleanDF


# packets:
import numpy as np
import pandas as pd

# Arguments:
#path_in       = r"C:\Users\AnastasiosKolovos\AK\codesys_me\python_codesys\pytest_codesys\results.csv"
#remove_str    = "\w*#"
#remove_str    = "REAL#"
#var_name      = "PLC_PRG.ADD_OUT"
#var_name      = "PLC_PRG.OR_OUT"
#data_type     = "str"
#data_type     = "float64"

class AssignType2ListOfDfGrCol:

    def __init__(self, path_in, remove_str, var_name, data_type):

        self.path_in       = path_in
        self.remove_str    = remove_str
        self.var_name      = var_name
        self.data_type     = data_type
        
        #self.arr           = np.array([]) 


    # --------------------- Top Bottom design -------------------

    def assign_bool_to_list(self):

        list_str = self.assign_dtype_to_list()

        list_bool = np.array([], dtype=bool)
        for elem_str in list_str:

            if (elem_str == 'TRUE'):
                elem_str = True
                list_bool = np.append(list_bool, elem_str)
            elif (elem_str == 'FALSE'):
                elem_str = False
                list_bool = np.append(list_bool, elem_str)
            else:
                pass

        #print("\n list_bool: ", list_bool)
        #print("\n list_bool.dtype: ", list_bool.dtype)

        return list_bool

    def assign_dtype_to_list(self):
        
        list_dtype = self.df_part_col_to_list()
        list_dtype = list_dtype.astype(self.data_type)

        #print("\n list_dtype.dtype: ", list_dtype.dtype)
        #print("\n list_dtype: ", list_dtype)

        return list_dtype

    def df_part_col_to_list(self):

        # Import & clean df
        obj_ImportCleanDF = ImportCleanDF(self.path_in, self.remove_str)
        df_clean = obj_ImportCleanDF.clean_df()

        # select chosen varable
        mask = df_clean["variables"] == self.var_name
        df_sel = df_clean[mask]

        list_col_sel = np.array(df_sel["values"].tolist()) 
        #print("\n list_col_sel: ", list_col_sel)

        return list_col_sel

    
#call class/fun
#obj_AssignType2ListOfDfGrCol = AssignType2ListOfDfGrCol(path_in, remove_str, var_name, data_type)
#obj_AssignType2ListOfDfGrCol.df_part_col_to_list() 
#obj_AssignType2ListOfDfGrCol.assign_dtype_to_list() 
#obj_AssignType2ListOfDfGrCol.assign_bool_to_list() 

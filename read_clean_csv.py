# read_clean_csv.py

# Purpose:
#   import file.csv
#   clean data (by removing extras)
#   clean_n_dtype.py
#   export file.csv

# packets:
import numpy as np
import pandas as pd
import re 

# Arguments:
#path_in       = r"C:\Users\AnastasiosKolovos\AK\codesys_me\python_codesys\pytest_codesys\results.csv"
#remove_str    = "REAL#"
#remove_str    = "\w*#"

class ImportCleanDF:

    def __init__(self, path_in, remove_str):

        self.path_in       = path_in       
        self.remove_str    = remove_str      

    # --------------------- Top Bottom design -------------------

    def clean_df(self):
        
        df_dirty = self.import_df()
        df_clean = df_dirty.copy()
        
        """
        # only use this if there is an issue with 
        # test_* recognizing the regex use
        clean_list = np.array([])
        for elem in df_clean["values"].to_list():

            elem = str(elem)
            elem = elem.replace(self.remove_str, "")
            #print(elem)
            
            clean_list = np.append(clean_list, elem)

        df_clean["values"] = clean_list 
        """

        df_clean["values"] = df_clean["values"].str.replace(self.remove_str,"", regex=True)
        #print("\n", df_clean)

        return df_clean

    def read_dtype(self):

        df_dirty = self.import_df()
        
        for elem in df_dirty["values"]:
            print(type(elem))

        return 

    def import_df (self):
        df_dirty = pd.read_csv(self.path_in)

        #print(df_dirty.shape)
        #print(df_dirty.columns)
        #print(self.df)

        return df_dirty

# call class/fn 
#obj_ImportCleanDF = ImportCleanDF(path_in, remove_str)
#obj_ImportCleanDF.import_df()
#obj_ImportCleanDF.read_dtype()
#obj_ImportCleanDF.clean_df()


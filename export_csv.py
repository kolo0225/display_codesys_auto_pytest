# export_csv.py

# Purpose:
#   export file.csv

# packets:
import pandas as pd

# Arguments:
#path_out      = r"C:\Users\AnastasiosKolovos\AK\codesys_me\python_codesys\pytest_codesys\results_clean.csv"

class ExportDF:

    def __init__(self, df, path_out ):
	
        self.df            = df
        self.path_out      = path_out

    # --------------------- Top Bottom design -------------------
    def export_to_csv(self):

        self.df.to_csv(self.path_out, index=False)

        return
#obj_ExportDF = ExportDF(df, path_out)
#obj_ExportDF.export_to_csv()

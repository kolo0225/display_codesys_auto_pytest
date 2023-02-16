# list_from_filetxt.py
# --------------------
# Purpose:
#   reads input values from files 
#   creates a 1d list 

# Note: 
#   you have to modify 
#       1. the paths

# ============================================================

# Arguments:
#input_txt  = r"C:\Users\AnastasiosKolovos\AK\codesys_me\python_codesys\pytest_codesys\var_in.txt"
#input_txt  = r"C:\Users\AnastasiosKolovos\AK\codesys_me\python_codesys\pytest_codesys\var_out.txt"

class ListFromText:

    def __init__ (self, input_txt):

        self.input_txt =  input_txt


    def list_maker_from_txt (self):

        with open(self.input_txt, "r") as r:

            dirty_list = r.readlines()

            list_from_txt = []
            for input_elem in dirty_list:
                input_elem = input_elem.strip()

                list_from_txt.append(input_elem)  

        print ("\n len(list_from_txt): ", len(list_from_txt))
        print ("list_from_txt: ", list_from_txt, "\n")

        return list_from_txt

# call function:
#obj_ListFromText = ListFromText(input_txt)
#list_from_txt = obj_ListFromText.list_maker_from_txt()

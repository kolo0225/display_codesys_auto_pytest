#  w_n_r_list_of_values.py
#--------------------------

# Purpose:
#   to write & read values of list of variables in codesys  

# Arguments:
#list_inputs  
#input_txt  = r"C:\Users\AnastasiosKolovos\AK\codesys_me\python_codesys\pytest_codesys\var_out.txt"

class WritesReadsValuesCodesys:

    def __init__ (self, input_txt):

        self.input_txt =  input_txt


    def list_maker_from_txt (self):

        with open(self.input_txt, "r") as r:

            dirty_list = r.readlines()

            list_from_txt = []
            for input_elem in dirty_list:
                input_elem = input_elem.strip()

                list_from_txt.append(input_elem)

        print ("\n list_from_txt: ", list_from_txt, "\n")

        return list_from_txt

# call function:
#obj_ListFromText = ListFromText(input_txt)
#list_from_txt = obj_ListFromText.list_maker_from_txt()

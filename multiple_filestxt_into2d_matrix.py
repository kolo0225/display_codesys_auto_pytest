# multiple_filestxt_into2d_matrix.py
# Purpose:
#   reads input values from files 
#   creates a 2d matrix from these files 

# Goal:
#   to have all input data (same index) - be tested at once

# Note: 
#   you have to modify 
#   1. the paths

# ============================================================

# Arguments:
#input0_txt  = r"C:\Users\AnastasiosKolovos\AK\codesys_me\python_codesys\pytest_codesys\input_value_a.txt"
#input1_txt  = r"C:\Users\AnastasiosKolovos\AK\codesys_me\python_codesys\pytest_codesys\input_value_b.txt"
#input2_txt  = r"C:\Users\AnastasiosKolovos\AK\codesys_me\python_codesys\pytest_codesys\input_value_c.txt"
#input3_txt  = r"C:\Users\AnastasiosKolovos\AK\codesys_me\python_codesys\pytest_codesys\input_value_d.txt"
#input_list = [input0_txt, input1_txt, input2_txt, input3_txt] 

class TwoDArrayMAker:

    def __init__ (self, input_list):

        self.input_list =  input_list

    def dict_to_2d_matrix (self): 

        print("len(self.input_values_dict): ", len(self.input_values_dict))

        list_of_inputs_inv = list(self.input_values_dict.values())
        # Transpose & tranforms "list of tuples"  in to "list of lists"
        list_of_inputs = [list(i) for i in zip(*list_of_inputs_inv)]

        print ("\nlist_of_inputs: ", list_of_inputs, "\n")
        print ("\nlen(list_of_inputs): ", len(list_of_inputs), "\n")
        print ("\nlen(list_of_inputs[0]): ", len(list_of_inputs[0]), "\n")

        return list_of_inputs


    def list_files_txt_to_dict_maker (self):

        self.input_values_dict = dict()
        for index, file in enumerate(self.input_list):
                        
            with open(file, "r") as r:

                input_values_list = r.readlines()

                input_values_list_  = []
                for input_values_clean in input_values_list:
                    input_values_clean = input_values_clean.strip()

                    input_values_list_.append(input_values_clean)  

            self.input_values_dict[index] = input_values_list_

        print ("\nself.input_values_dict: ", self.input_values_dict, "\n")

        return self.input_values_dict

# call function:
#obj_TwoDArrayMAker = TwoDArrayMAker(input_list)
#input_values_dict = obj_TwoDArrayMAker.list_files_txt_to_dict_maker()
#list_of_inputs = obj_TwoDArrayMAker.dict_to_2d_matrix()


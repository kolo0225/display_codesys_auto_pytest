# prep_write_var1d_val2d_v1.py
# Purpose:
#   matches var 1d-list to val 2d-list
#   prints var and val[index]
#   puts a delay for each index iteration 
#       prep - write - break - read 
#   import file/class to create csv file with the result

# packages 
import time

# ============================================================
# import files/classes
from list_from_filetxt import ListFromText
from multiple_filestxt_into2d_matrix import TwoDArrayMAker
from write_file_csv import CSVWriter
# ============================================================

class AssingVar1DtoVal2D:

    def __init__ (self, onlineapp, input_txt_inputs, input_txt_outputs, input_list, output_csv ):

        self.sleep_t05         = 1 #s
        self.sleep_t1          = 2 #s
        self.onlineapp         = onlineapp
        self.input_txt_inputs  = input_txt_inputs
        self.input_txt_outputs = input_txt_outputs
        self.input_list        = input_list
        self.output_csv        = output_csv 

    def input_val_output_csv_maker (self):

        # open csv file - write headers
        obj_CSVWriter      = CSVWriter("", "", self.output_csv)
        obj_CSVWriter.write_csv()

        # ------------------  list of inputs and outputs --------------
        # call function:
        # get list of inputs
        obj_input_list  = ListFromText(self.input_txt_inputs)
        list_of_in_var  = obj_input_list.list_maker_from_txt()
        # get list of outputs
        obj_output_list = ListFromText(self.input_txt_outputs)
        list_of_out_var  = obj_output_list.list_maker_from_txt()
        # -------------------------------------------------------------

        # ------------------  list of inputs values -------------------
        # call function:
        obj_TwoDArrayMAker = TwoDArrayMAker(self.input_list)
        input_values_dict  = obj_TwoDArrayMAker.list_files_txt_to_dict_maker()
        list_of_in_val     = obj_TwoDArrayMAker.dict_to_2d_matrix()
        # -------------------------------------------------------------
        for i in range(len(list_of_in_val)):

            for j in range(len(list_of_in_var)):
                
                # prep & write value
                self.onlineapp.set_prepared_value(list_of_in_var[j],list_of_in_val[i][j])
                self.onlineapp.write_prepared_values()

                time.sleep(self.sleep_t05)
                
                # read value of iVar1
                input_val = self.onlineapp.read_value(list_of_in_var[j])
                print(list_of_in_var[j])
                print(input_val)

                # whites input var/val in csv
                obj_CSVWriter      = CSVWriter(list_of_in_var[j], list_of_in_val[i][j], self.output_csv)
                obj_CSVWriter.append_csv()

            time.sleep(self.sleep_t1)

            for k in range(len(list_of_out_var)):
                
                # read value of iVar1
                output_val = self.onlineapp.read_value(list_of_out_var[k])
                print(list_of_out_var[k])
                print(output_val)

                # whites output var/val in csv
                obj_CSVWriter      = CSVWriter(list_of_out_var[k], output_val, self.output_csv)
                obj_CSVWriter.append_csv()



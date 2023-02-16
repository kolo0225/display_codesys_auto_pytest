# python_conn_codesys1.py
# -----------------------

# Purpose:
#   logs in to the device $ starts the application if necessary. 
#   imports all files/classes to prep/write/read input/output var/val
#   imports all files/classes to cereate var/val csv file

# Note:
#   All paths need to be abjusted to your local pc paths

# encoding:utf-8
# packages
from __future__ import print_function   # this library does not seem to be needed
import time

# ============================================================
# import files/classes
from prep_write_var1d_val2d_v1 import AssingVar1DtoVal2D
# ============================================================

# Arguments
# connect with CoDeSys
project_math      = r"C:\Users\AnastasiosKolovos\AK\codesys_me\python_codesys\pytest_codesys\MathDemo_0.project"
delay_1           = 1000          # ms

# list of input variables 
input_txt_inputs  = r"C:\Users\AnastasiosKolovos\AK\codesys_me\python_codesys\pytest_codesys\var_in.txt"
input_txt_outputs = r"C:\Users\AnastasiosKolovos\AK\codesys_me\python_codesys\pytest_codesys\var_out.txt"

# list of input variables 
input0_txt  = r"C:\Users\AnastasiosKolovos\AK\codesys_me\python_codesys\pytest_codesys\input_value_a.txt"
input1_txt  = r"C:\Users\AnastasiosKolovos\AK\codesys_me\python_codesys\pytest_codesys\input_value_b.txt"
input2_txt  = r"C:\Users\AnastasiosKolovos\AK\codesys_me\python_codesys\pytest_codesys\input_value_c.txt"
input3_txt  = r"C:\Users\AnastasiosKolovos\AK\codesys_me\python_codesys\pytest_codesys\input_value_d.txt"
input_list = [input0_txt, input1_txt, input2_txt, input3_txt]

# result csv file
output_csv = r"C:\Users\AnastasiosKolovos\AK\codesys_me\python_codesys\pytest_codesys\results.csv"

class PythonCodesysConnect:

    def __init__(self, project_math, delay_1, input_txt_inputs, input_txt_outputs, input_list, output_csv):

        self.project_math       = project_math
        self.delay_1            = delay_1
        self.input_txt_inputs   = input_txt_inputs
        self.input_txt_outputs  = input_txt_outputs
        self.input_list         = input_list 
        self.output_csv         = output_csv

    def python_codesys_cycle(self):

        # ------------------ connect with codesys -------------------------
        # close open project:
        if projects.primary:
            projects.primary.close()

        # opens project
        proj = projects.open(self.project_math)

        # set "name.project" to active application
        app = proj.active_application
        onlineapp = online.create_online_application(app)

        # login to device
        onlineapp.login(OnlineChangeOption.Try, True)

        # set status of application to "run"
        if not onlineapp.application_state == ApplicationState.run:
            onlineapp.start()

        # wait 1 second
        system.delay(self.delay_1 )
        # -------------------------------------------------------------

        # ---------  prepare, read & write values -> out to csv --------
        obj_AssingVar1DtoVal2D = AssingVar1DtoVal2D(onlineapp, self.input_txt_inputs, self.input_txt_outputs, self.input_list, self.output_csv )
        obj_AssingVar1DtoVal2D.input_val_output_csv_maker()
        

        # ------------------ connect with codesys -------------------------
        # log out from device and close "name.project"
        #onlineapp.logout()
        #proj.close()
        # -------------------------------------------------------------
        

        return

# call function:
obj_connect = PythonCodesysConnect(project_math, delay_1, input_txt_inputs, input_txt_outputs, input_list, output_csv)
obj_connect.python_codesys_cycle()

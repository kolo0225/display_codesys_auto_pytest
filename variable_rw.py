# variable_rw.py

# Purpose:
#   to write values into variables  
#   to print in the console the values of the variables  

from __future__ import print_function   # this library does not seem to be needed

# Arguments
var_in_1   = "PLC_PRG.in_a"
var_out_1  = "PLC_PRG.out_a"
var_out_2  = "PLC_PRG.out_not_a"

def read_variables_codesys (project_, delay_,  var_in_1, var_out_1, var_out_2):

    # close open project if necessary:
    if projects.primary:
        projects.primary.close()

    # opens project
    proj = projects.open(project_)

    # set "Ampel.project" to active application
    app = proj.active_application
    onlineapp = online.create_online_application(app)

    # login to device
    onlineapp.login(OnlineChangeOption.Try, True)

    # set status of application to "run", if not in "run"
    if not onlineapp.application_state == ApplicationState.run:
        onlineapp.start()

    # wait 1 second
    system.delay(delay_ )

    # write value of iVar1
    onlineapp.set_prepared_value("PLC_PRG.in_a","False")
    onlineapp.write_prepared_values()
    #onlineapp.set_prepared_value(var_in_1,"True")

    # read value of iVar1
    value1 = onlineapp.read_value(var_in_1)
    value2 = onlineapp.read_value(var_out_1)
    value3 = onlineapp.read_value(var_out_2)

    # display value in message view or command line
    print(value1)
    print(value2)
    print(value3)

    # log out from device and close "Ampel.project"
    #onlineapp.logout()
    #proj.close()

    return

# call function:
read_variables_codesys (project_, delay_,  var_in_1, var_out_1, var_out_2)

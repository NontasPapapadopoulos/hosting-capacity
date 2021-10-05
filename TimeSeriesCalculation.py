import os
import pandas as pd
import warnings
import math

#import tempfile

import pandapower as pp
from pandapower.timeseries import DFData
from pandapower.timeseries import OutputWriter
from pandapower.timeseries.run_time_series import run_timeseries
from pandapower.control import ConstControl
from overhead.overhead_network_for_TSS import overhead_network
warnings.simplefilter(action='ignore', category=FutureWarning)



july_LoadProfile_KW = [1.207, 1.1541, 1.0882, 0.9982, 0.9022, 0.8484, 0.8334,
                       0.8633, 0.3256, 0.7992, 1.30865, 0.8263, 0.93595, 1.254,
                       1.331, 1.1725, 1.4316, 1.621, 1.3541, 1.1422, 0.7352,
                       1.1045, 1.1111, 1.1948]

july_PV_Production_Watt = [0, 0, 0, 0,  0,  0,  32.85, 363.1,  1290,  2176.8,  2839.4,  3269.25,
                      3475.1,  3527.45, 3376.05,  2864.2,  2315.6, 1466.85,  515.25,  118, 0, 0, 0, 0, ]

def convert_from_kW_to_MW(number):
    return number / 1000

def convert_from_Watt_to_MW(number):
    return number / 1000000

# Convert from kW to MW
julyLoadProfile = list(map(convert_from_kW_to_MW, july_LoadProfile_KW))

# Conver from watt to MW
july_PV_Production = list(map(convert_from_Watt_to_MW, july_PV_Production_Watt))

def timeseries_example(output_dir):
    # 1. create test net
    net = overhead_network()

    # 2. create (random) data source
    n_timesteps = 24
    profiles, ds = create_data_source(n_timesteps)
    # 3. create controllers (to control P values of the load and the sgen)
    create_controllers(net, ds)

    # time steps to be calculated. Could also be a list with non-consecutive time steps
    time_steps = range(0, n_timesteps)

    # 4. the output writer with the desired results to be stored to files.
    ow = create_output_writer(net, time_steps, output_dir=output_dir)

    # 5. the main time series function
    run_timeseries(net, time_steps)


def create_data_source(n_timesteps=24):
    profiles = pd.DataFrame()
    profiles['load1_p'] = julyLoadProfile
    profiles['sgen1_p'] = july_PV_Production

    ds = DFData(profiles)

    return profiles, ds


def create_controllers(net, ds):
    for load in range(len(net.load)):
        ConstControl(net, element='load', variable='p_mw', element_index=load,
                     data_source=ds, profile_name=["load1_p"])

    for PV in range(len(net.sgen)):
        ConstControl(net, element='sgen', variable='p_mw', element_index=PV,
                     data_source=ds, profile_name=["sgen1_p"])




output_dir = "./results/"
def create_output_writer(net, time_steps, output_dir):
    ow = OutputWriter(net, time_steps, output_path=output_dir, output_file_type=".xls", log_variables=list())
    # these variables are saved to the harddisk after / during the time series loop
    ow.log_variable('res_load', 'p_mw')
    ow.log_variable('res_bus', 'vm_pu')
    ow.log_variable('res_line', 'loading_percent')
    ow.log_variable('res_line', 'i_ka')
    return ow

print("Results can be found in your local temp folder: {}".format(output_dir))
if not os.path.exists(output_dir):
    os.mkdir(output_dir)


timeseries_example(output_dir)

import matplotlib.pyplot as plt

#%matplotlib inline

# voltage results
vm_pu_file = os.path.join(output_dir, "res_bus", "vm_pu.xls")
vm_pu = pd.read_excel(vm_pu_file, index_col=0)
vm_pu.plot(label="vm_pu")
plt.xlabel("time step")
plt.ylabel("voltage mag. [p.u.]")
plt.title("Voltage Magnitude")
plt.grid()
plt.show()

# line loading results
ll_file = os.path.join(output_dir, "res_line", "loading_percent.xls")
line_loading = pd.read_excel(ll_file, index_col=0)
line_loading.plot(label="line_loading")
plt.xlabel("time step")
plt.ylabel("line loading [%]")
plt.title("Line Loading")
plt.grid()
plt.show()

# load results
load_file = os.path.join(output_dir, "res_load", "p_mw.xls")
load = pd.read_excel(load_file, index_col=0)
load.plot(label="load")
plt.xlabel("time step")
plt.ylabel("P [MW]")
plt.grid()
plt.show()

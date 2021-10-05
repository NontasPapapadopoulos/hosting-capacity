# hosting-Capacity 
In this project I created two low voltage networks of Electric Authority of Cyprus. 
One overhead and one with underground cables. 

Using Time Series algorithm I investigated the overhead network\`s behavior under the impact of PV penetration. 
During the day, the sun radiation changes, thus the power production of PVs, Similarly the load consumtion varies from hour to hour. 
With the use of Time Series algorithm we can see the level of voltage bus and the level of loading of the lines during the day. 
For TSS calculation you have to change the load profile and the pv production. Also you must load your own network. 

Time Series Calculation algorithm: 
https://github.com/e2nIEE/pandapower/blob/develop/tutorials/time_series.ipynb


I also calculated the maximum hosting capacity for the current network.
With the use of a Monte Carlo simulation I checked the maximum hosting capacity for PV installation. 
Hosting Capacity algorithm:
https://github.com/e2nIEE/pandapower/blob/develop/tutorials/hosting_capacity.ipynb


## Contents 

### In the Overhead folder you will find: 

#### 1) hosting_capacity.py 
 This calculates the hosting capacity for only one case. 
If you want to calculate hosting capacity, you can import your network which is in another file and you can also change the violations. 

#### 2) hosting_capacity_overhead_multiple_loads.py 
This calculates the hosting capacity for multiple loads. 
Here you must insert a list of load values and run the hosting capacity once for each value. 

#### 3) overhead_network_Simple.py 
This is the overhead network.

#### 4) overhead_network_for_TSS.py 
This is the overhead network for time series calculation. 
In this network i have installed a static generator in each load. A static generators represents a PV system. The controller of the TSS algorithm will change the value of the PV system in each timestep. 

#### 5) overhead_network_for_hosting_capacity_Multiple_Values.py 
This is the network for calculation hosting capacity for multiple values. 
This network is used from the file "hosting_capacity_overhead_multiple_loads". It is different from overhead_network_simple because it accepts a value as parameter. This parameter represents the value of load for the consumers. 

### In the underground folder you will find: 
#### 1) hosting_capacity_underground.py 
 The hosting capacity algorithm for the underground network. 
#### 2) underground_network.py 
 This is the underground network. 



## Required software 

 Python installed in your computer  
Ι strongly recomend PyCharm as IDE. Else you can use Jupiter Notebook 
* Download PyCharm: https://www.jetbrains.com/pycharm/ 
* Download Anaconda: https://www.anaconda.com/
* Download Python: https://www.python.org/downloads/ 
* Install pandapower: Open a cmd and type  pip install pandapower 
* Then Open pycharm and press Ctrl + alt + S, go to project -> python interpeter, select python interpeter and pres + to add Pandapower in your project 

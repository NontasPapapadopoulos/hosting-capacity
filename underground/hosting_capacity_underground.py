import pandapower as pp
from numpy.random import choice
from numpy.random import normal
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from underground.underground_network import underground_network
import math
import warnings

warnings.filterwarnings("ignore")


def violations(net):
    pp.runpp(net)
    if net.res_line.loading_percent.max() > 50:
        print("line overloading violation")
        print("max load" ,net.res_line.i_ka[0] * 1000)
        print("real power" ,net.res_line.p_from_mw[0] * 1000)
        print("reactive power" ,net.res_line.q_from_mvar[0] * 1000)
        print()
        return (True, "Line \n Overloading")
    elif net.res_trafo.loading_percent.max() > 50:
        print("transformer overloading violation")
        return (True, "Transformer \n Overloading")
    elif net.res_bus.vm_pu.max() > 1.05:
        print("bus overvoltage violation")
        return (True, "Voltage \n Violation")
    else:
        return (False, None)


def chose_bus(net):
    return choice(net.load.bus.values)


def get_plant_size_mw():
    return round(normal(loc=0.005, scale=0.001), 3)



iterations = 50
results = pd.DataFrame(columns=["installed", "violation"])
results_installed = []
for i in range(iterations):
    net = underground_network()
    installed_mw = 0
    while 1:
        violated, violation_type = violations(net)
        if violated:
            results.loc[i] = [installed_mw, violation_type]
            # results_installed.append(results["installed"])
            break
        else:
            plant_size = get_plant_size_mw()
            pp.create_sgen(net, chose_bus(net), p_mw=plant_size, q_mvar=0)
            installed_mw += plant_size


print(results.installed)

# %matplotlib inline
plt.rc('xtick', labelsize=18)  # fontsize of the tick labels
plt.rc('ytick', labelsize=18)  # fontsize of the tick labels
plt.rc('legend', fontsize=18)  # fontsize of the tick labels
plt.rc('axes', labelsize=20)  # fontsize of the tick labels
plt.rcParams['font.size'] = 20

sns.set_style("whitegrid", {'axes.grid': True})

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
ax = axes[0]
sns.boxplot(data=results.installed * 1000, width=.1, ax=ax, orient="v")
ax.set_xticklabels([""])
ax.set_ylabel("Installed Capacity [kW]")

ax = axes[1]
ax.axis("equal")
results.violation.value_counts().plot(kind="pie", ax=ax, autopct=lambda x: "%.0f %%" % x)
ax.set_ylabel("")
ax.set_xlabel("")
sns.despine()
plt.tight_layout()


plt.show()

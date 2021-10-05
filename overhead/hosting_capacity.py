import pandapower as pp
from numpy.random import choice
from numpy.random import normal
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from overhead import overhead_network_Simple

warnings.filterwarnings("ignore")


def violations(net):
    pp.runpp(net)
    if net.res_line.loading_percent.max() > 50:
        return (True, "Line \n Overloading")
    elif net.res_trafo.loading_percent.max() > 50:
        return (True, "Transformer \n Overloading")
    elif net.res_bus.vm_pu.max() > 1.05:
        return (True, "Voltage \n Violation")
    else:
        return (False, None)


def chose_bus(net):
    return choice(net.load.bus.values)


def get_plant_size_mw():
    return round(normal(loc=0.005, scale=0.001), 3)


iterations = 50
results = pd.DataFrame(columns=["installed", "violation"])

df = pd.DataFrame(columns=["results"])

for i in range(iterations):
    net = overhead_network_Simple.overhead_network()
    installed_mw = 0
    while 1:
        violated, violation_type = violations(net)
        if violated:
            results.loc[i] = [installed_mw, violation_type]
            break
        else:
            plant_size = get_plant_size_mw()
            pp.create_sgen(net, chose_bus(net), p_mw=plant_size, q_mvar=0)
            installed_mw += plant_size


print("mean:", results.mean())
print("max: ", results.max())
print("min:", results.min())

# -plant_size * tan(acos(0.95))
# -(plant_size * math.tan(math.acos(0.95)))




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
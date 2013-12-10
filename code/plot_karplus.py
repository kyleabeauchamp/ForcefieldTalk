import ALA3
from fitensemble.nmr_tools import scalar_couplings
import matplotlib.pyplot as plt
import numpy as np
import experiment_loader
import matplotlib

ff = "amber99sbnmr-ildn"  # Load FF data for comparison, not used in actual figure
alpha = 0.25
num_grid = 2000
phi = np.linspace(-180,180,num_grid)
O = np.ones(num_grid)
phi1, psi1, ass_raw, state_ind = experiment_loader.load_rama(ff, 1)

J = scalar_couplings.J3_HN_HA(phi)

predictions, measurements, uncertainties = experiment_loader.load(ff, keys=[("JC", 2, "J3_HN_HA")])
yi = measurements.iloc[0]
oi = uncertainties.iloc[0]
mu = predictions.mean(0).values[0]

sigma = uncertainties.values[0]
val = measurements.values[0]

fig, ax1 = plt.subplots()

ax1.plot(phi, J, 'k', linewidth=8)
lower = yi - oi
upper = yi + oi
ax1.fill_between(phi, lower * O, upper * O, color='k', alpha=alpha)
ax1.plot(phi, O * mu, 'b')
plt.ylabel("J [Hz]")
plt.xlabel(r"$\phi[^{\circ}]$")

plt.yticks([0, 5, 10])
plt.xticks([-180, -90, 0, 90, 180])
plt.xlim(-180,180)
plt.ylim(-0.5,10.5)

ax2 = ax1.twinx()
ax2.hist(phi1, bins=50, alpha=0.25)
plt.ylabel("Counts")



plot([], [], color='k', label="NMR")
plot([], [], color='b', label="MD")
plt.legend(loc=0)

plt.savefig("./figures/karplus_ala3.png", bbox_inches='tight', transparent=True)

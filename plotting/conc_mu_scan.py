import matplotlib.pyplot as plt
from ase.units import Ry
from glob import glob
from gpaw import GPAW
import numpy as np
import matplotlib

# True -> Scan chemical potential
# False -> Scan carrier concentration
chem_pot_scan = False

font ={'size'   : 16}
matplotlib.rc('font', **font)

# Tensor component ordering in interpolate.* files:
# xx xy xz? yx yy yz zx zy zz
# https://groups.google.com/g/boltztrap/c/p6c2mOraEyM/m/Ax7JZ_4EAgAJ

gpw = glob('*.gpw')

# Print out the cell being used incase multiple .gpw files in one directory.
print("Using this file to determine uc volume: ", gpw[0])
calc = GPAW(gpw[0])

# Calculate cell volume and convert to cm^3
Vol_ang = calc.atoms.cell.volume

# If you're not using GPAW , you need to
# input your own volume manually.
Vol = Vol_ang * 1.0e-24

plt.subplots(1, 2, figsize = (14, 6))

condtens = np.genfromtxt(f'interpolation.condtens', skip_header=1)
Ef = condtens[:, 0] * Ry  # Ef: Ry -> eV
T = condtens[:, 1]  # Leave T in Kelvin
N = condtens[:, 2] / Vol  # N : e/uc -> e/cm^3

sxx = condtens[:, 3]
syy = condtens[:, 7]
szz = condtens[:, 11]

Sxx = condtens[:, 12]
Syy = condtens[:, 16]
Szz = condtens[:, 20]

# For scaning by chemical potential:
if chem_pot_scan:
    for temp in np.unique(T):
        mask = T == temp

        plt.subplot(1, 2, 1)
        plt.plot(Ef[mask], 1000*(Sxx[mask]+Syy[mask]+Szz[mask])/3, label = f"{temp} K")
        plt.title("Seebeck Coefficient v.s. Chemical Potential")
        plt.ylabel("$S$ [mV K$^{-1}$]")
        plt.xlabel("Chemical Potential [eV]")

        plt.subplot(1, 2, 2)
        plt.plot(Ef[mask], np.abs((sxx[mask]+syy[mask]+szz[mask])/3), label = f"{temp} K")
        plt.title("$\\sigma$ v.s. Chemical Potential")
        plt.ylabel("$\\sigma$ [$\\Omega$ m$^{-1}$]")
        plt.xlabel("Chemical Potential [eV]")
    plt.legend()
# For scanning by carrier concentration:
else:
    for temp in np.unique(T):
        mask = T == temp

        plt.subplot(1, 2, 1)
        plt.plot(N[mask], 1000*(Sxx[mask]+Syy[mask]+Szz[mask])/3, label = f"{temp} K")
        plt.title("Seebeck Coefficient v.s. Carrier Concentration")
        plt.ylabel("$S$ [mV K$^{-1}$]")
        plt.xlabel("Carrier Concentration [e/cm$^3$]")

        plt.subplot(1, 2, 2)
        plt.plot(N[mask], np.abs((sxx[mask]+syy[mask]+szz[mask])/3), label = f"{temp} K")
        plt.title("$\\sigma$ v.s. Carrier Concentration")
        plt.ylabel("$\\sigma$ [$\\Omega$ m$^{-1}$]")
        plt.xlabel("Carrier Concentration [e/cm$^3$]")

plt.legend()
plt.show()

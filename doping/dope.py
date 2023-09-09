from BoltzTraP2.units import Ha, eV
from ase.units import Ry
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from glob import glob
from gpaw import GPAW

# Multiply sigmas by the relaxation time:
# THINGS THAT NEED TO BE CHANGED.

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

#doping_types = ["holes", "electrons"]
doping_types = ["electrons", "holes"]
colors = {"holes":"blue",
          "electrons":"red"}

plt.subplots(1, 2, figsize = (14, 6))
for i in doping_types:
    condtens = np.genfromtxt(f'interpolation.dope_{i}.condtens', skip_header=1)
    Ef = condtens[:, 0] * Ry  # Ef: Ry -> eV
    T = condtens[:, 1]  # Leave T in Kelvin
    N = condtens[:, 2] / Vol  # N : e/uc -> e/cm^3

    sxx = condtens[:, 3]
    syy = condtens[:, 7]
    szz = condtens[:, 11]

    Sxx = condtens[:, 12]
    Syy = condtens[:, 16]
    Szz = condtens[:, 20]

    plt.subplot(1, 2, 1)
    plt.plot(T, np.abs(1000*(Sxx+Syy+Szz)/3), color = colors[i], marker = 's')
    plt.title("Seebeck Coefficient v.s. Temperature")
    plt.ylabel("|$S$| [mV K$^{-1}$]")
    plt.xlabel("Temperature [K]")

    plt.subplot(1, 2, 2)
    plt.plot(T, np.abs((sxx+syy+szz)/3), color = colors[i], marker = 's', label = i)
    plt.title("$\\sigma$ v.s. Temperature")
    plt.ylabel("|$\\sigma$| [$\\Omega$ m$^{-1}$]")
    plt.xlabel("Temperature [K]")

plt.legend()
plt.show()



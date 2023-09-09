There are two scripts in this folder:

1. run_doping.py
- This is responsible for generating the condtens files containing the hole/electron data.
- Uncomment the interpolate step at the top if you do not already have the interpolation.bt2 file.

2. dope.py 
- This is responsible for plotting S and $\sigma$ from files obtained in the above step.
- You can edit this for 2D materials to plot the relevant components
- You can easily compute $S^2\sigma$ with minor modifications to this script
- If you have $\kappa_{lattice}$, **NOT** only $\kappa_{el}$ which is what BoltzTraP2 provides, you can also plot $ZT$ easily.

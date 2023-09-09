import subprocess, os

target_conc = "1e19"
# Interpolate bands
# subprocess.run(["btp2", "-vv", "interpolate", "-m", "10", "."])

# Run n-doped config.
subprocess.run(["btp2", "-vv", "dope", "interpolation.bt2", "300:801:50", f"-{target_conc}"])
# Change default file names to match make_plots.py formatting.
os.system("cp interpolation.dope.condtens interpolation.dope_electrons.condtens")

# Run p-doped config
subprocess.run(["btp2", "-vv", "dope", "interpolation.bt2", "300:801:50", f"{target_conc}"])
# Change default file names to match make_plots.py formatting.
os.system("cp interpolation.dope.condtens interpolation.dope_holes.condtens")


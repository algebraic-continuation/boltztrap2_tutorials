from gpaw import GPAW, PW
import ase.io

LiZnSb = ase.io.read('LiZnSb.cif')

calc = GPAW(mode=PW(500),
            #mode='lcao',
            #basis='dzp',
            kpts=(10, 10, 10),
            txt='LiZnSb_unpolarized.txt')

# E.g. for QE, VASP, CP2K, etc.
# 'scf' -> 4, 4, 4
# 'nscf' -> 10, 10, 10

LiZnSb.calc = calc
e = LiZnSb.get_potential_energy()
calc.write('LiZnSb_unpolarized.gpw')

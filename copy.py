# 20/12/2021
#
# SP - Dummy script to create and copy files in directories.

import numpy as np
import os

elements = ['Ag',
'Al',
'Ar',
'As',
'At',
'Au',
'Ba',
'Be',
'B',
'Bi',
'Br',
'Ca',
'Cd',
'Ce',
'C',
'Cl',
'Co',
'Cr',
'Cs',
'Cu',
'Dy',
'Er',
'Eu',
'Fe',
'F',
'Ga',
'Gd',
'Ge',
'He',
'Hf',
'H',
'Hg',
'Ho',
'I',
'In',
'Ir',
'K',
'Kr',
'La',
'Li',
'Lu',
'Mg',
'Mn',
'Mo',
'Na',
'Nb',
'Nd',
'Ne',
'N',
'Ni',
'O',
'Os',
'Pb',
'Pd',
'P',
'Pm',
'Po',
'Pr',
'Pt',
'Rb',
'Re',
'Rh',
'Rn',
'Ru',
'Sb',
'Sc',
'Se',
'S',
'Si',
'Sm',
'Sn',
'Sr',
'Ta',
'Tb',
'Tc',
'Te',
'Ti',
'Tl',
'Tm',
'V',
'W',
'Xe',
'Yb',
'Y',
'Zn',
'Zr']

for ii in np.arange(100):
#  os.system('mkdir '+str(elements[ii]))
#  os.system('mv '+str(elements[ii])+'.*  '+str(elements[ii])+'/')
  os.system('mv '+str(elements[ii])+'.*  '+str(elements[ii])+'/')





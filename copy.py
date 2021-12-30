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

#for ii in np.arange(100):
#  os.system('mkdir '+str(elements[ii]))
#  os.system('mv '+str(elements[ii])+'.*  '+str(elements[ii])+'/')
#  os.system('mv '+str(elements[ii])+'.*  '+str(elements[ii])+'/')

# for ii in np.arange(100):
#   os.system('cd '+str(elements[ii])+'/ && git mv '+str(elements[ii])+'.GGA_PBE-JTH.xml '+str(elements[ii])+'_std.xml && cd ../')

# for ii in np.arange(100):
#   exec_str = 'cd '+str(elements[ii])+'/ && cp '+str(elements[ii])+'_std.upf '+str(elements[ii])+'_str.upf && cd ../'
#   # print(exec_str)
#   os.system(exec_str)

# ➜  ATOMPAW-PBE-SR git:(main) ✗ cp ../PBE-sp-UPF/As.GGA-PBE-paw.UPF As/As_str.upf 
# ➜  ATOMPAW-PBE-SR git:(main) ✗ cp ../PBE-sp-UPF/Bi.GGA-PBE-paw.UPF Bi/Bi_str.upf 
# ➜  ATOMPAW-PBE-SR git:(main) ✗ cp ../PBE-sp-UPF/In.GGA-PBE-paw.UPF In/In_str.upf 
# ➜  ATOMPAW-PBE-SR git:(main) ✗ cp ../PBE-sp-UPF/Pb.GGA-PBE-paw.UPF Pb/Pb_str.upf 
# ➜  ATOMPAW-PBE-SR git:(main) ✗ cp ../PBE-sp-UPF/Sb.GGA-PBE-paw.UPF Sb/Sb_str.upf 
# ➜  ATOMPAW-PBE-SR git:(main) ✗ cp ../PBE-sp-UPF/Sn.GGA-PBE-paw.UPF Sn/Sn_str.upf 
# ➜  ATOMPAW-PBE-SR git:(main) ✗ cp ../PBE-sp-UPF/Tl.GGA-PBE-paw.UPF Tl/Tl_str.upf

for ii in np.arange(100):
  exec_str = 'cd '+str(elements[ii])+'/ && cp ../../paw_pbe_stringent/'+str(elements[ii])+'.xml '+str(elements[ii])+'_str.xml && cd ../'
  # print(exec_str)
  os.system(exec_str)




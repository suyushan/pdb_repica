# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 09:54:23 2018

@author: MARX-2
"""

import sys

T=sys.argv[1]

with open('./mdp/nvt.mdp', 'r') as f:
    para = f.readlines()
f.close()
line = para[32].split()
line[2] = str(T)
line[3] = str(T)
linef = ' '.join(line)
para[32] = linef + '\n'
line = para[39].split()
line[2] = str(T)
linef = ' '.join(line)
para[39] = linef + '\n'
with open('./mdp/nvt.mdp', 'w') as f:
    f.writelines(para)
f.close()

with open('./mdp/npt.mdp', 'r') as f:
    para = f.readlines()
f.close()
line = para[32].split()
line[2] = str(T)
line[3] = str(T)
linef = ' '.join(line)
para[32] = linef + '\n'
with open('./mdp/npt.mdp', 'w') as f:
    f.writelines(para)
f.close()
   
with open('./mdp/md.mdp', 'r') as f:
    para = f.readlines()
f.close()
line = para[33].split()
line[2] = str(T)
line[3] = str(T)
linef = ' '.join(line)
para[33] = linef + '\n'
with open('./mdp/md.mdp', 'w') as f:
    f.writelines(para)
f.close()

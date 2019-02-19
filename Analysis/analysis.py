# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
import MDAnalysis
import MDAnalysis.analysis.align
import MDAnalysis.analysis.rms
from matplotlib.ticker import MultipleLocator,MaxNLocator
from matplotlib.ticker import AutoMinorLocator,NullLocator

def calrmsd(u1,i1,u2,i2,groupdescription):
    #calculate rmsd between frame 1 and frame 2 after alignment
    #u1: object of trajectory 1
    #i1: the frame number of trajectory 1
    #u2: object of trajectory 2
    #i2: the frame number of trajectory 2
    #groupdescription: select the group we perform the alignment and rmsd calculation   
    u1.trajectory[i1]
    group1 = u1.select_atoms(groupdescription)
    r1 = group1.positions - group1.center_of_mass()
    u2.trajectory[i2]
    group2 = u2.select_atoms(groupdescription)
    r2 = group2.positions - group2.center_of_mass()
    R, rmsdtemp = MDAnalysis.analysis.align.rotation_matrix(r1, r2)
    return rmsdtemp

#num_cores = multiprocessing.cpu_count()
def rmsdsingtra(u,groupdescription):
    #In one trajectory, calculate rmsd between each frame and initial frame
    #return rmsd(A) at each time(ps)
    N=len(u.trajectory)
    t=[]
    rmsd=[]
    for i in range(N):
        u.trajectory[i]
        t.append(u.trajectory.time)
        rmsd.append(calrmsd(u,0,u,i,groupdescription))
    #rmsd = Parallel(n_jobs=num_cores)(delayed(calrmsd)(u,0,u,i,groupdescription) for i in range(N))
    return t,rmsd

def rmsd2tras(u1,u2,groupdescription):
    #calculate rmsd between 2 frames at the same simulation time
    #return rmsd(A) at each time(ps)
    N=len(u1.trajectory)
    t=[]
    rmsd=[]
    for i in range(N):
        u1.trajectory[i]
        t.append(u1.trajectory.time)
        rmsd.append(calrmsd(u1,i,u2,i,groupdescription))
    #rmsd = Parallel(n_jobs=num_cores)(delayed(calrmsd)(u,0,u,i,groupdescription) for i in range(N))
    return t,rmsd

ffi=13
pdbID='1sau'
T=300
tra=1
u1 = MDAnalysis.Universe('../output'+str(ffi)+'_'+str(pdbID)+'_'+str(T)+'K/'+str(pdbID)+'_solv_ions.gro', 
                        '../output'+str(ffi)+'_'+str(pdbID)+'_'+str(T)+'K/md_'+str(tra)+'.xtc')
tra=4
u2 = MDAnalysis.Universe('../output'+str(ffi)+'_'+str(pdbID)+'_'+str(T)+'K/'+str(pdbID)+'_solv_ions.gro', 
                        '../output'+str(ffi)+'_'+str(pdbID)+'_'+str(T)+'K/md_'+str(tra)+'.xtc')

t,rmsd=rmsd2tras(u1,u2,"protein and name CA")

fig=plt.figure(figsize=(10, 7.5))
axes = fig.add_subplot(1,1,1);
#set ticks' dense
axes.xaxis.set_major_locator(MaxNLocator(5));
axes.xaxis.set_minor_locator(AutoMinorLocator());
axes.yaxis.set_major_locator(MaxNLocator(7));
axes.yaxis.set_minor_locator(AutoMinorLocator());
#set ticks' size
for label_i in axes.get_xticklabels(): 
    label_i.set_fontsize(20) 
for label_i in axes.get_yticklabels(): 
    label_i.set_fontsize(20) 
plt.plot(t,rmsd,'--',label='forcefield'+str(ffi)+', '+str(pdbID)+', '+str(T)+'K', color='orange')
plt.legend(loc='upper right', prop={'size':18}, 
           numpoints=1, fancybox=True)
plt.ylabel('Rmsd of CA between 2 trajectories(${\AA}$)',fontsize=21)
plt.xlabel('Time (ps)',fontsize=21)
plt.savefig('Rmsd.png')
plt.show()
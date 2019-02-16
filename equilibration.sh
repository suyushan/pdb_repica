#!/bin/bash

this_dir=`pwd`

ffi=$1
pdbID=$2
T=$3

cd ./output${ffi}_${pdbID}_${T}K

gmx grompp -f ../mdp/nvt.mdp -c em.gro -r em.gro -p topol.top -o nvt.tpr
gmx mdrun -deffnm nvt
rm -f ./mdout.mdp

gmx grompp -f ../mdp/npt.mdp -c nvt.gro -r nvt.gro -t nvt.cpt -p topol.top -o npt.tpr
gmx mdrun -deffnm npt
rm -f ./mdout.mdp

cd ../

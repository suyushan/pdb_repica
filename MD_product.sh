#!/bin/bash

this_dir=`pwd`

ffi=$1
pdbID=$2
T=$3

cd ./output${ffi}_${pdbID}_${T}K

gmx grompp -f ../mdp/md.mdp -c npt.gro -t npt.cpt -p topol.top -o md_0_1.tpr

gmx mdrun -deffnm md_0_1
rm -f ./mdout.mdp

echo 10 0 | gmx energy -f md_0_1.edr -o potential1.xvg
echo 10 10 | gmx rms -s ${pdbID}_processed.gro -f md_0_1.xtc -n ../index/index${ffi}_${pdbID}.ndx -o ./rmsd/rms1.xvg

cd ../

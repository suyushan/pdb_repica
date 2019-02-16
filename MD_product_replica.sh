#!/bin/bash

this_dir=`pwd`

ffi=$1
pdbID=$2
T=$3

cd ./output${ffi}_${pdbID}_${T}K

for i in {1..10}
do
	gmx grompp -f ../mdp/md.mdp -c npt.gro -t npt.cpt -p topol.top -o md_${i}.tpr

	gmx mdrun -deffnm md_${i}
	rm -f ./mdout.mdp

	echo 10 10 | gmx rms -s ${pdbID}_processed.gro -f md_${i}.xtc -n ../index/index${ffi}_${pdbID}.ndx -o ./rmsd/rms_${i}.xvg
done

cd ../

#!/bin/bash

this_dir=`pwd`

ffi=$1
pdbID=$2
T=$3

mkdir ./output${ffi}_${pdbID}_${T}K
cd ./output${ffi}_${pdbID}_${T}K

mkdir ./rmsd

grep -v HETATM ../PDB/${pdbID}.pdb > ${pdbID}_clean.pdb
echo ${ffi} | gmx pdb2gmx -f ${pdbID}_clean.pdb -o ${pdbID}_processed.gro -water spce

gmx editconf -f ${pdbID}_processed.gro -o ${pdbID}_newbox.gro -c -d 1.0 -bt triclinic
gmx solvate -cp ${pdbID}_newbox.gro -cs spc216.gro -o ${pdbID}_solv.gro -p topol.top

gmx grompp -f ../mdp/ions.mdp -c ${pdbID}_solv.gro -p topol.top -o ions.tpr
echo SOL | gmx genion -s ions.tpr -o ${pdbID}_solv_ions.gro -p topol.top -pname NA -nname CL -neutral
rm -f ./mdout.mdp

gmx grompp -f ../mdp/minim.mdp -c ${pdbID}_solv_ions.gro -p topol.top -o em.tpr
gmx mdrun -v -deffnm em
rm -f ./mdout.mdp

echo 10 0 | gmx energy -f em.edr -o potential.xvg
echo 10 10 | gmx rms -s ${pdbID}_processed.gro -f em.gro -n ../index/index${ffi}_${pdbID}.ndx -o ./rmsd/rms.xvg

cd ../







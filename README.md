# pdb_replica
This is a package to run MD using Gromacs and analyse the result.

About MD:
1. 'submit_abc.sh' is the main bash file to perform the MD process, including initialization, equilibration and replica process:
   In initialization (init.sh), we set the protein in water environment with periodic boundary condition and perform energy minimization;
   In equilibration (equilibration.sh), NVT for 500 ps and NPT for 500 ps with position restrain on protein;
   In replica process (MD_product_replica.sh), we simulate ten MD processes (NPT) independently, 10 ns for each.
2. The detailed settings for MD can be seen at 'mdp' directory, and the PDB files we use are stored at 'PDB' directory.
3. The results are in 'output**_****_*K' directory.

About result analysis:
1. The code to analyse the result is at 'Analysis' directory.
2. Python package 'MDAnalysis' is required.

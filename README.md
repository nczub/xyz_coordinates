# xyz_coordinates
This script shows how to generate dataframe (csv file) from coordinates xyz for each molecule.

XYZ file is a chemical file format that represents molecular coordinates. It is a plain text file that stores information about the atoms in a molecule, including the element symbol, xyz-coordinates, and optionally, the atom charge. The file is commonly used in computational chemistry and materials science to store the results of simulations and analyses, and to share data with other researchers.

# Step one:
First step for dataframe is to create sdf files. This is possible thanks to rdkit library. 
https://www.rdkit.org/docs/GettingStartedInPython.html
Usually, when you're using conda enviroment, rdkit demands to create new enviroment. 

$ conda create -c conda-forge -n my-rdkit-env rdkit

$ conda activate my-rdkit-env

$ conda install -c conda-forge rdkit


File "test_database_smiles.csv" contains SMILES

SMILES (ChatGPT explanation):
SMILES (Simplified Molecular-Input Line-Entry System) is a string representation of a chemical structure used to uniquely identify a molecule. It consists of a sequence of characters, where each character represents a specific chemical element or type of bond. The atoms in a molecule are represented by their elemental symbols, and the bonds between them are represented by the characters -, =, #, :, or /. Additional characters can be used to specify certain characteristics of a molecule, such as aromaticity or chirality.

From SMILES you need to create sdf files. After activation of conda enviroment:

$ conda activate my-rdkit-env
run the script "generate_sdf_files.py"

# Step two:
generate xyz files with use of obabel
in console run:

obabel *.sdf -O*.xyz

It will change each sdf file into xyz, with specific name of sdf file.

# Step three:
In specific directory run script "create_dataframe_from_xyz_files.py".

Whole dataframe is save as csv file into xyz_coordinates_test.csv.

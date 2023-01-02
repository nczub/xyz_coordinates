# import packages
import pandas as pd
import os
from rdkit import Chem
from rdkit.Chem import AllChem

# read file with SMILES
df = pd.read_csv('test_database_smiles.csv')
mols = [Chem.MolFromSmiles(smi) for smi in df.smiles]
hmols = [Chem.AddHs(m) for m in mols]
for mol  in hmols:
    continue
    AllChem.EmbedMolecule(mol,AllChem.ETKDG())
    print(AllChem.UFFOptimizeMolecule(mol,1000))
    
smiles = list(df.smiles)
sid = list(df.id)
libs = df[df.columns[0]]

# create directory 'sdf_files'
os.mkdir('files')
for n in range(len(libs)):
    sid_n = sid[n]
    writer = Chem.SDWriter(f'files/{sid_n}.sdf')
    hmols[n].SetProp("_Name","%s"%sid[n])
    writer.write(hmols[n])
writer.close()

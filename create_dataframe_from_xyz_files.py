### creation a dataframe from xyz files
# import packages
import pandas as pd
import os
import glob

# read xyz files in specific direction 'xyz_files'
file = [os.path.basename(x).split(".")[0] for x in glob.glob(r'files/' + '*.xyz')]

os.mkdir('dataframe_files')
# creation of dataframes for each compound
for molecule_name in file:
#     print(molecule)
    molecule = pd.read_table(f"files/{molecule_name}.xyz", skiprows=2, delim_whitespace=True,
                         names=['atom', 'x', 'y', 'z'])


    # maksymalna liczba atomów może być nawet do 170,
    # mozliwe atomy: C, H, N, O, P, I, Br, F
    headers_coordinates = []
    list_of_letters = ["C", "H", "N", "O", "P", "I", "Br", "F"]
    xyz_list = ["x", "y", "z"]
    for number in range(1, 170):
    #     print(number)
        for letter in list_of_letters:
    #         print(str(number) + "_" + letter)
            for coordinate in xyz_list:
                headers_coordinates.append((str(number) + "_" + letter + "_" + coordinate))
    headers_coordinates.insert(0, "molecule_id")
    dataframe_molecule = pd.DataFrame(columns = headers_coordinates)

    i = 0
    locants = list(range(0,molecule.shape[0]))
    for i in locants:
        for coodinate in molecule:
            if molecule.loc[i].atom == "C":
                locant = i + 1
                dataframe_molecule.loc[0, f"{locant}_C_x"] = molecule.iloc[i].x
                dataframe_molecule.loc[0, f"{locant}_C_y"] = molecule.iloc[i].y
                dataframe_molecule.loc[0, f"{locant}_C_z"] = molecule.iloc[i].z
            elif molecule.loc[i].atom == "H":
                locant = i + 1
                dataframe_molecule.loc[0, f"{locant}_H_x"] = molecule.iloc[i].x
                dataframe_molecule.loc[0, f"{locant}_H_y"] = molecule.iloc[i].y
                dataframe_molecule.loc[0, f"{locant}_H_z"] = molecule.iloc[i].z
            elif molecule.loc[i].atom == "N":
                locant = i + 1
                dataframe_molecule.loc[0, f"{locant}_N_x"] = molecule.iloc[i].x
                dataframe_molecule.loc[0, f"{locant}_N_y"] = molecule.iloc[i].y
                dataframe_molecule.loc[0, f"{locant}_N_z"] = molecule.iloc[i].z
            elif molecule.loc[i].atom == "O":
                locant = i + 1
                dataframe_molecule.loc[0, f"{locant}_O_x"] = molecule.iloc[i].x
                dataframe_molecule.loc[0, f"{locant}_O_y"] = molecule.iloc[i].y
                dataframe_molecule.loc[0, f"{locant}_O_z"] = molecule.iloc[i].z
            elif molecule.loc[i].atom == "P":
                locant = i + 1
                dataframe_molecule.loc[0, f"{locant}_P_x"] = molecule.iloc[i].x
                dataframe_molecule.loc[0, f"{locant}_P_y"] = molecule.iloc[i].y
                dataframe_molecule.loc[0, f"{locant}_P_z"] = molecule.iloc[i].z
            elif molecule.loc[i].atom == "I":
                locant = i + 1
                dataframe_molecule.loc[0, f"{locant}_I_x"] = molecule.iloc[i].x
                dataframe_molecule.loc[0, f"{locant}_I_y"] = molecule.iloc[i].y
                dataframe_molecule.loc[0, f"{locant}_I_z"] = molecule.iloc[i].z
            elif molecule.loc[i].atom == "Br":
                locant = i + 1
                dataframe_molecule.loc[0, f"{locant}_Br_x"] = molecule.iloc[i].x
                dataframe_molecule.loc[0, f"{locant}_Br_y"] = molecule.iloc[i].y
                dataframe_molecule.loc[0, f"{locant}_Br_z"] = molecule.iloc[i].z
            elif molecule.loc[i].atom == "F":
                locant = i + 1
                dataframe_molecule.loc[0, f"{locant}_F_x"] = molecule.iloc[i].x
                dataframe_molecule.loc[0, f"{locant}_F_y"] = molecule.iloc[i].y
                dataframe_molecule.loc[0, f"{locant}_F_z"] = molecule.iloc[i].z
            dataframe_molecule.loc[0, "molecule_id"] = molecule_name
    dataframe_molecule.to_csv(f"dataframe_files/{molecule_name}_dataframe.csv", index = False, header = True)
    
    
# merge all dataframes into one
path = "dataframe_files/"
all_files = glob.glob(os.path.join(path, "*.csv"))

df = pd.concat((pd.read_csv(f) for f in all_files), ignore_index=True)
df.fillna(0, inplace=True)

# save dataframe
df.to_csv("xyz_coordinates_test.csv", index = False, header = True)

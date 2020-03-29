#Import des librairies necessaire  a l'analyse des Data
from functools import reduce
import numpy as np
import pandas as pd
import matplotlib as plt
import Normalize_Carac as normalize
import datetime

def getData2018Merge():
    # Import des données des different csv de l'année 2018
    DataAccident2018usagers = pd.read_csv("données/2018/usagers-2018.csv",",",encoding='latin-1', low_memory=False)
    DataAccident2018lieux = pd.read_csv("données/2018/lieux-2018.csv",",",encoding='latin-1',low_memory=False)
    DataAccident2018vehicules = pd.read_csv("données/2018/vehicules-2018.csv",",",encoding='latin-1', low_memory=False)
    DataAccident2018caracteristiques = pd.read_csv("données/2018/caracteristiques-2018.csv",",",encoding='latin-1',low_memory=False)

    # Merge dataFrame
    Data2018Frame = [DataAccident2018caracteristiques, DataAccident2018lieux, DataAccident2018vehicules, DataAccident2018usagers]
    Data2018merge = reduce(lambda left,right: pd.merge(left,right,on='Num_Acc'), Data2018Frame)

    # Normalize data
    Data2018merge = normalize.normalise_carac(Data2018merge)

    # Correction for dupplicate data
    Data2018merge = Data2018merge[Data2018merge['num_veh_x'] == Data2018merge['num_veh_y']]

    # Affichage data
    Data2018merge = Data2018merge.set_index(['Num_Acc','num_veh_x','num_veh_y'])
    return Data2018merge

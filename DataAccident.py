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
    Data2018merge['Num_Acc_Id'] = Data2018merge.Num_Acc

    # Affichage data
    Data2018merge = Data2018merge.set_index(['Num_Acc','num_veh_x','num_veh_y'])
    return Data2018merge

def getData2017Merge():
    # Import des données des different csv de l'année 2017
    DataAccident2017usagers = pd.read_csv("données/2017/usagers-2017.csv",",",encoding='latin-1', low_memory=False)
    DataAccident2017lieux = pd.read_csv("données/2017/lieux-2017.csv",",",encoding='latin-1',low_memory=False)
    DataAccident2017vehicules = pd.read_csv("données/2017/vehicules-2017.csv",",",encoding='latin-1', low_memory=False)
    DataAccident2017caracteristiques = pd.read_csv("données/2017/caracteristiques-2017.csv",",",encoding='latin-1',low_memory=False)

    # Merge dataFrame
    Data2017Frame = [DataAccident2017caracteristiques, DataAccident2017lieux, DataAccident2017vehicules, DataAccident2017usagers]
    Data2017merge = reduce(lambda left,right: pd.merge(left,right,on='Num_Acc'), Data2017Frame)

    # Normalize data
    Data2017merge = normalize.normalise_carac(Data2017merge)

    # Correction for dupplicate data
    Data2017merge = Data2017merge[Data2017merge['num_veh_x'] == Data2017merge['num_veh_y']]
    Data2017merge['Num_Acc_Id'] = Data2017merge.Num_Acc

    # Affichage data
    Data2017merge = Data2017merge.set_index(['Num_Acc','num_veh_x','num_veh_y'])
    return Data2017merge

def getData2016Merge():
    # Import des données des different csv de l'année 2016
    DataAccident2016usagers = pd.read_csv("données/2016/usagers-2016.csv",",",encoding='latin-1', low_memory=False)
    DataAccident2016lieux = pd.read_csv("données/2016/lieux-2016.csv",",",encoding='latin-1',low_memory=False)
    DataAccident2016vehicules = pd.read_csv("données/2016/vehicules-2016.csv",",",encoding='latin-1', low_memory=False)
    DataAccident2016caracteristiques = pd.read_csv("données/2016/caracteristiques-2016.csv",",",encoding='latin-1',low_memory=False)

    # Merge dataFrame
    Data2016Frame = [DataAccident2016caracteristiques, DataAccident2016lieux, DataAccident2016vehicules, DataAccident2016usagers]
    Data2016merge = reduce(lambda left,right: pd.merge(left,right,on='Num_Acc'), Data2016Frame)

    # Normalize data
    Data2016merge = normalize.normalise_carac(Data2016merge)

    # Correction for dupplicate data
    Data2016merge = Data2016merge[Data2016merge['num_veh_x'] == Data2016merge['num_veh_y']]
    Data2016merge['Num_Acc_Id'] = Data2016merge.Num_Acc

    # Affichage data
    Data2016merge = Data2016merge.set_index(['Num_Acc','num_veh_x','num_veh_y'])
    return Data2016merge

def getData2015Merge():
    # Import des données des different csv de l'année 2015
    DataAccident2015usagers = pd.read_csv("données/2015/usagers-2015.csv",",",encoding='latin-1', low_memory=False)
    DataAccident2015lieux = pd.read_csv("données/2015/lieux-2015.csv",",",encoding='latin-1',low_memory=False)
    DataAccident2015vehicules = pd.read_csv("données/2015/vehicules-2015.csv",",",encoding='latin-1', low_memory=False)
    DataAccident2015caracteristiques = pd.read_csv("données/2015/caracteristiques-2015.csv",",",encoding='latin-1',low_memory=False)

    # Merge dataFrame
    Data2015Frame = [DataAccident2015caracteristiques, DataAccident2015lieux, DataAccident2015vehicules, DataAccident2015usagers]
    Data2015merge = reduce(lambda left,right: pd.merge(left,right,on='Num_Acc'), Data2015Frame)

    # Normalize data
    Data2015merge = normalize.normalise_carac(Data2015merge)

    # Correction for dupplicate data
    Data2015merge = Data2015merge[Data2015merge['num_veh_x'] == Data2015merge['num_veh_y']]
    Data2015merge['Num_Acc_Id'] = Data2015merge.Num_Acc

    # Affichage data
    Data2015merge = Data2015merge.set_index(['Num_Acc','num_veh_x','num_veh_y'])
    return Data2015merge
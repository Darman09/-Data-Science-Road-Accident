import Normalize_Carac as normcarac
import Normalize_Lieux as normlieux
import Normalize_Usagers as normusager
import Normalize_Vehicule as normvehicule


def normalise_data(df1,df2,df3,df4):
    normcarac.normalise_carac(df1)
    normlieux.normalise_lieux(df2)
    normusager.normalise_usagers(df3)
    normvehicule.normalise_Véhicule(df4)
    return df1,df2,df3,df4

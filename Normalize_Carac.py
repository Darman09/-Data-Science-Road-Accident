import datetime

'''
    Normalisation des données de type caractéristique
'''
def normalise_carac(df):
    df.an = df.an + 2000
    df = gen_date(replace_lum(replace_agglo(replace_adr(replace_gps(replace_intersection(replace_conditions_atmo(replace_collision(df))))))))
    df = replace_dep(replace_com(df))
    df = df.rename(columns={"agg":"agglo","dep":"code_postal"})
    df = df.drop(columns=['mois','jour','hrmn','an','com'])
    df = df.rename(index=df.Num_Acc)
    return df

def replace_intersection(df):
    df.int = df.int.replace(1, 'Hors Intersection').replace(2, 'Intersection en X').replace(3, 'Intersection en T').replace(4, 'Intersection en Y').replace(5, 'Intersection à plus de 4 branches').replace(6, 'Giratoire').replace(7, 'Place').replace(8, 'Passsage à niveau').replace(9, 'Autre intersection')
    return df

def replace_conditions_atmo(df):
    df.atm = df.atm.replace(1,'Normale').replace(2,'Pluie Légère').replace(3,'Pluie Forte').replace(4,'Neig - grêle').replace(5,'Bouillard - Fumée').replace(6,'Vent fort - Tempête').replace(7,'Temps éblouissant').replace(8,'Temps couvert').replace(9,'Autre')
    return df

def replace_collision(df):
    df.col = df.col.replace(1,'Deux véhicules - frontale').replace(2,'Deux véhicules – par l’arrière').replace(3,'Deux véhicules – par le coté').replace(4,'Trois véhicules et plus – en chaîne').replace(5,'Trois véhicule et plus - collisions multiples').replace(6,'Autre collision').replace(7,'Sans collision')
    return df

def replace_gps(df):
    df.gps  = df.gps.replace('M','Métropole').replace('A','Antilles').replace('G','Guyane').replace('R','Réunion').replace('Y','Mayotte')
    return df

def replace_adr(df):
    df.adr = [str(x).upper() for x in df.adr]
    return df

def replace_lum(df):
    df.lum  = df.lum.replace(1,'Plein jour').replace(2,'Crépuscule ou aube').replace(3,'Nuit sans éclairage public').replace(4,'Nuit avec éclairage public non allumé').replace(5,'Nuit avec éclairage public allumé')
    return df

def gen_date(df):
    df['date'] = [datetime.datetime(df.an.iloc[i],df.mois.iloc[i],df.jour.iloc[i]) for i in range(len(df.an))]
    return df

def replace_agglo(df):
    df['agg'] = df['agg'].replace(1,'Hors agglomération').replace(2,'En agglomération')
    return df

def replace_com(df):
    list_com = [[i for i in str(x)] for x in df.com]
    for i in range(len(list_com)):
        if(len(list_com[i]) == 1):
            list_com[i].insert(0, "0")
        if(len(list_com[i]) == 2):
            list_com[i].insert(0, "0")
        list_com[i] = list_com[i][0] +list_com[i][1] +list_com[i][2]
    df.com = list_com
    return df

def replace_dep(df):
    list_dep = [[i for i in str(x)] for x in df.dep]
    for i in range(len(list_dep)):
        list_dep[i] = list_dep[i][0] +list_dep[i][1] + df.com.iloc[i]
    df.dep = list_dep
    return df

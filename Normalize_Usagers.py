'''
    Normalisation des données de type usagers
'''
def normalise_usagers(df):
    df = replace_etatp(replace_sexe(replace_trajet(replace_locp(replace_grav(replace_catu(replace_place(replace_actp(df))))))))
    df = df.fillna(value={"place":"Inconnu","actp":0,"locp":"Inconnu","etatp":"Inconnu"})
    return df

# Replace les valeurs de place
def replace_place(df):
    df.place  = df.place.replace(1,'Conducteur').replace(2,'Passager Avant Droite').replace(3,'Passager Arrière Droite').replace(4,'Passager Arrière Gauche').replace(5,'Passager Arrière Central').replace(6,'Passager Avant Central').replace(7,'Passager Milieu Gauche').replace(8,'Passager Milieu Central').replace(9,'Passager Milieu Droite')
    return df

# Remplace les valeyrs de catégorie d'usager
def replace_catu(df):
    df.catu = df.catu.replace(1,'Conducteur').replace(2,'Passager').replace(3,'Piéton').replace(4,'Piéton en rollet ou trotinette')
    return df

# Remplace les valeurs de gravité de l'accident
def replace_grav(df):
    df.grav = df.grav.replace(1,'Indemne').replace(2,'Tué').replace(3,'Hospitalisation').replace(4,'Blessé léger')
    return df

# Remplace le sexe de l'usager
def replace_sexe(df):
    df.sexe = df.sexe.replace(1,'Masculin').replace(2,'Féminin')
    return df

# Remplace le motif du déplacement au moment de l'accident
def replace_trajet(df):
    df.trajet = df.trajet.replace(0,'Inconnu').replace(1,'Domicile - travail').replace(2,'Domicile - école').replace(3,'Courses - achats').replace(4,'Utilisation professionnelle').replace(5,'Promenade - loisirs').replace(9,'Autres')
    return df

# Remplace la localisation du piétion
def replace_locp(df):
    df.locp = df.locp.replace(0,'Pas de piéton').replace(1,'Sur la chaussée à + de 50 m du passager piéton').replace(2,'Sur la chaussée à - de 50 du passage piétion').replace(3,'Sur un passage piéton sans signalisation lumineuse').replace(4,'Sur un passage piéton avec signalisation lumineuse').replace(5,'Sur un trottoir').replace(6,'Sur accotement').replace(7,'Sur refuge ou BAU').replace(8,'Contre allée')
    return df

# Repmlace les valeurs de l'action du piéton
def replace_actp(df):
    df.actp = df.actp.replace(0,'non renseigné ou sans objet').replace(1,'Sens véhicule heurtant').replace(2,'Sens inverse du véhicule').replace(3,'Traversant').replace(4,'Masqué').replace(5,'Jouant - Courant').replace(6,'Avec animal').replace(9,'Autre')
    return df

# Repmlace les valeurs de l'action du piéton
def replace_etatp(df):
    df.etatp = df.etatp.replace(1,'Seul').replace(2,'Accompagné').replace(3,'En groupe').replace(0,'Inconnu')
    return df

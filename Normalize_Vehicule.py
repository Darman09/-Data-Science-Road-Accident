# Replacement Int Rubrique Véhicule
def normalise_Véhicule(df):
    df = replace_choc(replace_manv(replace_obsm(replace_catv(replace_senc(replace_obs(df))))))
    return df

# Replacement de la valeur du sens de circulation
def replace_senc(df):
    df.senc = df.senc.replace(0,'Inconnu').replace(1, 'Point Kilométrique ou Point Repère Routier ou Numéro d’adresse postale croissant').replace(2, 'Point Kilométrique ou Point Repère Routier ou Numéro d’adresse postale décroissant')
    return df

# Replacement de la valeur de l'obstacle
def replace_obs(df):
    df.obs = df.obs.replace(0, 'Aucun').replace(1, 'Véhicule en stationnement').replace(2, 'Arbre').replace(3, 'Glissière métallique').replace(4, 'Glissière béton').replace(5, 'Autre Glissière').replace(6, 'Bâtiment, mur, pile de pont').replace(7, 'Support de signalisation verticale ou poste d’appel d’urgence').replace(8, 'Poteau').replace(9, 'Mobilier urbain').replace(10, 'Parapet').replace(11, 'Ilot, refuge, borne haute').replace(12, 'Bordure de trottoir').replace(13, 'Fossé, talus, paroi rocheuse').replace(14, 'Autre obstacle fixe sur chaussée ').replace(15, 'Autre obstacle fixe sur trottoir ou accotement').replace(16, 'Sortie de chaussée sans obstacle').replace(2, 'Point Kilométrique ou Point Repère Routier ou Numéro d’adresse postale décroissant')
    return df

def replace_catv(df):
    df.catv = df.catv.replace(1, 'Bicyclette').replace(2, 'Cyclomoteur <50cm3').replace(3, 'Voiturette').replace(4, 'Scooter immatriculé').replace(5, 'Motocyclette').replace(6, 'Side-Car').replace(7, 'Véhicule Léger seul').replace(8, 'Véhicule léger + caravane').replace(9, 'Véhicule léger + remorque').replace(10, 'Véhicule Utilitaire seul').replace(11, 'Véhicule Utilitaire + caravane').replace(12, 'Véhicule Utilitaire + remorque').replace(13, 'Poids Lourd < 7.5T seul').replace(14, 'Poids Lourd > 7.5T seul').replace(15, 'Poids Lourd > 3.5T + remorque').replace(16, 'Tracteur Routier seul').replace(17, 'Tracteur routier + semi-remorque').replace(18, 'Transport en commun').replace(19, 'Tramway').replace(20, 'Engin spécial').replace(21, 'Tracteur agricole').replace(30, 'Scooter < 50 cm3').replace(31, 'Motocyclette > 50 cm3   et <= 125 cm3').replace(32, 'Scooter > 50 cm3 et <= 125 cm3').replace(33, 'Motocyclette > 125 cm3').replace(34, 'Scooter > 125 cm3').replace(35, 'Quad léger <= 50 cm3').replace(36, 'Quad léger > 50 cm3').replace(37, 'Autobus').replace(38, 'Autocar').replace(39, 'Train').replace(40, 'Tramway').replace(99, 'Autre véhicule')
    return df

def replace_obsm(df):
    df.obsm = df.obsm.replace(1, 'Piéton').replace(2, 'Véhicule').replace(3, 'Véhicule sur rail').replace(4, 'Animal domestique').replace(5, 'Animal sauvage').replace(6, 'Autre')
    return df

def replace_choc(df):
    df.choc = df.choc.replace(0, 'Inconnu').replace(1, 'Avant').replace(2, 'Avant droit').replace(3, 'Avant gauche').replace(4, 'Arrière').replace(5, 'Arrière droit').replace(6, 'Arrière gauche').replace(7, 'Côté droit').replace(8, 'Côté gauche').replace(9, 'Chocs multiples')
    return df

def replace_manv(df):
    df.manv = df.manv.replace(0, 'Inconnu').replace(1, 'Sans changement de direction').replace(2, 'Même sens, même file').replace(3, 'Entre 2 files').replace(4, 'En marche arrière').replace(5, 'A contresens').replace(6, 'En franchissant le terre-plein central').replace(7, 'Dans le couloir bus, dans le même sens').replace(8, 'Dans le couloir bus, dans le sens inverse').replace(9, 'En s’insérant').replace(10, 'En faisant demi-tour sur la chaussée').replace(11, 'Changeant de file à gauche').replace(12, 'Changeant de file à droite').replace(13, 'Déporté à gauche').replace(14, 'Déporté à droite').replace(15, 'Tournant à gauche').replace(16, 'Tournant à droite').replace(17, 'Dépassant à gauche').replace(18, 'Dépassant à droite').replace(19, 'Traversant la chaussée').replace(20, 'Manœuvre de stationnement').replace(21, 'Manœuvre d’évitement').replace(22, 'Ouverture de porte').replace(23, 'Arrêté (hors stationnement)').replace(24, 'En stationnement (avec occupants)')
    return df
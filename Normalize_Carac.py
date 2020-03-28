import datetime

'''
    Normalisation des données de type caractéristique
'''
def normalise_carac(df):
    # df.an = df.an + 2000
    df = gen_date(replace_lum(replace_agglo(replace_adr(replace_gps(replace_intersection(replace_conditions_atmo(replace_collision(replace_etatp(replace_sexe(replace_trajet(replace_locp(replace_grav(replace_catu(replace_place(replace_actp(replace_catr(replace_circ(replace_infra(replace_plan(replace_prof(replace_situ(replace_surf(replace_surf(replace_vosp(replace_choc(replace_manv(replace_obsm(replace_catv(replace_senc(replace_obs(df)))))))))))))))))))))))))))))))
    # df = replace_dep(replace_com(df))
    # df = df.rename(columns={"agg":"agglo","dep":"code_postal"})
    # df = df.drop(columns=['mois','jour','hrmn','an','com'])
    # df = df.rename(index=df.Num_Acc)
    # df = df.fillna(value={"place": "Inconnu", "actp": 0, "locp": "Inconnu", "etatp": "Inconnu"})
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

'''
    Normalisation des données de type usagers
'''
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

# Replacement catr (Categorie de route)
def replace_catr(df):
    df.catr = df.catr.replace(1, 'Autoroute').replace(2, 'Route Nationale').replace(3, 'Route Départementale').replace(4, 'Voie Communale').replace(5, 'Hors réseau public').replace(6, ' Parc de stationnement ouvert à la circulation publique').replace(9, 'Autre')
    return df
# Replacement circ (Régime de circulation)
def replace_circ(df):
    df.circ = df.circ.replace(1,'A sens unique').replace(2,'Bidirectionnelle').replace(3,'A chaussées séparées').replace(4,'Avec voies d’affectation variable')
    return df
# Replacement vosp (Existence d’une voie réservée)
def replace_vosp(df):
    df.vosp = df.vosp.replace(0,'Aucune voie réservée').replace(1,'Piste cyclable ').replace(2,'Banque cyclable').replace(3,'Voie réservée')
    return df
# Replacement prof (décrit la déclivité de la route à l'endroit de l'accident)
def replace_prof(df):
    df.prof = df.prof.replace(1,'Plat').replace(2,'Pente').replace(3,'Sommet de côte').replace(4,'Bas de côte')
    return df
# Replacement plan (Tracé en plan)
def replace_plan(df):
    df.plan = df.plan.replace(1,'Partie rectiligne').replace(2,'En courbe à gauche').replace(3,'En courbe à droite').replace(4,'En « S »')
    return df
# Replacement surf (Etat de la surface)
def replace_surf(df):
    df.surf = df.surf.replace(1,'Normale').replace(2,'Mouillée').replace(3,'Flaques').replace(4,'Inondée').replace(5,'Enneigée').replace(6,'Boue').replace(7,'Verglacée').replace(8,'Corps gras - Huile').replace(9,'Autre')
    return df
# Replacement infra (Aménagement - Infrastructure)
def replace_infra(df):
    df.infra = df.infra.replace(1,'Souterrain - tunnel').replace(2,'Pont - autopont').replace(3,'Bretelle d’échangeur ou de raccordement').replace(4,'Voie ferrée').replace(5,'Carrefour aménagé').replace(6,'Zone piétonne').replace(7,' Zone de péage')
    return df
# Replacement situ (Situation de l’accident :)
def replace_situ(df):
    df.situ = df.situ.replace(1,' Sur chaussée').replace(2,'Sur bande d’arrêt d’urgence ').replace(3,'Sur accotement').replace(4,'Sur trottoir').replace(5,'Sur piste cyclable')
    return df


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


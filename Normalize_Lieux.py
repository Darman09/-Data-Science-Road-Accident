# Replacement Int Rubrique Lieux
def normalise_lieux(df) :
    df = replace_catr(replace_circ(replace_infra(replace_plan(replace_prof(replace_situ(replace_surf(replace_surf(replace_vosp(df)))))))))
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
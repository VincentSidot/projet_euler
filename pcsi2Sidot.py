## Fonction 

def bissextile(annee):
    if (annee%4==0 and annee%100!=0) or annee%400==0:
        return True
    else:
        return False
        
def nombreAnneeBissextile(a1,a2):
    return abs((a1//4-a1//100+a1//400)-(a2//4-a2//100+a2//400))
        
JourSemaine = ['Lundi','Mardi','Mercredi','Jeudi','Vendredi','Samedi','Dimanche']

def Doomsdays(annee):
    doomsdays2018 = 2
    return (doomsdays2018 - abs(2018 - annee + nombreAnneeBissextile(2018,annee)))%7

def DateVersNombreJour(jour,mois,annee):
    """
    Date au format jj/mm/aa
    Par exemple DateVersNombreJour(31,1,xxxx) = 31
    
    reforme calendrier passage du 9/12/1582 à 20/12/1582
    
    """
    NombreJour = [31,0,31,30,31,30,31,31,30,31,30,31]
    if bissextile(annee):
        NombreJour[1] = 29
    else:
        NombreJour[1] = 28
    if jour > NombreJour[mois-1]:
        return "Date inexistante"                
    rep = jour
    if annee == 1582: #Annee de la réforme
        if mois == 12 and jour > 9: # Mois de la réforme
            if jour < 20: # Cette date n'existe pas
                return "Date inexistante"
            else:
                rep -= 10 # On retire les 10jour en trop
    for i in range(mois-1):
        rep += NombreJour[i]
    return rep

def JourDeLaSemaine(jour,mois,annee):
    """
        On sait que le dernier jour de février sera le doomsdays
        par exemple le doomsdays de 2018 est mercredi, par consequent le 28/02/2018 est un mercredi
    """
    return JourSemaine[(DateVersNombreJour(jour,mois,annee)-DateVersNombreJour(0,3,annee)+Doomsdays(annee))%7]
    
##
# Programme
jour,mois,annee = -1,-1,-1    

annee = int(input("Entrez l'année :"))
while mois > 12 or mois < 1:
    mois = int(input("Entrez le mois :"))

NombreJour = [31,0,31,30,31,30,31,31,30,31,30,31]
if bissextile(annee):
    NombreJour[1] = 29
else:
    NombreJour[1] = 28
    
while jour < 1 or jour > NombreJour[mois-1]:
    jour = int(input("Entrez le jour :"))

if annee == 1582 and mois == 12 and jour > 9 and jour < 20:
    print("Date inexistante")
else:
    print("Le jour de la semaine du {}/{}/{} est un {}".format(jour,mois,annee,JourDeLaSemaine(jour,mois,annee)))
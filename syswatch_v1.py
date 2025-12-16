import collector  # Importation fichier collector 

def octets_vers_go(octets):
    """Convertit des octets en Go formatés (string)."""
    go = octets / (1024 ** 3)
    return f"{go:.2f} Go"

def afficher_infos_globales(data):
    # On formate la date proprement
    date_str = data['timestamp'].strftime("%d/%m/%Y à %H:%M:%S")
    print(f"=== Rapport système du {date_str} ===")

def afficher_systeme(data_sys):
    print("\n--- SYSTÈME ---")
    print(f"OS        : {data_sys['os']}")
    print(f"Version   : {data_sys['version']}")
    print(f"Machine   : {data_sys['hostname']}")

def afficher_cpu(data_cpu):
    print("\n--- CPU ---")
    print(f"Physiques : {data_cpu['coeurs_physiques']}")
    print(f"Logiques  : {data_cpu['coeurs_logiques']}")
    print(f"Utilisation : {data_cpu['utilisation']}%")

def afficher_memoire(data_mem):
    print("\n--- MÉMOIRE ---")
    # On utilise notre fonction de conversion ici
    total = octets_vers_go(data_mem['total'])
    dispo = octets_vers_go(data_mem['disponible'])
    
    print(f"Total     : {total}")
    print(f"Dispo     : {dispo}")
    print(f"Utilisé   : {data_mem['pourcentage']}%")

def afficher_disques(liste_disques):
    print("\n--- DISQUES ---")
    for disque in liste_disques:
        total = octets_vers_go(disque['total'])
        print(f"[{disque['point_montage']}] : {disque['pourcentage']}% (Total: {total})")

#Affichage principal
if __name__ == "__main__":
    print("Collecte des données en cours... (Patientez 1s)")
    
    donnees = collector.collecter_tout()
    
    afficher_infos_globales(donnees)
    afficher_systeme(donnees['systeme'])
    afficher_cpu(donnees['cpu'])
    afficher_memoire(donnees['memoire'])
    afficher_disques(donnees['disques'])
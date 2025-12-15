import platform
import psutil

def afficher_infos_systeme():
    print("\n=== Système ===")
    print(f"OS           : {platform.system()}")
    print(f"Version      : {platform.release()}")
    print(f"Architecture : {platform.machine()}")
    print(f"Processeur   : {platform.processor()}")

def afficher_infos_cpu():
    print("\n=== CPU ===")
    nb_physiques = psutil.cpu_count(logical=False)
    nb_logiques = psutil.cpu_count(logical=True)
    usage = psutil.cpu_percent(interval=1)

    print(f"Coeurs physiques : {nb_physiques}")
    print(f"Coeurs logiques  : {nb_logiques}")
    print(f"Utilisation      : {usage}%")

def afficher_infos_memoire():
    print("\n=== Mémoire ===")
    mem = psutil.virtual_memory()
    
    # Conversion en Go (1024 puissance 3)
    total_go = mem.total / (1024 ** 3)
    dispo_go = mem.available / (1024 ** 3)
    
    print(f"Total       : {total_go:.2f} Go")
    print(f"Disponible  : {dispo_go:.2f} Go")
    print(f"Utilisation : {mem.percent}%")

def afficher_infos_disques():
    print("\n=== Disques ===")
    partitions = psutil.disk_partitions()
    
    for p in partitions:
        try:
            usage = psutil.disk_usage(p.mountpoint)
            print(f"{p.mountpoint} : {usage.percent}% utilisé")
        except PermissionError:
            print(f"{p.mountpoint} : Accès refusé")

if __name__ == "__main__":
    print("=== SysWatch v1.0 ===")
    afficher_infos_systeme()
    afficher_infos_cpu()
    afficher_infos_memoire()
    afficher_infos_disques()
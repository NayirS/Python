import platform
import psutil
from datetime import datetime

def collecter_info_systeme():
    """Récupère les informations statiques de l'OS."""
    return {
        'os': platform.system(),
        'version': platform.release(),
        'architecture': platform.machine(),
        'hostname': platform.node()
    }

def collecter_cpu():
    """Récupère les infos CPU. Bloque pendant 1 seconde pour la mesure."""
    return {
        'coeurs_physiques': psutil.cpu_count(logical=False),
        'coeurs_logiques': psutil.cpu_count(logical=True),
        'utilisation': psutil.cpu_percent(interval=1)
    }

def collecter_memoire():
    """Récupère les infos de la RAM en octets bruts."""
    mem = psutil.virtual_memory()
    return {
        'total': mem.total,
        'disponible': mem.available,
        'pourcentage': mem.percent
    }

def collecter_disques():
    """Récupère une liste de partitions et leur utilisation."""
    liste_partitions = []
    partitions = psutil.disk_partitions()

    for p in partitions:
        try:
            usage = psutil.disk_usage(p.mountpoint)
            infos_disque = {
                'point_montage': p.mountpoint,
                'total': usage.total,
                'utilise': usage.used,
                'pourcentage': usage.percent
            }
            liste_partitions.append(infos_disque)
        except PermissionError:
            continue # On ignore les disques inaccessibles
            
    return liste_partitions

def collecter_tout():
    """Fonction globale qui assemble toutes les données."""
    return {
        'timestamp': datetime.now(),
        'systeme': collecter_info_systeme(),
        'cpu': collecter_cpu(),
        'memoire': collecter_memoire(),
        'disques': collecter_disques()
    }
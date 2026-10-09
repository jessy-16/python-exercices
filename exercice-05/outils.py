def convertir_note(texte):
    """Convertit "12,5" en 12.5. Renvoie None si le texte est invalide"""
    try:
        return float(texte.replace(",", "."))
    except ValueError:
        return None


def moyenne(valeurs):
    """Renvoie la moyenne d'une liste de nombres"""
    return sum(valeurs) / len(valeurs)


def mention(note):
    """Renvoie la mention correspondant à une note sur 20"""
    if note >= 16:
        return "Très bien"
    elif note >= 14:
        return "Bien"
    elif note >= 12:
        return "Assez bien"
    elif note >= 10:
        return "Passable"
    else:
        return "Insuffisant"
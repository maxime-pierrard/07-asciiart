"""
Exercice 07-asciiart : Encodage d'une chaîne en une liste de tuples représentant
les caractères consécutifs et leur nombre d'occurrences.
"""

#### Imports et définition des variables globales

#### Fonctions secondaires


def artcode_i(s):
    """Encode une chaîne de caractères en une liste de tuples représentant les caractères
    consécutifs et leur nombre d'occurrences.

    Args:
        s (str): La chaîne de caractères à encoder.

    Returns:
        list: Une liste de tuples encodant la chaîne.
    """
    if not s:
        return []

    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append((s[i - 1], count))
            count = 1
    result.append((s[-1], count))
    return result


def artcode_r(s):
    """Encode une chaîne de caractères en une liste de tuples représentant les caractères
    consécutifs et leur nombre d'occurrences, en utilisant une approche itérative.

    Args:
        s (str): La chaîne de caractères à encoder.

    Returns:
        list: Une liste de tuples (caractère, nombre d'occurrences) encodant la chaîne.
    """
    result = []
    while s:
        char = s[0]
        count = 1
        while count < len(s) and s[count] == char:
            count += 1
        result.append((char, count))
        s = s[count:]
    return result


#### Fonction principale


def main():
    """Fonction principale pour tester les fonctions artcode_i et artcode_r."""
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))


if __name__ == "__main__":
    main()

def search4vowels (phrase: str) -> set:
    """ Returns vowels found in the phrase."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def searchforletters (phrase: str, letters: str = 'aeiou') -> set:
    """ Returns user defined letters found in the phrase.
        Default letters for search are vowels. """
    return letters.intersection(set(phrase))

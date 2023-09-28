def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """

    words_list = phrase.split()
    capitalized_words = [word.capitalize() for word in words_list]

    return " ".join(capitalized_words)

print(titleize('this is awesome'))


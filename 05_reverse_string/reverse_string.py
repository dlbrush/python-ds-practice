def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    phrase_arr = list(phrase)
    phrase_arr.reverse()
    return "".join(phrase_arr)

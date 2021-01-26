def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    forwards_list = [char.lower() for char in phrase if char != " "]

    backwards_list = forwards_list.copy()
    backwards_list.reverse()

    if forwards_list == backwards_list:
        return True

    return False

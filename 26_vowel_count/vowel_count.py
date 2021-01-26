def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    freq_map = {}
    for char in phrase:
        if char.lower() in 'aeiou':
            if freq_map.get(char.lower()) == None:
                freq_map[char.lower()] = 1
            else:
                freq_map[char.lower()] += 1

    return freq_map
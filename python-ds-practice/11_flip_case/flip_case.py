def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    result = []
    to_swap_lower_case = to_swap.lower()

    for char in phrase:
        if char.lower() == to_swap_lower_case:
            result.append(char.swapcase())
        else:
            result.append(char)
            
    return ''.join(result)
    

print(flip_case('Aaaahhh', 'a'))
print(flip_case('Aaaahhh', 'A'))

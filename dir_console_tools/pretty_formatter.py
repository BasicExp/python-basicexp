

def print_title_with_stars(title: str, count: int = 100, symbol: str = "~`*"):
    """ Print a title centred with two rows of stars above and below
    :rtype None
    """
    centring_space_count = int((count - len(title)) / 2)
    count = count / int(len(symbol))
    print_symbols(symbol, count)
    print(' ' * centring_space_count + title)
    print_symbols(symbol, count)
    print()
    return None


def print_symbol_rows(row_count: int, count: int, symbol: str = "~`*"):
    """Prints out the symbol indicated until the maximum character count
    is reached. For example, a three character string and a count of 100
    would print the symbol 33 times
    :rtype: None
    """
    star_count = int(count / len(symbol))
    print()
    for i in range(0, row_count):
        print_symbols(symbol, star_count)
    print()
    return None


def print_symbols(string: str, count: int):
    """Print a string or character the number of times specified
    :rtype: None
    """
    count = int(count)
    print(string * count)
    return None



def print_title_with_stars(title, star_count):
    """ Print a title centred with two rows of stars above and below"""
    centring_space_count = (star_count - len(title)) / 2
    print('*' * star_count)
    print(' ' * centring_space_count + title)
    print('*' * star_count)
    return None


def print_stars_rows(row_count, star_count):
    """Print rows of stars with a newline before and after"""
    print()
    for i in range(row_count, 3):
        print('*' * star_count)
    print()
import random


def divide_with_overlap(lst, splits):
    """
    split up the 1d list into a 2d list with len(splits) where a value from
    one sublist may appear in another sublist, but values will not be
    duplicated within a particular sublist
    """
    shuffled_lst = lst.copy()
    random.shuffle(shuffled_lst)
    grouped_lst = group(shuffled_lst, splits)
    for sublist in grouped_lst:
        for i in range(random.randint(0, splits)):
            overlap_element = random.choice(shuffled_lst)
            if overlap_element not in sublist:
                sublist.append(overlap_element)
    return grouped_lst


def group(lst, splits):
    """
    https://stackoverflow.com/questions/24483182
    """
    # Subdivide list.

    chunk_size = len(lst) // splits
    lst = [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]
    # If it is an uneven list.
    if len(lst) > splits:
        # Take the last part of the list and append
        # it to the last equal division.
        lst[splits-1].extend(sum(lst[splits:], []))
    # Return the list up to that point.
    return lst[:splits]


def curses_multiline_add_str(stdscr, start_row, col, string):
    lines_to_print = string.splitlines()
    row_delta = 0
    for line in lines_to_print:
        stdscr.addstr(start_row + row_delta, col, line)
        row_delta += 1

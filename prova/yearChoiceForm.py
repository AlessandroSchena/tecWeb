def yearChoice(first, last):
    year = []
    for y in range(last, first, -1):
        year_tuple = str(y), y
        year.append(year_tuple)
    year.append(('empty', 'empty'))
    return year
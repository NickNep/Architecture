def volume_calc(consumption, distance):
    """
    aplly consumption, distance
    :param consumption:
    :param distance:
    :return: volume:
    >>> volume_calc(5,10)
    50

    """
    return consumption * distance


def distance_calc(consumption, volume):
    """
    sub volume, consumption
    :param consumption:
    :param volume:
    :return: distance:
    >>> distance_calc(2,20)
    10.0

    """
    return volume / consumption

if __name__ == "__main__":
    import doctest
    doctest.testmod()

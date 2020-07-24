""" Convert between different units of temperature """


def celsius_to_fahrenheit(celsius: float, digits: int = 2) -> float:
    """
    Convert a given value from Celsius to Fahrenheit and round it to 2 decimal places.
    Wikipedia reference: https://en.wikipedia.org/wiki/Celsius
    Wikipedia reference: https://en.wikipedia.org/wiki/Fahrenheit

    >>> celsius_to_fahrenheit(-40.0)
    -40.0
    >>> celsius_to_fahrenheit(-20.0)
    -4.0
    >>> celsius_to_fahrenheit(0)
    32.0
    >>> celsius_to_fahrenheit(20)
    68.0
    >>> celsius_to_fahrenheit("40")
    104.0
    >>> celsius_to_fahrenheit("celsius")
    Traceback (most recent call last):
    ...
    ValueError: could not convert string to float: 'celsius'
    """
    return round((float(celsius) * 9 / 5) + 32, digits)


def celsius_to_kelvin(celsius: float, digits: int = 2) -> float:
    """
    Convert a given value from Celsius to Kelvin and round it to 2 decimal places.
    Wikipedia reference: https://en.wikipedia.org/wiki/Celsius
    Wikipedia reference: https://en.wikipedia.org/wiki/Kelvin

    >>> celsius_to_kelvin(0)
    273.15
    >>> celsius_to_kelvin(20.0)
    293.15
    >>> celsius_to_kelvin("40")
    313.15
    >>> celsius_to_kelvin("celsius")
    Traceback (most recent call last):
    ...
    ValueError: could not convert string to float: 'celsius'
    """
    return round(float(celsius) + 273.15, digits)


def celsius_to_rankine(celsius: float, digits: int = 2) -> float:
    """
    Convert a given value from Celsius to Rankine and round it to 2 decimal places.
    Wikipedia reference: https://en.wikipedia.org/wiki/Celsius
    Wikipedia reference: https://en.wikipedia.org/wiki/Rankine_scale

    >>> celsius_to_rankine(0)
    491.67
    >>> celsius_to_rankine(20.0)
    527.67
    >>> celsius_to_rankine("40")
    563.67
    >>> celsius_to_rankine("celsius")
    Traceback (most recent call last):
    ...
    ValueError: could not convert string to float: 'celsius'
    """
    return round((float(celsius) * 9 / 5) + 491.67, digits)


def fahrenheit_to_celsius(fahrenheit: float, digits: int = 2) -> float:
    """
    Convert a given value from Fahrenheit to Celsius and round it to 2 decimal places.
    Wikipedia reference: https://en.wikipedia.org/wiki/Fahrenheit
    Wikipedia reference: https://en.wikipedia.org/wiki/Celsius

    >>> fahrenheit_to_celsius(0)
    -17.78
    >>> fahrenheit_to_celsius(20.0)
    -6.67
    >>> fahrenheit_to_celsius(40.0)
    4.44
    >>> fahrenheit_to_celsius(60)
    15.56
    >>> fahrenheit_to_celsius(80)
    26.67
    >>> fahrenheit_to_celsius("100")
    37.78
    >>> fahrenheit_to_celsius("fahrenheit")
    Traceback (most recent call last):
    ...
    ValueError: could not convert string to float: 'fahrenheit'
    """
    return round((float(fahrenheit) - 32) * 5 / 9, digits)


def fahrenheit_to_kelvin(fahrenheit: float, digits: int = 2) -> float:
    """
    Convert a given value from Fahrenheit to Kelvin and round it to 2 decimal places.
    Wikipedia reference: https://en.wikipedia.org/wiki/Fahrenheit
    Wikipedia reference: https://en.wikipedia.org/wiki/Kelvin

    >>> fahrenheit_to_kelvin(0)
    255.37
    >>> fahrenheit_to_kelvin(20.0)
    266.48
    >>> fahrenheit_to_kelvin(40.0)
    277.59
    >>> fahrenheit_to_kelvin(60)
    288.71
    >>> fahrenheit_to_kelvin(80)
    299.82
    >>> fahrenheit_to_kelvin("100")
    310.93
    >>> fahrenheit_to_kelvin("fahrenheit")
    Traceback (most recent call last):
    ...
    ValueError: could not convert string to float: 'fahrenheit'
    """
    return round(((float(fahrenheit) - 32) * 5 / 9) + 273.15, digits)


def fahrenheit_to_rankine(fahrenheit: float, digits: int = 2) -> float:
    """
    Convert a given value from Fahrenheit to Rankine and round it to 2 decimal places.
    Wikipedia reference: https://en.wikipedia.org/wiki/Fahrenheit
    Wikipedia reference: https://en.wikipedia.org/wiki/Rankine_scale

    >>> fahrenheit_to_rankine(0)
    459.67
    >>> fahrenheit_to_rankine(20.0)
    479.67
    >>> fahrenheit_to_rankine(40.0)
    499.67
    >>> fahrenheit_to_rankine(60)
    519.67
    >>> fahrenheit_to_rankine(80)
    539.67
    >>> fahrenheit_to_rankine("100")
    559.67
    >>> fahrenheit_to_rankine("fahrenheit")
    Traceback (most recent call last):
    ...
    ValueError: could not convert string to float: 'fahrenheit'
    """
    return round(float(fahrenheit) + 459.67, digits)


def kelvin_to_celsius(kelvin: float, digits: int = 2) -> float:
    """
    Convert a given value from Kelvin to Celsius and round it to 2 decimal places.
    Wikipedia reference: https://en.wikipedia.org/wiki/Kelvin
    Wikipedia reference: https://en.wikipedia.org/wiki/Celsius

    >>> kelvin_to_celsius(273.15)
    0.0
    >>> kelvin_to_celsius(300)
    26.85
    >>> kelvin_to_celsius("315.5")
    42.35
    >>> kelvin_to_celsius("kelvin")
    Traceback (most recent call last):
    ...
    ValueError: could not convert string to float: 'kelvin'
    """
    return round(float(kelvin) - 273.15, digits)


def kelvin_to_fahrenheit(kelvin: float, digits: int = 2) -> float:
    """
    Convert a given value from Kelvin to Fahrenheit and round it to 2 decimal places.
    Wikipedia reference: https://en.wikipedia.org/wiki/Kelvin
    Wikipedia reference: https://en.wikipedia.org/wiki/Fahrenheit

    >>> kelvin_to_fahrenheit(273.15)
    32.0
    >>> kelvin_to_fahrenheit(300)
    80.33
    >>> kelvin_to_fahrenheit("315.5")
    108.23
    >>> kelvin_to_fahrenheit("kelvin")
    Traceback (most recent call last):
    ...
    ValueError: could not convert string to float: 'kelvin'
    """
    return round(((float(kelvin) - 273.15) * 9 / 5) + 32, digits)


def kelvin_to_rankine(kelvin: float, digits: int = 2) -> float:
    """
    Convert a given value from Kelvin to Rankine and round it to 2 decimal places.
    Wikipedia reference: https://en.wikipedia.org/wiki/Kelvin
    Wikipedia reference: https://en.wikipedia.org/wiki/Rankine_scale

    >>> kelvin_to_rankine(0)
    0.0
    >>> kelvin_to_rankine(20.0)
    36.0
    >>> kelvin_to_rankine("40")
    72.0
    >>> kelvin_to_rankine("kelvin")
    Traceback (most recent call last):
    ...
    ValueError: could not convert string to float: 'kelvin'
    """
    return round((float(kelvin) * 9 / 5), digits)


def rankine_to_celsius(rankine: float, digits: int = 2) -> float:
    """
    Convert a given value from Rankine to Celsius and round it to 2 decimal places.
    Wikipedia reference: https://en.wikipedia.org/wiki/Rankine_scale
    Wikipedia reference: https://en.wikipedia.org/wiki/Celsius

    >>> rankine_to_celsius(273.15)
    -121.4
    >>> rankine_to_celsius(300)
    -106.48
    >>> rankine_to_celsius("315.5")
    -97.87
    >>> rankine_to_celsius("rankine")
    Traceback (most recent call last):
    ...
    ValueError: could not convert string to float: 'rankine'
    """
    return round((float(rankine) - 491.67) * 5 / 9, digits)


def rankine_to_fahrenheit(rankine: float, digits: int = 2) -> float:
    """
    Convert a given value from Rankine to Fahrenheit and round it to 2 decimal places.
    Wikipedia reference: https://en.wikipedia.org/wiki/Rankine_scale
    Wikipedia reference: https://en.wikipedia.org/wiki/Fahrenheit

    >>> rankine_to_fahrenheit(273.15)
    -186.52
    >>> rankine_to_fahrenheit(300)
    -159.67
    >>> rankine_to_fahrenheit("315.5")
    -144.17
    >>> rankine_to_fahrenheit("rankine")
    Traceback (most recent call last):
    ...
    ValueError: could not convert string to float: 'rankine'
    """
    return round(float(rankine) - 459.67, digits)


def rankine_to_kelvin(rankine: float, digits: int = 2) -> float:
    """
    Convert a given value from Rankine to Kelvin and round it to 2 decimal places.
    Wikipedia reference: https://en.wikipedia.org/wiki/Rankine_scale
    Wikipedia reference: https://en.wikipedia.org/wiki/Kelvin

    >>> rankine_to_kelvin(0)
    0.0
    >>> rankine_to_kelvin(20.0)
    11.11
    >>> rankine_to_kelvin("40")
    22.22
    >>> rankine_to_kelvin("rankine")
    Traceback (most recent call last):
    ...
    ValueError: could not convert string to float: 'rankine'
    """
    return round((float(rankine) * 5 / 9), digits)


if __name__ == "__main__":

    import doctest

    doctest.testmod()

def convert_to_celcius(fahrenheit):
    '''(number) -> float
    Return the number of celcius degrees equivalent to Fahrenheit degrees
    >>> convert_to_celcius(32)
    0.0
    >>> convert_to_celcius(212)
    100.0'''
    return (fahrenheit-32)/1.8

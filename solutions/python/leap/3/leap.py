def leap_year(year):
    
    """Determine if a year is a leap year in the Gregorian calendar.

    A leap year occurs every 4 years, except for years divisble by 100(unless also dvisible by 400).

    Args:
        year - int: representing the year to check

    Returns:
        bool: True if the year is a leap year, False otherwise
    """
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
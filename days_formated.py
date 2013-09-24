#! /usr/bin/env python
# -*- coding: utf-8 ; mode: python -*-
# © Copyright 2010–2 ospalh@gmail.com
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html

import math
import sys
from decimal import Decimal

__version__ = '1.3.0'

year = 365.2421897

if sys.platform.startswith("win32"):
    # Chicken out. use ASCII on windows.
    day_format_separators =  {-1: '.', -3: "'", -4: "'", -6: "'" }
else:
    day_format_separators =  {-1: u'.', -3: u"’", -4: u"’", -6: u"’" }

year = 365.2421897

def omag(x):
    """Return the order of magnitude of a number."""
    try:
        return int(math.floor(math.log10(abs(x))))
    except ValueError:
        return 0

def days_formated(days=0, hours=0, minutes=0, seconds=0,
                  years=0, sigfig=3, maybe_show_years=True):
    """
    Return a value formated in a specific way.

    Returns a string that represents the number of days given as an
    argument formated in a specific way that should make parsing the
    decimal part of the age easier for humans.
    """
    days = days + hours/24.0 + minutes/1440.0 + seconds/86400.0 + \
        years*year
    # Calculate how many digits to show. Show full precision of days,
    # limited for shorter times.
    show_digits = max(sigfig - omag(days) - 1, 0)
    out_string = ''
    if 0 == show_digits:
        out_string = str(int(round(days,0)))
    else:
        decimal_days = Decimal(str(days))\
            .quantize(Decimal('0.' + '0'*(show_digits-1) + '1'))
        dec_sign, dec_digits, dec_exponent = decimal_days.as_tuple()
        ndig = len(dec_digits)
        if dec_sign:
            out_string = '-'
        for pad in range(0, dec_exponent + ndig - 1, -1):
            try:
                out_string += day_format_separators[pad]
            except KeyError:
                pass
            out_string += '0'
        for ex, dg in enumerate(dec_digits):
            # Add a decorator if it is the right position
            try:
                out_string += \
                    day_format_separators[-ex + dec_exponent + ndig - 1]
            except KeyError:
                pass
            out_string += str(dg)
    if days > year and maybe_show_years:
        out_string += " ({0:.1f} years)".format(days/year)
    return out_string

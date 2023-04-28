#!/usr/bin/python3
# -*- coding: utf-8 ; mode: python -*-
#
#  © 2017–2022 Roland Sieker <ospalh@gmail.com>
#
# License: GNU AGPL, version 3 or later;
#  http://www.gnu.org/licenses/agpl.html


import argparse
import unicodedata
import ftfy

__version__ = '0.2.0'

def uform(character):
    """Return the U+-form of the code point in question

    Return an "U+" and the hex value of the Unicode code point, four
    digits for BPM characters or six for others
    """
    oc = ord(character)
    if oc < 0x10000:
        return f'U+{oc:04x}'
    return f'U+{oc:06x}'
        
    
def name_em(characters):
    """Name unicode characters

    Print the names of each unicode character in characters, together
    with the character itself, and the hexedecimal code point.
    """
    for one_char in characters:
        try:
            uc_name = unicodedata.name(one_char)
        except ValueError as ve:
            uc_name = "({ve})".format(ve=ve)
        print(
            "» {c} «: {n} {u}".format(
                c=one_char, n=uc_name,
                u=uform(one_char)))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="""Print each character, its Unicode name and code \
        point of the argument.""")
    parser.add_argument("characters", type=str, help='''Characters to name''')
    args = parser.parse_args()
    print(f"{args.characters=}, {len(args.characters)=}, {type(args.characters)=}")
    chars = ftfy.ftfy(args.characters)
    print(f"{chars=}, {len(chars)=}, {type(chars)=}")    
    uc = args.characters.encode('UTF-16')
    print(f"{uc=}, {len(uc)=}, {type(uc)=}")    
    # name_em(args.characters)
    name_em(chars)

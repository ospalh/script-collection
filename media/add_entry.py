#!/usr/bin/env python3
# -*- coding: utf-8 ; mode: python -*-
#
#  © Copyright 2023 Roland Sieker <ospalh@gmail.com>
#
# License: GNU AGPL, version 3 or later;
#  http://www.gnu.org/licenses/agpl.html




import argparse
import os
import re
import yaml
import json

__version__ = '0.0.1'


def do_process(filename):
    dirname, basename = os.path.split(filename)
    temp = tempfile.NamedTemporaryFile(
        prefix=basename, suffix='~', dir=dirname, delete=False, mode='w')
    with open(filename, 'r') as inf:
        # Do processing here.
        for line in inf.readlines():
            # or here, if it's by line
            temp.write(line)
    temp.close()
    os.rename(temp.name, filename)

def add_to_files(file_list, new_file):
    pass
    

def json_from_list(plain_list):
    pass
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="""Add the entries from the Yaml-file »new« to the files for the namespaces listed in the Json file »namespaces«.""")
    parser.add_argument("infile", type=str, help='''The file to process''')
    args = parser.parse_args()
    do_process(args.infile)

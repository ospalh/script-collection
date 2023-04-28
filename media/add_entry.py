#!/usr/bin/env python3
# -*- coding: utf-8 ; mode: python -*-
#
#  © Copyright 2023 Roland Sieker <ospalh@gmail.com>
#
# License: GNU AGPL, version 3 or later;
#  http://www.gnu.org/licenses/agpl.html




import argparse
import json
import os
import re
import sys
import yaml

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
    

def make_list(raw_list, is_json):
    if raw_list == '-':
        stdin_list = sys.stdin.readlines()
        if len(stdin_list) > 1:
            return [item.strip() for item in stdin_list]
        raw_list = stdin_list[0]  # Blow up if empty
    if is_json:
        pass
    else:
        the_list = raw_list.split()
    return the_list
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="""Add the entries from the Yaml-file »new« to the files for the namespaces listed in the Json file »namespaces«.""")
    parser.add_argument("--namespacelist", "-l", type=str, help='''The list of namespaces''')
    parser.add_argument("--yamlfile", "-y", type=str, help='''The yaml entry to add to the namespaces''')
    parser.add_argument("--jsonlist", "-j", action='store_true', help='''Whether the entries ar a Json list, not implemented yet''')
    args = parser.parse_args()
    nasp_list = make_list(args.namespacelist, args.jsonlist)
    print(nasp_list)
    #do_process(args.infile)

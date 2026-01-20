import os
from os import path 
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('src',
                    nargs='?',
                    default='C:\\aiosu',
                    help='C:\\aiosu')

parser.add_argument('dest',
                    nargs='?',
                    default='D:\\國展報告',
                    help='D:\\國展報告')

args = parser.parse_args()

if not path.isdir(args.src):
    print(f'{args.src} is not a valid directory')
    sys.exit(2)

if not path.isdir(args.dest):
    print(f'{args.dest} is not a valid directory')
    sys.exit(2)
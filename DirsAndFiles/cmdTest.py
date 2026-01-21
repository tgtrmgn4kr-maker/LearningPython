import argparse
import sys
from os import path


parser = argparse.ArgumentParser()
parser.add_argument('src',
                    nargs='?',
                    default='C:\\aiosu',
                    help='sourse path')
parser.add_argument('dest',
                    nargs='?',
                    default='D:\\國展報告',
                    help='D:\\國展報告')
args = parser.parse_args()

if not path.isdir(args.src):
    print(f'{args.src} is not a valid directory')
    sys.exit(1)


print(args.src)
print(args.dest)
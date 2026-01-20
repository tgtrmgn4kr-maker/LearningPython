import argparse
import os 
from os import path
import shutil
import sys

parser = argparse.ArgumentParser()
parser.add_argument('src',                       #取得來源資料夾路徑
                    nargs='?',
                    default='D:\\learn\\ttest',
                    help='Sourse directory'
                    )

parser.add_argument('dest',                      #取得目標資料夾路徑
                    nargs='?',
                    default='D:\\learn\\ttest_backup',
                    help='Destination directory'
                    )

args = parser.parse_args()                       #解析命令列參數

if not path.isdir(args.src):
    print(f'{args.src} is not a directory')      #檢查來源路徑是否為目錄
    sys.exit(2)

if not path.isdir(args.dest):
    print(f'{args.dest} is not a directory')     #檢查目標路徑是否為目錄 
    sys.exit(2)

#   目前路徑  子目錄列表   檔案列表               來源路徑
for dir_path, dir_names, file_names in os.walk(args.src):
    rel_path = path.relpath(dir_path, args.src)     #將絕對路徑轉換成相對路徑

    if rel_path == '.':     #兩路徑相同時
        dest_path = args.dest
    else:                   #兩路徑不同時
        dest_path = path.join(args.dest, rel_path)

    os.makedirs(dest_path, exist_ok=True) 
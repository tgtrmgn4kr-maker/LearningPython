import argparse
import os 
from os import path
import shutil
import sys

parser = argparse.ArgumentParser()               #建立參數解析器
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

#   目前路徑  子目錄列表  檔案列表             來源路徑
for dir_path, dir_names, file_names in os.walk(args.src):
    rel_path = path.relpath(dir_path, args.src)     #將絕對路徑轉換成相對路徑
                            #相對路徑 絕對路徑

    if rel_path == '.':     #兩路徑相同時
        dest_path = args.dest
    else:                   #兩路徑不同時
        dest_path = path.join(args.dest, rel_path)

    os.makedirs(dest_path, exist_ok=True) #建立目標資料夾，若已存在則忽略

    for f in file_names:
        src_path = path.join(dir_path, f) #來源檔案完整路徑(路徑+檔名)
        save_path = path.join(dest_path, f) #目標檔案完整路徑(路徑+檔名)

        if not path.isfile(save_path):
            shutil.copy2(src_path, save_path) #複製檔案
            print(f'Copied: {src_path} to {save_path}')
        else:
            print(f'Skipped: {save_path} already exists')
            src_time = int(path.getmtime(src_path))
            dest_time = int(path.getmtime(save_path))

            if src_time > dest_time:   #若來源檔較新          
                shutil.copy2(src_path, save_path) #複製檔案
                print(f'Updated: {src_path} to {save_path}')
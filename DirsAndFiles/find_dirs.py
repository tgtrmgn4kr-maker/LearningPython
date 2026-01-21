import os

path='D:\\learn'

for dir_path, dir_names, file_names in os.walk(path):
    print('Current Path:', dir_path)

    if len(dir_names) > 0:
        print('Subdirectories:', dir_names)
    else:
        print('No subdirectories found.')

    if len(file_names) > 0:
        print('Files:', file_names)
    else:
        print('No files found.')

    for f in file_names:
        print('Full Path:', os.path.join(dir_path, f))
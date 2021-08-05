# Exercise jpg to png converter
import sys
import os
from PIL import Image

'''
just in case the user doesn't input with / at the end of
the directory name
'''


def checkDirFormat(directory):
    if directory.endswith('/'):
        return directory
    else:
        return directory + '/'


# grab first and second argument
try:
    source_dir = checkDirFormat(sys.argv[1])
    target_dir = checkDirFormat(sys.argv[2])
except IndexError:
    print('No arguments given, please provide source/target directories')
    sys.exit()

# check is new/exists, if not create
if not os.path.isdir(source_dir):
    print(f'Source directory {source_dir} does not exist')
    sys.exit()
if not os.path.isdir(target_dir):
    os.mkdir(target_dir)
    print(f'Directory {target_dir} created.')

# loop through pokedex
# convert images to png
# save to the new folder
for img in os.listdir(source_dir):
    pokemon = Image.open(f'{source_dir}{img}')
    pokemon.save(target_dir + os.path.splitext(img)[0] + '.png', 'png')

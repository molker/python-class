# Exercise jpg to png converter
import sys
import os
from PIL import Image

# grab first and second argument
try:
    source_dir = sys.argv[1]
    target_dir = sys.argv[2]
except IndexError:
    print('No directories given, please provide arguments')
    sys.exit()

# check is new/exists, if not create
if not os.path.isdir(source_dir):
    print(f'Source directory {source_dir} does not exist')
    sys.exit()
if not os.path.isdir(target_dir):
    os.mkdir(target_dir)
    print(f'Directory {target_dir} created.')

# loop through pokedex
files = os.listdir(source_dir)

# convert images to png
# save to the new folder
for img in files:
    pokemon = Image.open(f'{source_dir}/{img}')
    pokemon.save(target_dir + '/' + img.split('.')[0] + '.png', 'png')

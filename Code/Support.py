from csv import reader
import os
from os import walk
import pygame

# Support for importing CSV files into Python and more stuff here

# This is for file (images specifically) importing (This line changes the directory to where the project is saved)
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def import_csv_layout(path): 
    
    terrain_map = []

    with open(path) as level_map:
        layout = reader(level_map, delimiter = ",")

        for row in layout:
            terrain_map.append(list(row))
        
        return terrain_map


def import_folder(path):
    
    surface_list = []
    
    for _, __, img_files in walk(path):
        for image in img_files:
            full_path = path + "/" + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)
    return surface_list
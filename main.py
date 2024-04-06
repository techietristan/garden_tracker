import argparse

from utils.datetime import getDateTime
from utils.json import readJson, writeJson
from utils.inventory_seeds import promptForSeedInfo


parser = argparse.ArgumentParser(
    prog = 'Garden Tracker',
    description = 'Simple app for tracking plants in a home garden.',
)

parser.add_argument('-i', '--inventory_seeds', help = 'Inventory new seeds, associating each package with a serial number.', action = 'store_true')
parser.add_argument('-s', '--sprout_seeds', help = 'Sprout seeds, associating a seed package\'s serial number with a sprouting pod\'s serial number', action = 'store_true')
parser.add_argument('-p', '--pot_sprouts', help = 'Pot sprouts, associating a pod\'s serial number with a pot\'s serial number', action = 'store_true')
parser.add_argument('-l', '--plant_seedlings', help = 'Plant seedlings, associating a pot\'s serial number with a plot location.', action = 'store_true')
args = parser.parse_args()

promptForSeedInfo()
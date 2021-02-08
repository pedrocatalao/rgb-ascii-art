#!/usr/bin/python

# This script will colorize a ascii banner and print it slowly along with the last login info

import re
import sys
import subprocess
from time import sleep

# Read original file
banner = """             _                                     _  _
 _ _ _  ___ | | ___  ___ ._ _ _  ___   _ _  ___  _| |<_>__
| | | |/ ._>| |/ | '/ . \| ' ' |/ ._> | '_><_> |/ . || |\ \/
|__/_/ \___.|_|\_|_.\___/|_|_|_|\___. |_|  <___|\___||_|/\_\\
"""
content = banner.splitlines()

# Add last login line
subprocess = subprocess.Popen("last -1 pedro | awk '{print \"Last login: \" $3 \" \" $4 \" \" $5 \" \" $6 \" on \" $2}'", shell=True, stdout=subprocess.PIPE)
subprocess_return = subprocess.stdout.read()
content.append(subprocess_return)

# Spin speed
spinSpeed = 1

RED=(255, 0, 0)
ORANGE=(255, 102, 0)
YELLOW=(255, 255, 0)
GREEN=(102, 255, 51)
CYAN=(102, 255, 255)
BLUE=(51, 153, 255)
VIOLET=(127, 0, 255)

COLORS=[RED, ORANGE, YELLOW, GREEN, CYAN, BLUE, VIOLET]

number_of_colors = len(COLORS)

# This is the length of the biggest line of the banner
maxLength = len(max(content, key=len))

# Number of transitions is the number of colors - 1
each_color_length = maxLength / (number_of_colors - 1)

# This makes sure we have enough colors for the lenght of the banner
while each_color_length * (number_of_colors - 1) < maxLength:
    each_color_length += 1

# Appends first color to allow nice color spinning transition for last color
COLORS.append(COLORS[0])

# Generate color transitions
all_colors_ansi = []
for c in range(number_of_colors):
    for x in range(each_color_length):
        p = x / float(each_color_length)
        r = int((1.0-p) * COLORS[c][0] + p * COLORS[c+1][0] + 0.5)
        g = int((1.0-p) * COLORS[c][1] + p * COLORS[c+1][1] + 0.5)
        b = int((1.0-p) * COLORS[c][2] + p * COLORS[c+1][2] + 0.5)
        all_colors_ansi.append((r, g, b))

# Generate and print color coded characters
for l in content:
    for c in range(len(l)):
        r = all_colors_ansi[c][0]
        g = all_colors_ansi[c][1]
        b = all_colors_ansi[c][2]
        sys.stdout.write("\033[38;2;" + str(r) + ";" + str(g) + ";" + str(b) + "m" + l[c])
        sys.stdout.flush()
        sleep(0.0015)

    sys.stdout.write("\n")

    # Spins colors before going to next line
    for i in range(spinSpeed):
        all_colors_ansi.append(all_colors_ansi.pop(0))

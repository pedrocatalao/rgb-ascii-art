#!/usr/bin/python

# This script will colorize a text file with smooth color transitions
# first generate your ascii here: http://patorjk.com/software/taag/

import re
import sys

# Check arguments
if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " <inputfile> <outputfile>")
    exit(1)

# Read original file
original_file = open(sys.argv[1], "r")
content = original_file.read().splitlines()

# Spin speed (can be 0) TODO: get from args
spinSpeed = 2

maxLength = len(max(content, key=len))

RED=(255, 0, 0)
ORANGE=(255, 102, 0)
YELLOW=(255, 255, 0)
GREEN=(102, 255, 51)
CYAN=(102, 255, 255)
BLUE=(51, 153, 255)
PINK=(255, 51, 204)

COLORS=[RED, ORANGE, YELLOW, GREEN, CYAN, BLUE, PINK]

number_of_colors = len(COLORS)

each_color_length = maxLength / (number_of_colors - 1)

while each_color_length * (number_of_colors - 1) < maxLength:
    each_color_length += 1

COLORS.append(COLORS[0])

all_colors_ansi = []
for c in range(number_of_colors):
    for x in range(each_color_length):
        p = x / float(each_color_length)
        r = int((1.0-p) * COLORS[c][0] + p * COLORS[c+1][0] + 0.5)
        g = int((1.0-p) * COLORS[c][1] + p * COLORS[c+1][1] + 0.5)
        b = int((1.0-p) * COLORS[c][2] + p * COLORS[c+1][2] + 0.5)
        all_colors_ansi.append((r, g, b))

result=[]
for l in content:
    line=""
    for c in range(len(l)):
        r = all_colors_ansi[c][0]
        g = all_colors_ansi[c][1]
        b = all_colors_ansi[c][2]
        line = line + "\033[38;2;" + str(r) + ";" + str(g) + ";" + str(b) + "m" + l[c]

    result.append(line)
    for i in range(spinSpeed):
        all_colors_ansi.append(all_colors_ansi.pop(0))

output = "\n" + "\n".join(result) + "\n\n"
output_file = open(sys.argv[2],"w+")
output_file.write(output)
print(output),


# TODO: Spin colors - done
# TODO: ASK for the colors (when user enters empty line, that's the last color) - accept hex codes #ff00d3
# TODO: Then ask for the text
# TODO: Then ask for the font
# TODO: ASK for spin speed (can be 0 for no spin)
# TODO: ASk file to output instead of arg
# TODO: Actually maybe better to allow doing everything with arg for better automation/integration with other stuff ;)
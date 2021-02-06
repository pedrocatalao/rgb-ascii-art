#!/usr/bin/python

# This script converts a text file color tags with hex values to ansi codes
# So first generate your ascii here: http://patorjk.com/software/taag/
# Then colorize it here: http://patorjk.com/text-color-fader/

import re
import sys

# Check arguments
if len(sys.argv) < 2:
    print "Usage: " + sys.argv[0] + " <inputfile> <outputfile>"
    exit(1)

# Read original file
original_file = open(sys.argv[1], "r")
content = original_file.read()

# Regex to find colors
color_finder = re.compile(r'#[0-9A-Fa-f]{3}(?:[0-9A-Fa-f]{3})?(?!$)', re.M)

# Stores all hex codes in array
all_colors = color_finder.findall(content)

# Strips # character from the colors
all_colors_hex = [e.lstrip('#') for e in all_colors]

# Convert to RGB values
all_colors_rgb = [tuple(int(h[i:i+2], 16) for i in (0, 2, 4)) for h in all_colors_hex]

# Store ANSI codes in new array
all_colors_ansi = []
for rgb in all_colors_rgb:
    all_colors_ansi.append("\033[38;2;" + str(rgb[0]) + ";" + str(rgb[1]) + ";" + str(rgb[2]) + "m")

# Replace all original hex codes with ANSI codes
for i in range(len(all_colors)):
    content = content.replace(all_colors[i], all_colors_ansi[i])

# Writes new file
output_file = open(sys.argv[2],"w+")
output_file.write(content)

# Shows result
print(content)

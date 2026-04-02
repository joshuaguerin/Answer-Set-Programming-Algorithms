

from sys import argv, stderr

if len(argv) < 2:
   print("Error: A valid PPM file name is required.", file=stderr)
   exit()
   
try:
    image_in = open(argv[1], 'r')
except FileNotFoundError:
    print("Error:", argv[1], "not found.", file=stderr)
    exit()

image = []

# Read, pre-process image
for line in image_in:
    line = line.strip()
    line = line.split()
    
    image.append(line)

image_in.close()
    
# Flatten the image
image = [entry for line in image for entry in line]

# Grab the header information
(magic_num, cols, rows, depth) = image[:4]

# Color information only
image = image[4:]

## Start Reporting Values:

# Header
print("type(", magic_num, ").", sep="")
print("cols(", cols, ").", " rows(", rows, ").", sep="")
print("depth(", depth, ").", sep="")

for i in range(0, len(image), 3):
    print("pixel(", "row, ", "col, ", image[i], ' ', image[i+1], ' ', image[i+2], ").", sep="")


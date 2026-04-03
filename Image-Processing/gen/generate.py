

from sys import argv, stderr

if len(argv) < 2:
   print("Error: A valid PPM file name is required.", file=stderr)
   exit()

file_name = argv[1]

try:
    image_in = open(file_name, 'r')
except FileNotFoundError:
    print("Error:", file_name, "not found.", file=stderr)
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

cols = int(cols)
rows = int(rows)

# Color information only
image = image[4:]

## Start Reporting Values:

# Header
print("%% Image: ", file_name.strip())
print()
print("type(", magic_num, ").", sep="")
print("cols(", cols, ").", " rows(", rows, ").", sep="")
print("depth(", depth, ").", sep="")
print()

# Pixel Data

for i in range(rows):
    for j in range(cols):
        print("pixel(", i, ", ", j, ", ",
              image[i], ', ', image[i+1], ', ', image[i+2], ").", sep="")

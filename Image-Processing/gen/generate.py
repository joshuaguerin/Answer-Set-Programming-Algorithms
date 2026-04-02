

from sys import argv, stderr

if len(argv) < 2:
   print("Error: A valid PPM file name is required.", file=stderr)
   exit()
   
try:
    image_in = open(argv[1], 'r')
except FileNotFoundError:
    print("Error:", argv[1], "not found.", file=stderr)
    exit()
    
for line in image_in:
    print(line)

image_in.close()

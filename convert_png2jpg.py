import os
from glob import glob
from PIL import Image

#After importing all dependencies, getting all png files inside a directory into a list
#If source_png/ is empty first run convert_jpg2png!!

files = []
files.extend(glob('target_png/*.png'))

#No loop through these files and simply - as python usual - save as new format file

counter = 0
for file in files:    
    #Remove the file extension and the path
    base_filename_without_extension = os.path.basename(
        os.path.splitext(file)[0]
    )
    counter = counter + 1
    image = Image.open(file)
    image.save('target_jpg/' + base_filename_without_extension + '.jpg')

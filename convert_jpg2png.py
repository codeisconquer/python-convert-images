import os
from glob import glob
from PIL import Image

#After importing all dependencies, getting all jpg files inside a directory into a list

files = []
files.extend(glob('source_jpg/*.jpeg'))
files.extend(glob('source_jpg/*.jpg'))

#No loop through these files and simply - as python usual - save as new format file

counter = 0
for file in files:    
    #Remove the file extension and the path
    base_filename_without_extension = os.path.basename(
        os.path.splitext(file)[0]
    )
    counter = counter + 1
    image = Image.open(file)
    image.save('target_png/' + base_filename_without_extension + '.png')

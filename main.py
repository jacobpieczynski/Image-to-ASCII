## Image to ASCII Art
import numpy as np
from PIL import Image
from sys import argv

ascii = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
RESIZE_FACTOR = 2

def main():
    # Gets the filename, either with a default or user-inputted value
    filename = 'images/test.jpg'
    if len(argv) > 1: filename = argv[1]
    print(f'File: {filename}')

    # Load the image
    try:
        image = Image.open(filename)
        print('Successfully loaded image')
        width, height = image.size[0], image.size[1]
        image = image.resize((width // RESIZE_FACTOR, height // RESIZE_FACTOR))
        print(f'Image size: {image.size[0]} x {image.size[1]} pixels')
    except:
        print('Failed to load image')
        return

    # Convert the image to an array
    print('Converting image to array...')
    img_array = np.array(image)
    
    ascii_image = []

    # Convert the image to a brightness matrix
    print('Converting image to brightness matrix...')
    for line in img_array:
        ascii_line = []
        for pixel in line:
            r, g, b = int(pixel[0]), int(pixel[1]), int(pixel[2])

            # 3 Methods of determining brightness: Average, Luminosity, and Lightness
            brightness = (r + g + b) / 3 # Average
            #brightness = 0.21*r + 0.72*g + 0.07*b # Luminosity
            #brightness = min(round(max(r, g, b) + min(r, g, b) / 2), 254) # Lightness

            char = ascii[int(brightness / 255 * len(ascii))]

            # 3 characters per pixel (to adjust for most characters being 3x as tall as they are wide)
            ascii_line.append(char)
            ascii_line.append(char)
            ascii_line.append(char)
        ascii_image.append(ascii_line)

    # Print the ASCII image
    print('Printing ASCII image...')
    with open('ascii_image_average.txt', 'w') as f:
        for line in ascii_image:
            for pixel in line:
                f.write(pixel)
            f.write('\n')

if __name__ == '__main__':
    main()
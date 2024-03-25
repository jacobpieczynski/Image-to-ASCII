## Image to ASCII Art
from PIL import Image
from sys import argv

def main():
    # Gets the filename, either with a default or user-inputted value
    filename = 'images/test.jpg'
    if len(argv) > 1: filename = argv[1]
    print(f'File: {filename}')

    # Read the image
    try:
        image = Image.open(filename)
        print('Successfully loaded image')
        print(f'Image size: {image.size[0]} x {image.size[1]} pixels')
    except:
        print('Failed to load image')
        return


if __name__ == '__main__':
    main()
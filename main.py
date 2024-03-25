## Image to ASCII Art
from sys import argv

def main():
    height, width = 0, 0
    filename = 'test.jpg'
    if len(argv) > 1:
        filename = argv[1]
    print(f'Filename: {filename}')

    # Read the image
    if load_image(filename):
        print('Successfully loaded image')


def load_image(filename):
    print('Loading image...')


if __name__ == '__main__':
    main()
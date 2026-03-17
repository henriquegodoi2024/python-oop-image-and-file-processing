

from hmcpng import load_pixels
from hmcpng import save_pixels
from hmcpng import compare_images

def create_green_image(height, width):
    """ creates and returns a 2-D list of pixels with height rows and
        width columns in which all of the pixels are colored green.
        inputs: height and width are non-negative integers
    """
    pixels = []

    for r in range(height):
        row = [[0, 255, 0]] * width
        pixels += [row]

    return pixels

def brightness(pixel):
    """ takes a pixel (an [R, G, B] list) and returns a value
        between 0 and 255 that represents the brightness of that pixel.
    """
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    return (21*red + 72*green + 7*blue) // 100

## put your functions below

# function 1

def bw(pixels,threshold):
    ''' creates and returns 2-D list that is the
    black-white version of an image'''
    white = [255,255,255]
    black = [0,0,0]
    height = len(pixels)
    width = len(pixels[0])
    new_pixels = create_green_image(height, width)
    
    for r in range(height):
        for c in range(width):
            if brightness(pixels[r][c]) > threshold:
                new_pixels[r][c] = white
            else:
                new_pixels[r][c] = black
                
    return new_pixels

# function 2

def fold_diag(pixels):
    ''' creates and returns a new 2-D list that folds the original image along its diagonal'''
    white = [255,255,255]
    height = len(pixels)
    width = len(pixels[0])
    new_pixels = create_green_image(height, width)
    
    for r in range(height):
        for c in range(width):
            if r == c:
                new_pixels[r][c] = pixels[r][c]
                
            elif r > c:
                new_pixels[r][c] = white
            
            else:
                new_pixels[r][c] = pixels[r][c]
                
    return new_pixels


# function 3

def flip_horiz(pixels):
    ''' creates and returns a 2-D list that flips the image horizontally'''
    height = len(pixels)
    width = len(pixels[0])
    new_pixels = create_green_image(height, width)
    
    for r in range(height):
        for c in range(width):
            new_pixels[r][width-1-c] = pixels[r][c]
            
    return new_pixels
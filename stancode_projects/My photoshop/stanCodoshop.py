"""
SC101 - Assignment3
Adapted from Nick Parlante's Ghost assignment by
Jerry Liao.

-----------------------------------------------

"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the square of the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): squared distance between red, green, and blue pixel values

    """
    dist = ((red-pixel.red)**2+(green-pixel.green)**2+(blue-pixel.blue)**2)**0.5
    return dist


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    rgb = [] #create a list for the average
    red = 0 #variable, the total red value
    green = 0 #variable, the total green value
    blue = 0 #variable, the total green value
    for i in range(len(pixels)): #for each pixel
        red += pixels[i].red
        green += pixels[i].green
        blue += pixels[i].blue
    rgb += [int(red/len(pixels)),int(green/len(pixels)), int(blue/len(pixels))]
    return rgb


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    red = get_average(pixels)[0] #the average red value of pixels
    green = get_average(pixels)[1] #the average green value of pixels
    blue = get_average(pixels)[2] #the average blue value of pixels
    best = pixels[0] #the best pixels in the list
    dist = get_pixel_dist(pixels[0], red, green, blue)
    for i in range(len(pixels)):
        if get_pixel_dist(pixels[i], red, green, blue) < dist:
            best = pixels[i]
            dist = get_pixel_dist(pixels[i], red , green, blue)
    return best


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    ######## YOUR CODE STARTS HERE #########
    pixels = [] #the list for plxels in the same position
    for x in range(result.width):
        for y in range(result.height):
            for img in images:
                pixel = img.get_pixel(x, y) #the pixel in every image
                pixels.append(pixel) #add the pixel in the pixels list
            best = get_best_pixel(pixels) #get the best pixel in the pixels list
            pixels = [] # clear the pixel list
            pixel2 = result.get_pixel(x, y)
            pixel2.red = best.red
            pixel2.green = best.green
            pixel2.blue = best.blue
    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()

# Rename this file to be "filters.py"
# Add commands to import modules here.
from PIL import Image
import PIL.ImageOps
# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(filename):
    return Image.open(filename)


# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img(image):
    image.show()


# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
def save_img(image, saveName):
    image.save(saveName)

# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.
def obamicon(image):
    pixelMap = image.load()
    for row in range(image.size[0]):
      for col in range(image.size[1]):
        intensity = 0
        pixel = pixelMap[row, col]
        intensity = pixel[0] + pixel[1] + pixel[2]
        if (intensity < 182):
            pixelMap[row, col] = (0, 51, 76)
        elif (182 <= intensity < 364):
            pixelMap[row, col] = (217, 26, 33)
        elif (364 <= intensity < 546):
            pixelMap[row, col] = (112, 150, 158)
        else:
            pixelMap[row, col] = (252, 227, 166)
    return image


def invert_image(image):
    inverted_img = PIL.ImageOps.invert(image)
    return inverted_img

def warm(image):
    pixelMap = image.load()
    for row in range(image.size[0]):
      for col in range(image.size[1]):
        intensity = 0
        pixel = pixelMap[row, col]
        intensity = pixel[0] + pixel[1] + pixel[2]
        if (intensity < 76):
            pixelMap[row, col] = (211, 201, 206)
        elif (76 <= intensity < 152):
            pixelMap[row, col] = (183, 166, 173)
        elif (152 <= intensity < 228):
            pixelMap[row, col] = (132, 109, 116)
        elif (228 <= intensity < 304):
            pixelMap[row, col] = (231, 227, 181)
        elif (304 <= intensity < 380):
            pixelMap[row, col] = (223, 210, 124)
        elif (380 <= intensity < 456):
            pixelMap[row, col] = (180, 168, 81)
        elif (456 <= intensity < 532):
            pixelMap[row, col] = (199, 195, 151)
        elif (532 <= intensity < 608):
            pixelMap[row, col] = (157, 151, 84)
        else:
            pixelMap[row, col] = (110, 118, 73)
    return image

def grayscale(image):
    #get size with image.size
    width, height = image.size
    #new image and pixel map
    pixelMap = image.load()
    #new = create_image(width,height)

    for row in range(width):
        for col in range(height):
            pixel = pixelMap[row,col]

            #get RGB values
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]

            #go to grayscale
            gray = (red * 0.299) + (green * 0.587) + (blue * 0.114)

            #set pixels in new Image
            pixelMap[row, col] = (int(gray), int(gray), int(gray))
    return image

def invert2(image):
    pixelMap = image.load()
    width, height = image.size
    for row in range(width):
      for col in range(height):
          pixel = pixelMap[row, col]

          red = pixel[0]
          green = pixel[1]
          blue = pixel[2]

          flipred = 255 - red
          flipgreen = 255 - green
          flipblue = 255 - blue

          pixelMap[row, col] = (int(flipred), int(flipgreen), int(flipblue))
    return image

def yellow_tint(image):
    pixelMap = image.load()
    width, height = image.size
    for row in range(width):
      for col in range(height):
          pixel = pixelMap[row, col]

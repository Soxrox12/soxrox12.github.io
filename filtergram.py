#get functions from Pillow and filters.py
from PIL import Image
import filters

#main function
def main():
    #load the image to apply filters to
    #change "hannah-eli.jpg" to own image file name. image file must be in same directory as python files
    newImg = filters.load_img("group-pic.jpg")
    ''' #show the image to the user
        #filters.show_img(newImg)
    #save the new image
        #filters.save_img(newImg, "group-pic2.jpg")
    #apply obamicon
    obamiconImg = filters.obamicon(newImg)
        #filters.show_img(obamiconImg)
    filters.save_img(obamiconImg, "group-obamicon.jpg")
    '''
    #apply and save inverted pic
    invertImg = filters.invert2(newImg)
    filters.show_img(invertImg)
    filters.save_img(invertImg, "group-invert.jpg")
    #apply and save warm filter
    '''warmImg = filters.warm(newImg)
        #filters.show_img(warmImg)
    filters.save_img(warmImg, "group-warm.jpg")
    #apply and save grayscale
    grayImg = filters.grayscale(newImg)
    #filters.show_img(grayImg)
    #filters.save_img(grayImg, "HE-gray.jpg")
    '''


if __name__ == ("__main__"):
    main()

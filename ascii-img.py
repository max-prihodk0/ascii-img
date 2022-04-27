import os
from PIL import Image

chars = " .:-=+*#%@"

def get_pixels(img):
    pixels = list(img.getdata())
    width, height = img.size
    pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]

    return pixels

def resize(image):
    # Get dimentions of terminal and image
    height, width = os.get_terminal_size()
    iwidth, iheight = image.size

    # Determine the height ratio of the image
    wpercent = (width / float(iwidth))
    hpercent = wpercent + 0.3
    hsize = int((float(iheight) * float(wpercent)))
    wsize = int((float(iwidth) * float(hpercent)))

    if hsize == iheight and wsize == iwidth:
        return get_pixels(image)
    
    print(f"(w) {wsize} {hsize}")
    print(f"(i) {iwidth} {iheight}")
    # Resize and save the image
    new_image = image.resize(( int(wsize * 0.77), int(hsize * 0.77) ), Image.ANTIALIAS)

    # Get an array of pixels
    pixels = get_pixels(new_image)
    print(f"[DEBUG] Resized from {len(get_pixels(image))}px to {len(pixels)}px")

    return pixels

def display(pixels):
    for row in pixels:
        for pixel in row:
            avg = (pixel[0] + pixel[1] + pixel[2]) / 3
            pos = int(avg / (255 / len(chars)))
            
            if pos >= len(chars):
                pos = len(chars) - 1

            print(chars[pos], end="")
        print()



# Get and resize image
image = Image.open("images/dog.png")
image = image.convert("RGBA")
pixels = resize(image)

display(pixels)
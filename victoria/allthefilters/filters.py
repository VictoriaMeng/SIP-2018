from PIL import Image

def load_img(filename):
    return Image.open(filename)

def show_img(img):
    img.show()

def save_img(img, filename):
    img.save(filename)
    show_img(img)

def obamicon(img):
    pixels = img.getdata()

    new_pixels = []

    dark_blue = (0, 51, 76)
    red = (217, 26, 33)
    light_blue = (112, 150, 158)
    yellow = (252, 227, 166)

    for p in pixels:
        intensity = p[0] + p[1] + p[2]

        if intensity < 182:
            new_pixels.append(dark_blue)

        elif intensity in range(182, 365):
            new_pixels.append(red)

        elif intensity in range(364, 547):
            new_pixels.append(light_blue)

        else:
            new_pixels.append(yellow)

    new_img = Image.new("RGB", img.size)
    new_img.putdata(new_pixels)
    return new_img

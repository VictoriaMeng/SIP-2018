from PIL import Image
import filters

def main():
    filename = input("Enter file name: ")
    img = filters.load_img(filename)
    new_img = filters.obamicon(img)
    filters.save_img(new_img, "new_img.jpg")

main()

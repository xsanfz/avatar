from PIL import Image

image = Image.open("monro1.jpg")
red, green, blue= image.split()
red.save("красный1.jpg")
green.save("зеленый1.jpg")
blue.save("синий1.jpg")

crp = 100

red1 = Image.open("красный1.jpg")
coordinates1 = (crp, 0, image.width, image.height)
red1_cropped = image.crop(coordinates1)
red1.save("red1_crop.jpg", format="JPEG")
red2 = Image.open("красный1.jpg")
coordinates2 = (0.5*crp, 0, 0.5*crp, image.height)
red2_cropped = image.crop(coordinates2)
red2.save("red2_crop.jpg",format="JPEG")
image_red_1 = Image.open("red1_crop.jpg")
image_red_2 = Image.open("red2_crop.jpg")
image_red_crop = Image.blend(image_red_1, image_red_2, 0.5)
image_red_crop.save("image_red_crop.jpg")



# image_green = Image.open("зеленый1.jpg")
# coordinates = (x / 2, 0, 696 - x / 2 , 522)
# cropped_green = image_green.crop(coordinates)
#
# image_green_red = Image.blend(cropped_red, cropped_green, 0.5)
# image_green_red.save("красный_зеленый.jpg")
#
# image_blue = Image.open("синий.jpg")
# coordinates = (0, 0, 696-2*crop, 522)
# cropped_blue = image_blue.crop(coordinates)
#
# image_green_red = Image.open("красный_зеленый.jpg")
# coordinates = (crop/2, 0, 656 - crop/2, 522)
# cropped_green_red = image_green_red.crop(coordinates)
# print(cropped_green_red.size)
# image_green_red_blue = Image.blend(cropped_blue, cropped_green_red, 0.5)
# image_green_red_blue.save("красный_зеленый_синий.jpg")

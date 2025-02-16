from PIL import Image

image = Image.open("monro.jpg")
(red, green, blue) = image.split()

crop_x = 50
red1 = red.crop((crop_x, 0, image.width, image.height))
red2 = red.crop((crop_x/2, 0, image.width - crop_x/2, image.height))
red.smash = Image.blend(red1, red2, 0.5)


blue1 = blue.crop((0 ,0 , image.width - crop_x, image.height))
blue2 = blue.crop((crop_x/2, 0, image.width - crop_x/2, image.height))
blue.smash = Image.blend(blue1, blue2, 0.5)

green1 = green.crop((crop_x/2, 0, image.width - crop_x/2, 522))

new_image = Image.merge("RGB", (red.smash, green1, blue.smash))
new_image.thumbnail((80, 80))

new_image.save("avatar.jpg")


import os
from PIL import Image
from itertools import product

if __name__ == '__main__':
	converted_images = []

	for file in os.listdir("images_to_convert"):
		file_format = file.split('.')[-1]

		with open("formats.txt", 'r') as f:
			formats = [FORMAT.strip() for FORMAT in f.read().split(',')]

		if (file_format in formats):
			with Image.open("images_to_convert/"+file) as image:
				image_rgb = image.convert("RGB")

				result = tuple(product(range(image.size[0]), range(image.size[1])))

				for x, y in result:
					R, G, B = image_rgb.getpixel((x, y))
					inverted_pixel_color = (255 - R, 255 - G, 255 - B)

					image.putpixel((x, y), inverted_pixel_color)

				image.save(image.filename)
				
				converted_images.append(image)

			print(f"inverted '{file}'")

	while True:
		answer = input("Open files? [y/n]")
		
		if answer.lower() == "y": break
		if answer.lower() == "n": exit()

	[image.show() for image in converted_images]
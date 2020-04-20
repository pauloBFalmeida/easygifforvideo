#! python3
from PIL import Image, ImageDraw, ImageColor, ImagePalette, ImageEnhance, ImageFilter, ImageStat, ImageOps
import sys, time
import random
import imageio
import cv2
import argparse
import os


# palavra = input('Enter picture name\n')
palavra = 'print.jpg'
im = Image.open(palavra)
blur_radio	= 3
cores = 20
# qtde = 5**2
qtde = 4
larg, alt = im.size
print(im.size)
im = im.filter(ImageFilter.BoxBlur(radius=blur_radio))
# im = im.quantize(colors=cores,method=1)
# print(im.getbands())
# im.show()
left  = 0
upper = 0
right = larg % qtde
lower = alt  % qtde

quadradros = []

for i in range(qtde):
	lower = upper + (alt  // qtde)
	left  = 0
	# right = larg % qtde
	# print(upper)
	for j in range(qtde):
		right = left + (larg // qtde)
		box = (left,upper,right,lower)
		# im.crop(box).show()
		quadradros.append(((left,upper),im.crop(box)))
		left = right
	upper = lower

random.shuffle(quadradros)

# for i in quadradros:
	# print(str(i[0])+" "+str(i[1]))
	# i[2].show()

im_n = Image.new("RGB",im.size,(0,0,0))
seq = [im_n.copy()]
for q in quadradros:
	im_n.paste(q[1], q[0])
	seq.append(im_n.copy())

# for s in seq:
# 	s.show();

# images = []
# for filename in filenames:
#     images.append(imageio.imread(filename))
# imageio.mimsave('/path/to/movie.gif', images)



# imageio.mimsave('giferson.gif', seq)
# seq[0].save('giferson.gif', format='GIF', append_images=seq[1:], save_all=True, duration=1000, loop=0)




image_folder = ''
video_name = 'video.avi'

images = seq
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, 1, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()

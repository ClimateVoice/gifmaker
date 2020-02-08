'''
python gif.py 2 1.png 2.png 3.png
'''
#gif.py 
import sys
import datetime
import imageio
import os 

VALID_EXTENSIONS = ('png', 'jpg')


def create_gif(filenames, duration):
    images = []
    for filename in filenames:
        images.append(imageio.imread(filename))
    output_file = 'Gif-%s.gif' % datetime.datetime.now().strftime('%Y-%M-%d-%H-%M-%S')
    imageio.mimsave(output_file, images, duration=duration)


if __name__ == "__main__":

    listdir=os.listdir()
    filenames=list()
    for i in range(len(listdir)):
        if listdir[i].endswith('.png'):
            filenames.append(listdir[i])

    duration=1

    if not all(f.lower().endswith(VALID_EXTENSIONS) for f in filenames):
        print('Only png and jpg files allowed')
        sys.exit(1)

    create_gif(filenames, duration)
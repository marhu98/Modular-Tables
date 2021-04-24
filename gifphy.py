from glob import glob
import re
import imageio

def index(value):
    return int(re.search("frame(?P<number>\d*)\.png",value).groupdict()["number"])


# filepaths
fp_in = "frames/1/png/*.png"
fp_out = "gifs/1.gif"

filenames= sorted(glob(fp_in),key=index)

images = []

for file in filenames:
    images.append(imageio.imread(file))

imageio.mimsave(fp_out,images)

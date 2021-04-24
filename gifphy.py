from glob import glob
import imageio
# filepaths
fp_in = "frames/1/png/*.png"
fp_out = "gifs/1.gif"

filenames= sorted(glob(fp_in))

images = []

for file in filenames:
    images.append(imageio.imread(file))

imageio.mimsave(fp_out,images)

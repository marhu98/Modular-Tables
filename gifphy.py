from glob import glob
import re
import imageio



def index(value):
    search = re.search("frame(?P<number>\d*)\.png",value)

    if not search:
        return -1

    return int(search.groupdict()["number"])

def togif(name):
    # filepaths
    fp_in = f"frames/{name}/png/*.png"
    fp_out = f"gifs/{name}.gif"
    
    filenames= sorted(glob(fp_in),key=index)
    
    images = []
    
    for file in filenames:
        images.append(imageio.imread(file))
    
    imageio.mimsave(fp_out,images)



dirs = glob("frames/*/")
names = [s.split("/")[-2] for s in dirs]

for name in names:
    togif(name)

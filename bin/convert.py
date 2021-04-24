import os
from glob import glob
import cairosvg
from tqdm import tqdm

def createIfNot(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

folders = glob("/frames/*")

for folder in folders:
    createIfNot(folder+"/png")
    for file in tqdm(glob(f"{folder}/svg/*.svg")):
        dest = file.split("/")
        name = dest.pop()
        dest.pop()
        dest.append("png")
        dest.append(name.replace(".svg",".png"))
        dest = "/".join(dest)
        cairosvg.svg2png(url=file, write_to=dest)

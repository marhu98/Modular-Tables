import os
import drawSvg as draw
import numpy as np
from tqdm import tqdm

class Table:
    
    def printlines_(self):
        for i in range(self.mod):
            for j in range(2,int(self.number)+1):
                self.draw.append(draw.Line(*self.rads[i],
                                *self.rads[j*i%int(self.mod)],
                                          stroke="blue",
                                          stroke_width=0.1,
                                          fill="none"))
                
    def printlines(self):
        for i in range(self.mod):
            endpoint = int(self.number*i)%int(self.mod)
            self.draw.append(draw.Line(*self.rads[i],
                            *self.rads[endpoint],
                                      stroke=self.color,
                                      stroke_width=0.1,
                                      fill="none"))
    
    def __init__(self,number,mod, size=100, put_numbers = True, color = "blue",name="picture"):
        
        self.size=size
        
        self.draw = draw.Drawing(size, size, origin="center")
        
        if put_numbers:
            self.radius = 0.35*size
        else:
            self.radius= 0.5*size-5
        self.mod = mod
        self.number = number
        self.color = color
        self.dir = dir
        self.name = name
        
        self.draw.append(
            draw.Circle(0,0,self.radius,fill="white",
                       stroke_width=2,stroke="black"))
        self.coords = []
        self.rads = []
        
        #d.append(draw.Line(30, -20, 0, -10,
        #    stroke='red', stroke_width=2, fill='none',
        #    marker_end=arrow))
        
        for i in range(mod):
            #self.draw.append(draw.Text("aefd",0,0,fill="white"))
            nr = self.radius + 0.07*size
            ang = 2*np.pi*i/mod
            self.coords.append((nr*np.sin(ang),nr*np.cos(ang)))
            self.rads.append((self.radius *np.sin(ang),self.radius *np.cos(ang)))
            #if i!=0:
            #    text = str(i) 
            #else: 
            #    text = str(mod)
            
            text = str(i)
            if put_numbers:
                self.draw.append(draw.Text(text,
                                           10,*self.coords[i],fill="black",
                                          text_anchor='middle',valign="middle"))
        
        self.printlines()
    
    def save(self, dir=""):
        if dir == "":
            dir=self.dir
        dir+="/svg"
        if not os.path.exists(dir):
            os.makedirs(dir)
            
        self.draw.saveSvg(f"{dir}/{self.name}.svg")
        
            
            
        
class Animate_mod:
    
    def __init__(self,number,mods, size=100, put_numbers = True,name="frame",color="blue"):
        self.size=size
        
        self.draw = draw.Drawing(size, size, origin="center")
        
        self.mods = mods
        self.number = number
        self.put_numbers=put_numbers
        self.color = color
        
        self.name = name
        
        self.frames = []
        
    def get_frames(self):
        current = self.mods[0]
        with draw.animate_jupyter(self.draw_frame, delay=0.05) as anim:
            while current<self.mods[1]:
                current = current+1
                self.frames.append(self.draw_frame(current))
        
    def save(self,dir="frames"):
        dir+="/svg"
        if not os.path.exists(dir):
            os.makedirs(dir)
        self.get_frames()
        for i in tqdm(range(len(self.frames))):
            self.frames[i].saveSvg(f"{dir}/frame{i}.svg")
        
    def draw_frame(self,current):
        d = Table(self.number,current,size=self.size, put_numbers = self.put_numbers, color = self.color).draw
        d.setRenderSize(h=self.size)
        return d
        
    def animate(self):
        current = self.mods[0]
        with draw.animate_jupyter(self.draw_frame, delay=0.05) as anim:
            while current<=self.mods[1]:
                #print(current)
                current = current+1
                anim.draw_frame(current)
                
            #This is just to make the last frame nicer
            anim.draw_frame(int(current+1))
        
        
class Animate_number:
    
    def __init__(self,numbers,mod, size=100, put_numbers = True,step=0.1,name="frame",color="blue"):
        self.size=size
        
        self.draw = draw.Drawing(size, size, origin="center")
        
        self.mod = mod
        self.numbers = numbers
        self.put_numbers=put_numbers
        self.color = color
        
        self.step = step
        
        self.name = name
        
        self.frames = []
        
    def get_frames(self):
        current = self.numbers[0]
        with draw.animate_jupyter(self.draw_frame, delay=0.05) as anim:
            while current<self.numbers[1]:
                #print(current)
                current = current+self.step
                self.frames.append(self.draw_frame(current))
        
    def save(self,dir="frames"):
        dir+="/svg"
        if not os.path.exists(dir):
            os.makedirs(dir)
        self.get_frames()
        for i in tqdm(range(len(self.frames))):
            self.frames[i].saveSvg(f"{dir}/frame{i}.svg")
        
    def draw_frame(self,current):
        d = Table(current,self.mod,size=self.size, put_numbers = self.put_numbers, color = self.color).draw
        d.setRenderSize(h=self.size)
        #d.append(draw.Rectangle(-2, -2, 4, 8, fill='white'))
        #d.append(draw.Rectangle(-1, -1.05, 2, 0.05, fill='brown'))
        return d
        
    def animate(self):
        current = self.numbers[0]
        with draw.animate_jupyter(self.draw_frame, delay=0.05) as anim:
            while current<=self.numbers[1]:
                #print(current)
                current = current+self.step
                anim.draw_frame(current)
                
            #This is just to make the last frame nicer
            anim.draw_frame(int(current+self.step))

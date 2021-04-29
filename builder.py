import os, re, math
import cv2, numpy as np
import PIL.Image as Image
import c2e

class ImageBuilder():
    def __init__(self, p, r):
        self._PATH = p
        self._LOD = r
        self._RES = self.getRes()
        self._QUADS = []
        self.run()

    def run(self):
        pattern = "(.*)_(.*)_(.*)"
        pct = 0

        for folder in os.listdir(self._PATH):
            if os.path.isdir(os.path.join(self._PATH, folder)):
                plate = Image.new('RGB', (self._RES * 258, self._RES * 258))
                for file in os.listdir(os.path.join(self._PATH, folder)):
                    filename = file[:-4]
                    if int(re.search(pattern, filename).group(1)) == self._LOD:
                        tex = cv2.imread(os.path.join(self._PATH, folder, file))
                        x = int(re.search(pattern, filename).group(2))
                        y = int(re.search(pattern, filename).group(3))
                        plate.paste(Image.fromarray(tex), (258 * y, 258 * x))

                plate.save(f"{self._PATH}/{folder}.png", "PNG")
                self._QUADS.append(f"{folder}.png")
                pct += 1
                print(f"Building Quadrants: {pct} / 6")
        
        cubemap = Image.new('RGB', (self._RES * 258 * 4, self._RES * 258 * 3))
        pct = 0
        for folder in os.listdir(self._PATH):
            if folder in self._QUADS:
                if folder == "pos_x.png":
                    x = 2
                    y = 1
                elif folder == "neg_x.png":
                    x = 0
                    y = 1
                elif folder == "pos_y.png":
                    x = 1
                    y = 0
                elif folder == "neg_y.png":
                    x = 1
                    y = 2
                elif folder == "pos_z.png":
                    x = 1
                    y = 1
                elif folder == "neg_z.png":
                    x = 3
                    y = 1
                
                quad = cv2.imread(os.path.join(self._PATH, folder))
                cubemap.paste(Image.fromarray(quad), (258 * self._RES * x, 258 * self._RES * y))
                pct += 1
                print(f"Building Cubemap: {pct} / 6")
        
        cubemap.save(os.path.join(self._PATH, "cubemap.png"), "PNG")
        data =  np.array(cubemap)
        print("Converting to Equirectangular Projection...")
        equirect = c2e(data, self._RES * 258 * 2, self._RES * 258 *4)
        equirect = Image.fromarray(np.uint8(equirect)).convert('RGB')
        equirect.save(os.path.join(self._PATH, "equirect.png"), "PNG")
        equirect.show()

    def getRes(self):
        count = 0
        for folder in os.listdir(self._PATH):
            if os.path.isdir(os.path.join(self._PATH, folder)):
                for file in os.listdir(os.path.join(self._PATH, folder)):
                    if int(file[0]) == self._LOD:
                        count += 1
                break

        return int(math.sqrt(count))
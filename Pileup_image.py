import numpy as np
import open3d as o3d
import sys
import math
import pandas as pd
import cv2
import os

def main():
    args=sys.argv
    dir1=args[1]
    dir2=args[2]
    outdir=args[3]
    over=float(args[4])
    files1=os.listdir("./"+dir1)
    files2=os.listdir("./"+dir2)

    for file in files1:
        #print(file)
        imagename1="./"+dir1+"/"+file
        imagename2="./"+dir2+"/"+file
        image1=cv2.imread(imagename1)
        image2=cv2.imread(imagename2)
        blend_image=cv2.addWeighted(image1,over,image2,(1-over),0)
        #outputname="./"+outdir+"/"+file
        print(outputname)
        cv2.imwrite(outputname,blend_image)
        print("end:",file)
        
        

if __name__=="__main__":
    main()

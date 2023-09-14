from img_recognitizon import get_coords
import math
from math import sqrt

def pix_to_cm(pix:int,cm:int):

    one_pix:float =pix/cm
    coorx_on_cm:float=float(dimensions[0])/one_pix
    coory_on_cm:float=float(dimensions[1])/one_pix

    return one_pix, coorx_on_cm, coory_on_cm

def get_parameters(coor_x:int ,coor_y:int):


    #Get all x an y distances
    cathetus_x:float=int(coords_sphero[0][0])-coor_x
    cathetus_y:float=int(coords_sphero[0][1])-coor_y

    print(cathetus_x,cathetus_y)
    print(coords_sphero[0][0],coords_sphero[0][1])

    #Get the value of 1cm
    one_pix,coorx_on_cm,coory_on_cm=pix_to_cm(506,20) # 506 px is equal to 20 cm

    #convert the cathetus to cm
    cathetus_x:float=cathetus_x/one_pix
    cathetus_y:float=cathetus_y/one_pix
    print(cathetus_x,cathetus_y)

    #Get the value of teta
    teta=math.atan(cathetus_x/cathetus_y)

    hypotenuse:float=sqrt((cathetus_x**2)+(cathetus_y**2))

    #the speed is constant 5
    time=hypotenuse/5

    return hypotenuse, teta, time

if __name__ == "__main__":
    coords_sphero, coords_obstacles,dimensions= get_coords('img/Boxes.png')
    print(get_parameters(128,1346))
import numpy as np
import cv2
import shutil, os

def scale(img, long_size=192,short_size=48):
    h, w = img.shape[0:2]

    a = short_size - h
    b = long_size - w

    if a > 0:
        img = np.pad(img,((0,a),(0,0),(0,0)),"constant",constant_values=200)
    if b> 0:
        img = np.pad(img, ((0, 0), (0, b), (0, 0)), "constant", constant_values=200)
    h2, w2 = img.shape[0:2]
    scale = short_size * 1.0 / h2
    scale2 = long_size*1.0/w2
    img = cv2.resize(img, dsize=None, fx=scale2, fy=scale)
    print(img.shape)
    return img

dir_root = r"C:\002workspace\02data\02haoda\haoda_data\/"
img_src = dir_root + "/img0811_big/"
img_tar = dir_root + "/img0811/"
for imgname in os.listdir(img_src):
    img_path = img_src + imgname
    img_save = img_tar + imgname
    img = cv2.imread(img_path)
    h, w = img.shape[0:2]
    a = w-h
    img = np.pad(img, ((0, a), (0, 0), (0, 0)), "constant", constant_values=0)
    scale = 1024 * 1.0 / w
    img = cv2.resize(img, dsize=None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)
    cv2.imwrite(img_save, img)
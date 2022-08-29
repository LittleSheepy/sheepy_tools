import numpy as np
import cv2
import shutil, os


dir_root = r"C:\002workspace\02data\02haoda\haoda_data\haoda_train_xqzs20220811\train\/"
img_src = dir_root + "/images/"
img_tar = dir_root + "/images1/"

beishu = 10
for filename in os.listdir(img_src):
    for i in range(beishu):
        filename_new = str(i) + "_" + filename
        shutil.copy(img_src + filename, img_tar + filename_new)












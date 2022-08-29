import shutil, os


dir_root = r"C:\002workspace\02data\02haoda\haoda_data/"
img_all = dir_root + "/img_all/0811/"
img0801 = dir_root + "/img0811_big/"
for diename in os.listdir(img_all):
    diepath = img_all + diename + "/"
    for imgname in os.listdir(diepath):
        imgname_new = "0811-" + diename + "-" + imgname
        shutil.copy(diepath + imgname, img0801 + imgname_new)

























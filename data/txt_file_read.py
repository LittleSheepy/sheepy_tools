import shutil, os

#classes = ["heidian", "huahen", "liehen", "diuqiu","quejiao"]
classes = ["0", "1", "2"]
dir_root = r"C:\002workspace\02data\02haoda\haoda_data/"
dir_label = dir_root + "/labels0811/"
dir_huahen = dir_root + "/labels0811_liewen/"
dir_img = dir_root + "/img0811/"
dir_img_liewen = dir_root + "/img0811_liewen/"
filename = '21_0_0.txt'
txt_file = dir_label + filename
for filename in os.listdir(dir_label):
    txt_file = dir_label + filename
    with open(txt_file, 'r') as f:
        data = f.readlines()
        print(data)
        flg = False
        for line in data:
            splits = line.split(' ')
            print(splits[0])
            if int(splits[0]) == classes.index('1'):
                flg = True
                break
    if flg:
        shutil.copy(dir_label + filename, dir_huahen + filename)
        filename_img = filename.replace("txt","bmp")
        shutil.copy(dir_img + filename_img, dir_img_liewen + filename_img)

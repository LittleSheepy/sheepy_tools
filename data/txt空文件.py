import shutil, os

dir_root = r"C:\MyGithub\sheepy_tools\data\截图\output\/"
dir_label = dir_root + "/labels/"
dir_images = dir_root + "/images_biaozhu/"
dir_label_null = dir_root + "/label_null/"

movelist = []
for filename in os.listdir(dir_label):
    filepath = dir_label + filename
    with open(filepath, 'r') as f:
        data = f.readlines()
        if len(data) == 0:
            print(filename)
            movelist.append(filename)

for filename in movelist:
    shutil.move(dir_label + filename, dir_label_null + filename)
    shutil.move(dir_images + filename.replace("txt", "bmp"), dir_label_null + filename.replace("txt", "bmp"))
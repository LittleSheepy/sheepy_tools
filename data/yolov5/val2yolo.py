import shutil, os

# "image_id","0801-4M951023003-0011-4M951023003-83","category_id",1,"bbox",651.815,433.149,9.213,9.34,"score",0.10199
classes = ["0", "1", "2"]
dir_root = r"C:\MyGithub\yolov5\yolov5-train\runs\val\exp7/"
file_label = dir_root + "2.csv"
dir_label = dir_root + "/2label/"
# file_label = dir_root + "1high.csv"
# dir_label = dir_root + "/1high/"


with open(file_label, 'r') as f:
    data = f.readlines()
    for line in data:
        splits = line.split(',')
        file_path = dir_label + splits[1] + ".txt"
        with open(file_path, "a") as f1:
            xmin = float(splits[5])
            ymin = float(splits[6])
            w = float(splits[7])
            h = float(splits[8])
            xcenter = xmin + w/2
            ycenter = ymin + h/2
            line = splits[3] + " " + str(round(xcenter/1024, 4)) + " " + str(round(ycenter/1024, 4))\
                   + " " +str(round(w/1024, 4)) + " " + str(round(h/1024, 4)) + "\n"
            f1.write(line)
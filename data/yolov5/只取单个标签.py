import os,sys
import cv2

dir_root = r"C:\shared_folder\haoda_train0816\exp_cn3_08162\predict\val0816\/"
dir_label_src = dir_root + "/labels/"
dir_label_tar = dir_root + "/labels_3/"



def main():
    for filename in os.listdir(dir_label_src):
        filepath_src = dir_label_src + filename
        filepath_tar = dir_label_tar + filename
        with open(filepath_src, 'r') as f_src:
            lines_src = f_src.readlines()
        delete_flg = True
        with open(filepath_tar, 'a') as f_tar:
            for line in lines_src:
                line_items = line.split(" ")
                if line_items[0] == "3":
                    delete_flg = False
                    f_tar.write(line)
        if delete_flg:
            os.remove(filepath_tar)

if __name__ == '__main__':
    main()


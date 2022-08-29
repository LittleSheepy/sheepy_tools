import os,sys
import cv2
import numpy as np
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir + "/tools")
import boxFuncs
#from tools.boxFuncs import IOU
dir_root = r"./"
dir_imgs_big = dir_root + 'input/'
dir_imgs_small = dir_root + 'output/images_biaozhu/'
dir_txt_small = dir_root + 'output/labels/'
dir_labels_big= dir_root + 'output/labels_big_out/'
dir_labels_big_output = dir_root + 'output/labels_big_out/'

def main():
    for filename_small in os.listdir(dir_txt_small):
        print(filename_small)
        filename_only = filename_small[:-4]
        filename = filename_only
        [filename,ymin_smal] = filename.rsplit("_", 1)
        ymin_smal = int(ymin_smal)
        [filename,xmin_smal] = filename.rsplit("_", 1)
        xmin_smal = int(xmin_smal)
        [filename_big_only,num] = filename.rsplit("_", 1)
        num = int(num)
        img_big_path = dir_imgs_big + filename_big_only + ".bmp"
        txt_big_path = dir_labels_big + filename_big_only + ".txt"
        img_small_path = dir_imgs_small + filename_only + ".bmp"
        img_big = cv2.imread(img_big_path, cv2.IMREAD_GRAYSCALE)
        w_big, h_big = img_big.shape[::-1]
        img_small = cv2.imread(img_small_path, cv2.IMREAD_GRAYSCALE)
        w_small, h_small = img_small.shape[::-1]

        with open(txt_big_path, "r") as f:
            lines_big = f.readlines()
        with open(dir_txt_small + filename_small, "r") as f:
            lines_small = f.readlines()
        # txt 合在一起
        labels_big_output_path = dir_labels_big_output + filename_big_only + ".txt"
        with open(labels_big_output_path, "w+") as f:
            # 小坐标转大坐标
            lines_small2big = []
            for line in lines_small:
                line_items = line.split(" ")
                center_x_little = float(line_items[1]) * w_small
                center_y_little = float(line_items[2]) * h_small
                w_box = float(line_items[3]) * w_small
                h_box = float(line_items[4]) * h_small

                center_x_big = round((center_x_little + xmin_smal) / w_big,6)
                center_y_big = round((center_y_little + ymin_smal) / h_big,6)
                w_box = round(w_box / w_big,6)
                h_box = round(h_box / h_big,6)
                line_tmp = line_items[0] + " " + str(center_x_big) \
                                              + " " + str(center_y_big) \
                                              + " " + str(w_box) \
                                              + " " + str(h_box) + "\n"
                lines_small2big.append(line_tmp)

            # iou 去重
            lines_big_new = []
            for line_big in lines_big:
                line_big_items = line_big.split(" ")
                line_big_items = [float(num) for num in line_big_items]
                # 如果label是1
                if line_big_items[0] == 1:
                    lines_big_new.append(line_big)
                    continue
                # 找重复
                repeat_flg = False
                for line_small in lines_small2big:
                    line_small_items = line_small.split(" ")
                    line_small_items = [float(num) for num in line_small_items]
                    is_repeat = boxFuncs.box_repeat(line_big_items, line_small_items)
                    if is_repeat:
                        repeat_flg = True
                        break
                if not repeat_flg:
                    lines_big_new.append(line_big)
            # 小图框 顺便改labels
            for line_small in lines_small2big:
                line_small_items = line_small.split(" ", 1)
                lines_big_new.append("3 "+ line_small_items[1])

            # 保存新的
            for line in lines_big_new:
                f.write(line)


if __name__ == '__main__':
    main()




















































import os
import cv2
import numpy as np
dir_root = r"./"
dir_imgs_input = dir_root + 'input/'
dir_imgs_output = dir_root + 'output/images/'
dir_tmplate_result = dir_root + 'tmplate_result/'
dir_txt_input = dir_root + 'txt/'
dir_txt_output = dir_root + 'output/labels/'
#模板匹配批量截图
fangda = 4
def main():
    #template_name_list = ["rx7.bmp"]
    template_name_list = ["rx7.bmp", "rx41.bmp", "rx0103.bmp", "rx3439.bmp"]

    for filename in os.listdir(dir_imgs_input):
        filenames = filename.split('.')
        filename_only = filenames[0]
        big_img_file = dir_imgs_input + filename
        big_img_org = cv2.imread(big_img_file, cv2.IMREAD_COLOR)
        big_img_result = cv2.imread(big_img_file, cv2.IMREAD_COLOR)
        big_img = cv2.imread(big_img_file, cv2.IMREAD_GRAYSCALE)

        w_bigimg, h_bigimg = big_img.shape[::-1]
        #save_little_imgs = dir_imgs_output + filename_only + '/'
        save_little_imgs = dir_imgs_output + '/'
        #创建文件夹
        if not os.path.exists(save_little_imgs):
            os.mkdir(save_little_imgs)

        # 模板匹配 res[hight][weight]
        big_img = cv2.cvtColor(big_img, cv2.COLOR_GRAY2BGR)
        big_img = cv2.resize(big_img, dsize=None, fx=fangda, fy=fangda, interpolation=cv2.INTER_AREA)
        big_img = cv2.cvtColor(big_img, cv2.COLOR_BGR2GRAY)
        for template_name in template_name_list:
            template = cv2.imread("./template/" + template_name, cv2.IMREAD_GRAYSCALE)
            w, h = template.shape[::-1]
            template = cv2.cvtColor(template, cv2.COLOR_GRAY2BGR)
            template = cv2.resize(template, dsize=None, fx=fangda, fy=fangda, interpolation=cv2.INTER_AREA)
            template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
            res = cv2.matchTemplate(big_img, template, cv2.TM_CCOEFF_NORMED)

            threshold = 0.8
            locs = np.where(res >= threshold)

            # 判断个数 为0 就continue
            if len(locs[0]) < 5:
                continue

            # 遍历结果
            have_list = []
            for loc in zip(*locs[::-1]):
                have_flg = False
                have_loc_tmp = 0
                have_loc_tmp_i = 0
                for i, have_loc in enumerate(have_list):
                    if abs(have_loc[0] - loc[0]) < 200 and abs(have_loc[1] - loc[1]) < 200:
                        have_flg = True
                        have_loc_tmp = have_loc
                        have_loc_tmp_i = i
                        break
                # 替换判断
                if not have_flg:
                    have_list.append(loc)
                elif res[(have_loc_tmp[1], have_loc_tmp[0])] < res[(loc[1], loc[0])]:
                    have_list.pop(have_loc_tmp_i)
                    have_list.insert(have_loc_tmp_i, loc)

            # 遍历保存
            num = 0
            for loc in have_list:
                score = res[loc[1]][loc[0]]
                loc = (int(loc[0]/fangda), int(loc[1]/fangda))
                new_little_file_name_only = filename_only + "_" + str(num) + "_" + str(loc[0]) + "_" + str(loc[1])
                num += 1
                new_little_file_name = new_little_file_name_only + ".bmp"

                # 保存图片
                new_little_file_img = big_img_org[loc[1]:loc[1]+h, loc[0]:loc[0]+w, :]
                cv2.imwrite(save_little_imgs + new_little_file_name, new_little_file_img)

                # 保存txt
                txt_path = dir_txt_input + filename_only + ".txt"
                save_txt_path = dir_txt_output + new_little_file_name_only + ".txt"
                if not os.path.exists(txt_path):
                    continue
                with open(txt_path, "r") as f_in:
                    with open(save_txt_path, "a") as f_out:
                        lines_in = f_in.readlines()
                        for line in lines_in:
                            line_items = line.split(" ")
                            center_x_big = float(line_items[1]) * w_bigimg
                            center_y_big = float(line_items[2]) * h_bigimg
                            w_big = float(line_items[3]) * w_bigimg
                            h_big = float(line_items[4]) * h_bigimg

                            # 判断是否在当前die
                            if loc[0] < center_x_big < loc[0]+w and loc[1] < center_y_big < loc[1]+h:
                                center_x_little = (center_x_big - loc[0]) / w
                                center_y_little = (center_y_big - loc[1]) / h
                                w_big = w_big / w
                                h_big = h_big / h

                                line_little = line_items[0] + " " + str(center_x_little) \
                                              + " " + str(center_y_little) \
                                              + " " + str(w_big) \
                                              + " " + str(h_big) + "\n"
                                f_out.write(line_little)




                cv2.rectangle(big_img_result, loc, (loc[0] + w, loc[1] + h), (255, 0, 255), 2)
                #score = res[loc[1]][loc[0]]
                cv2.putText(big_img_result, str(score), loc, 0, 1/3, (0,0,255), lineType=cv2.LINE_AA)
            cv2.imwrite(dir_tmplate_result + filename, big_img_result)



if __name__ == '__main__':
    main()










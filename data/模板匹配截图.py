import os
import cv2
import numpy as np
dir_root = r"C:\002workspace\02data\01chaocai\/"
dir_big_imgs = dir_root + 'chaocai_data/'
dir_little_imgs = dir_root + 'little_imgs/'
dir_tmplate_result = dir_root + 'tmplate_result/'
#模板匹配批量截图
def main():
    template = cv2.imread("template.jpg", cv2.IMREAD_GRAYSCALE)
    w, h = template.shape[::-1]
    for filename in os.listdir(dir_big_imgs):
        filenames = filename.split('.')
        filename_only = filenames[0]
        big_img_file = dir_big_imgs + filename
        big_img_org = cv2.imread(big_img_file, cv2.IMREAD_COLOR)
        big_img_result = cv2.imread(big_img_file, cv2.IMREAD_COLOR)
        big_img = cv2.imread(big_img_file, cv2.IMREAD_GRAYSCALE)
        save_little_imgs = dir_little_imgs + filename_only + '/'
        #创建文件夹
        if not os.path.exists(save_little_imgs):
            os.mkdir(save_little_imgs)

        # 模板匹配
        res = cv2.matchTemplate(big_img, template, cv2.TM_CCOEFF_NORMED)
        threshold = 0.7
        locs = np.where(res >= threshold)

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
            new_little_file_name = filename_only + "_" + str(num) + "_" + str(loc[0]) + "_" + str(loc[1]) + ".jpg"
            new_little_file_img = big_img_org[loc[1]:loc[1]+h, loc[0]:loc[0]+w, :]
            cv2.imwrite(save_little_imgs + new_little_file_name, new_little_file_img)
            cv2.rectangle(big_img_result, loc, (loc[0] + w, loc[1] + h), (255, 0, 255), 2)
            num += 1
        cv2.imwrite(dir_tmplate_result + filename, big_img_result)



if __name__ == '__main__':
    main()










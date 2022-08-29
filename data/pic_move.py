
import os, shutil







def move1():
    img_root = r"C:\002workspace\02data\02haoda\haoda_data\haoda_train20220816\val\/"
    img_dir = img_root + r"\images/"
    biaozhu = img_root + r"\images_3/"
    nobiaozhu = "D:/01sheepy/01work/01baojie_ocr/pp/img_nobiaozhu/"
    xml_dir = img_root + r"\labels_3/"
    for imgfile in os.listdir(img_dir):
        moveFlg = False
        for xmlfile in os.listdir(xml_dir):
            print(xmlfile)
            if xmlfile[:-4] == imgfile[:-4]:
                shutil.copyfile(img_dir + imgfile, biaozhu + imgfile)
                #shutil.move(img_dir + imgfile, biaozhu + imgfile)
                moveFlg = True
        # if not moveFlg:
        #     shutil.copyfile(img_dir + imgfile, nobiaozhu + imgfile)



if __name__ == '__main__':
    move1()
#*--coding="utf-8"*
import xml.etree.ElementTree as ET
import os

classes = ["heidian", "huahen", "liehen", "diuqiu","quejiao"]
dir_root = r"C:\Users\jxcao\Desktop\data\auto_label\pre_output21/"
dir_label = dir_root + "/labels/"
dir_huahen = dir_root + "/huahen/"
dir_huahen_xml = dir_root + "/huahen_xml/"
def txt2voc():
    for filename in os.listdir(dir_label):
        txt_file = dir_label + filename
        xml_file = dir_huahen_xml + filename.replace("txt", 'xml')
        with open(xml_file, 'w') as f_xml:

            with open(txt_file, 'r') as f:
                data = f.readlines()









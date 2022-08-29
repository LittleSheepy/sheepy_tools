import shutil, os

labels_train = r"C:\002workspace\02data\02haoda\haoda_data\haoda_train20220801\train\labels\/"
labels_predict = r"C:\MyGithub\yolov5\yolov5-train\runs\val\exp7\2label\/"
labels_save = r"C:\MyGithub\yolov5\yolov5-train\runs\val\exp7\2_nolabel\/"


def IOU(yolo_box1, yolo_box2):
    xmin1 = yolo_box1[1] - yolo_box1[3]/2
    ymin1 = yolo_box1[2] - yolo_box1[4]/2
    xmax1 = yolo_box1[1] + yolo_box1[3]/2
    ymax1 = yolo_box1[2] + yolo_box1[4]/2

    xmin2 = yolo_box2[1] - yolo_box2[3]/2
    ymin2 = yolo_box2[2] - yolo_box2[4]/2
    xmax2 = yolo_box2[1] + yolo_box2[3]/2
    ymax2 = yolo_box2[2] + yolo_box2[4]/2

    # 计算每个矩形的面积
    s1 = (xmax1 - xmin1) * (ymax1 - ymin1)  # b1的面积
    s2 = (xmax2 - xmin2) * (ymax2 - ymin2)  # b2的面积

    # 计算相交矩形
    xmin = max(xmin1, xmin2)
    ymin = max(ymin1, ymin2)
    xmax = min(xmax1, xmax2)
    ymax = min(ymax1, ymax2)

    w = max(0, xmax - xmin)
    h = max(0, ymax - ymin)
    a1 = w * h  # C∩G的面积
    a2 = s1 + s2 - a1
    iou = a1 / a2  # iou = a1/ (s1 + s2 - a1)
    return iou

for predict_filename in os.listdir(labels_predict):
    predict_file_path = labels_predict + predict_filename
    train_file_path = labels_train + predict_filename
    save_file_path = labels_save + predict_filename
    lable_list = []
    with open(train_file_path, "r") as f:
        data = f.readlines()
        for line in data:
            splits = line.split(" ")
            splits = [float(num) for num in splits]
            lable_list.append(splits)

    box_no_label_list = []
    with open(predict_file_path, "r") as predict_f:
        data = predict_f.readlines()
        for line in data:
            splits = line.split(" ")
            splits = [float(num) for num in splits]
            findFlg = False
            for label_item in lable_list:
                iou = IOU(label_item, splits)
                if iou > 0.5:
                    findFlg = True
                    break
            if not findFlg:
                box_no_label_list.append(line)

    if len(box_no_label_list) > 0:
        with open(save_file_path, "a") as f:
            for line in box_no_label_list:
                f.write(line)



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

def box_repeat(yolo_box1, yolo_box2):
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
    if 0.9 < s1/s2 < 1.1 and iou > 0.8:
        return True
    return False
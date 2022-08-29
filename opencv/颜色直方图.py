"""
hist = cv2.calcHist([image],             # 传入图像（列表）
                    [0],                 # 使用的通道（使用通道：可选[0],[1],[2]）
                    None,                # 没有使用mask(蒙版)
                    [256],               # HistSize
                    [0.0,255.0])         # 直方图柱的范围
                                         # return->list
"""
import cv2
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def calcAndDrawHist(image, color):
    hist= cv2.calcHist([image],[0],None,[256],[0.0,255.0])
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(hist)
    histImg = np.zeros([256,256,3], np.uint8)
    hpt =int(0.9*256)
    for h in range(256):
        intensity =int(hist[h]*hpt/maxVal)
        cv2.line(histImg,(h,256),(h,256-intensity), color)
    return histImg


def main():
    original_img = cv2.imread("template.jpg")
    img = cv2.resize(original_img,None,fx=0.6,fy=0.6,interpolation = cv2.INTER_CUBIC)
    b, g, r = cv2.split(img)

    histImgB = calcAndDrawHist(b,[255,0,0])
    histImgG = calcAndDrawHist(g,[0,255,0])
    histImgR = calcAndDrawHist(r,[0,0,255])

    cv2.imshow("histImgB", histImgB)
    cv2.imshow("histImgG", histImgG)
    cv2.imshow("histImgR", histImgR)
    cv2.imshow("Img", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def grayHist():
    img = cv.imread(r'C:\002workspace\02data\01chaocai\little_imgs\32/32_246_55701_1633.jpg')
    cv.imshow('Img', img)

    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow('GrayImg', gray_img)

    # Gray Histogram
    gray_hist = cv.calcHist([gray_img], [0], None, [256], [0, 256], False)
    # cv.calcHist(images, channels, mask, histSize, ranges, accumulate)

    plt.figure(1)
    plt.title('Gray Histogram Contour')
    plt.xlabel('gray level')
    plt.ylabel('number of pixels')
    plt.plot(gray_hist)
    plt.xlim([0, 256])

    plt.figure(2)
    plt.title('Gray Histogram')
    plt.xlabel('gray level')
    plt.ylabel('number of pixels')
    plt.hist(gray_img.ravel(), 256)

    plt.show()

    cv.waitKey(0)
if __name__ =='__main__':
    grayHist()
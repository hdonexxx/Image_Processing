import cv2 as cv2
import os
from PIL import Image, ImageFont, ImageDraw
import argparse

ascii_char = list(
    "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


# 将像素转换为ascii码
def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return ''
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0 + 1) / length
    return ascii_char[int(gray / unit)]


def Pic_to_ascii(name):
    im = Image.open(path + name)
    print('原始图片尺寸：', im.width, im.height)

    # 如果原始图片的尺寸太大就不要放大的太多
    min_bian = im.width if im.width <= im.height else im.height
    (x, y, a) = (6, 15, 1) if min_bian >= 2000 else (2, 5, 3)
    WIDTH = int(im.width / x)  #高度比例为原图的1/6较好，由于字体宽度
    HEIGHT = int(im.height / y)  #高度比例为原图的1/15较好，由于字体高度
    im_txt = Image.new("RGB", (a * im.width, a * im.height), (255, 255, 255))
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)
    print('新图片的行数与列数：', WIDTH, HEIGHT)

    txt = ""
    colors = []
    for i in range(HEIGHT):
        for j in range(WIDTH):
            pixel = im.getpixel((j, i))
            colors.append((pixel[0], pixel[1], pixel[2]))  #记录像素颜色信息
            if (len(pixel) == 4):
                txt += get_char(pixel[0], pixel[1], pixel[2], pixel[3])
            else:
                txt += get_char(pixel[0], pixel[1], pixel[2])
        txt += '\n'
        colors.append((255, 255, 255))
    dr = ImageDraw.Draw(im_txt)
    font = ImageFont.load_default().font  #获取字体
    x = y = 0

    #获取字体的宽高
    font_w, font_h = font.getsize(txt[1])
    font_h *= 1.37  #调整后更佳

    #ImageDraw为每个ascii码进行上色
    for i in range(len(txt)):
        if (txt[i] == '\n'):
            x += font_h
            y = -font_w
        dr.text([y, x], txt[i], colors[i])
        y += font_w
    im_txt.save(path2 + name[:-4] + '_ascii.jpg')


path = r'C:\Users\Administrator\Pictures\Saved Pictures\\'
path2 = r'C:\Users\Administrator\Pictures\Saved Pictures\\'
Pic_to_ascii('捕获x.png')

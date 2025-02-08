from PIL import Image
import numpy as np

# 原始图片路径
path = 'F:\Face\\'
name = 'output.jpg'
original_image_path = path + name
# 要生成的手绘图片路径，可自定义
handdrawn_image_path = path + name[:-4] + '_handdrawn.jpg'

# 加载原图，将图像转化为数组数据
a = np.asarray(Image.open(original_image_path).convert('L')).astype('float')
depth = 10.

#取图像灰度的梯度值
grad = np.gradient(a)

#取横纵图像梯度值
grad_x, grad_y = grad
grad_x = grad_x * depth / 100.
grad_y = grad_y * depth / 100.
A = np.sqrt(grad_x**2 + grad_y**2 + 1.)
uni_x = grad_x / A
uni_y = grad_y / A
uni_z = 1. / A

#光源的俯视角度转化为弧度值
vec_el = np.pi / 2.2

#光源的方位角度转化为弧度值
vec_az = np.pi / 4.

#光源对x轴的影响
dx = np.cos(vec_el) * np.cos(vec_az)
dy = np.cos(vec_el) * np.sin(vec_az)
dz = np.sin(vec_el)

#光源归一化，把梯度转化为灰度
b = 255 * (dx * uni_x + dy * uni_y + dz * uni_z)

#避免数据越界，将生成的灰度值裁剪至0-255内
b = b.clip(0, 255)

#图像重构
im = Image.fromarray(b.astype('uint8'))

im.save(handdrawn_image_path)

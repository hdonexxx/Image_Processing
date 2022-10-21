import imageio
path = './'
path2 = './save_gif/'
gif_images=[]
for i in range(1,100):
    gif_images.append(imageio.imread(path+str(i)+'.jpg'))
imageio.mimsave(path2+'output.gif',gif_images,fps=10)

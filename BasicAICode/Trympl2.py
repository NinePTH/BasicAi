plt.figure(figsize=(18,8))
for index, (image,label) in enumerate(zip(x[0:10],y[0:10])):
  plt.subplot(1, 10, index+1)
  plt.imshow(np.reshape(image, (8,8)), cmap=plt.cm.gray)
  plt.title('%i\n' % label ,fontsize =18)

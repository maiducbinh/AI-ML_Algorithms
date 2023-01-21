import matplotlib.pyplot as plt
import cv
from sklearn.cluster import KMeans
import numpy

# ham doc anh
img = plt.imread("a.jpg")
# = cv.imread()
height = img.shape[0]
width = img.shape[1]
# print(img)

# dan cac nested list
img = img.reshape(height*width, 3)
# print(img)
# print(img.shape)

# su dung kmeans de phan cum
kmeans = KMeans(n_clusters=2).fit(img)
labels = kmeans.predict(img)
clusters = kmeans.cluster_centers_

# tao hinh moi toan so 0 co kich thuoc = img
img2 = numpy.zeros_like(img)

for i in range(len(img2)):
    img2[i] = clusters[labels[i]]

# ve lai anh tu vector
img2 = img2.reshape(height, width, 3)
plt.imshow(img2)
plt.show()



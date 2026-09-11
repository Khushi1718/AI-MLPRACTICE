#1d tensor example
import numpy as np
from wcwidth import width
arr=[1,2,3,4]
print("1D Tensor:",arr) 
print("Shape of 1D Tensor:",np.array(arr).shape)
print("Rank of 1D Tensor:",np.array(arr).ndim)

#2d tensor example
arr2d=[[1,2,3],[4,5,6]]
print("2D Tensor:",arr2d)
print("Shape of 2D Tensor:",np.array(arr2d).shape)
print("Rank of 2D Tensor:",np.array(arr2d).ndim)    

#3d tensor example
arr3d=[[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]
print("3D Tensor:",arr3d)
print("Shape of 3D Tensor:",np.array(arr3d).shape)
print("Rank of 3D Tensor:",np.array(arr3d).ndim)

# 3d tensors are used in nlp 
# hi nitish.  hi  nitish rahu ankit
# hi  rahu     1    0.     0    0
# hi ankit          1
#                          1 
#                                 1
# hi nitish = [1,0,0,0][0,1,0,0]
# [[[][]] [[][]] [[] [] ]]

# 4d tensor example = images are represented as 4d tensors in cv 
image = np.random.rand(2, 128, 128, 3) # 2 images of size 128x128 with 3 channels (RGB)
print("4D Tensor (Images):", image)
print("Shape of 4D Tensor:", image.shape)
print("Rank of 4D Tensor:", image.ndim)

# one_image = (3,1200,800) = 3 rgb channels, 1200 height, 800 width ager 1 s jyda image ho toh 4


#5d tensor example = videos are represented as 5d tensors in cv
video = np.random.rand(2, 10, 128, 128, 3) # 2 videos, each with 10 frames means 10 image of size 128x128 with 3 channels (RGB)
print("5D Tensor (Videos):", video)
print("Shape of 5D Tensor:", video.shape)
print("Rank of 5D Tensor:", video.ndim) 

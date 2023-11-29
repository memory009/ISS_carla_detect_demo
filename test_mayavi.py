import mayavi.mlab as mlab
import numpy as np

# 生成一些数据
x, y, z = np.ogrid[-5:5:100j, -5:5:100j, -5:5:100j]
scalar_field = x**2 + y**2 + z**2

# 绘制等值面
mlab.contour3d(scalar_field, contours=8, transparent=True)

# 显示场景
mlab.show()
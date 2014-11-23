from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
import xlrd

data = xlrd.open_workbook('atomsplot.xlsx')                             
table = data.sheet_by_name(u'Sheet1')                                               
                                  

fig = plt.figure()
#ax = fig.gca(projection='3d')                                                       
ax = Axes3D(fig)

X = table.col_values(0)
Y = table.col_values(1)
Z = table.col_values(2)
#X, Y = np.meshgrid(X, Y)
#print X
#print Y
#print Z
#surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,             
#       linewidth=0, antialiased=False)                                             
##ax.set_zlim(-1.01, 1.01)                                                           
#
#ax.zaxis.set_major_locator(LinearLocator(10))                                       
#ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))                           
#
surf = ax.plot_trisurf(X, Y, Z, cmap=cm.jet, linewidth=0.2)
#ax.plot(X,X,color = 'black')
#ax.plot_surface(Z, Y, X, cmap=cm.hot)
#ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10, cmap=cm.hot)
fig.colorbar(surf, shrink=0.5, aspect=5)
#ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=cm.hot)
#ax.set_zlim(-2,2)

plt.savefig('plot3d.png',dpi=800)
plt.show()

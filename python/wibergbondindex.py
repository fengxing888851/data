#! /usr/bin/python2.7

import os
from matplotlib.pyplot import *
import xlrd 

data = xlrd.open_workbook('BSi-CH4.xlsx')
table = data.sheet_by_name(u'Sheet1')

x = table.col_values(3)[1:]
y1 = table.col_values(4)[1:]
y2 = table.col_values(5)[1:]
y3 = table.col_values(6)[1:]
y4 = table.col_values(7)[1:]
y5 = table.col_values(8)[1:]

x1 = [0,0]
y_1 = [0,1]

a1=plot(x,y1,'-p',color='dodgerblue',label='B-Si')
#a1=plot(x,y1,'-p',color='dodgerblue',label='B-Si',linewidth=2.5, markersize=12)
a2=plot(x,y2,'-v',color='violet',label='B-C')
a3=plot(x,y3,'-H',color='pink',label='B-H')
a4=plot(x,y4,'->',color='cyan',label='Si-H')
a5=plot(x,y5,'-o',color='springgreen',label='C-H')

plot(x1,y_1,color='crimson',linewidth=2.5)

ymin = min(y5)
ymax = max(y1)

dy = (ymax - ymin) * 0.1

ylim(ymin - dy, ymax + dy)

#a1=scatter(x,y1,marker='p',color='dodgerblue')
#a2=scatter(x,y2,marker='s',color='violet')
#a3=scatter(x,y3,marker='*',color='y')
#a4=scatter(x,y4,marker='D',color='cyan')
#a5=scatter(x,y5,color='lime')

ax = gca()
#ax.spines['top'].set_alpha(0)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
#ax.spines['right'].set_alpha(0)
ax.tick_params(right=False,top=False)
ax.xaxis.set_ticks_position('bottom')
#ax.yaxis.set_ticks_position('right')
#ax.xaxis.set_ticklabels('12345')

#ax.set_title("")
ax.set_xlabel("IRC/angstrom")
ax.set_ylabel('Wiberg Bond Index')
#ax.set_ylabel("$wiberg \,bond\, index$")

#legend((a1,a2,a3,a4,a5),('B-Si','B-C','B-H','Si-H','C-H'),loc='center left')
legend=legend(loc='center left',fontsize=12,frameon=1,shadow = 1)
legend.get_frame().set_facecolor("lavender")

savefig('wibergbondindex.png',dpi=800)
show()

